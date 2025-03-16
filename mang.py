import sys 
import subprocess
import threading
import webbrowser
import pyttsx3
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QPushButton  , QVBoxLayout #type:ignore
from PyQt5.QtGui import QFont  #type:ignore
from PyQt5.QtCore import QTimer , QTime , Qt , pyqtSignal , QObject  #type:ignore

# initialise the speech recognizer and text-to-speech engine 
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
   engine.say(text)
   engine.runAndWait()
   
app_dict = {
   'copilot' :  "https://copilot.microsoft.com",
   'chatgpt' : "https://openai.com/",
'notepad': "notepad.exe",
    'calculator': "calc.exe",
     'chrome': "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    'excel': "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    'word': "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    'powerpoint': "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    'mysql': "C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql.exe",
    'google': "https://www.google.com", 
    'bing': "https://www.bing.com",  # Bing Search
    'duckduckgo': "https://duckduckgo.com",  # DuckDuckGo Search

    # Social Media
    'facebook': "https://www.facebook.com",  # Facebook
    'instagram': "https://www.instagram.com",  # Instagram
    'twitter': "https://www.twitter.com",  # Twitter
    'linkedin': "https://www.linkedin.com",  # LinkedIn
    'reddit': "https://www.reddit.com",  # Reddit
    'pinterest': "https://www.pinterest.com",  # Pinterest

    # Video Streaming
    'youtube': "https://www.youtube.com",  # YouTube
    'netflix': "https://www.netflix.com",  # Netflix
    'amazon prime': "https://www.primevideo.com",  # Amazon Prime Video
    'disney plus': "https://www.disneyplus.com",  # Disney+
    'twitch': "https://www.twitch.tv",  # Twitch

    # Productivity
    'gmail': "https://mail.google.com",  # Gmail
    'outlook': "https://outlook.live.com",  # Outlook Web
    'google drive': "https://drive.google.com",  # Google Drive
    'dropbox': "https://www.dropbox.com",  # Dropbox
    'onedrive': "https://onedrive.live.com",  # OneDrive

    # Education
    'wikipedia': "https://www.wikipedia.org",  # Wikipedia
    'coursera': "https://www.coursera.org",  # Coursera
    'udemy': "https://www.udemy.com",  # Udemy
    'khan academy': "https://www.khanacademy.org",  # Khan Academy

    # News
    'bbc': "https://www.bbc.com",  # BBC News
    'cnn': "https://www.cnn.com",  # CNN
    'nytimes': "https://www.nytimes.com",  # The New York Times

    # Shopping
    'amazon': "https://www.amazon.com",  # Amazon
    'flipkart': "https://www.flipkart.com",  # Flipkart
    'ebay': "https://www.ebay.com",  # eBay

    # Entertainment
    'spotify': "https://www.spotify.com",  # Spotify
    'soundcloud': "https://www.soundcloud.com",  # SoundCloud
    'imdb': "https://www.imdb.com",  # IMDb

    # Tech
    'github': "https://www.github.com",  # GitHub
    'stackoverflow': "https://stackoverflow.com",  # Stack Overflow
    'medium': "https://www.medium.com",  # Medium

    # Communication
    'whatsapp web': "https://web.whatsapp.com",  # WhatsApp Web
    'telegram web': "https://web.telegram.org",  # Telegram Web
    'zoom web': "https://zoom.us",  # Zoom Web
    'slack web': "https://slack.com",  # Slack Web
    'discord web': "https://discord.com"

    
}
def open_app(app_name):
   app_name = app_name.lower().strip()
   if app_name in app_dict:
      if app_name in ['notepad' , 'calculator' , 'chrome' , 'excel' , 'word' , 'powerpoint' , 'mysql']:
         subprocess.Popen(app_dict[app_name])
         
      else:
         webbrowser.Popen(app_dict[app_name])
      
   else:
      speak(f"sorry , i don't know how to open {app_name}")
   
      print(f"sorry , i dont know how to open the {app_name}")
   

def handle_response(command):
   polite_responses = {
    # Greetings
    "hello": "Hi! How can I assist you today?",
    "hi": "Hey there! What can I do for you?",
    "good morning": "Good morning! How can I make your day better?",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! What can I do for you?",
    "good night": "Good night! Rest well and take care!",

    # Gratitude
    "thanks": "You're welcome! Happy to help.",
    "thank you": "You're welcome! I'm always here.",
    "thank you so much": "You're very welcome! It's my pleasure to help.",
    "thanks a lot": "You're welcome! Let me know if you need anything else.",

    # Apologies
    "sorry": "No problem! Don't worry about it.",
    "i apologize": "No need to apologize! Everything is fine.",
    "my bad": "It's okay! We all make mistakes.",

    # Polite Requests
    "please": "Sure! How can I assist you?",
    "could you": "Of course! What do you need?",
    "would you": "Absolutely! How can I help?",

    # Compliments
    "you are amazing": "Thank you! You're pretty amazing too!",
    "you are awesome": "Aww, thank you! You're awesome as well!",
    "you are the best": "Thanks! You're the best too!",

    # Encouragement
    "i am feeling sad": "I'm really sorry you're feeling that way. Everything will be alright!",
    "i am happy": "That's great! I'm glad you're feeling good!",
    "i am stressed": "Take a deep breath. You've got this!",
    "i am tired": "You deserve some rest. Take care of yourself!",

    # Small Talk
    "how are you": "I'm just a program, but thank you for asking! How about you?",
    "how are you doing": "I'm functioning at full capacity! Thanks for asking!",
    "what's up": "Not much, just waiting to assist you. How can I help?",
    "how is your day": "My day is great, thanks for asking! How about yours?",

    # Farewells
    "goodbye": "Goodbye! Have a great day ahead!",
    "see you later": "See you later! Take care!",
    "bye": "Bye! Don't hesitate to reach out if you need anything.",

    # Fun Responses
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "make me laugh": "What do you call fake spaghetti? An impasta!",
    "are you a robot": "I am a virtual assistant, here to help you!",
    "what is your name": "I am your personal assistant. You can call me whatever you like!",
}
   for phrase, response in polite_responses.items():
      if phrase in command:
         speak(response)
         print(response)
         return True
      return False
   
def run_voice_assistant():
   while True:
     try:
        with sr.Microphone as source:
           print('Listening.......')
           recognizer.energy_threshold = 4000
           audio = recognizer.listen(source , timeout=5 , phrase_time_limit=5)
           command = recognizer.recognize_google(source).lower()
           print(f"Your Command : {command}");
           
           if command.startswith('nova'):
                  speak('Hey sir , what can i assist you with ?')
                  command = command[4:].strip()
              
              
                  if handle_response(command):
                     continue
            
                  if "open" in command:
                     app_name = command.replace("open", "").strip()
                     open_app(app_name)
                  else:
                     print("No valid command found")
    
           else:
              speak("I only respond to commands that start with 'nova'.")
              print("I only respond to commands that start with 'nova'.")

     except sr.UnknownValueError:
        print("sorry! , I didn't understand") 
        
     except sr.RequestError:
        print("Could not request results from google speech recognition service.")
        
     except sr.WaitTimeoutError:
        print("no speech detected. Trying again.......")
     except KeyboardInterrupt:
        print("Assistant stoped.")
        
     break
         
           
           
