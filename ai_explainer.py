import os
import openai
import pygame
import tempfile
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key! Set it in the .env file.")

client = OpenAI(api_key=OPENAI_API_KEY)

# Define the allowed math topics based on the MAT 095 syllabus
SYLLABUS_TOPICS = [
    "Real Numbers", "Order of Operations", "Absolute Value", "Exponents", "Linear Equations",
    "Graphing Lines", "Inequalities", "Scientific Notation", "Polynomials", "Factoring",
    "Coordinate System", "Slopes", "Intercepts", "Simplifying Expressions"
]

def explain_math(query):
    """Uses OpenAI's GPT-4 Turbo to explain a math topic, only if it is part of the MAT 095 syllabus."""
    query_lower = query.lower()

    # Check if the topic is in the syllabus
    if any(topic.lower() in query_lower for topic in SYLLABUS_TOPICS):
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "Explain this math concept in a simple way suitable for a beginner, with examples."},
                {"role": "user", "content": f"Explain {query} in detail with examples."}
            ],
            max_tokens=250
        )
        explanation = response.choices[0].message.content.strip()

        # Convert the explanation to speech
        play_audio(explanation)

        return explanation

    return "This topic is beyond the scope of MAT 095."

def play_audio(text):
    """Converts text to speech using OpenAI's TTS API and plays it."""
    try:
        tts_response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )

        # Save the audio to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_audio.write(tts_response.content)
            temp_audio_path = temp_audio.name

        # Initialize pygame mixer and play the audio
        pygame.mixer.init()
        pygame.mixer.music.load(temp_audio_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue  # Wait until playback is finished

    except Exception as e:
        print(f"Error in text-to-speech: {e}")