#from flask_mysqldb import MySQL,MySQLdb  

from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_cors import CORS
from app import app
from app import mysql
#A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
#Axios doesnt work without this
# from app.src.Disease import predictDisease
from app.src.HealthcareBot import chat1

CORS(app)

#######################################################
##################''' Controllers '''##################
#######################################################
from app.src import User, Controllers


#######################################################
##################''' User Routes '''##################
#######################################################
@app.route('/register', methods=["GET", "POST"]) 
def register():
    if request.method == 'GET':
        return request.get_json()['email']
    else:
        return User.register(mysql)


@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        return User.login(mysql)
    else:
        return "Done"

@app.route('/logout')
def logout():
    return User.logout()
     
#######################################################
################''' Telecom Routes '''#################
#######################################################

@app.route("/")
def test():
    return {"members":["Member","Hello Sandaruwan"]}

@app.route("/chat")
def chat():
    re = chat1("Hi")
    return {"members":["Member",re]}

@app.route("/reply",methods=["GET","POST"])
def reply():
    if request.method == 'POST':
        # if request.get_json()['msg'] == "Hi":
        re = chat1(request.get_json()['msg'])
        # print(re)
        return {"members": re}

@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method == 'POST':
        # if request.get_json()['msg'] == "Hi":
        # re = predictDisease(request.get_json()['diseases'])
        return {"members": "re"}

@app.route("/getDoc",methods=["GET","POST"])
def add():
    # re = chat1("Hi")
    return Controllers.getDoctor(mysql);


@app.route("/channelDoc",methods=["GET","POST"])
def channel():
    # re = chat1("Hi")

    return Controllers.channelDoctor(mysql);

@app.route("/sendFeedback",methods=["GET","POST"])
def sendFeedback():
    # re = chat1("Hi")
    return Controllers.sendFeedback(mysql);


@app.route("/getClinic", methods=["GET", "POST"])
def getClinic():
    # re = chat1("Hi")
    return Controllers.getClinic(mysql);


@app.route("/getEyeClinic", methods=["GET", "POST"])
def getEyeClinic():
    # re = chat1("Hi")
    return Controllers.getClinic(mysql);