import os
import urllib
import urllib2
import json
from naoqi import ALProxy
import time

api_key = os.getenv("OPENAI_API_KEY")
tts = ALProxy("ALTextToSpeech", "192.168.60.80", 9559)
stt = ALProxy("ALSpeechRecognition", "192.168.60.80", 9559) # might not exist

stt.setLanguage("English")

with open(r"C:\Users\Sasha\Documents\Uni\Extension_Programming\Softbank\Pepper-Translator\english3.txt") as f:
    words = f.read().splitlines()

stt.setVocabulary(words)

#TODO Pepper Listening
speech_heard = False
while True:
    tts.say("Hi, my name is Pepper. Can I help you with anything?")
    stt.subscribe("Test_STT")
    time.sleep(20)
    stt.unsubscribe("Test_STT")

    #TODO Speech to text
    if speech_heard == True:
        break
    else:
        # wait XX number of seconds
        x = 1 # filler code

#TODO Run gcloud function from propmt
# To delete test variables language and message
language = "Chinese"
message = "Test message"

url = "https://callgpt-gemqjtz7eq-ts.a.run.app"
values = {"api_key": api_key,
        "language": language,
        "message": message}
headers = {"Authorization":"bearer $(gcloud auth print-identity-token)",
        "Content-Type": "application/json"}

data = json.dumps(values, indent=len(values))
req = urllib2.Request(url, data, headers)
url_response = urllib2.urlopen(req)
translated_message = url_response.read()
print(translated_message)

#TODO Say to user
tts.say(message + " translated into " + language + " is " + translated_message)