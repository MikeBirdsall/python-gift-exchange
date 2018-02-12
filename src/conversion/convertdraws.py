""" Convert secret santa draw lists into drawingresult table """

import sqlite3
import argparse
import os
from warnings import warn

# Global translation list of user IDs.
# Immutable list except not initialized until database connected in convert
IDS = {}

def getglobalid(username):
    # Use the user table to find the userid for username
    # Complain and fail if not found
    return IDS[username]

class convert:

    def __init__(self):
        self.conn = None
        self.cursor = None

    def set_db(self, db):
        self.reset_db(sqlite3.connect(db))

    def reset_db(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        global IDS
        self.cursor.execute("""select id, userid from person""")
        IDS = {row[1]:row[0] for row in self.cursor.fetchall()}

    def run(self, file_):
        print("In convertdraws Converting file {}".format(file_.name))

        with file_ as infile:
            filename = file_.name
            prefix, clan, list_, title = os.path.basename(filename).split('.')
            if prefix != 'list':
                warn("Drawing file {} does not start with 'list'".format(filename))

            if not os.stat(filename).st_size:
                warn("Empty drawing file {}".format(filename))

            # Put listid, title, status into santalistdrawing
            # Get clanid
            clanid = self.cursor.execute("select id from clan where clanname = ?",
                (clan,)).fetchone()
            if not clanid:
                warn("No clanid for clan %s" % (clan))
                return

            clanid = clanid[0]

            # Get santalist id
            listid = self.cursor.execute(
                "select id from santalist where listname = ? and clan = ?",
                (list_, clanid)).fetchone()
            if listid:
                listid = listid[0]
            else:
                self.cursor.execute(
                    "insert into santalist (listname, clan) values (?,?)",
                    (list_, clanid))
                listid = self.cursor.lastrowid
                warn("Creating secret santa list, listid:{}".format(listid))

            # Add this drawing
            self.cursor.execute(
                """insert into santalistdrawing (listid, title, status)
                    values (?, ?, ?)""", (listid, title, "over"))
            # Add all the results
            lines = infile.read().splitlines()
            stripped = [x.strip() for x in lines]
            pairs = [x.split() for x in stripped]
            pairs = [(getglobalid(x.strip()), getglobalid(y.strip()))
                for x,y in pairs]
            pairs = [(listid, e[0], e[1]) for e in pairs]
            self.cursor.executemany(
                """insert into drawingresult (drawing, giver, giftee) values
                   (?, ?, ?)""", pairs)
            self.conn.commit()




def main():
    """ Run as command line program """

    parser = argparse.ArgumentParser(
        description="Load drawingresult table from list.clan.group.title file")
    parser.add_argument("-d", "--database", help="Database updated")
    parser.add_argument("infile", nargs='+', type=argparse.FileType('r'),
        help="Input files")

    args = parser.parse_args()

    converter = convert()
    converter.reset_db(sqlite3.connect(args.database))
    for file_ in args.infile:
        converter.run(file_)

if __name__ == "__main__":
    main()

