""" convert person files into database records

    The person files don't have all the information that I'd like to put in,
    but it can start it and create palceholders. The plan is to add extra
    fields into the person file; I don't think that will cause any problem

"""

import argparse
import sqlite3
from os.path import splitext
import os


class person:
    """ Class for each person """
    def __init__(self, userid):
        self.userid = userid
        self.fullname = None
        self.nickname = None
        self.birthday = None
        self.email = None

    def params(self):
        return [
            self.userid,
            self.fullname,
            self.nickname,
            self.birthday,
            self.email]


class convert():
    "Do conversion across files "

    def __init__(self, db=None):
        self.files = []
        if db:
            self.connection = sqlite3.connect(db)
        else:
            self.connection = None

    def reset_db(self, connection):
        self.connection = connection

    def run(self, files):
        if not self.connection:
            print("Warning: No database connected")
            return

        # userid from filename
        # fullname from name field
        # nickname from nickname (later)
        # birthday from birthday (later)
        # email from email (later?)


        people = []
        for personfile in files:
            # Using one file per person, can we get the file name?
            if not os.stat(personfile.name).st_size:
                print("Warning: Empty personfile {}".format(personfile.name))
                continue
            userid = splitext(personfile.name)[1][1:]
            if not userid:
                print("Warning: No userid found in {}".format(personfile.name))
                continue
            this_person = person(userid)

            for line in personfile:
                if line.startswith("#") or not line.strip():
                    continue

                field, value = line.strip().split("=", 1)
                if field == "name":
                    this_person.fullname = value
                elif field == 'nickname':
                    this_person.nickname = value
                elif field == 'birthday':
                    this_person.birthday = value
                elif field == 'email':
                    this_person.email = value
                elif field in ('group', 'exclude', 'spouse', 'admin'):
                    pass
                else:
                    print("Warning: Unknown field %s in %s" % (field, personfile.name))
            people.append(this_person.params())

        if not people:
            print("Warning: no people defined")
            return

        cursor = self.connection.cursor()
        try:
            # Debugging to print the tables
            #cursor.execute("select name from sqlite_master where type='table'")
            #print("tables:", cursor.fetchall())

            cursor.executemany("""insert into person
                ('userid', 'fullname', 'nickname', 'birthday', 'email') VALUES
                (?,?,?,?,?)""", people)
        except sqlite3.IntegrityError as e:
            print("Warning: Couldn't put %s in database: %s" % (userid, e))

        self.connection.commit()

    def ___del__(self):
        self.connection.close()


def main():
    """ Run as command line program """

    parser = argparse.ArgumentParser(
        description="Load database from person files")
    parser.add_argument("database", help="Database to update")
    parser.add_argument("infile", nargs='+', type=argparse.FileType('r'),
        help="Input file[s]")
    args = parser.parse_args()

    convert(args.database).run(args.infile)

if __name__ == "__main__":
    main()
