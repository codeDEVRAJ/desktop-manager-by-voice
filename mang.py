import sys
import subprocess
import threading
import webbrowser
import pyttsx3
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout # type: ignore
from PyQt5.QtCore import Qt # type: ignore

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Dictionary of applications and websites
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

# Function to open an app or website
def open_app(app_name):
    app_name = app_name.lower().strip()
    if app_name in app_dict:
        if app_name in ['notepad', 'calculator', 'chrome', 'excel', 'word', 'powerpoint', 'mysql']:
            subprocess.Popen(app_dict[app_name])
        else:
            webbrowser.open(app_dict[app_name])
    else:
        speak(f"Sorry, I don't know how to open {app_name}")
        print(f"Sorry, I don't know how to open {app_name}")

# Function to handle polite responses
def handle_response(command):
    polite_responses = {
        "hello": "Hi! How can I assist you today?",
        "hi": "Hey there! What can I do for you?",
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
        "what is your name": "I am your personal assistant. You can call me whatever you like!"
    }

    for phrase, response in polite_responses.items():
        if phrase in command:
            speak(response)
            print(response)
            return True
    return False

# Function to run the voice assistant
def run_voice_assistant():
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)  # Adjust sensitivity
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = recognizer.recognize_google(audio).lower()
                print(f"Your Command: {command}")

                # Handle commands directly
                if "open" in command:
                    app_name = command.replace("open", "").strip()
                    open_app(app_name)
                else:
                    handle_response(command)

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand. Could you please repeat that?")
            print("Sorry, I didn't understand. Could you please repeat that?")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
        except sr.WaitTimeoutError:
            print("No speech detected. Trying again...")
        except KeyboardInterrupt:
            print("Assistant stopped.")
            break

# Main GUI class
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nova Assistant")
        self.setGeometry(500, 500, 500, 500)

        # Create labels and button
        self.label1 = QLabel("Manage everything with Nova Assistant")
        self.label = QLabel("Press Start to Begin")
        self.button = QPushButton("Start")

        # Initialize the UI
        self.initUI()

    def initUI(self):
        # Set up a layout manager
        layout = QVBoxLayout()

        # Add widgets to the layout
        layout.addWidget(self.label1)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Set the layout for the window
        self.setLayout(layout)

        # Style the label1
        self.label1.setStyleSheet("""
            font-size: 20px;
            background-color: black;
            color: gray;
            font-style: italic;
            padding: 10px;
        """)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFixedSize(400, 50)

        # Style the label
        self.label.setStyleSheet("font-size: 30px;")

        # Style the button
        self.button.setStyleSheet("font-size: 30px;")

        # Connect the button click event
        self.button.clicked.connect(self.on_click)

    # Function to handle button click
    def on_click(self):
        print("Button clicked")
        self.label.setText("Listening...")
        self.button.setEnabled(False)
        threading.Thread(target=run_voice_assistant, daemon=True).start()

# Main program entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())