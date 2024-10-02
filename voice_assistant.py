import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time
import requests

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Sorry unable to understand")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

def get_weather(city):
    api_key = "your_openweathermap_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        weather_info = f"The current temperature in {city} is {temp} degrees Celsius with {weather_desc}."
        return weather_info
    else:
        return "Sorry, I couldn't fetch the weather information."
    
def get_news():
    api_key = "your_news_api_key"
    base_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(base_url)
    if response.status_code == 200:
        articles = response.json()['articles']
        for article in articles[:5]:
            speechtx(article['title'])
    else:
        speechtx("Sorry, I couldn't fetch the news.")

if __name__ == '__main__':
    
     if "hello" in sptext().lower():
          while True:
               data1 = sptext().lower()

               if "your name" in data1:
                    name = "my name is peter"
                    speechtx(name)

               elif "old are you" in data1:
                    age = "i am two years old"
                    speechtx(age)
               
               elif "how are you" in data1:
                    speechtx("i am good, how are you?")
               
               elif "good" in data1:
                    speechtx("that's great to hear")

               elif "time" in data1:
                    time = datetime.datetime.now().strftime("%I%M%p")
                    speechtx(time)

               elif "today's date" in data1:
                    date = datetime.datetime.now().strftime("%B %d, %Y")
                    speechtx(date)

               elif "day today" in data1:
                    day = datetime.datetime.now().strftime("%A")
                    speechtx(day)

               elif "youtube" in data1:
                    webbrowser.open("https://www.youtube.com/")

               elif "github" in data1:
                    webbrowser.open("https://github.com/")
               
               elif "google" in data1:
                    webbrowser.open("https://www.google.com/")

               elif "joke" in data1:
                    joke1 = pyjokes.get_joke(language="en",category="neutral")
                    print(joke1)
                    speechtx(joke1)
               
               elif "search" in data1:
                    speechtx("What do you want to search for?")
                    search_query = sptext()  # Get the search query from the user
                    if search_query:
                        speechtx(f"Searching for {search_query}")
                        search_url = f"https://www.google.com/search?q={search_query}"
                        webbrowser.open(search_url)

               elif "weather" in data1:
                    speechtx("Please say the city name.")
                    city = sptext()
                    if city:
                         weather = get_weather(city)
                         speechtx(weather)

               elif "news" in data1:
                    get_news()

               elif "exit" in data1:
                    speechtx("thank you")
                    break

               time.sleep(5)

     else:
        print("thanks")