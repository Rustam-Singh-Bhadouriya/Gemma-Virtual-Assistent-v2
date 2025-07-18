# All Modules
from gtts import gTTS
import pygame
import google
from google import genai
import google.genai
from google.genai import types
import speech_recognition  as sr
import pyttsx3
import base64
import os
import json
import webbrowser
import wikipediaapi
import requests
import pyaudio
import ai_resposne
import urls
import voice
import article


with open("API.json") as Key:
    api = json.load(Key)

api_str = api['API']