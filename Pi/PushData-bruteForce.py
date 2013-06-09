#!/usr/bin/python
#
#
#
'''
 PushData-bruteForce.py

 created 7 June, 2013
 Modified 7 June, 2013
 by Erik Meike (erik [at] tribeawsome [dot] com)
 
 This code is in the public domain.  I hereby grant a nonexclusive worldwide
 license to use this code for any purpose.  No warranty expressed or implied.

'''

import csv
import MySQLdb
from localInfo import *

mydb = MySQLdb.connect(host=hst,
                       user=usr,
                       passwd=passwd,
                       db=dbase)
cursor = mydb.cursor()

csv_data = csv.reader(file(logfile))

numrows = 0
numerrors = 0
for row in csv_data:
    numrows += 1
    for value in row:
        value = value.strip().strip('\'').strip()

    sql = 'INSERT INTO aerodata (time, id, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12) VALUES(FROM_UNIXTIME(%s), "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (int(round(float(row[0]))), row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])
    #print sql
    try:
        cursor.execute(sql)
    except MySQLdb.IntegrityError:
        #print "Duplicate entry: " + sql
        numerrors += 1
    
    except:
        print sys.exc_info()[0]

#close the connection to the database.
mydb.commit()
print "Done,", numrows-numerrors, "out of", numrows, "row(s) were added"


cursor.close()
