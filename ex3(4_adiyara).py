# pip install SpeechRecognition
# in case of error use 'pip install pyaudio' or...
# in case of error use 'pip install pipwin' then 'pipwin install pyaudio'
# if error continued you may need to use python 3.6 or lower as the latest
# python may not support pyaudio...
import os

import speech_recognition as sr
import pyttsx3

# audio of system to respond
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# simple function to recognise speech from user
def takecommand():
    # it takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print('Listening.....')
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:

        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')

        def takecommand1():

            try:

                if query == "Alexa":
                    # alex kiuwama ,dan thamai apita onade kiyanna one

                    speak("ok ruchira , what do you want? ")

                    s = sr.Recognizer()
                    with sr.Microphone() as source:

                        print('Listening2.....')
                        s.pause_threshold = 1
                        s.energy_threshold = 4000
                        audio = s.listen(source)

                    query2 = s.recognize_google(audio, language='en-in')
                    print(query2)
                    ARRAY = [["WhatsApp", "Facebook", "whatsapp", ], ["camera", "Facebook", "maths"], ["science", "twitter"]]
                    for x in ARRAY:
                        for y in x:
                            print(y, end="")
                            if query2 == "bye":
                                speak( "Exite your alexa, goodbuy")
                                exit()
                                System.out;



                            elif query2  == y:
                                speak("Ok Ruchira , open your file")

                                os.system('start'+' '+query2+':')

                                speak("your " + query2 + " file is open ,have a nice day Ruchira")
                                System.out;



                            else:
                                speak("Sorry I found it hard to find " +query2+ " you said, Ruchira try it again")






                        try:
                            return query
                        except:
                            print('exception : ', e)
                            return "None"








            except Exception as e:
                print('exception : ', e)

                return "None"
            return query2



        while True:
            query2 = takecommand1()  # whatever user says will be stored in this variable
            print("The Test2 got in program is : " + query2)










    except Exception as e:
        print('exception : ', e)

        return "None"

    return query


while True:
    query = takecommand()  # whatever user says will be stored in this variable
    print("The Test got in program is : " + query)

