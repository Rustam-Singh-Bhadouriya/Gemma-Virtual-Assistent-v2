# Here will all pygame gTTS and voice support
from modules import *
import time

""" 
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #         print("🎤 Speak something...")
    #         r.adjust_for_ambient_noise(source , duration=1)  # Adjust for ambient noise
    #         # r.energy_threshold = 200
    #         r.pause_threshold = 1.2
    #         audio = r.listen(source, phrase_time_limit=7)

    # try:
    #     userInput = r.recognize_google(audio, language=lang)
    #     return userInput
    
    # except sr.UnknownValueError:
    #     print("Can't Understand..")

    # except sr.WaitTimeoutError:
    #     print("Server timeout..")
    
    # except sr.RequestError:
    #     print("Can't Connect to Server")
"""


"""listen = userInput & speak = output"""

def speak(text: str, file_name : str , InLang : str):
    outPut = gTTS(text=text , lang=InLang)
    outPut.save(file_name)

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1.0) 
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()

    # Wait until audio finishes
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
def tell(text , filename):
    telle = gTTS(text=text , lang="en")
    telle.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.set_volume(1.0) 
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


def listen(lang) -> str:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak Something...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        userInput = r.recognize_google(audio, language=lang)
        return userInput
    
    except sr.UnknownValueError:
        print("Can't Understand..")

    except sr.WaitTimeoutError:
        print("Server timeout..")
    
    except sr.RequestError:
        print("Can't Connect to Server")




if __name__ == "__main__":
    # listen()
    speak(text=listen() , file_name="response.mp3" , InLang="en")