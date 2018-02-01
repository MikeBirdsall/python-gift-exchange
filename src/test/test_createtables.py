""" Unit tests for conversion creation of tables """

from ..conversion.createtables import create_tables

import sqlite3
import unittest

TABLE_NAMES = 'person santalist santalistmember clan clanmember wish gift'.split()
TABLE_QUERY = """select name from sqlite_master where
                     type='table' and not name like 'sqlite__%' escape '_'"""

class test_table_creation(unittest.TestCase):

    def test_from_memory(self):
        """ create tables in :memory: """
        cursor = create_tables(":memory:")
        table_names = [x[0] for x in cursor.execute(TABLE_QUERY).fetchall()]
        self.assertCountEqual(table_names, TABLE_NAMES)
        #self.assertCountEqual(table_names, TABLE_NAMES, "Tables {} not {}".format(table_names, TABLE_NAMES))



