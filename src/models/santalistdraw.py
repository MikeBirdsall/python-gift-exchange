#!/usr/bin/python3
"""
Draw Names from a Hat program

"""

import sys
import sqlite3
import argparse
from collections import defaultdict
from hat import Hat, NoValidDraw

class Draw:
    def __init__(self):
        self._get_parms()
        self.db = sqlite3.connect(self.args.database)

    def _get_parms(self):
        self.parser = parser = argparse.ArgumentParser()
        parser.add_argument('title', help="Title for the drawing")

        parser.add_argument('--clanname', '--clan', '-c', required=True,
            help="Which clan is this list in")

        # Was exchange
        parser.add_argument('--listname', '-l', required=True,
            help="Which secret santa list of people to use?")

        parser.add_argument('--comment', required=True,
            help="Comment to those in drawing")

        parser.add_argument('--drawingdate', '-d',
            help="Date drawing was held, defaults to today")

        parser.add_argument('--giftdate', '--when', '-w', required=True,
            help='Date gifts are given, drawing expires')

        parser.add_argument("--database", "--db", required=True,
            help="Database file")

        self.args = parser.parse_args()

    def get_clan(self, clanname):

        cursor = self.db.cursor()
        cursor.execute(
            "select id from clan where clanname=?",
            (clanname,))
        clans = [x[0] for x in cursor.fetchall()]
        if not clans:
            sys.exit("No clan named {}".format(clanname))

        if len(clans) > 1:
            sys.exit("Multiple clans named {}".format(clanname))

        return clans[0]

    def get_list_id(self, listname, clanid):
        cursor = self.db.cursor()
        sql = "select id from santalist where listname=? and clan=?"
        answer = cursor.execute(sql, (listname, clanid)).fetchone()
        if answer:
            return answer[0]
        else:
            self.invalid_listname_exit(clanid, "No listname {}".format(
                listname))

    def get_people(self, listid):

        cursor = self.db.cursor()
        # Get all members to draw from
        cursor.execute(
            "select userid from santalistmember where listid=?",
            (listid,))
        return list(x[0] for x in cursor.fetchall())

    def invalid_listname_exit(self, clanid, message):
        """ Handle empty listnames error

            Print diagnostic including empty listnames name
            and list of all valid (not empty) listnames
            in this clan

        """

        cursor = self.db.cursor()
        query = """select listname from
            santalistmember join santalist on (listid = santalist.id)
            where clan = ?
            group by listname"""
        rows = cursor.execute(query, (clanid,)).fetchall()

        self.parser.error(
            message +
            "\nValid listnames:" +
            ','.join("{0}".format(*row) for row in rows)
        )

        print(message, file=sys.stderr)
        print("Valid listnames:",
            ','.join("{0}".format(*row) for row in rows),
            file=sys.stderr)
        print(file=sys.stderr)


    def set_exclusions(self, people):
        """ Determine excluded set for each person

        Args:
            people: An interable of people to go get excludes for

        Returns:
            dict of set of excluded people for each person specified

        Currently pulls results directly from database, but may eventually
        have business rules like excluding last years draw.

        """

        cursor = self.db.cursor()
        query = """select notfrom, notto from santalistexclude where
                 notfrom in (%s)""" % ','.join('?' * len(people))
        rows = cursor.execute(query, people)

        excludes = defaultdict(set)
        for row in rows:
            excludes[row[0]].add(row[1])

        return dict(excludes)

    def output(self, listname, people):
        """ Output results in requested manner

            Currently always writes to stdout, but eventualy will update
            database table

        """
        # Get the names for the people involved
        cursor = self.db.cursor()
        query = """select id, fullname from person
            where id in (%s)""" % ','.join('?' * len(people))
        names = {x[0]:x[1] for x in cursor.execute(query, people).fetchall()}

        for from_, to_ in listname.result.items():
            print("{} -> {}".format(names[from_], names[to_]))

    def run(self):
        """ Make random draw honoring exclusions

            Using the people in the listname self.args.listname,
            make a random drawing where no person draws someone
            prohibited to them in the database exclude table
            Print the results in a file with eacj "from to" pair
            on a separate line.

        """
        self.db = sqlite3.connect(self.args.database)
        clanid = self.get_clan(self.args.clanname)
        santalist_id = self.get_list_id(self.args.listname, clanid)

        people = self.get_people(santalist_id)

        # If no people are listed, no listname, so show valid listname
        if not people:
            self.invalid_listname_exit(clanid, "No members in {}".format(
                self.args.listname))

        excludes = self.set_exclusions(people)

        try:
            listname = Hat(people, excludes).draw()
        except NoValidDraw:
            print("Could not make a draw for", file=sys.stderr)
            print("people: %s" % (people), file=sys.stderr)
            print("excludes:", file=sys.stderr)
            for person, exclude in excludes.items():
                print("    %s: %s" % (person, exclude), file=sys.stderr)
        else:
            self.output(listname, people)

if __name__ == '__main__':
    Draw().run()

