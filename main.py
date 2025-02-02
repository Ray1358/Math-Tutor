import tkinter as tk
import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Function to speak the result
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Create the main window
root = tk.Tk()
root.title("Math Tutor")
root.geometry("800x500")

# Set the background color to grey
root.config(bg='gray')

# Label for the title
label = tk.Label(root, text="Math Tutor", font=("Arial", 26), bg='gray')
label.pack(pady=20)


# Function to handle search
def search():
    query = search_entry.get()  # Get the text from the search entry
    result_label.config(text=f"Search for: {query}")  # Display the search term
    speak(f"You searched for: {query}")  # Speak the search term


# Function to convert speech to text
def listen():
    recognizer = sr.Recognizer()  # Initialize recognizer
    with sr.Microphone() as source:
        speak("Please say your math problem")
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            # Convert speech to text
            query = recognizer.recognize_google(audio)
            search_entry.delete(0, tk.END)  # Clear any previous text
            search_entry.insert(0, query)  # Insert the recognized text
            result_label.config(text=f"Searching for: {query}")
            speak(f"You said: {query}")
        except sr.UnknownValueError:
            result_label.config(text="Sorry, I couldn't understand that.")
            speak("Sorry, I couldn't understand that.")
        except sr.RequestError:
            result_label.config(text="Could not connect to the speech service.")
            speak("Could not connect to the speech service.")


# Label to show search results
result_label = tk.Label(root, text="Enter Your Math Question", font=("Arial", 14), bg='gray')
result_label.pack(pady=20)

# Create the search entry field
search_entry = tk.Entry(root, font=("Arial", 14), width=30)
search_entry.pack(pady=10)

# Create the search button
search_button = tk.Button(root, text="Search", command=search, font=("Arial", 14))
search_button.pack(pady=10)

# Create the button for speech input
speech_button = tk.Button(root, text="Speech", command=listen, font=("Arial", 14))
speech_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
