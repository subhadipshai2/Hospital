import speech_recognition as sr 
import os
import webbrowser
import openai
from config import apikey
import datetime
import random 


def chat(query):

def ai():
    openai.api_key = apikey
    text = f"OpenAI response for Pormt: {prompt} \n******************************************\n\n"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    prensence_penalty=0
)

print(response["choices"][0]["text"])
text += response["choices"][0]["text"]) 
if not os.path.exits("openai")
     os.mkdir("openai")

#with open("f"prompt- {random.randitnt(1,2343434356)}","w") as f:
    with open("f"prompt[0:30] }","w") as f:
          f.write(text)
def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshould =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language="en-in,bn-gb,hi-in")
            print(f"User said: {query}")
            return query
        except exceptions as e:
            return "some error occurred.sorry from jenney: " + str(e)
if __name__=='__main__':
   print('VS code')
   say("Hello I am jenny,your hospital facality pratner.")
   while True:
       print("Listening.....")
       query = takeCommand()
       sites = [["You Tube","https://www.youtube.com/"],["google","https://www.google.com"],["wikipedia","https://www.wikipedia.com"]]
       for site in sites:
           if f"Open {site[0]}".lower() in query.lower():
           say(f"Opening {site[0]}sir...")
           webbrowser.open(site[1])

        if "the time" in query:
           
           hour = datetime.datetime.now().strtime("%H")
           min = datetime.datetime.now().strtime("%M")
           say(f"sir the time is {hour} hours {min} minutes")
           
        elif "using Aritificial intelligence".lower()in query.lower():
           ai(prompt=query)

else:
    chat(query)

       


   