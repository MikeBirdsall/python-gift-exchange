""" Convert secret santa group lists into santalist table """
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
    try:
        return IDS[username]
    except KeyError:
        warn("No user named '{}'".format(username))

class convert:
    "manage the conversion"

    def __init__(self, clan):
        self.clan = clan
        self.clanid = None
        print("Converting for clan {}".format(clan))

    def set_db(self, db):
        self.reset_db(sqlite3.connect(db))

    def reset_db(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        global IDS
        self.cursor.execute("""select id, userid from person""")
        IDS = {row[1]:row[0] for row in self.cursor.fetchall()}
        self.cursor.execute("select id from clan where clanname = ?",
            (self.clan,))
        result = self.cursor.fetchone()
        if not result:
            warn(
                "No definition for clan:{} while setting santalist".format(self.clan))
            self.clanid = 1
            return
        self.clanid = result[0]


    def run(self, files):
        "Do the conversion for all files"

        if not files:
            warn("No santa group files")
        for file_ in files:
            print("In convertssgroup Converting file {}".format(file_.name))
            self.run_one(file_)
        self.conn.commit()

    def run_one(self, file_):
        "Convert one file"

        with file_ as infile:
            filename = file_.name
            prefix, listname = os.path.basename(filename).split('.')
            if prefix != "group":
                warn("Group file {} does not start with 'group'".format(filename))

            if not os.stat(file_.name).st_size:
                warn("Empty santa group file {}".format(file_.name))

            # Put group name and clanid into santalist
            print("Inserting secret santa list:{} for clan:{} clanid:{}".format(listname, self.clan, self.clanid))
            self.cursor.execute("""insert into santalist
                ('listname', 'clan') values (?, ?)""",
                (listname, self.clanid))
            listid = self.cursor.lastrowid
            print("Listid:{}".format(listid))

            # Put member ids into santalistmembers
            members = [getglobalid(x.strip())
                for x in infile.read().splitlines() if x.strip()]
            self.cursor.executemany(
                "insert into santalistmember (listid, userid) values (?, ?)",
                zip([listid] * len(members), members))

def main():
    """ Run as command line program """

    parser = argparse.ArgumentParser(
        description="Load santalist table from group.name file")
    parser.add_argument("-d", "--database", help="Database updated")
    parser.add_argument("-c", "--clan")
    parser.add_argument("infile", nargs='+', type=argparse.FileType('r'),
        help="Input files")

    args = parser.parse_args()

    converter = convert(args.clan)
    converter.set_db(args.database)
    converter.run(args.infile)

if __name__ == "__main__":
    main()

