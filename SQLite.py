import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE Initial_Ideas(idea)")
cursor.execute("CREATE TABLE Initial_10_Ideas(idea,vote)")
cursor.execute("CREATE TABLE Top_4_Ideas(idea)")
cursor.execute("CREATE TABLE Developed_Ideas(idea)")
cursor.execute("CREATE TABLE Developed_5_Ideas(idea)")

connection.commit()
cursor.close()
connection.close()
