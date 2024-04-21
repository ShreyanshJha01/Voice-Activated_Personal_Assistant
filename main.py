import pyttsx3 as p
import speech_recognition as sr
from Selenium_web import *
from YT_auto import *
#from New import *

from jokes import *

#from weather import *
import randfacts
import datetime
engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',190 )
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(text):
    engine.say(text)
engine.runAndWait()
print("Hi. I am your virtual assistant.")
speak("Hi. I am your virtual assistant.")
today_date=datetime.datetime.now()
print("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") +
", and its currently " + (today_date.strftime("%I")) + (today_date.strftime("%M")) +
(today_date.strftime("%p")))
speak("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + ",and its currently " + (today_date.strftime("%I")) + (today_date.strftime("%M")) +
(today_date.strftime("%p")))
#print("The temperature in Vellore is " + str(temp()) + " degree celsius and with " +
#str(des()) + ". How are you doing today?")
#speak("The temperature in Vellore is " + str(temp()) + " degree celsius and with " +
#str(des()) + ". How are you doing today?"
r =sr.Recognizer()
def microphone():
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1)
    print("listening...")
    audio =r.listen(source)
    text = r.recognize_google(audio)
    return text
text1 =microphone()
print(text1)
if "what" and "about" and "you" in text1:
    print("I am also having a good day sir.")
    speak("I am also having a good day sir.")
    print("What can I do for you?")
    speak("What can I do for you?")
text2 = microphone()
print(text2)
if "play" and "song" in text2:
    print("Sure. Which song do you want me to play?")
    speak("Sure. Which song do you want me to play?")
    vid = microphone()
    print(vid)
    print("Playing {} on youtube".format(vid))
    speak("Playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)
elif "information" in text2:
    print("Sure. You need information related to which topic?")
    speak("Sure. You need information related to which topic?")
    info = microphone()
    print(info)
    print("Searching {} in wikipedia".format(info))
    speak("Searching {} in wikipedia".format(info))
    assist = infow()
    assist.get_info(info)
#elif "news" in text2:
#    print("Sure. Now I will read the news for you.")
 #   speak("Sure. Now I will read the news for you.")
  #  arr=news()
   # for i in range(len(arr)):
    #    print(arr[i])
     #   speak(arr[i])
elif "fact" in text2:
    speak("Sure sir.")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that, "+x)
elif "joke" in text2:
    arr = joke()
    speak("Sure. Get ready for some chuckles.")
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])
else:
    print("Sorry. I am not programmed to do that yet.")
    speak("Sorry. I am not programmed to do that yet.")