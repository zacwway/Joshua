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
  'audacity':SYS_START_MENU + r"Audacity"
}


greetings = ['hi', 'hello', 'sup', "what's up"]
goodbyes = ['goodbye', 'bye', 'exit', 'quit']


while True:
  text = joshua.recordAudio().lower()
  # text = 'open vim'

  if text in greetings:
    joshua.hello()

  elif text in goodbyes:
    joshua.goodbye()
    break

  elif 'what' in text or "what's" in text and 'time' in text:
    time = joshua.getTime()
    joshua.speak("The current time is: " + time)

  elif "open program" in text or fnmatch(text, "open *"):
    text = text.replace('open ', '')
    text = text.replace('program ', '')

    if text in pathToProgram:
      joshua.openApp(text, pathToProgram[text])
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

  elif 'open' in text and 'on youtube' in text or 'play' in text and 'on youtube' in text:
    if 'open' in text:
      text = text.replace('open ', '')

    elif 'play' in text:
      text = text.replace('play', '')

    text = text.replace(' on youtube', '')
    
    joshua.speak("Opening " + text + " on YouTube...")
    webSearch.openInYoutube(text)

  else:
    joshua.speak("Sorry, I don't know how to do that ...... yet.")