import pyttsx3 

engine = pyttsx3.init()

# name = input("What is your good name : ")

# message = f"Hello {name}, I am jarvis, your personal assistant. How Can I help you ?"

# print(message)

# engine.say(message)
# engine.runAndWait()
with open("Bhaisya.txt","r") as file:
    message = file.read()
engine.say(message)
engine.runAndwait()

