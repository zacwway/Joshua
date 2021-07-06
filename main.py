from webSearch import WebSearch
from joshua import Joshua
from fnmatch import fnmatch

webSearch = WebSearch()
joshua = Joshua()

USR_START_MENU = r"C:\\Users\\zacwa\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\"
SYS_START_MENU = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\"

pathToProgram = {
  'discord':USR_START_MENU + r"Discord Inc\\Discord",
  'element':USR_START_MENU + r"Element\\Element",
  'github desktop':USR_START_MENU + r"GitHub, Inc\\GitHub Desktop",
  'rekordbox':USR_START_MENU + r"Pioneer\\rekordbox 5.8.6\\rekordbox 5",
  'retroarch':USR_START_MENU + r"RetroArch\\RetroArch",
  'dolphin':USR_START_MENU + r"Dolphin",
  'vim':USR_START_MENU + r"Vim 8.2\\Vim",
  'vs code':USR_START_MENU + r"Visual Studio Code\\Visual Studio Code",
  'powershell':USR_START_MENU + r"Windows PowerShell\\Windows PowerShell",
  'file explorer':USR_START_MENU + r"Windows System\\File Explorer",
  'settings':SYS_START_MENU + r"Settings",
  'coding projects':USR_START_MENU + r"Coding projects",
  'zoom':USR_START_MENU + r"Zoom\\Zoom",
  'librewolf':USR_START_MENU + r"LibreWolf",
  'edge':SYS_START_MENU + r"Microsoft Edge",
  'microsoft edge':SYS_START_MENU + r"Microsoft Edge",
  'audacity':SYS_START_MENU + r"Audacity"
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
      # text = 'open youtube'

      if 'what' in text or "what's" in text and 'time' in text:
        x = joshua.getTime()
        joshua.speak("The current time is: " + x)

      elif fnmatch(text, "open *"):
        text = text.replace('open ', '')

        if text in pathToProgram:
          joshua.openApp(text, pathToProgram[text])
        
        elif  text in urlForWebsite:
          joshua.speak("Opening " + text)
          webSearch.openPage(urlForWebsite[text])

        else:
          joshua.speak("Sorry, I could not find that program.")

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

      else:
        joshua.speak("Sorry, I don't know how to do that ...... yet.")