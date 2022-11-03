import os
import speech_recognition as sr
import time
import ctypes
import speech_recognition
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from youtube_search import YoutubeSearch
from datetime import datetime
import pyttsx3

wikipedia.set_lang('en')
language = 'en'
robot_ear = speech_recognition.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    print(text)
    engine.say(text)
    engine.runAndWait()


def get_audio():
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


def stop():
    speak("Bye bye, see you later!")


def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("I can't hear you")
    stop()
    return 0


def hello(name):
    speak("Hi, {}".format(name))


def get_time(text):
    now = datetime.now()
    speak('Now is %d hour %d minutes' % (now.hour, now.minute))


def open_application(text):
    if "garena" in text:
        speak("Opening Garena")
        os.startfile("C:\Program Files (x86)\Garena\Garena\Garena.exe")
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile('C:\Program Files\Microsoft Office\Office15\WINWORD.EXE')
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile('C:\Program Files\Microsoft Office\Office15\EXCEL.EXE')
    elif "Sublime Text" in text:
        speak("Sublime Text đang được mở, bạn chờ xíu nha Ihihi")
        os.startfile('C:\Program Files\Sublime Text 3\sublime_text.exe')
    else:
        speak("Cannot find this app")


def open_website(text):
    reg_ex = re.search('open (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain + '.com'
        webbrowser.open(url)
        speak("Opened")
        return True
    else:
        return False


def open_google_and_search(text):
    search_for = text.split("search", 1)[1]
    speak('Okay!')
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)


# Alex còn biết gửi mail mà không cần bật gmail á, thấy giỏi hôn nè ^^
def send_email(text):
    speak('Bạn gửi email cho ai nhỉ')
    recipient = get_text()
    if 'nghĩa' in recipient:  # 'nghĩa' ở đây là keywords để máy tiếp tục gửi email cho bạn. Bạn có thể thay cái keywords này
        speak('Nội dung bạn muốn gửi là gì')
        content = get_text()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('xyz',
                   'abc')  # 'xyz' ở đây là địa chỉ email của bạn (địa chỉ email gửi), 'abc' là mật khẩu của email đó
        mail.sendmail('xyz',
                      '123', content.encode(
                'utf-8'))  # 'xyz' ở đây cũng như bên trên, nhưng '123' là địa chỉ email nhận (email được bạn gửi thư)
        mail.close()
        speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
    else:
        speak('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không')


# Muốn đi chơi mà sợ trời mưa thì hãy xem dự báo thời tiết nha, nhớ gọi Alex đó
def current_weather():
    speak("Where your location")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_text()
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
        speak(content)
    else:
        speak("Can not find your location")


def play_song():
    speak("Whats song")
    mysong = get_text()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Opened")


def read_news():
    speak("What's news?")

    queue = get_text()
    params = {
        'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
        "q": queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()
    print("News: ")

    for number, result in enumerate(api_response['articles'], start=1):
        print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
    """)
        if number <= 3:
            webbrowser.open(result['url'])


def change_wallpaper():
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
    speak('Changed the screen background!')


def tell_me_about():
    try:
        speak("What you want to hear?")
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0].split(".")[0])
        for content in contents[1:]:
            speak("Wanna more")
            ans = get_text()
            if "yes" not in ans:
                break
            speak(content)

        speak('Thank for listening')
    except:
        speak("I don't get it")


def introduce():
    speak("I'm Jarvis, stand for Just A Really Very Intelligent System \nDesign by Anh Duc Griffin rom UET")


def help_me():
    speak("""Uhm hmm, I can:
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


# Nếu như bạn không thích tắt máy ngay thì hãy dụng bộ cài đặt hẹn giờ sau đây nè
def shutdown():
    h = int(speak("Nhập giờ: "))
    m = int(speak("Nhập phút: "))
    s = int(speak("Nhập giây: "))
    while True:
        t = speak("Mời bạn chọn chế độ (ShutDown = s, Restart = r ): ")
        if t == "s" or t == "r":
            break

    h = h * 60 * 60
    m = m * 60
    s = s + m + h
    print("Bắt đầu hẹn giờ")
    os.system(f"ShutDown -{t} -t {s}")  # Lệnh thực hiện dòng lệnh
    print("Gõ lệnh ShutDown -a để hủy hẹn giờ")
    speak("Nhớ tắt hết ứng dụng trước khi tắt máy nhoa, ihihi ^^")


def assistant():
    speak("Hi Griffin, welcome back, i'm Jarvis!")
    name = "Griffin"
    while True:
        text = get_text()
        if not text:
            break
        elif "stop" in text or "goodbye" in text or "go to sleep" in text:
            stop()
            break
        elif "help me" in text:
            help_me()
        elif "hi" in text:
            hello(name)
        elif "time" in text:
            get_time(text)
        elif 'search' in text:
            open_google_and_search(text)
        elif "open" in text:
            open_website(text)
        elif "application" in text:
            speak("What's app? ")
            text1 = get_text()
            open_application(text1)
        elif "email" in text or "mail" in text or "gmail" in text:
            send_email(text)
        elif "weather" in text:
            current_weather()
        elif "music" in text:
            play_song()
        elif "background" in text:
            change_wallpaper()
        elif "tell me about" in text:
            tell_me_about()
        elif "who are you" in text:
            introduce()
        elif "shutdown" in text in text:
            shutdown()
        elif "thank" in text:
            speak("You are welcome!")
        elif "where are you" in text:
            speak("Technically, I'm every where. But you can control me through ROS. "
                  "I guess you dont have a real robot here? Just use turtlesim simulation")
        else:
            speak("Try something else")
