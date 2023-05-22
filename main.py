import speech_recognition as sr
import pyttsx3
import requests
import json
import webbrowser
import os
import pyjokes
import datetime
import pywhatkit as kit
import wikipedia
import cv2
from googletrans import Translator
from playsound import playsound

# Initialize text-to-speech engine
engine = pyttsx3.init()
fire_cascade = cv2.CascadeClassifier('fire_detection.xml')

while True:
    # Set up speech recognition
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)

    # Try to recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you.")
        text = ""
    except sr.RequestError as e:
        print("Sorry, I couldn't request results from the Google Speech Recognition service.")
        text = ""

    # Process recognized text
    if "song" in text:
        # Play a song on YouTube using pywhatkit
        song = text.replace("play song", "")
        kit.playonyt(song)
    elif "movie" in text:
        # Play a movie on YouTube using pywhatkit
        movie = text.replace("play movie", "")
        kit.playonyt(movie)
    elif "play game" in text:
        # Open a game in the default web browser
        game_url = "https://www.google.com/search?q=pacman"
        webbrowser.open(game_url)
    elif "current affairs" in text:
        # Get current news headlines from NewsAPI
        api_key = "e4834781787c45ab8e19018ae1d10790"
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url)
        news = json.loads(response.text)
        for article in news["articles"]:
            engine.say(article["title"])
            engine.runAndWait()
    elif "time" in text:
        # Get current time and say it aloud
        time = datetime.datetime.now().strftime("%I:%M %p")
        engine.say(f"The current time is {time}")
        engine.runAndWait()
    elif "calculate" in text:
        # Calculate a math expression using eval()
        expression = text.replace("calculate", "")
        try:
            result = eval(expression)
            engine.say(f"The result of {expression} is {result}")
        except:
            engine.say("Sorry, I couldn't calculate that expression.")
        engine.runAndWait()
    elif "fire" in text:
        # Detect fire using OpenCV and play an alert sound

        cap = cv2.VideoCapture(0)

        while (True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

            for (x, y, w, h) in fire:
                cv2.rectangle(frame, (x - 20, y - 20), (x + w + 20, y + h + 20), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]
                print("fire is detected")
                playsound('audio.mp3')

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    elif "translate" in text:
        # Translate a phrase to another language
        translator = Translator()
        source_lang = 'en'
        target_lang = 'es'
        phrase = text.replace("translate", "")
        translation = translator.translate(phrase, src=source_lang, dest=target_lang)
        engine.say(f"{phrase} translates to {translation.text} in Spanish.")
        engine.runAndWait()
    elif "weather" in text:
        # Get current weather data from OpenWeatherMap
        api_key = "d22aeabf44a43094602dc813e97c617e"
        city = "Bilaspur"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            weather = response.json()
            temp_kelvin = weather["main"]["temp"]
            temp_celsius = round(temp_kelvin - 273.15, 2)
            description = weather["weather"][0]["description"]
            engine.say(
                f"The current temperature in {city} is {temp_celsius} degrees Celsius and the weather is {description}.")
            engine.runAndWait()
        else:
            engine.say("Sorry, I could not fetch the weather data at this time.")
            engine.runAndWait()
            print(response.status_code)
    elif "who" in text:
        # Look up a query on Wikipedia and read the summary
        query = text.replace("who", "")
        results = wikipedia.summary(query, sentences=2)
        engine.say(results)
        engine.runAndWait()
    elif "where" in text:
        # Look up a query on Wikipedia and read the summary
        query = text.replace("where", "")
        results = wikipedia.summary(query, sentences=2)
        engine.say(results)
        engine.runAndWait()
    elif "what" in text:
        # Look up a query on Wikipedia and read the summary
        query = text.replace("what", "")
        results = wikipedia.summary(query, sentences=2)
        engine.say(results)
        engine.runAndWait()
    elif "how" in text:
        # Look up a query on Wikipedia and read the summary
        query = text.replace("how", "")
        results = wikipedia.summary(query, sentences=2)
        engine.say(results)
        engine.runAndWait()
    elif "open camera" in text:
        # Speak the message and open the device camera using OpenCV
        engine.say("Opening camera. Press q to close the camera.")
        engine.runAndWait()
        cap = cv2.VideoCapture(0)
        while True:
            # Read the video feed from the camera
            ret, frame = cap.read()
            # Display the video feed on the screen
            cv2.imshow("Camera", frame)
            # Check for user input to stop the camera
            key = cv2.waitKey(1)
            if key == ord('q') or key == 27:  # 'q' or 'esc' key
                break
        # Release the camera and close the window
        cap.release()
        cv2.destroyAllWindows()
    elif "joke" in text:
        # Tell a joke using pyjokes
        joke = pyjokes.get_joke()
        engine.say(joke)
        engine.runAndWait()
    elif "bye" in text:
        engine.say("Goodbye!")
        engine.runAndWait()
        break
    else:
        engine.say("I'm sorry, I didn't understand your request.")
        engine.runAndWait()
