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
        parser.add_argument('--exchange', '-e', required=True,
            help="Which people - name of group in gift_exchange table")

        parser.add_argument("--database", "--db", "-d", required=True,
            help="Database file")

        self.args = parser.parse_args()

    def get_people(self):

        cursor = self.db.cursor()
        # Get all members to draw from
        cursor.execute(
            "select member from gift_exchange where name=?",
            (self.args.exchange,))
        return list(x[0] for x in cursor.fetchall())

    def list_valid_exchanges(self):
        """ Handle empty exchange error

            Print diagnostic including empty exchange name
            and list of all valid (not empty) exchanges

        """

        cursor = self.db.cursor()
        query = "select distinct name from gift_exchange"
        rows = cursor.execute(query)

        print("No members in exchange {}".format(self.args.exchange),
            file=sys.stderr)
        print("Valid exchanges:",
            ','.join("{0}".format(*row) for row in rows),
            file=sys.stderr)
        print(file=sys.stderr)

        self.parser.print_help(file=sys.stderr)

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
        query = """select from_whom, to_whom from exclude where
                 from_whom in (%s)""" % ','.join('?' * len(people))
        rows = cursor.execute(query, people)

        excludes = defaultdict(set)
        for row in rows:
            excludes[row[0]].add(row[1])

        return dict(excludes)

    def output(self, exchange):
        """ Output results in requested manner

            Currently always writes to stdout, but eventualy will update
            database table

        """

        for from_, to_ in exchange.result.items():
            print(from_, to_)

    def run(self):
        """ Make random draw honoring exclusions

            Using the people in the exchange self.args.exchange,
            make a random drawing where no person draws someone
            prohibited to them in the database exclude table
            Print the results in a file with eacj "from to" pair
            on a separate line.

        """
        self.db = sqlite3.connect(self.args.database)
        people = self.get_people()

        # If no people are listed, no exchange, so show valid exchanges
        if not people:
            self.list_valid_exchanges()
            quit()

        excludes = self.set_exclusions(people)

        try:
            exchange = Hat(people, excludes).draw()
        except NoValidDraw:
            print("Could not make a draw for", file=sys.stderr)
            print("people: %s" % (people), file=sys.stderr)
            print("excludes:", file=sys.stderr)
            for person, exclude in excludes.items():
                print("    %s: %s" % (person, exclude), file=sys.stderr)
        else:
            self.output(exchange)

if __name__ == '__main__':
    Draw().run()

