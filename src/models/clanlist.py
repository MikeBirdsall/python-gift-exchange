""" clanlist manage a list of members in a clan """
import sqlite3

DATABASE = "./database"


class XmasListException(Exception):
    pass


class XmasNoClan(XmasListException):
    pass


class clanlist:

    def __init__(self, clanname=None, clanid=None):
        self.__clanname = None
        self.__clanid = None
        self.cursor = None
        if clanname and clanid:
            raise ValueError
        if clanname:
            self.clanname = clanname
        if clanid:
            self.clanid = clanid

    def connect_database(self):
        conn = sqlite3.connect(DATABASE)
        self.cursor = conn.cursor()

    def from_database(self, sql, parm):
        self.connect_database()
        return self.cursor.execute(sql, (parm,)).fetchone()[0]

    @property
    def clanname(self):
        if not self.__clanname and not self.__clanid:
            raise XmasNoClan
        elif not self.__clanname:
            sql = "select clanname from clan where id = ?"
            self.__clanname = self.from_database(sql, self.__clanid)
        return self.__clanname

    @clanname.setter
    def clanname(self, name_):
        if not self.__clanid:
            self.__clanname = name_

    @property
    def clanid(self):
        if not self.__clanname and not self.__clanid:
            raise XmasNoClan
        elif not self.__clanid:
            sql = "select id from clan where clanname = ?"
            self.__clanid = self.from_database(sql, self.__clanname)
        return self.__clanid

    @clanid.setter
    def clanid(self, id_):
        if not self.__clanname:
            self.__clanid = id_


if __name__ == "__main__":
    for y in [1, 2]:
        x = clanlist()
        x.clanid = y
        print(x.clanname)
