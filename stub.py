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

    response = VoiceResponse()
    gather = Gather(num_digits =1,action = '/procNumbers')

    gather.say('For Dining press 1, for busses press 2')
    response.append(gather)
    response.redirect('/')
    return str(response)


@app.route('/procNumbers', methods = ['GET','POST'])
def proc():

    response = VoiceResponse()
    if 'Digits' in request.values:
        if request.values['Digits'] == '1':
             #send dining data

             gather = Gather(num_digits =1,action = '/dining')
             gather.say("For Brower press 1, For Busch Press 2, For Livingston Press 3, For Neilson Press 4")
             response.append(gather)
             return (str(response))
        elif request.values['Digits'] =='2':
            #send bus flow
            pass
        else: 
            response.say("Dont Understand my duders")
            return str(response)
    else:
        response.say("wat");
        return(str(response))

@app.route("/dining",methods = ["GET","POST"])
def dining():

    response = VoiceResponse()
    if 'Digits' in request.values:
        numb = request.values['Digits']
        #make rest to rutgers api and parse

        req = requests.get("https://rumobile.rutgers.edu/1/rutgers-dining.txt")
        reqjson = req.json()
        if numb == '1':
            response.say("Brower Bizza is the best Bizza")
            #make the request
            for i in reqjson:
                if i["location_name"] == "Brower Commons":
                    ret_ = printMeals(i,response)
                    return str(ret_)
        elif numb =='2':
            for i in reqjson:
                if i["location_name"] == "Busch Dining Hall":
                    ret_ = printMeals(i,response)
                    return str(ret_)
        elif numb == '3':
            for i in reqjson:
                if i["location_name"] == "Livingston Dining Commons":
                    ret_ = printMeals(i,response)
                    return str(ret_)
        elif numb == '4':
            for i in reqjson:
                if i["location_name"] == "Neilson Dining Hall":
                    ret_ = printMeals(i,response)
                    return str(ret_)
        else:
            response.say("Invalid request")
            return str(response)
    else:
        response.say("Invalid")
        return str(response)






        



