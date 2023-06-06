import sqlite3

db = sqlite3.connect("App.db")

for i in db.execute("SELECT name FROM sqlite_master WHERE type='table'"):
    tables = i[0].split("=")
    if len(tables) > 1:
        print(i)