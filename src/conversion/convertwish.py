""" Convert Wish table - convert a wishlist file into database records """
import argparse
import sys
import sqlite3
import re

#from createdb import createtables;

def convert(file_, db):
    "Do the conversion for a file "

    # createtables(db)

    conn = sqlite3.connect(db)

    with file_ as infile:
        sentinel = infile.readline()
        try:
            userid = re.search('Defining a wishlist for (.+)',
                sentinel).group(1)
        except AttributeError:
            print("Input file is not in wishlist regex form. Line 1")
            sys.exit(1)

        print("We got %s this far" % userid)



        for line in infile:
            # Ignore comments and empty lines
            if line.startswith("#") or not line.strip(): continue


            # Lines are tab-delimited
            #    datetime,who,op,ident,description,number,expires
            # Each "added" op becomes a wish,
            # each "bought" becomes a gift.
            # Each "delete" op changes a gift.
            # A "purge" is ignored at this point.
            # Other ops: unbuy
            datetime, who, op, ident, description, number, expires = line.strip().split("\t")
            print("datetime=%s, who=%s, op=%s, ident=%s, description=%s, number=%s, expires=%s" % (datetime, who, op, ident, description, number, expires))
            sys.exit()


def main():
    """ Run as command line program """

    parser = argparse.ArgumentParser(
        description="Load database from wishfile")
    parser.add_argument("infile", nargs='?', type=argparse.FileType('r'),
        default=sys.stdin, help="Input file (stdin used if left blank)")
    parser.add_argument("database", help="Database created or updated")

    args = parser.parse_args()

    convert(args.infile, args.database)

if __name__ == "__main__":
    main()

