""" Unit tests for convertperson """

from test import suck_database, reldir, relfile_list
from ..conversion.convertperson import convert

import unittest

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

    def assertNoClan(self, clan_name):
        cursor = self.__mem
        cursor.execute("select count(*) from clan where clanname = ?",
            (clan_name,))
        self.assertFalse(cursor.fetchone()[0])

    def assertClanExists(self, clan_name):
        cursor = self.__mem
        cursor.execute("select count(*) from clan where clanname = ?",
            (clan_name,))
        self.assertTrue(cursor.fetchone()[0], "Didn't add clan %s" % clan_name)

    def assertClanMember(self, clan_name, member_name):
        cursor = self.__mem
        cursor.execute("""select 1 from clan join clanmember
            on clanmember.clanid = clan.id join person
            on clanmember.userid = person.id
            where person.userid = ? and clan.clanname = ?""",
            (member_name, clan_name))
        self.assertTrue(cursor.fetchone())

    def test_no_files(self):
        with self.assertWarns(UserWarning):
            self.assertConverts([], 0)

    def test_one_empty_file(self):
        with self.assertWarns(UserWarning):
            self.assertConverts(['person.empty'], 0)

    def test_missing_userid(self):
        with self.assertWarns(UserWarning):
            self.assertConverts(['person-nouserid'], 0)

    def test_single_good_person(self):
        self.assertConverts(['person.sgpone'])
        self.assertUserIds(['sgpone'])

    def test_two_good_persons(self):
        self.assertConverts(['person.second', 'person.sgpone'])
        self.assertUserIds(['second', 'sgpone'])

    def test_clan_created(self):
        db = suck_database(reldir("empty_tables.db"))
        self.__mem = db.cursor()
        self.assertNoClan('clan1')
        # Debug during development
        self.__mem.execute("""insert into clan (clanname)
            values ('Clan2'), ('Clan3')""")
        converter = convert("")
        converter.reset_db(db)
        files = relfile_list(['person.clanmember1'])
        converter.run(files)
        self.assertClanExists('Clan1')
        self.assertClanMember('Clan1', 'clanmember1')




