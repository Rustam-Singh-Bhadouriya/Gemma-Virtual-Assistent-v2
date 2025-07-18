# include all Source for run
from modules import *

# print("Initlizating Gemma...")
# print("Welcome to Gemma V2")
# voice.tell(text="Welcome to Gemma V2" , filename="greet.mp3")

# voice.tell(text="Enter Your prefer language" , filename="greet.mp3")
# lang = input("hi/en: ")
# voice.tell(text=f"Thank you for language selection", filename="greet.mp3")
# print(f"language Selected {lang}")

# print("Model ready lets go...")
# voice.tell("Model ready" , "greet.mp3")

lang = 'en'
# Taking User Input
UserInput = voice.listen(lang=lang)
print(UserInput)

# GenAI Work-

AI_response = ai_resposne.generate(UserInput , lang=lang)
print(AI_response)
print(UserInput)

# In cunstruction