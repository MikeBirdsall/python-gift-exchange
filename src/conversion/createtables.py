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
        userid text unique not null,
        fullname text unique not null,
        nickname text,
        birthday text,
        email text)''')

    cursor.execute('''CREATE TABLE wish(
        id integer primary key autoincrement not null,
        created text,
        by integer references person,
        for integer references person,
        description text,
        numberwanted integer,
        expires text)''')

    cursor.execute('''CREATE TABLE gift(
        id integer primary key autoincrement not null,
        bought text,
        wishid references wish,
        by references person,
        for references person,
        note text,
        numberbought integer)''')


def main():
    parser = argparse.ArgumentParser(
        description="Create tables for wishlist conversion")
    parser.add_argument("database", help="Database created or updated")

    args = parser.parse_args()

    create_tables(args.database)

if __name__ == "__main__":
    main()
