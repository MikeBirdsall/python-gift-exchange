#!/usr/bin/python3
"""
A Draw Names from a Hat module

How To Use This Module
======================

1. Import it: ``import hat``

2. Define the full hat
   - A set or other interable of all the participants (hashable value)
   - A dict (or other mapping) from the participants to those they cannot draw

3. Do the drawing

   drawn = Hat(participants, excluded).draw()

4. It returns a Hat object with a attribute `result` which is a map giving the
   person drawn for each participant or raises a NoValidDraw exception if that
   is not possible.


"""
from typing import Iterable, Mapping
from random import choice
from collections import defaultdict
from collections import Counter


class NoValidDraw(Exception):
    pass

class Hat:
    """
    A hat for drawing a name out of, holding the current state of a drawing,
    either just before or just after the latest draw.

    Hats are kept in a linked list from the original 'full' hat down to the
    empty hat.

    A Hat has the following attributes:
    - `parent`: The preceeding draw. If None, this is the first draw
    - `participants`: A set of all those in the original hat
    - `candidates`: Those who have not yet drawn
    - `targets`: Those who have not yet been drawn, who are still in the hat
    - `excluded`: A dict of sets of invalid draws for each participant
    - `allowed`: A dict of sets of valid draws for each candidate
    - `from`: participant who last drew from the hat
    - `to`: participant last drawn from the hat
    - `result`: A dict of who drew whom
    - `events`: A count of events which happened throughout draws

    """

    def __init__(
        self,
        participants: Iterable,
        excluded: Mapping,
        parent=None) -> None:
        """
        Initialize a `Hat` object either de novo or from a previous partial
        drawing.

        Parameters:
        - `participants`: iterable of all those in the drawing
        - `excluded`: mapping of iterables of those illegal to draw for key
        - `parent`: a Hat object with a partial drawing.

        """

        if parent:
            self.parent = parent
            self.participants = parent.participants
            self.events = parent.events
            self.candidates = parent.candidates.difference((parent.from_,))
            self.targets = parent.targets.difference((parent.to_,))
            self.excluded = parent.excluded
            self.result = parent.result
        else:
            self.parent = None
            self.events = Counter()
            self.participants = set(participants)
            self.candidates = set(participants)
            self.targets = set(participants)
            self.excluded = excluded
            self.result = dict()

        self.from_ = None
        self.to_ = None
        self.allowed = dict()

        for each in self.candidates:
            self.allowed[each] = set(self.targets).difference(
                self.excluded.get(each, set()))

    def draw(self):
        """ if possible,
                makes a valid draw from the current hat
                creates the child hat
                makes a draw from it.
            if not and has a parent,
                backs out the draw from its parent
                makes a draw from it
            else
                raise a NoValidDraw exception
        """
        if not self.candidates:
            if self.parent:
                return self.parent
            else:
                raise NoValidDraw

        # Candidate with fewest choices drawing first minimizes backtrack
        self.from_ = choice(self.min_choices(self.candidates))

        # Without that optimization
        # self.from_ = choice(self.candidates)



        if not self.allowed[self.from_]:
            # Retry previous draw without
            self.events['backtracks'] += 1
            if self.parent:
                return self.parent._backtrack()
            else:
                raise NoValidDraw
            # Let garbage collection get rid of impossible draw

        self.to_ = choice(tuple(self.allowed[self.from_]))
        self.result[self.from_] = self.to_

        return Hat(None, None, self).draw()

    def _backtrack(self):
        """ Retry draw without allowing the same choice """
        self.excluded[self.from_].add(self.to_)
        self.allowed[self.from_].remove(self.to_)
        self.from_ = self.to_ = None
        return self.draw()


    def __str__(self):
        return ",".join(
            "%s drew %s" % (x, self.result[x])
            for x in self.result)

    def min_choices(self, candidates):
        allowed = self.allowed
        level = min(len(allowed[x]) for x in candidates)
        answer = [x for x in candidates if len(allowed[x]) == level]
        return answer

import sqlite3
import argparse
import pprint

class ExerciseHat:
    def __init__(self):
        self.get_parms()
        self.db = sqlite3.connect(self.args.database)
        if not self.args.exchange:
            print("Must select exchange")
            self.args.listexchanges = True
        if self.args.listexchanges:
            print("Possible exchanges:")
            cursor = self.db.cursor()
            query = "select distinct name from gift_exchange"
            rows = cursor.execute(query)
            for row in rows:
                print("{}".format(row[0]))
            quit()
        self.stats = Counter()
        self.events = Counter()

    def get_parms(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--howmany', '-n', type=int, default=1,
            help="How many trials")
        exchgroup = parser.add_mutually_exclusive_group()
        exchgroup.add_argument("--listexchanges", "-l", action='store_true',
            help="List exchanges")
        exchgroup.add_argument('--exchange', '-e',
            help="Which people - name of group in gift_exchange table")

        parser.add_argument("--database", "--db", "-d", required=True,
            help="Database file")

        self.args = parser.parse_args()


    def run(self):
        self.stats.clear()
        self.events.clear()
        for dummy in range(self.args.howmany):
            result = self.runone()
            if result:
                self.stats.update(Counter(result.result.items()))
                self.events.update(result.events)
            else:
                self.events['failed'] += 1

        self.report()

    def report(self):
        print("Printing statistics")
        print("Backtracked {} total steps".format(self.events['backtracks']))

        if 'failed' in self.events:
            print("Failed {} time(s) to make a valid draw".format(
                self.events['failed'])
            )
        for row in self.stats.most_common(5):
            print("{0[0][0]:>8} => {0[0][1]:>8} : {0[1]} times".format(row))
        print("...")
        for row in self.stats.most_common()[:-6:-1]:
            print("{0[0][0]:>8} => {0[0][1]:>8} : {0[1]} times".format(row))

    def runone(self):
        "Create a random list"
        people = self.get_people()
        excludes = self.set_exclusions(people)
        try:
            exchange = Hat(people, excludes).draw()
        except NoValidDraw:
            print("Could not make a draw for %s exclude:%s" %
                (people, excludes))
            return
        return exchange

    def get_people(self):
        cursor = self.db.cursor()

        cursor.execute("select member from gift_exchange where name='%s'" %
            (self.args.exchange))
        return [x[0] for x in cursor.fetchall()]

    def set_exclusions(self, people):
        cursor = self.db.cursor()
        query = """select from_whom, to_whom from exclude where
                 from_whom in (%s)""" % ','.join('?' * len(people))
        rows = cursor.execute(query, people)

        excludes = defaultdict(set)
        for row in rows:
            excludes[row[0]].add(row[1])

        return dict(excludes)

if __name__ == '__main__':
    ExerciseHat().run()

