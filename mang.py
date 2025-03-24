import sys
import subprocess
import threading
import webbrowser
import pyttsx3
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt , QTimer , QTime

# Initialize with better defaults
engine = pyttsx3.init()
recognizer = sr.Recognizer()
recognizer.pause_threshold = 1.0  # More natural pause detection

# Your complete application dictionary (unchanged)
app_dict = {
    'copilot': "https://copilot.microsoft.com",
    'chatgpt': "https://openai.com/",
    'notepad': "notepad.exe",
    'calculator': "calc.exe",
    'chrome': "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    'excel': "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    'word': "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    'powerpoint': "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    'mysql': "C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql.exe",
    'google': "https://www.google.com",
    'bing': "https://www.bing.com",
    'duckduckgo': "https://duckduckgo.com",
    'facebook': "https://www.facebook.com",
    'instagram': "https://www.instagram.com",
    'twitter': "https://www.twitter.com",
    'linkedin': "https://www.linkedin.com",
    'reddit': "https://www.reddit.com",
    'pinterest': "https://www.pinterest.com",
    'youtube': "https://www.youtube.com",
    'netflix': "https://www.netflix.com",
    'amazon prime': "https://www.primevideo.com",
    'disney plus': "https://www.disneyplus.com",
    'twitch': "https://www.twitch.tv",
    'gmail': "https://mail.google.com",
    'outlook': "https://outlook.live.com",
    'google drive': "https://drive.google.com",
    'dropbox': "https://www.dropbox.com",
    'onedrive': "https://onedrive.live.com",
    'wikipedia': "https://www.wikipedia.org",
    'coursera': "https://www.coursera.org",
    'udemy': "https://www.udemy.com",
    'khan academy': "https://www.khanacademy.org",
    'bbc': "https://www.bbc.com",
    'cnn': "https://www.cnn.com",
    'nytimes': "https://www.nytimes.com",
    'amazon': "https://www.amazon.com",
    'flipkart': "https://www.flipkart.com",
    'ebay': "https://www.ebay.com",
    'spotify': "https://www.spotify.com",
    'soundcloud': "https://www.soundcloud.com",
    'imdb': "https://www.imdb.com",
    'github': "https://www.github.com",
    'stackoverflow': "https://stackoverflow.com",
    'medium': "https://www.medium.com",
    'whatsapp web': "https://web.whatsapp.com",
    'telegram web': "https://web.telegram.org",
    'zoom web': "https://zoom.us",
    'slack web': "https://slack.com",
    'discord web': "https://discord.com"
}

# Your complete polite responses (unchanged)
polite_responses = {
    "hello": "Hi! How can I assist you today?",
    "hii": "Hey there! What can I do for you?",
    "good morning": "Good morning! How can I make your day better?",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! What can I do for you?",
    "good night": "Good night! Rest well and take care!",
    "thanks": "You're welcome! Happy to help.",
    "thank you": "You're welcome! I'm always here.",
    "thank you so much": "You're very welcome! It's my pleasure to help.",
    "thanks a lot": "You're welcome! Let me know if you need anything else.",
    "sorry": "No problem! Don't worry about it.",
    "i apologize": "No need to apologize! Everything is fine.",
    "my bad": "It's okay! We all make mistakes.",
    "please": "Sure! How can I assist you?",
    "could you": "Of course! What do you need?",
    "would you": "Absolutely! How can I help?",
    "you are amazing": "Thank you! You're pretty amazing too!",
    "you are awesome": "Aww, thank you! You're awesome as well!",
    "you are the best": "Thanks! You're the best too!",
    "i am feeling sad": "I'm really sorry you're feeling that way. Everything will be alright!",
    "i am happy": "That's great! I'm glad you're feeling good!",
    "i am stressed": "Take a deep breath. You've got this!",
    "i am tired": "You deserve some rest. Take care of yourself!",
    "how are you": "I'm just a program, but thank you for asking! How about you?",
    "how are you doing": "I'm functioning at full capacity! Thanks for asking!",
    "what's up": "Not much, just waiting to assist you. How can I help?",
    "how is your day": "My day is great, thanks for asking! How about yours?",
    "goodbye": "Goodbye! Have a great day ahead!",
    "see you later": "See you later! Take care!",
    "bye": "Bye! Don't hesitate to reach out if you need anything.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "make me laugh": "What do you call fake spaghetti? An impasta!",
    "are you a robot": "I am a virtual assistant, here to help you!",
    "what is your name": "I am your personal assistant. You can call me whatever you like!" ,
    "what is the time" : "The current time is " + QTime.currentTime().toString("hh:mm AP"),
    "what time is it" : "it is " +QTime.currentTime().toString("hh:mm AP")
}

def speak(text):
    """Improved speaking function"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
def say_time(time):
    time = time
    
    
    
def open_app(app_name):
    """Your original app opening logic with better feedback"""
    app_name = app_name.lower().strip()
    if app_name in app_dict:
        try:
            if app_name in ['notepad', 'calculator', 'chrome', 'excel', 'word', 'powerpoint', 'mysql']:
                subprocess.Popen(app_dict[app_name])
            else:
                webbrowser.open(app_dict[app_name])
            speak(f"Opening {app_name}")
        except Exception as e:
            speak(f"Failed to open {app_name}")
            print(f"Error: {e}")
    else:
        speak(f"I don't know how to open {app_name}")

def handle_response(command):
    """Enhanced response handling with exact matching"""
    command = command.lower().strip()
    
    # Check for exact matches first
    if command in polite_responses:
        speak(polite_responses[command])
        return True
    
    # Check for partial matches
    for phrase, response in polite_responses.items():
        if phrase in command:
            speak(response)
            return True
    
    return False

def listen():
    """Reliable listening function"""
    with sr.Microphone() as source:
        print("\nAdjusting for ambient noise... (stay silent)")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("Speak now...")
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Didn't catch that")
            speak("Could you repeat that?")
        except sr.RequestError:
            print("API unavailable")
            speak("Having trouble with the speech service")
        except Exception as e:
            print(f"Error: {e}")
    
    return None

def run_assistant():
    """Main assistant loop"""
    while True:
        command = listen()
        if command:
            if command.startswith("open "):
                open_app(command[5:].strip())
            else:
                if not handle_response(command):
                    speak("Try saying 'open chrome' or ask me something")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Personal Assistant")
        self.setGeometry(500, 500, 500, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        self.title = QLabel("Personal Voice Assistant")
        self.title.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.title.setAlignment(Qt.AlignCenter)
        
        self.status = QLabel("Press Start to begin")
        self.status.setStyleSheet("font-size: 18px;")
        self.status.setAlignment(Qt.AlignCenter)
        
        self.btn = QPushButton("Start")
        self.btn.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                padding: 10px;
                background: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background: #45a049;
            }
        """)
        self.btn.clicked.connect(self.start)
        
        layout.addWidget(self.title)
        layout.addWidget(self.status)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def start(self):
        self.status.setText("Listening... (Say 'open chrome' etc.)")
        self.btn.setEnabled(False)
        threading.Thread(target=run_assistant, daemon=True).start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())