import sqlite3

conn = sqlite3.connect("users_data.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
    name varchar(40) NOT NULL,
    mail text NOT NULL,
    username varchar(20) NOT NULL,
    password varchar(30) NOT NULL
);
""")

