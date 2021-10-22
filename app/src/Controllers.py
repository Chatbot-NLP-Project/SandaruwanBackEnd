from flask import Blueprint, render_template, request, redirect, url_for, session
import bcrypt
from flask import jsonify
from flask_mysqldb import MySQL, MySQLdb
import re
import datetime



def getDoctor(mysql):
    specialty = request.get_json()['specialist']
    specialty = specialty.upper()
    print(specialty)
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('select * from Doctor where specialty = % s', (specialty,))
    doctors = cur.fetchall()
    if len(doctors) == 0:
        return jsonify(doc=doctors, er=1)
    else:
        return jsonify(doc=doctors, er=0)


def channelDoctor(mysql):
    channelObject = request.get_json()['channel']
    userID = channelObject["userID"]
    docID = channelObject["id"]
    date = channelObject["date"]
    time = channelObject["time"]
    hospital = channelObject["hospital"]
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('select * from Channel where doctor = % s AND date = % s AND time = % s', (docID, date, time))
    doctors = cur.fetchall()
    print(request.get_json()['channel'])

    if len(doctors) != 0:
        return jsonify(doc=doctors, er=1)
    else:
        cur.execute('INSERT INTO Channel (doctor,userID, time,date,hospital) VALUES (%s,%s,%s,%s,%s)',
                    (docID, userID, time, date, hospital))
        mysql.connection.commit()
        return jsonify(doc=doctors, er=0)


def sendFeedback(mysql):
    feedBack = request.get_json()['feedback']
    userID = feedBack["userID"]
    fb = feedBack["msg"]
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('INSERT INTO Feedback (user_id,feedback) VALUES (%s,%s)', (userID, fb))
    mysql.connection.commit()
    return "successful"


def getClinic(mysql):
    clinicType = request.get_json()['clinicType']
    print(clinicType)
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('select * from Clinic where clinicType = % s', (clinicType,))
    clinics = cur.fetchall()
    if len(clinics) == 0:
        return jsonify(clinic=clinics, er=1)
    else:
        return jsonify(clinic=clinics, er=0)


def getEyeClinic(mysql):
    eyeClinicType = request.get_json()['clinicType']
    print(eyeClinicType)
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('select * from EyeClinic where clinicType = % s', (eyeClinicType,))
    clinics = cur.fetchall()
    print(clinics)
    if len(clinics) == 0:
        return jsonify(clinic=clinics, er=1)
    else:
        return jsonify(clinic=clinics, er=0)
