""" clans manages the set of all clans """
import sqlite3
from bidict import bidict

DATABASE = "./database"

class clans:

    def __init__(self):
        conn = sqlite3.connect(DATABASE)
        self.cursor = conn.cursor()
        sql = "select id, clanname from clan"
        allclans = self.cursor.execute(sql).fetchall()
        self.id2name = bidict(allclans)

    def namelist(self):
        return(list(self.id2name.values()))