# Converting hatdraw to the target database tables

The current state:
hat.py has the class that implements the draw - Hat, and an exerciser - ExerciseHat which runs it repeatedly and and generates statistics. 
hatdraw.py has a class has a class - Draw;  which runs it once to create and print out a single valid drawing

The Hat class itself is isolated from the source of the data (the database) but ExerciseHat and Draw each get the data from an obsolete form of database which isn't what will be used in the production version.

This file is used to help in converting them to the new format by spelling out the differences.

The current programs use these tables:

CREATE TABLE exclude(
          id integer primary key autoincrement not null, 
          from_whom text, 
          to_whom text);

CREATE TABLE gift_exchange(
   id integer primary key autoincrement not null,
   name text,
   member text,
   foreign key (member) references person (userid));

A gift exchange is input, the names of the members of the drawing is pulled from the gift exchange table, and pairs of names are gotten from the exclude table. 

In the production form, the appropriate tables are 
santalistdrawing
drawingresult
clan
santalist
santalistmember
santalistexclude
person

One production usecase is to run a drawing.
The inputs are:
    clanname
    listname
    title
    comment
    drawdate
    giftdate

The outputs are to add an entry to the santalistdrawing table:

    CREATE TABLE santalistdrawing(
        id integer primary key autoincrement not null,
        listid integer references santalist,
        title text not null,
        comment text,
        drawdate text,
        giftdate text,
        status text check(status in ('active', 'over'));

and an entry for each draw in the drawingresult table.

    CREATE TABLE drawingresult(
        id integer primary key autoincrement not null,
        drawing integer references santalistdrawing(id),
        giver integer references person(id),
        giftee integer references person(id)
    );

We use the clanname to get the clan id from the clan table:

    CREATE TABLE clan(
        id integer primary key autoincrement not null,
        clanname text unique not null,
        description text,
        admin integer references person(id));

the listname and clan id are used to get the santalist id from the santalist table:

    CREATE TABLE santalist(
        id integer primary key autoincrement not null,
        listname text,
        clan integer references clan(id));

Which is to get userids from the santalistmember table:

    CREATE TABLE santalistmember(
        listid integer references santalist(id),
        userid integer references person(id));

and exclusions from the santalistexclude table,

    CREATE TABLE santalistexclude(
        listid integer references santalist(id),
        notfrom integer references person(id),
        notto integer references person(id));

That's sufficient information to do the drawing. The results are printed using the userid,
which can be gotten from the person table using the userid already gotten from the santalist 
member table.

    CREATE TABLE person(
        id integer primary key autoincrement not null,
        userid text unique not null check (length(userid) <= 30),
        fullname text unique not null,
        nickname text,
        birthday date,
        email text,
        status text check(status in ( 'active', 'hold', 'left' )) default 'active');


