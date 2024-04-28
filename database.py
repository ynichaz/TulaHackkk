import sqlite3

#создание бд и таблицы admins
with sqlite3.connect('/Users/varya_kurkubet/Desktop/database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS admins (id INTEGER PRIMARY KEY, username TEXT NOT NULL) """
    query1 = """ INSERT INTO admins (username) VALUES('615000137') """
    query2 = """ INSERT INTO admins (username) VALUES('901771297') """
    query3 = """ INSERT INTO admins (username) VALUES('tosha') """
    query4 = """ INSERT INTO admins (username) VALUES('kodzuken') """
    query5 = """ INSERT INTO admins (username) VALUES('cachenn') """
    cursor.execute(query2)

db.close()

