import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen(search_entry, result_label):
    """Convert speech to text and update the GUI."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Please say your math problem")
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio)
            search_entry.delete(0, "end")
            search_entry.insert(0, query)
            result_label.config(text=f"Searching for: {query}")
            speak(f"You said: {query}")
        except sr.UnknownValueError:
            result_label.config(text="Sorry, I couldn't understand that.")
            speak("Sorry, I couldn't understand that.")
        except sr.RequestError:
            result_label.config(text="Could not connect to the speech service.")
            speak("Could not connect to the speech service.")
