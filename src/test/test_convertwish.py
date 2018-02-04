""" Unit tests for converting wishlist.<person> files """

import os
import sqlite3

from ..conversion.convertwish import convert

import unittest

HERE = os.path.dirname(__file__)

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

def relfile_list(files):
    return [open(reldir(file_name), 'r') for file_name in files]

class test_conversion(unittest.TestCase):

    def assertConverts(self, files, numwishes, numgifts,
            dbfile="empty_wishes.db"):
        db = suck_database(reldir(dbfile))
        #print("\n".join(db.iterdump()))
        converter = convert("")
        converter.reset_db(db)
        files = relfile_list(files)
        converter.run(files)
        cursor = db.cursor()
        wishes = cursor.execute("select count(*) from wish").fetchone()[0]
        self.assertEqual(wishes, numwishes)
        gifts = cursor.execute("select count(*) from gift").fetchone()[0]
        self.assertEqual(gifts, numgifts)

    def test_single_person_no_data(self):
        self.assertConverts(['wishlist.oneempty'],0,0 )

    def test_single_person_wishes(self):
        self.assertConverts(['wishlist.fivewishes'], 5, 0)

    def test_single_person_wishes_and_gifts(self):
        self.assertConverts(['wishlist.wishesandgifts'], 5, 1)

    def test_three_Files(self):
        files = ['wishlist.oneempty', 'wishlist.fivewishes',
            'wishlist.wishesandgifts']
        self.assertConverts(files, 10, 1)



