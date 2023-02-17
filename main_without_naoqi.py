import os
import urllib
# import urllib2
import json
import time

api_key = os.getenv("OPENAI_API_KEY")

############################################################################################################################

#TODO Pepper Listening
import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

mic_name = 'Microphone (Arctis 5 Chat)'
mic = sr.Microphone(device_index=sr.Microphone.list_microphone_names().index(mic_name))

# Start listening
try:
    with sr.Microphone(device_index=sr.Microphone.list_microphone_names().index(mic_name)) as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
except:
    sr.WaitTimeoutError

print("Processing...")

try:
    text = r.recognize_google(audio)
    print("You said: ", text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

############################################################################################################################





# #TODO Run gcloud function from propmt
# # To delete test variables language and message
# language = "Chinese"
# message = "Test message"

# url = "https://callgpt-gemqjtz7eq-ts.a.run.app"
# values = {"api_key": api_key,
#         "language": language,
#         "message": message}
# headers = {"Authorization":"bearer $(gcloud auth print-identity-token)",
#         "Content-Type": "application/json"}

# data = json.dumps(values, indent=len(values))
# req = urllib.Request(url, data, headers)
# url_response = urllib.urlopen(req)
# # req = urllib2.Request(url, data, headers)
# # url_response = urllib2.urlopen(req)
# translated_message = url_response.read()
# # print(translated_message)

# #TODO Say to user
# print(message + " translated into " + language + " is " + translated_message)