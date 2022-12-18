import os

import playsound
import speech_recognition
import speech_recognition as sr
from gtts import gTTS


class Jarvis:
    robot_ear = speech_recognition.Recognizer()
    ting = os.path.dirname(__file__) + '/ting.mp3'

    def speak(self, text):
        output = gTTS(text, lang="vi", slow=False)
        output.save("./output.mp3")
        audio_file = os.path.dirname(__file__) + '/output.mp3'
        playsound.playsound(audio_file, True)

    def get_audio(self):
        self.speak("iLib")
        playsound.playsound(self.ting, True)
        print("\nBot: \tListening \t *__^ \n")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Me: ", end='')
            audio = r.listen(source, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio, language="vi")
                print(text)
                return text.lower()
            except:
                print("...")
                return 0

    def get_text(self):
        for i in range(3):
            text = self.get_audio()
            if text:
                return text.lower()
            elif i < 2:
                self.speak("I can't hear you")
        self.stop()
        return 0

    def help_me(self):
        self.speak("""Uhm hmm, I can:
        Say hello
        and Introduce myself
        Beside it, i can Tell you what time is it
        or Open a website, application
        Search on Google
        Open email
        Take information about weather
        Play music
        or even Change your computer screen
        How about Read today newspaper
        or can i Tell you about the world
        Maybe i can Shutdown this computer
        just kidding, we can Q and A""")
