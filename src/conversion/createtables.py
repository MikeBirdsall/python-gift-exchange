""" Create tables for wishlist application """
import argparse
import sqlite3

def create_tables(db):
    """ Create all the tables from scratch, deleting if need be """

    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    cursor.execute('''DROP TABLE IF EXISTS person''')
    cursor.execute('''DROP TABLE IF EXISTS santalist''')
    cursor.execute('''DROP TABLE IF EXISTS santalistmember''')
    cursor.execute('''DROP TABLE IF EXISTS clan''')
    cursor.execute('''DROP TABLE IF EXISTS clanmember''')
    cursor.execute('''DROP TABLE IF EXISTS wish''')
    cursor.execute('''DROP TABLE IF EXISTS gift''')


    cursor.execute('''CREATE TABLE person(
        id integer primary key autoincrement not null,
        userid text unique not null check (length(userid) <= 30),
        fullname text unique not null,
        nickname text,
        birthday date,
        email text,
        status text check(status in ( 'active', 'hold', 'left' ))
            default 'active'
    )''')

    cursor.execute('''CREATE TABLE wish(
        id integer primary key autoincrement not null,
        when_suggested text,
        by integer references person,
        giftee integer references person,
        description text,
        numberwanted integer,
        expires date
    )''')

    cursor.execute('''CREATE TABLE gift(
        id integer primary key autoincrement not null,
        when_bought text,
        wishid references wish,
        giver references person,
        giftee references person,
        note text,
        numberbought integer,
        givedate text,
        status text check(
            status in ('reserved', 'bought', 'given', 'removed'))
    )''')

    cursor.execute('''CREATE TABLE clan(
        clanname text,
        description text,
        admin references person
    )''')

    cursor.execute('''CREATE TABLE santalist(
        id integer primary key autoincrement not null,
        listname text,
        clan references clan
    )''')


def main():
    parser = argparse.ArgumentParser(
        description="Create tables for wishlist conversion")
    parser.add_argument("database", help="Database created or updated")

    args = parser.parse_args()

    create_tables(args.database)

if __name__ == "__main__":
    main()
