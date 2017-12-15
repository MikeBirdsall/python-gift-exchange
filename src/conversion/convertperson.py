""" convert person files into database records

    The person files don't have all the information that I'd like to put in,
    but it can start it and create palceholders. The plan is to add extra
    fields into the person file; I don't think that will cause any problem

"""

import argparse
import sqlite3
from os.path import splitext


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


def convert(files, db):
    "Do conversion across files "

    # userid from filename
    # fullname from name field
    # nickname from nickname (later)
    # birthday from birthday (later)
    # email from email (later?)


    people = []
    for personfile in files:
        # Using one file per person, can we get the file name?
        userid = splitext(personfile.name)[1][1:]
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
                print("Unknown field %s in %s" % (field, personfile.name))
        people.append(this_person.params())

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    try:
        cursor.executemany("""Insert into person
            ('userid', 'fullname', 'nickname', 'birthday', 'email') VALUES
            (?,?,?,?,?)""", people)
    except sqlite3.IntegrityError as e:
        print("Couldn't put %s in database: %s" % (userid, e))

    connection.commit()
    connection.close()


def main():
    """ Run as command line program """

    parser = argparse.ArgumentParser(
        description="Load database from person files")
    parser.add_argument("database", help="Database created or updated")
    parser.add_argument("infile", nargs='+', type=argparse.FileType('r'),
        help="Input file (stdin used if left blank)")
    args = parser.parse_args()

    convert(args.infile, args.database)

if __name__ == "__main__":
    main()
