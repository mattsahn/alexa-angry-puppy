import logging
import requests
import json
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request

app = Flask(__name__)

ask = Ask(app, "/")

## barks
barks = "https://s3.amazonaws.com/angry-pup/barks_16000.mp3"
growl = "https://s3.amazonaws.com/angry-pup/growl_16000.mp3"
growl2 = "https://s3.amazonaws.com/angry-pup/growl2_16000.mp3"
growl_bark = "https://s3.amazonaws.com/angry-pup/growl_bark_16000.mp3"
bark_angry = "https://s3.amazonaws.com/angry-pup/angry_pup_16000.mp3"
bark_angry2 = "https://s3.amazonaws.com/angry-pup/angry_pup2_16000.mp3"
bark_angry3 = "https://s3.amazonaws.com/angry-pup/angry_pup3_16000.mp3"
bark_once = "https://s3.amazonaws.com/angry-pup/single_bark_16000.mp3"
bark_once2 = "https://s3.amazonaws.com/angry-pup/single_bark2_16000.mp3"
bark_twice = "https://s3.amazonaws.com/angry-pup/bark_twice_16000.mp3"
bark_twice2 = "https://s3.amazonaws.com/angry-pup/bark_twice2_16000.mp3"

@ask.launch

def welome():
    return question("What do you want your pup to do?")

@ask.intent("Bark")
def Bark():
    print("Intent: Bark")
    return question("<speak><audio src='" + barks + "'/> </speak>").reprompt("<speak><audio src='" + bark_twice2 + "'/> </speak>")

@ask.intent("Growl")
def Growl():
    print("Intent: Growl")
    return question("<speak><audio src='" + growl + "'/> </speak>").reprompt("<speak><audio src='" + growl2 + "'/> </speak>")
    
@ask.intent("AngryPup")
def AngryPup():
    print("Intent: AngryPup")
    return question("<speak><audio src='" + bark_angry3 + "'/> </speak>").reprompt("<speak><audio src='" + growl_bark + "'/> </speak>")

@ask.intent("BarkOnce")
def BarkOnce():
    print("Intent: BarkOnce")
    return question("<speak><audio src='" + bark_once + "'/> </speak>").reprompt("<speak><audio src='" + bark_once2 + "'/> </speak>")

@ask.intent("BarkTwice")
def BarkTwice():
    print("Intent: BarkTwice")
    return question("<speak><audio src='" + bark_twice2 + "'/> </speak>").reprompt("<speak><audio src='" + growl_bark + "'/> </speak>")
    
@ask.intent("GrowlBark")
def GrowlBark():
    print("Intent: GrowlBark")
    return question("<speak><audio src='" + growl_bark + "'/> </speak>").reprompt("<speak><audio src='" + bark_once2 + "'/> </speak>")
    

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