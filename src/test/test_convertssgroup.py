""" Unit tests for converting secret santa group lists """

from test import suck_database, reldir, relfile_list
import string
import os
from ..conversion.convertssgroup import convert

import unittest
import random

class test_conversion(unittest.TestCase):

    def test_no_files(self):
        with self.assertWarns(UserWarning):
            self.assertConvertEmpty(relfile_list([]))

    def assertConvertEmpty(self, files):
        db = suck_database(reldir("empty_santalist.db"))
        converter = convert('Clan1')
        converter.reset_db(db)
        files = relfile_list(files)
        converter.run(files)
        cursor = self.cursor = db.cursor()
        lists = cursor.execute("select listname from santalist").fetchall()
        self.assertEqual(len(lists), 0)

    def assertConvertFilled(self, files, members):
        clanname = ''.join(
            random.choice(string.ascii_letters) for _ in range(6))
        db = suck_database(reldir("empty_santalist.db"))
        cursor = db.cursor()
        cursor.execute(
            """insert into clan (clanname, description) values (?,?)""",
            (clanname, "Test clan"))
        converter = convert(clanname)
        converter.reset_db(db)
        files = relfile_list(files)
        converter.run(files)
        clanid = cursor.execute(
            "select id from clan where clanname = ?", (clanname,)).fetchone()[0]
        lists = cursor.execute(
            "select id, clan, listname from santalist").fetchall()
        self.assertEqual(len(lists), 1)
        self.assertEqual(lists[0][1], clanid)

        for file_, list_ in zip(files, lists):
            flname = os.path.splitext(file_.name)[1][1:]
            dblname = list_[2]
            self.assertEqual(flname, dblname)
            dbmembers = cursor.execute(
                """select person.userid from santalistmember join person on
                    (santalistmember.userid = person.id) where listid=?""",
                (list_[0],)).fetchall()
            dbmembers = [x[0] for x in dbmembers]
            self.assertCountEqual(dbmembers, members)



    def test_empty_file(self):
        with self.assertWarns(UserWarning):
            self.assertConvertFilled(["group.empty"], [])

    def test_filled_file(self):
        self.assertConvertFilled(["group.testfilledfile"],
            ['ed', 'mike', 'peg', 'steve', 'pat', 'bob'])

    def test_file_with_blank_line(self):
        self.assertConvertFilled(["group.testblankline"],
            ['ed', 'mike', 'peg', 'steve', 'pat', 'bob'])

