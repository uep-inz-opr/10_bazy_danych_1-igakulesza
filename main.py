import pymysql
import csv
import datetime

plik_csv = open('polaczenia_duze.csv', 'r')
czytaj = csv.reader(plik_csv,delimiter='|')

connection = pymysql.connect(host='ego.kie.ue.poznan.pl', port = 8080, user='inz_opr', passwd='inz_opr', database='inzynieria_oprogramowania')
cursor = connection.cursor()

for i, rekord in enumerate(czytaj):
    if i == 0:
        pass
    else:
        from_user = int(rekord[0])
        to_user = int(rekord[1])
        duration = int(rekord[3])
        cell_tower = int(rekord[4])
        year, month, day, hour, minute = [rekord[2][0:4], rekord[2][4:6], rekord[2][6:8], rekord[2][9:11], rekord[2][11:]]
        connection_datetime =  '-'.join([year, month, day]) + ' ' + ':'.join([hour, minute, '00'])
        query = 'insert into polaczenia(`from` , `to` , `datetime` , `duration` , `celltower`) values (%s, %s, %s, %s, %s)'
        cursor.execute(query, (from_user, to_user, connection_datetime, duration, cell_tower))
                       
connection.commit()
