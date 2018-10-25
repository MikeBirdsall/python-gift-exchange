""" convert person files into database records

    Creates entries into person, clan, clanmember, and relationship tables

    The person files don't have all the information that I'd like to put in,
    but it can start it and create palceholders. The plan is to add extra
    fields into the person file; I don't think that will cause any problem



"""

import argparse
from warnings import warn
import sqlite3
from os.path import splitext
from collections import defaultdict
import os

import warnings

def custom_formatwarning(msg, *args, **kwargs):
    return str(msg) + '\n'

warnings.formatwarning = custom_formatwarning

class person:
    """ Class for each person """
    def __init__(self, userid):
        self.userid = userid
        self.fullname = None
        self.nickname = None
        self.birthday = None
        self.email = None
        self.inclan = False

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
        self.clanmembers = defaultdict(set)
        if db:
            self.connection = sqlite3.connect(db)
        else:
            self.connection = None

    def reset_db(self, connection):
        self.connection = connection

    def run(self, files):
        if not self.connection:
            warn("No database connected")
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
                warn("Empty personfile {}".format(personfile.name))
                continue
            userid = splitext(personfile.name)[1][1:]
            if not userid:
                warn("No userid found in {}".format(personfile.name))
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
                elif field == 'group':
                    for clan in value.strip().split():
                        self.clanmembers[clan].add(userid)
                        this_person.inclan = True
                elif field in ('exclude', 'spouse', 'admin'):
                    pass
                else:
                    warn("Unknown field %s in %s" % (field, personfile.name))
            if not this_person.inclan:
                warn("No clan for {}".format(this_person.userid))
            people.append(this_person.params())
            personfile.close()

        if not people:
            warn("No people defined")
            return

        cursor = self.connection.cursor()
        try:
            cursor.executemany("""insert into person
                ('userid', 'fullname', 'nickname', 'birthday', 'email') VALUES
                (?,?,?,?,?)""", people)
        except sqlite3.IntegrityError as e:
            warn("Couldn't put %s in database: %s" % (userid, e))

        self.connection.commit()

        # deal with clans
        # We could use sql to only write new clans
        #insert into clan ('clanname') select ?
        #    where not exists(select 1 from clan where clanname = ?)
        # but would have to read back in old ones anyway, to map clanid
        # or use join

        # Read back in all existing clans (id, clanname)
        sql = """select id, clanname from clan"""
        clans = cursor.execute(sql).fetchall()
        clans = dict((clanname, id) for id, clanname in clans)

        # Compute new clans
        newclans = set(self.clanmembers)
        newclans.difference_update(clans)

        # Write out all new clans update memory copy of clans
        sql = """insert into clan ('clanname') values (?)"""

        for clan in newclans:
            cursor.execute(sql, [clan])
            id = cursor.lastrowid
            clans[clan] = id

        # Read in all persons (id, userid)
        ids = cursor.execute("""select id, userid from person""").fetchall()
        ids = {userid:id for id, userid in ids}
        updates = [(clans[clan], ids[member]) for clan in self.clanmembers for member in self.clanmembers[clan]]

        sql = """insert into clanmember ('clanid', 'userid') values (?,?)"""
        cursor.executemany(sql, updates)

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
