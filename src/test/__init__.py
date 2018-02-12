""" Common pieces for test files """
import os
import sqlite3

HERE = os.path.dirname(__file__)

def suck_database(path):
    " Create memory database from database on disk "

    dsk = sqlite3.connect(path)
    mem = sqlite3.connect(":memory:")
    cursor = mem.cursor()

    lines = '\n'.join(dsk.iterdump())
    cursor.executescript(lines)
    mem.commit()

    return mem

def reldir(file):
    return os.path.join(HERE, "data", file)

def relfile_list(files):
    return [open(reldir(file_name), 'r') for file_name in files]

