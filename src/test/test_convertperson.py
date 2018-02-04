""" Unit tests for conversion """

import os
import sqlite3

from ..conversion.convertperson import convert
import unittest

HERE = os.path.dirname(__file__)

def relfile_list(files):
    return [open(reldir(file_name), 'r') for file_name in files]

def suck_database(path):
    " Create memory database from database on disk "

    dsk = sqlite3.connect(path)
    mem = sqlite3.connect(":memory:")
    cursor = mem.cursor()

    lines = '\n'.join(dsk.iterdump())
    cursor.executescript(lines)
    mem.commit()

    return mem

def reldir(file):
    return os.path.join(HERE, "data", file)

class test_conversion(unittest.TestCase):

    def setUp(self):
        self.__mem = None

    def tearDown(self):
        #Database.rollback('')
        #for file in files:
        #    file.close()
        pass

    def assertConverts(self, files, how_many=None):
        if how_many is None:
            how_many = len(files)
        db = suck_database(reldir("empty_tables.db"))
        converter = convert("")
        converter.reset_db(db)
        files = relfile_list(files)
        converter.run(files)
        # people table should be empty
        self.__mem = db.cursor()
        people = self.__mem.execute("select count(*) from person").fetchone()[0]
        self.assertEqual(people, how_many)

    def assertUserIds(self, ids):
        ids_ = self.__mem.execute("select userid from person").fetchall()
        self.assertEqual(len(ids_), len(ids))
        self.assertCountEqual([x[0] for x in ids_], ids)
        # from collections import Counter
        # assertEqual(Counter([x[0] for x in ids_), Counter(ids_))

    def test_no_files(self):
        self.assertConverts([], 0)

    def test_one_empty_file(self):
        self.assertConverts(['person.empty'], 0)

    def test_missing_userid(self):
        self.assertConverts(['person-nouserid'], 0)

    def test_single_good_person(self):
        self.assertConverts(['person.sgpone'])
        self.assertUserIds(['sgpone'])

    def test_two_good_persons(self):
        self.assertConverts(['person.second', 'person.sgpone'])
        self.assertUserIds(['second', 'sgpone'])



