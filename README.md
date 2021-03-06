A Siri-like voice assistant named after the AI in the movie "War Games."

You have to configure a few things before you can use it.

1. You need the Microsoft Edge driver installed. Copy the full path to it and paste it in the file "webSearch.py" in the variable "self.driver" where it says r'C:\path\to\msedgedriver.exe'."
2. You need an API key from https://newsapi.org/ and also one from https://openweathermap.org/. Paste the one from https://newsapi.org/ in the file "newsSearch.py" in the variable "self.api_key" where it says "your API key." Paste the one from https://openweathermap.org/ in the file "weather.py" in the variable "self.api_key" where it says "your API key."
3. If you want to be able to open programs through Joshua, you need to put the name you want to call the program to open it and the path to that program in the file "main.py" in the dictionary "pathToProgram." For example, if you wanted to say "Open text editor" to open notepad, you would put 'text editor':r"C:\\WINDOWS\\system32\\notepad.exe" in the "pathToProgram" dictionary. Hopefully this makes sense.
4. If you want to use the variable "USR_START_MENU" in the file "main.py" to help put the path to some programs as described in the previous step, you have to replace where it says "USERNAME" with your Windows username.

To start Joshua, you need to have Python installed. After you've installed Python and configured everything, open the directory you cloned this repository in in your terminal and type ".\venv\Scripts\activate.bat" if you're using CMD, or type ".\venv\Scripts\Activate.ps1" if you're using PowerShell to activate the virtual environment (I'm not sure if the batch script I wrote to start it works correctly or not). After you've activated the virtual environment, type "python main.py" to start Joshua.
