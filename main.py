import pyttsx3 as p
import speech_recognition as sr
import webbrowser
import requests
import randfacts
import datetime
from jokes import *


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

print("Hi, I am your virtual assistant.")
speak("Hi, I am your virtual assistant.")
today_date = datetime.datetime.now()
date_info = f"Today is {today_date.strftime('%d')} of {today_date.strftime('%B')}, and it's currently {today_date.strftime('%I:%M %p')}"
print(date_info)
speak(date_info)

r = sr.Recognizer()

def microphone():
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            speak("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak(f"Could not request results; {e}")
            return ""

while True:
    text1 = microphone()
    print(text1)

    if "bye" in text1:
        print("Ending program.")
        speak("Ending program.")
        break

    if "what" in text1 and "about" in text1 and "you" in text1:
        print("I am also having a good day.")
        speak("I am also having a good day.")
        print("What can I do for you?")
        speak("What can I do for you?")

    elif "play" in text1 and "song" in text1:
        print("Sure. Which song do you want me to play?")
        speak("Sure. Which song do you want me to play?")
        
        song = microphone()
        print(f"Playing '{song}' on YouTube.")
        speak(f"Playing '{song}' on YouTube.")
        
        search_url = f"https://www.youtube.com/results?search_query={song.replace(' ', '+')}"
        response = requests.get(search_url)
        
        if response.status_code == 200:
            search_result_page = response.text
            start_index = search_result_page.find('watch?v=')
            
            if start_index != -1:
                end_index = search_result_page.find('"', start_index)
                video_url = "https://www.youtube.com/" + search_result_page[start_index:end_index]
                webbrowser.open(video_url)
            else:
                print("Sorry, couldn't find the requested song on YouTube.")
                speak("Sorry, couldn't find the requested song on YouTube.")
        else:
            print("Failed to fetch YouTube search results.")
            speak("Failed to fetch YouTube search results.")

    elif "information" in text1:
        print("Sure. You need information related to which topic?")
        speak("Sure. You need information related to which topic?")
        info = microphone()
        print(f"Searching {info} in Wikipedia.")
        speak(f"Searching {info} in Wikipedia.")
        wiki_url = f"https://en.wikipedia.org/wiki/{info.replace(' ', '_')}"
        webbrowser.open(wiki_url)

    elif "fact" in text1:
        speak("Sure.")
        fact = randfacts.get_fact()
        print(fact)
        speak(f"Did you know that {fact}")

    elif "joke" in text1:
        joke_arr = joke()
        speak("Sure. Get ready for some chuckles.")
        print(joke_arr[0])
        speak(joke_arr[0])
        print(joke_arr[1])
        speak(joke_arr[1])

    else:
        print("Sorry, I am not programmed to do that yet.")
        speak("Sorry, I am not programmed to do that yet.")
