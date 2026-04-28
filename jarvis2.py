import pyttsx3
import  speech_recognition as sr
import webbrowser
import datetime

# initialize text-to-speech
engine = pyttsx3.init()
# windsurf:Refacter|explain|Genreate Docstrstring
def speak(text):
    print("Assistant:",text)
    engine.say(text)
    engine.runAwait()
    # take voice input 
def take_command():
    r = sr.Recoginzer() 
    with sr.Microphone() as source:
        print("listening...")
        r.adjust_for_amient_noise(source)
        audio = r.leaten(source)
    try:
         print("Recogintion.....")
         command = r.recogninze_googl(aduio).lower()
         print("you said :",command)
        
    except Exception as a:
         speak("sorryI,didn,t catch that, please say it again.")
         return""
    return command
# function================
def open_googal():
    webbrowser.open("https://www.googal.com")
    speak("opening googal")
    
def open_youtube():
    webbrowser.open("http://www,youtube.com/")
    speak("opening you tube")
def tell_time(): 
 time = datetime.datetime.now().strftime("%I,%M,%P")
 speak(f"the current time is {time}")
def tell_joke():
    joke = "why do programers prefer dark mode? Because ligth attracts bugs!"
    speak(joke)
# main assistance loop
def run_assistannce():
    speak("Hello,I am your voice assistance, how can i help you")
    
    while True:
        command = take_command()  
        if "open youtube" in command:
            open_youtube()
        elif "open googal" in command:
            open_googal()
        elif "tell me a joke" in command:
            tell_joke()
        elif "time" in command:
            tell_time()
        elif "exit" in command or "quit"in command:
            speak("goodbye!")
            break
        elif command == "": 
            continue
    else:
     speak("sorry,I don't understand that command")
     run 
