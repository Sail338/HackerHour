from flask import Flask,request
from twilio.twiml.voice_response import Play, VoiceResponse, Say,Gather
import requests
app = Flask(__name__)

def printMeals(jsonToPrint,response):

    for i in jsonToPrint['meals']:
        print(i)
        response.say("For" + i['meal_name'])
        if 'genres' in i:
            for j in i['genres']:
                for k in j['items']:
                    response.say(k)
        return response

@app.route('/')
def hello_world():
    pass


@app.route('/procNumbers', methods = ['GET','POST'])
def proc():
    pass

@app.route("/dining",methods = ["GET","POST"])
def dining():
    pass
