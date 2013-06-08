#!/usr/bin/python
#
# Uses library from https://github.com/kasun/python-tail
#
#
#
#

from time import sleep
import csv
import MySQLdb

import tail

def insertData(text):
    text = text.strip()
    row = text.split(", ")
    for value in row:
        value = value.strip().strip('\'').strip()
    sql = 'INSERT INTO aerodata (time, id, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12) VALUES(FROM_UNIXTIME(%s), "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (int(round(float(row[0]))), row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])
    #print row, sql

    try:
        cursor.execute(sql)
    except MySQLdb.IntegrityError:
        #print "Duplicate entry: " + sql
        pass
    except:
        print sys.exc_info()[0]

    mydb.commit()
    print "Done"


t = tail.Tail('../log.csv')

t.register_callback(insertData)

mydb = MySQLdb.connect(host='host',
                       user='user',
                       passwd='password',
                       db='database')
cursor = mydb.cursor()

t.follow(s=5)


cursor.close()