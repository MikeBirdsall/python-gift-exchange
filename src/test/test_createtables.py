""" Unit tests for conversion creation of tables """

from ..conversion.createtables import create_tables

import sqlite3
import os.path
import shutil
from tempfile import NamedTemporaryFile, gettempdir

import unittest

# Database for each test is set up in TEMPDIR, most overwriting TEMPFILE
TEMPDIR = None
TEMPFILE = None

HERE = os.path.dirname(__file__)

# Names of tables which should be created
TABLE_NAMES = """person santalist santalistmember clan clanmember wish
                 gift""".split()
TABLE_QUERY = """select name from sqlite_master where
                     type='table' and not name like 'sqlite__%' escape '_'"""

def setUpModule():
    """ Find the directory used for temperary files for all tests """
    global TEMPDIR
    global TEMPFILE

    TEMPDIR = gettempdir()
    TEMPFILE = NamedTemporaryFile()

class test_table_creation(unittest.TestCase):

    def assertModifiedDatabase(self, cursor, tables=[]):
        """ Method called when database should differ from standard """
        table_names = [x[0] for x in cursor.execute(TABLE_QUERY).fetchall()]
        tables.extend(TABLE_NAMES)
        self.assertCountEqual(tables, table_names)

    def assertCanonicalDatabase(self, cursor):
        """ Method called when database should be initialized to
            standard
        """
        table_names = [x[0] for x in cursor.execute(TABLE_QUERY).fetchall()]
        self.assertCountEqual(table_names, TABLE_NAMES)
        # do a sqldiff comparison of the databasefile with a canonical output?

    def test_from_memory(self):
        """ Create tables: create tables in :memory: """
        cursor = create_tables(":memory:")
        self.assertCanonicalDatabase(cursor)

    def test_new_file(self):
        """ Create database in new file """
        fname = os.path.join(TEMPDIR, "test_createtables.db")
        try:
            os.remove(fname)
        except FileNotFoundError:
            pass
        cursor = create_tables(fname)
        self.assertCanonicalDatabase(cursor)

    def test_empty_file(self):
        """ Create database in empty file """
        # Create a new temp, so I know it's empty
        global TEMPFILE
        saved = TEMPFILE
        TEMPFILE = NamedTemporaryFile()
        cursor = create_tables(TEMPFILE.name)
        self.assertCanonicalDatabase(cursor)
        TEMPFILE.close()
        TEMPFILE = saved


    def test_replace_old_file(self):
        """ Create database in filled file """
        shutil.copy(os.path.join(HERE, "data", "filled.db"), TEMPFILE.name)
        cursor = create_tables(TEMPFILE.name)
        self.assertCanonicalDatabase(cursor)

    def test_add_to_file(self):
        """ Create database in filled file """
        shutil.copy(os.path.join(HERE, "data", "partial.db"), TEMPFILE.name)
        cursor = create_tables(TEMPFILE.name)
        self.assertModifiedDatabase(cursor, ["extra1", "extra2"])

