import logging
import requests
import json
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request

app = Flask(__name__)

ask = Ask(app, "/")


## barks
growl_bark = "https://s3.amazonaws.com/angry-pup/growl_bark_16000.mp3"
bark_angry = "https://s3.amazonaws.com/angry-pup/angry_pup_16000.mp3"
bark_angry2 = "https://s3.amazonaws.com/angry-pup/angry_pup2_16000.mp3"
bark_once = "https://s3.amazonaws.com/angry-pup/single_bark_16000.mp3"
bark_twice = "https://s3.amazonaws.com/angry-pup/bark_twice_16000.mp3"
bark_twice2 = "https://s3.amazonaws.com/angry-pup/bark_twice2_16000.mp3"

@ask.launch

def welome():
    return question("What do you want your pup to do?")

@ask.intent("AngryPup")

def angry_pup():
    return question("<speak><audio src='" + bark_angry + "'/> </speak>").reprompt("<speak><audio src='" + growl_bark + "'/> </speak>")

@ask.intent("BarkOnce")

def BarkOnce():
    return question("<speak><audio src='" + bark_once + "'/> </speak>").reprompt("<speak><audio src='" + bark_twice + "'/> </speak>")

@ask.intent("BarkTwice")

def BarkTwice():
    return question("<speak><audio src='" + bark_twice2 + "'/> </speak>").reprompt("<speak><audio src='" + growl_bark + "'/> </speak>")
    
@ask.intent("GrowlBark")

def GrowlBark():
    return question("<speak><audio src='" + growl_bark + "'/> </speak>").reprompt("<speak><audio src='" + bark_angry2 + "'/> </speak>")
    

## Amazon built-in intents
##

@ask.intent("AMAZON.StopIntent")

def stop():
    return statement("<speak>Ok, goodbye. <audio src='" + bark_once + "'/> </speak>")
 

@ask.intent("AMAZON.HelpIntent")

def help():
    return question("<speak>Hello, there is an Angry puppy here <audio src='" + bark_once + "'/> You can play with him by asking him to bark, growl, bark twice and be quiet </speak>").reprompt("What do you want the puppy to do?")


@ask.intent("AMAZON.CancelIntent")

def cancel():
    return statement("<speak>Ok, goodbye. <audio src='" + bark_once + "'/> </speak>")
    

## BEGIN Run Server
## ----------------
if __name__ == '__main__':

    app.run(debug=True)

## END of Server