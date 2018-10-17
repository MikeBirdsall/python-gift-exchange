#!/usr/bin/python3
"""
Draw Names from a Hat program

"""

from hat import Hat, NoValidDraw
import sqlite3
import argparse
from collections import defaultdict

class Draw:
    def __init__(self):
        self.get_parms()
        self.db = sqlite3.connect(self.args.database)
        if not self.args.exchange:
            self.parser.print_help()
            print("Valid exchanges:")
            cursor = self.db.cursor()
            query = "select distinct name from gift_exchange"
            rows = cursor.execute(query)
            for row in rows:
                print("{0}".format(row))
                quit()

    def get_parms(self):
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

        cursor = self.db.cursor()
        query = "select distinct name from gift_exchange"
        rows = cursor.execute(query)

        print("No members in exchange {}".format(self.args.exchange))
        print("Valid exchanges:",
            ','.join("{0}".format(*row) for row in rows))

    def set_exclusions(self, people):
        cursor = self.db.cursor()
        query = """select from_whom, to_whom from exclude where
                 from_whom in (%s)""" % ','.join('?' * len(people))
        rows = cursor.execute(query, people)

        excludes = defaultdict(set)
        for row in rows:
            excludes[row[0]].add(row[1])

        return dict(excludes)
    def run(self):
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
            print("Could not make a draw for %s exclude:%s" %
                (people, excludes))
            return

        for from_, to_ in exchange.result.items():
            print(from_, to_)


if __name__ == '__main__':
    Draw().run()
