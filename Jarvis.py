import ctypes
import datetime
import json
import os
import re
import smtplib
import ssl
import urllib.request as urllib2
import webbrowser
from datetime import datetime

import pyttsx3
import requests
import speech_recognition
import speech_recognition as sr
import wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from youtube_search import YoutubeSearch


class Jarvis:
    language = 'en'
    robot_ear = speech_recognition.Recognizer()

    def __int__(self):
        wikipedia.set_lang('en')

    def speak(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 175)
        print(text)
        engine.say(text)
        engine.runAndWait()

    def get_audio(self):
        print("\nBot: \tListening \t *__^ \n")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Me: ", end='')
            audio = r.listen(source, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio, language="en-us")
                print(text)
                return text.lower()
            except:
                print("...")
                return 0

    def stop(self):
        self.speak("Bye bye, see you later!")

    def get_text(self):
        for i in range(3):
            text = self.get_audio()
            if text:
                return text.lower()
            elif i < 2:
                self.speak("I can't hear you")
        self.stop()
        return 0

    def hello(self, name):
        self.speak("Hi, {}".format(name))

    def get_time(self, text):
        now = datetime.now()
        self.speak('Now is %d hour %d minutes' % (now.hour, now.minute))

    def open_application(self, text):
        if "teamviewer" in text:
            self.speak("Opening")
            os.startfile("C:\Program Files\TeamViewer\TeamViewer.exe")
        else:
            self.speak("Cannot find this app")

    def open_website(self, text):
        reg_ex = re.search('open (.+)', text)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain + '.com'
            webbrowser.open(url)
            self.speak("Opened")
            return True
        else:
            return False

   # def open_google_and_search(self, text):
    #    search_for = text.split("search", 1)[1]
     #   self.speak('Okay!')
      #  driver = webdriver.Chrome(path)
       # driver.get("http://www.google.com")
        #que = driver.find_element_by_xpath("//input[@name='q']")
        #que.send_keys(str(search_for))
        #que.send_keys(Keys.RETURN)

    def read_news(self):
        self.speak("What news")

        queue = self.get_text()
        params = {
            'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
            "q": queue,
        }
        api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
        api_response = api_result.json()
        print("News: ")

        for number, result in enumerate(api_response['articles'], start=1):
            print(
                f"""Number {number}:\nTitle: {result['title']}\nDescription: {result['description']}\nLink: {result['url']}
        """)
            if number <= 3:
                webbrowser.open(result['url'])

    def send_email(self, text):
        self.speak('Send who')
        recipient = self.get_text()
        if 'myself' in recipient:
            self.speak("What's content")
            content = self.get_text()

            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            sender_email = "nhocato20161@gmail.com"
            receiver_email = "loanhduc0102@gmail.com"
            password = "Shin2001"
            message = content

            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

            self.speak('Sended')
        else:
            self.speak('I dont get it')

    def current_weather(self):
        self.speak("Where your location")
        ow_url = "http://api.openweathermap.org/data/2.5/weather?"
        city = self.get_text()
        if not city:
            pass
        api_key = "fe8d8c65cf345889139d8e545f57819a"
        call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        response = requests.get(call_url)
        data = response.json()
        if data["cod"] != "404":
            city_res = data["main"]
            current_temperature = city_res["temp"]
            current_pressure = city_res["pressure"]
            current_humidity = city_res["humidity"]
            suntime = data["sys"]
            sunrise = datetime.fromtimestamp(suntime["sunrise"])
            sunset = datetime.fromtimestamp(suntime["sunset"])
            wthr = data["weather"]
            now = datetime.now()
            content = """
            Today is {day} {month} {year}
            The sun rise at {hourrise} hour {minrise} minutes
            The sun set at {hourset} hour {minset} minutes
            The temp is {temp} C""".format(day=now.day, month=now.month, year=now.year,
                                           hourrise=sunrise.hour,
                                           minrise=sunrise.minute,
                                           hourset=sunset.hour, minset=sunset.minute,
                                           temp=current_temperature,
                                           pressure=current_pressure,
                                           humidity=current_humidity)
            self.speak(content)
        else:
            self.speak("Can not find your location")

    def play_song(self):
        self.speak("Whats song")
        mysong = self.get_text()
        while True:
            result = YoutubeSearch(mysong, max_results=10).to_dict()
            if result:
                break
        url = 'https://www.youtube.com' + result[0]['url_suffix']
        webbrowser.open(url)
        self.speak("Opened")

    def read_news(self):
        self.speak("What's news?")

        queue = self.get_text()
        params = {
            'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
            "q": queue,
        }
        api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
        api_response = api_result.json()
        print("News: ")

        for number, result in enumerate(api_response['articles'], start=1):
            print(
                f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
        """)
            if number <= 3:
                webbrowser.open(result['url'])

    def change_wallpaper(self):
        api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
        url = 'https://api.unsplash.com/photos/random?client_id=' + \
              api_key
        f = urllib2.urlopen(url)
        json_string = f.read()
        f.close()
        parsed_json = json.loads(json_string)
        photo = parsed_json['urls']['full']
        urllib2.urlretrieve(photo, "C:/Users/nhoca/Downloads/maxresdefault.jpg")
        image = os.path.join("C:/Users//nhoca/Downloads/maxresdefault.jpg")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 3)
        self.speak('Changed the screen background!')

    def tell_me_about(self):
        try:
            self.speak("What you want to hear?")
            text = self.get_text()
            contents = wikipedia.summary(text).split('\n')
            self.speak(contents[0].split(".")[0])
            for content in contents[1:]:
                self.speak("Wanna more")
                ans = self.get_text()
                if "yes" not in ans:
                    break
                self.speak(content)

            self.speak('Thank for listening')
        except:
            self.speak("I don't get it")

    def introduce(self):
        self.speak("I'm Jarvis, stand for Just A Really Very Intelligent System \nDesign by Anh Duc Griffin from UET")

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

    def shutdown(self):
        h = int(self.speak("Nhập giờ: "))
        m = int(self.speak("Nhập phút: "))
        s = int(self.speak("Nhập giây: "))
        while True:
            t = self.speak("Mời bạn chọn chế độ (ShutDown = s, Restart = r ): ")
            if t == "s" or t == "r":
                break

        h = h * 60 * 60
        m = m * 60
        s = s + m + h
        print("Bắt đầu hẹn giờ")
        os.system(f"ShutDown -{t} -t {s}")  # Lệnh thực hiện dòng lệnh
        print("Gõ lệnh ShutDown -a để hủy hẹn giờ")
        self.speak("Nhớ tắt hết ứng dụng trước khi tắt máy nhoa, ihihi ^^")

    def assistant(self):
        self.speak("Hi Griffin, welcome back, i'm Jarvis!")
        name = "Griffin"
        while True:
            text = self.get_text()
            if "hello" in text:
                self.speak("Ask me something")
                while True:
                    text = self.get_text()
                    if not text:
                        break
                    elif "stop" in text or "goodbye" in text or "go to sleep" in text:
                        self.stop()
                        break
                    elif "help me" in text:
                        self.help_me()
                    elif "hi" in text:
                        self.hello(name)
                    elif "time" in text:
                        self.get_time(text)
                    elif 'search' in text:
                        self.open_google_and_search(text)
                    elif "open" in text:
                        self.open_website(text)
                    elif "application" in text:
                        self.speak("What's app? ")
                        text1 = self.get_text()
                        self.open_application(text1)
                    elif "email" in text or "mail" in text or "gmail" in text:
                        self.send_email(text)
                    elif "weather" in text:
                        self.current_weather()
                    elif "music" in text:
                        self.play_song()
                    elif "background" in text:
                        self.change_wallpaper()
                    elif "tell me about" in text:
                        self.tell_me_about()
                    elif "who are you" in text:
                        self.introduce()
                    elif "shutdown" in text in text:
                        self.shutdown()
                    elif "thank" in text:
                        self.speak("You are welcome!")
                    elif "newspaper" in text:
                        self.read_news()
                    elif "where are you" in text:
                        self.speak("Technically, I'm every where. But you can control me through ROS. "
                                   "I guess you dont have a real robot here? Just use turtlesim simulation")
                    else:
                        self.speak("Try something else")
            if "stop" in text:
                self.stop()
                break
