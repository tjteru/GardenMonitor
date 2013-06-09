#!/usr/bin/python
#
# Uses library from https://github.com/kasun/python-tail
#
#
<<<<<<< HEAD

'''
 PushData-incremental.py

=======
'''
 PushData-incremental.py

>>>>>>> 8327f232b911969d2b57fffbf75dc579678fa5cf
 created 7 June, 2013
 Modified 7 June, 2013
 by Erik Meike (erik [at] tribeawsome [dot] com)
 
 This code is in the public domain.  I hereby grant a nonexclusive worldwide
 license to use this code for any purpose.  No warranty expressed or implied.

'''
from time import sleep
import csv
import MySQLdb
<<<<<<< HEAD
import os, sys, inspect


=======
>>>>>>> 8327f232b911969d2b57fffbf75dc579678fa5cf
from localInfo import *

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


t = tail.Tail(logfile)

t.register_callback(insertData)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
hst, usr, passwd, db = readLocalInfo()

>>>>>>> 8327f232b911969d2b57fffbf75dc579678fa5cf
=======
hst, usr, passwd, db = readLocalInfo()

>>>>>>> 8327f232b911969d2b57fffbf75dc579678fa5cf
=======
hst, usr, passwd, db = readLocalInfo()

>>>>>>> 8327f232b911969d2b57fffbf75dc579678fa5cf
mydb = MySQLdb.connect(host=hst,
                       user=usr,
                       passwd=passwd,
                       db=dbase)
cursor = mydb.cursor()

t.follow(s=5)


cursor.close()
