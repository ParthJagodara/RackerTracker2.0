#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('rackertracker.db')

with con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    print "SQLite version: %s" % data 

con2 = lite.connect('tracker.db')

with con2:

    cur1 = con2.cursor()
    cur1.execute('SELECT SQLITE_VERSION()')

    data = cur1.fetchone()
    print "SQLite version: %s" % data
    
    cur1.execute("SELECT email FROM user")
    rackers = cur1.fetchall()

with con:
    for racker in rackers:
	i = racker[0].index('@')
	cur.execute("insert into rackertracker_racker (email,name) values (?,?)", (racker[0],racker[0][:i])) 

with con2:
    
    cur1.execute("select * from workout")
    
    workouts = cur1.fetchall()
    workouts_len = len(workouts)
    print workouts_len

with con:

    cur = con.cursor()

    count = 0

    while count < workouts_len:
        cur.execute("select id from rackertracker_racker where email=:email", {"email": workouts[count][0]})
	id_object = cur.fetchone()
	id = id_object[0]
	cur.execute("insert into rackertracker_workout (racker_id,date) values (?,?)", (id,workouts[count][1]))
	print count
	count = count+1
	
