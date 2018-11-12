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
    cursor.execute('''DROP TABLE IF EXISTS santalistdrawing''')
    cursor.execute('''DROP TABLE IF EXISTS santalistexclude''')
    cursor.execute('''DROP TABLE IF EXISTS drawingresult''')
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
        by integer references person(id),
        giftee integer references person(id),
        description text,
        numberwanted integer,
        expires date
    )''')

    cursor.execute('''CREATE TABLE gift(
        id integer primary key autoincrement not null,
        when_bought text,
        wishid integer references wish(id),
        giver integer references person(id),
        giftee integer references person(id),
        note text,
        numberbought integer,
        givedate text,
        status text check(
            status in ('reserved', 'bought', 'given', 'removed'))
    )''')

    cursor.execute('''CREATE TABLE clan(
        id integer primary key autoincrement not null,
        clanname text unique not null,
        description text,
        admin integer references person(id)
    )''')

    cursor.execute('''CREATE TABLE clanmember(
        clanid integer references clan(id),
        userid integer references person(id)
    )''')

    cursor.execute('''CREATE TABLE santalist(
        id integer primary key autoincrement not null,
        listname text,
        clan integer references clan(id)
    )''')

    cursor.execute('''CREATE TABLE santalistmember(
        listid integer references santalist(id),
        userid integer references person(id)
    )''')

    cursor.execute('''CREATE TABLE santalistdrawing(
        id integer primary key autoincrement not null,
        listid integer references santalist,
        title text not null,
        comment text,
        drawdate text,
        giftdate text,
        status text check(
            status in ('active', 'over'))
    )''')

    cursor.execute('''CREATE TABLE santalistexclude(
        listid integer references santalist(id),
        notfrom integer references person(id),
        notto integer references person(id)
    )''')

    cursor.execute('''CREATE TABLE drawingresult(
        id integer primary key autoincrement not null,
        drawing integer references santalistdrawing(id),
        giver integer references person(id),
        giftee integer references person(id)
    )''')

    return cursor


def main():
    parser = argparse.ArgumentParser(
        description="Create tables for wishlist conversion")
    parser.add_argument("database", help="Database created or updated")

    args = parser.parse_args()

    create_tables(args.database)

if __name__ == "__main__":
    main()
