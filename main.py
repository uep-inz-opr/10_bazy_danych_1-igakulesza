import requests
import csv

import sqlite3

if __name__ == '__main__':
    file = input()

    open('file.csv', 'r')
    con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cursor = con.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS polaczenia_duze (
    from_subscriber INTEGER, to_subscriber INTEGER,  datetime TIMESTAMP, duration INTEGER, celltower INTEGER);''')
    with open(file, 'r') as a_file:
        reader = csv.reader(a_file, delimiter=",")
        next(reader, None)
        rows = [row for row in reader]
        cursor.executemany("INSERT INTO polaczenia_duze VALUES (?, ?, ?, ?, ?)", rows)

    query2 = 'select sum(duration) from polaczenia_duze'

    cursor.execute(query2)

    for i in cursor:
        print(i)
