import sqlite3

conn = sqlite3.connect("users_data.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id integer AUTOINCREMENT NOT NULL,
    name varchar(40) NOT NULL,
    mail text NOT NULL,
    username varchar(20) NOT NULL,
    password varchar(30) NOT NULL,
    PRIMARY KEY(id)
);
""")
