# Voice-Assistant-with-AI-Enabled-Features

The Project is a Python script that implements a voice-controlled assistant with various functionalities. Here's a description of the code:

• The script starts by importing necessary libraries, such as speech_recognition, pyttsx3, requests, json, webbrowser, os, pyjokes, datetime, pywhatkit, wikipedia, cv2, Translator from googletrans, and playsound.
• It initializes a text-to-speech engine using pyttsx3.init() and loads a cascade classifier for fire detection using cv2.CascadeClassifier.
• The script enters an infinite loop that listens for user speech input using the microphone.
• It uses the speech_recognition library to recognize the speech and convert it into text. If the recognition is successful, the recognized text is printed.
• The recognized text is then processed using a series of if-elif-else statements to determine the user's command and execute the corresponding functionality.

The functionalities include:
• Playing a song or movie on YouTube using pywhatkit.playonyt().
• Opening a game in the default web browser.
• Retrieving current news headlines from NewsAPI and speaking them aloud using text-to-speech.
• Getting the current time and speaking it aloud.
• Performing calculations on mathematical expressions using eval() and speaking the result.
• Detecting fire using OpenCV and playing an alert sound.
• Translating a phrase to another language using googletrans.Translator.
• Getting current weather data from OpenWeatherMap and speaking the temperature and weather conditions.
• Looking up queries on Wikipedia and reading the summary.
• Opening the device camera using OpenCV and displaying the video feed.
• Telling jokes using pyjokes.
• Saying goodbye and exiting the loop.
• If the recognized text does not match any predefined command, the assistant responds with an "I'm sorry" message.

Please note that the code assumes the availability of necessary resources such as the fire_detection.xml cascade classifier file and the audio.mp3 alert sound file.
