from flask import Blueprint, render_template, request, redirect, url_for, session
import bcrypt
from flask import jsonify
from flask_mysqldb import MySQL,MySQLdb
import re
import datetime


def getDoctor(mysql):
    specialty = request.get_json()['specialist']
    specialty = specialty.upper()
    print(specialty)
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('select * from doctor where specialty = % s', (specialty, ))
    doctors = cur.fetchall()
    if len(doctors) ==0:
        return jsonify(doc=doctors,er=1)
    else:
        return jsonify(doc = doctors,er=0)

def channelDoctor(mysql):
    channelObject = request.get_json()['channel']
    docID = channelObject["id"]
    date = channelObject["date"]
    time = channelObject["time"]
    hospital = channelObject["hospital"]
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('select * from channel where doctor = % s AND date = % s AND time = % s', (docID,date,time ))
    doctors = cur.fetchall()
    print(request.get_json()['channel'])

    if len(doctors) != 0:
        return jsonify(doc=doctors, er=1)
    else:
        cur.execute('INSERT INTO channel (doctor,userID, time,date,hospital) VALUES (%s,%s,%s,%s,%s)',(docID,1,time,date,hospital))
        mysql.connection.commit()
        return jsonify(doc=doctors, er=0)

