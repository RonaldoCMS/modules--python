import webbrowser

url = 'http://docs.python.org/'

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
#chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
i = 0
while i<100:
    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open_new("https://www.ilmattino.it/")
    i += 1


# Linux
# chrome_path = '/usr/bin/google-chrome %s'
