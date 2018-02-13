""" Unit test for convertdraws """

from test import suck_database, reldir, relfile_list
from ..conversion.convertdraws import convert

import unittest

class test_conversion(unittest.TestCase):

    def assertConvertFilled(self, list_, results, dbfile="empty_draws.db"):
        dummy, clan, title = list_.split('.',2)
        db = suck_database(reldir(dbfile))
        converter = convert()
        converter.reset_db(db)
        list_ = relfile_list([list_])[0]
        converter.run(list_)
        for line in db.iterdump():
            if "INSERT" in line:
                print(line)
        cursor = self.cursor = db.cursor()

        sql = """select p1.userid, p2.userid
            from drawingresult as d
            join santalistdrawing as sld on (d.drawing = sld.listid)
            join clan on (clan.id = sl.clan)
            join person as p1 on (giver = p1.id)
            join person as p2 on (giftee = p2.id)
            join santalist as sl on (sld.listid = sl.id)
            where clan.clanname = ? and sl.listname = ? and sld.title = ?
            """
        #print(sql)
        #print(cursor.execute(sql,(clan, clan, title)).fetchall())
        dbresults = cursor.execute(sql, (clan, clan, title)).fetchall()

        self.assertEqual(dbresults, results)

    def test_filled_file(self):
        result = [('ed', 'mike'), ('mike', 'peg'), ('peg', 'ed')]
        self.assertConvertFilled("list.Clan1.list1.title", result)

    def test_new_list(self):
        result = [('pat', 'bob'), ('bob', 'mike'), ('mike', 'pat')]
        self.assertConvertFilled("list.Clan1.list2.title", result)

