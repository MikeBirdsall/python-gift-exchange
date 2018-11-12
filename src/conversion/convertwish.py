""" Convert Wish table - convert a wishlist file into database records """
import argparse
import sys
import sqlite3
import re
from datetime import datetime


# Global translation list of user IDs.
# Immutable list except not initialized until database connected in convert
IDS = {}

def getglobalid(username):
    # Use the user table to find the userid for username
    # Complain and fail if not found
    return IDS[username]

def format_date(intime):
    "Return sqlite datetime given current wishfile datetime format"
    return datetime.strftime(datetime.strptime(intime, "%b %d %Y"), "%Y-%m-%d")

def format_datetime(intime):
    "Return sqlite date given current wishfile expires date format"
    return datetime.strftime(datetime.strptime(intime, "%a %b %d %H:%M:%S %Y"),
        "%Y-%m-%d %H:%M:%S")

class wish:
    "Class for a single wish"
    def __init__(self, username, created, by, ident, description,
        number, expires):

        self.username = username
        self.when_suggested = format_datetime(created)
        self.suggestedby = by
        self.localident = ident
        self.description = description
        self.howmany = number
        # Do we want to use None, or a sentinel date?
        if expires == "never":
            self.expires = None
        else:
            self.expires = format_date(expires)

        self.globalid = getglobalid(username)
        self.byid = getglobalid(by)
        self.id = None #pylint: disable=invalid-name

    def emit(self, connection):
        "Write wish to database"

        cursor = connection.cursor()
        sql = """insert into wish ('when_suggested', 'by', 'giftee',
            'description', 'numberwanted', 'expires') VALUES (?,?,?,?,?,?)"""
        values = (self.when_suggested, self.byid, self.globalid,
            self.description, self.howmany, self.expires)

        try:
            cursor.execute(sql, values)
            self.id = cursor.lastrowid
        except sqlite3.IntegrityError as e: #pylint: disable=invalid-name
            print("Couldn't put %s in database: %s" % (self.description, e))

    def __str__(self):
        "Debug formatted wish"
        return("Wish object:'%s' when_suggested:%s for:%s by:%s expires:%s" %
            (self.description[:30], self.when_suggested, self.globalid,
            self.byid, self.expires))

class gift:
    "Class for a single gift"
    def __init__(self, when, buyer, thiswish, note, number):
        self.when_bought = format_datetime(when)
        self.wish = thiswish
        self.giver = getglobalid(buyer)
        self.giftee = self.wish.globalid
        self.note = note
        self.number = number

    def __str__(self):
        "Debug formatted gift string"
        return("Gift object:'%s' when:%s giftee:%s(%s) giver:%s note:%s "
            "howmany:%s" %
            (self.wish.description[:30],
            self.when_bought,
            self.giftee,
            self.wish.username,
            self.giver,
            self.note,
            self.number))

    def emit(self, connection):
        "Write gift to database"

        cursor = connection.cursor()
        sql = """insert into gift(when_bought, wishid, giver, giftee,
            note, numberbought) VALUES (?,?,?,?,?,?)"""
        values = (self.when_bought, self.wish.id, self.giver, self.giftee,
            self.note, self.number)

        try:
            cursor.execute(sql, values)
        except sqlite3.IntegrityError as e: #pylint: disable=invalid-name
            print("Couldn't put %s in database: %s" % (self, e))


class convert:
    "Manage the conversion"

    def __init__(self, db=None):
        self.wishlist = {}
        self.giftlist = []
        self.conn = None
        if db:
            self.reset_db(sqlite3.connect(db))

    def set_global_id_dictionary(self):
        global IDS
        cursor = self.conn.cursor()
        cursor.execute('''select id, userid from person''')
        IDS = {row[1]:row[0] for row in cursor.fetchall()}

    def reset_db(self, conn):
        self.conn = conn
        self.set_global_id_dictionary()

    def run(self, files):
        "Do the conversion for all files "

        for file_ in files:
            self.run_one(file_)

    def run_one(self, file_):
        "Do the conversion for a file "

        self.wishlist = {}
        self.giftlist = []

        with file_ as infile:
            try:
                sentinel = infile.readline()
            except UnicodeDecodeError:
                print(infile.name)
                raise
            try:
                username = re.search('Defining a wishlist for (.+)',
                    sentinel).group(1)
            except AttributeError:
                print("Input file is not in wishlist regex form. Line 1")
                sys.exit(1)

            for line in infile:
                # Ignore comments and empty lines
                if line.startswith("#") or not line.strip():
                    continue

                # Lines are tab-delimited
                #    created,who,command,ident,description,number,expires
                # Each "added" command becomes a wish,
                # each "bought" becomes a gift.
                # Each "delete" command changes a gift.
                # A "purge" is ignored at this point.
                # Other command: unbuy

                # First break into enough fields to decode command
                created, who, command, rest = line.strip().split("\t", 3)
                if command in ['purge', 'delete']:
                    purgefrom = rest
                elif command == 'bought':
                    ident, note, number = rest.strip().split("\t")
                else:
                    ident, description, number, expires = rest.strip().split("\t")

                if command == 'purge':
                    pass
                elif command == 'added':
                    thiswish = wish(username, created, who, ident, description,
                        number, expires)
                    self.wishlist[ident] = thiswish
                elif command == 'delete':
                    # Write wish method for deletion
                    # TODO: implement the deletion code
                    pass
                elif command == 'bought':
                    thisgift = gift(created, who, self.wishlist[ident], note,
                        number)
                    self.giftlist.append(thisgift)
                    # Any changes to gift?
                elif command == 'unbuy':
                    # Write method for gift
                    pass
                else:
                    print("Unknown operator %s" % (command))

            for thiswish in self.wishlist.values():
                #TODO: Remove print(thiswish)
                thiswish.emit(self.conn)

            for thisgift in self.giftlist:
                #TODO: Remove print(thisgift)
                thisgift.emit(self.conn)

            self.conn.commit()

def main():
    """ Run as command line program """

    parser = argparse.ArgumentParser(
        description="Load database from wishfile")
    parser.add_argument("database", help="Database created or updated")
    parser.add_argument("infile", nargs='+', type=argparse.FileType('r'),
        default=sys.stdin, help="Input file (stdin used if left blank)")

    args = parser.parse_args()

    convert(args.database).run(args.infile)

if __name__ == "__main__":
    main()

