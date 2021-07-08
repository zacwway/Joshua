from webSearch import WebSearch
from newsSearch import NewsSearch
from weather import Weather
from joshua import Joshua
from fnmatch import fnmatch

webSearch = WebSearch()
newsSearch = NewsSearch()
weather = Weather()
joshua = Joshua()

USR_START_MENU = r"C:\\Users\\USERNAME\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\"
SYS_START_MENU = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\"

pathToProgram = {
  'program name':r"C:\\path\\to\\program.exe"
}

urlForWebsite = {
  'youtube':"https://www.youtube.com",
  'duckduckgo':"https://duckduckgo.com",
  'google maps':"https://www.google.com/maps",
  'songsterr':"https://www.songsterr.com",
  'icloud':"https://www.icloud.com",
  'github':"https://github.com"
}


greetings = ['hi', 'hello', 'sup', "what's up"]
goodbyes = ['goodbye', 'bye', 'exit', 'quit']
wake_words = ['joshua', 'hi', 'hello']

print('')
print('######################################################################################')
print('NOTE: Please wait to start giving commands until you see "Listening..." in the console')
print('######################################################################################')
print('')

while True:
  text = joshua.recordAudio().lower()
  # text = 'joshua'

  if text in goodbyes:
    joshua.goodbye()
    break

  for word in wake_words:
    if text.count(word) > 0 :
      if text in greetings:
        joshua.hello()

      joshua.speak("How can I help you?")
      text = joshua.recordAudio().lower()
      # text = 'what is the weather'

      if 'what' in text and 'time' in text or "what's" in text and 'time' in text:
        x = joshua.getTime()
        joshua.speak("The current time is: " + x)

      elif 'what' in text and 'is' in text and 'day' in text:
        day = joshua.getDay()
        joshua.speak("Today is " + day)

      elif 'what' in text and 'date' in text or "what's" in text and 'date' in text:
        date = joshua.getDate()
        joshua.speak("The current date is: " + date)

      elif fnmatch(text, "open *"):
        text = text.replace('open ', '')

        if text in pathToProgram:
          joshua.openApp(text, pathToProgram[text])
        
        elif text in urlForWebsite:
          joshua.speak("Opening " + text)
          webSearch.openPage(urlForWebsite[text])

        else:
          joshua.speak("Sorry, I could not find that program.")

      elif 'tell' in text and 'news' in text or 'read' in text and 'news' in text:
        headlines = newsSearch.getHeadlines()
        descriptions = newsSearch.getDescriptions()
        contents = newsSearch.getContents()
        urls = newsSearch.getURLs()

        joshua.speak("Please read the console output for a list of commands.")
        joshua.speak("Reading latest news headlines...")
        print('')
        print('=> Say "next" to continue reading news headlines.')
        print('=> Say "back" to go back to the previous headline.')
        print('=> Say "tell me more" to hear more about a news headline.')
        print('=> Say "read article" or "read contents" to read the entire article')
        print('=> Say "open in browser" to open the article in the browser')
        print('=> Say "stop" or "cancel" to stop reading news headlines.')
        print('')

        i = 0
        while True:
          joshua.speak(headlines[i])
          print('')

          text = joshua.recordAudio().lower()

          if 'tell' in text and 'more' in text:
            joshua.speak(descriptions[i])
            print('')
            i = i + 1
            continue

          elif 'read article' in text or 'read contents' in text:
            joshua.speak(contents[i])
            print('')
            i = i + 1
            continue

          elif 'open' in text and 'browser' in text:
            joshua.speak('Opening article in browser...')
            webSearch.openPage(urls[i])
            break

          elif 'next' in text:
            i = i + 1
            continue

          elif 'back' in text:
            i = i - 1
            continue

          elif 'stop' in text or 'cancel' in text:
            break

          i = i + 1

      elif 'what' in text and 'weather' in text or "what's" in text and 'weather' in text or 'what' in text and 'tempature' in text or "what's" in text and 'tempature' in text:
        joshua.speak("What city do you need to know the weather for?")
        city = joshua.recordAudio()
        # city = 'Rock Hill South Carolina'

        states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
                "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
                "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
                "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
                "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
                "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
                "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
                "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

        state = ''
        for i in states:
          if i in city:
            state = i
            city = city.replace(i, '').rstrip()
        city = f"{city}, {state}"

        joshua.speak("Would you like the tempature to be in the Fahrenheit, Celsius, or Kelvin unit?")
        unit = joshua.recordAudio().lower()

        high = weather.maxTemp(city, unit)
        low = weather.lowTemp(city, unit)
        average = weather.averageTemp(city, unit)
        feelsLike = weather.feelsLike(city, unit)
        description = weather.description(city)

        joshua.speak("The high in " + city + " is " + high + ", and the low is " + low + " with an average of " + average + ". It feels like " + feelsLike + " and there is " + description)

      elif 'search wikipedia for' in text:
        query = text.replace("search wikipedia for ", "")
        joshua.speak("Searching Wikipedia for " + query)
        webSearch.wikipedia(query)

      elif 'search youtube for' in text:
        query = text.replace('search youtube for ', '')
        joshua.speak("Searching YouTube for " + query)
        webSearch.youtube(query)

      elif 'search duckduckgo for' in text or 'search for' in text:
        if 'search duckduckgo for' in text:
          query = text.replace('search duckduckgo for ', '')

        elif 'search for' in text:
          query = text.replace('search for ', '')

        joshua.speak("Searching for " + query)
        webSearch.duckduckgo(query)

      elif 'open website' in text or 'go to' in text and 'website' in text:
        if 'open website' in text:
          text = text.replace('open website', '')

        elif 'go to' in text and 'website' in text:
          text = text.replace('go to ', '')
          text = text.replace(' website', '')

        joshua.speak("Opening " + text + "'s website...")
        webSearch.openSite(text)

      elif 'open' in text and 'on youtube' in text or 'open' in text and 'in youtube' in text or 'play' in text and 'on youtube' in text or 'play' in text and 'in youtube' in text:
        if 'open' in text:
          text = text.replace('open ', '')

        elif 'play' in text:
          text = text.replace('play', '')

        if 'on' in text:
          text = text.replace(' on youtube', '')

        elif 'in' in text:
          text = text.replace(' in youtube', '')
        
        joshua.speak("Opening " + text + " on YouTube...")
        webSearch.openInYoutube(text)

      elif 'cancel' in text:
        break

      else:
        joshua.speak("Sorry, I don't know how to do that ...... yet. Woudld you like me to search the internet for: " + text + "?")
        action = joshua.recordAudio().lower()

        if 'yes' in action or 'yeah' in action or 'sure' in action:
          joshua.speak("Searching for " + text)
          webSearch.duckduckgo(text)
        else:
          continue