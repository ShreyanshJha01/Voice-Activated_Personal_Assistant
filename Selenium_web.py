from selenium import webdriver
import pyttsx3 as px
engine = px.init()
engine.setProperty('rate',190)
def speak(text):
    engine.say(text)
    engine.runAndWait()
class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\\Drivers\\chromedriver.exe')
    def get_info(self,query):
        self.query = query
        self.driver.get(url="https://en.wikipedia.org/wiki/"+query)