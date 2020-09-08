import sqlite3





class DataBase:
    __cur: sqlite3.Cursor = None
    __conn: sqlite3.connect = None


    def __init__(self, dbname):
        self.__conn = sqlite3.connect(dbname)
        self.__cur = self.__conn.cursor()
        self.__cur.execute(
            "CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER , isbn INTEGER )")
        self.__conn.commit()

    def get_all(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows

    def insert(self, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES(NULL, ?,?,?,?)", (title, author, year, isbn))
        conn.commit()
        conn.close()

    def search(self, title="", author="", year="", isbn=""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self, id):
        self.__conn = sqlite3.connect("books.db")
        self.__cur = self.__conn.cursor()
        self.__cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.__conn.commit()
        self.__conn.close()

    def update(self, id, title, author, year, isbn):
        self.__conn = sqlite3.connect("books.db")
        self.__cur = self.__conn.cursor()
        self.__cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.__conn.commit()
        self.__conn.close()

    def close_connection(self):
        if self.__conn is not None:
            self.__conn.close()

    def __del__(self):
        self.close_connection()
