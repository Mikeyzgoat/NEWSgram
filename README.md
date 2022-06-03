# NEWSgram - A NEWS notification app
## Description
<i>This python file runs in the background and obtains all the top news from google news feed directly onto your notifications tab.</i>

## Requirements
- Python 3.6 or Higher
- A terminal, WSL or Command prompt, pointing to the directory where the file is at

- Running Commands : 
`python3 newpost.py`

- After the file starts execution it will be running in the background and can be terminated by typing 
`Ctrl + C` 
on the terminal. <br>

## Modules used
* `GoogleNews` from `pygooglenews`
* `notification` from `plyer`
* `time`

## Installation and Documentation
### [plyer](https://pypi.org/project/plyer/)
<i>Installation</i>
```
pip install plyer
```
### [pygooglenews](https://github.com/kotartemiy/pygooglenews)
<i>Installation</i>
```
pip install pygooglenews
```
### [time](https://docs.python.org/3/library/time.html)
<i>It should be available on the device by default.</i><br>

<i>Now let's understand how the notification pushing works</i>
### notification.notify()
<i>Here in this function the parameters that are to be passed can be explained as follows :</i>
```python
from plyer import notification
notification.notify(title = "Enter any title",message = "Enter any message as body of the notification",
                app_icon = None,timeout = <time in seconds>,toast = False)
```

* app_icon can be a path to the icon declared elsewhere or mentioned here itself but keep in mind it must be .ico file<br>
* <b>Note : </b>
Title and message fields must not exceed <b><i><q>64 characters</q></i><b>.<br>

### plyer - an alternative to kivy
* Kivy is a powerful module in developing android applications in python
* Push Notifications are a part of Kivy, but are restricted to android only
* Plyer, on the other hand is a <b>platform-independent api</b> to use features commonly found on various platforms, notably mobile ones, in Python.

  
### pygooglenews - Web scraper Library
* If Google News had a Python Library - Kortartmiy (Creator) 
* This is the Heart and Soul of the project.
* Special thanks to [Kortartmiy](https://github.com/kotartemiy) for building such a powerful yet simple web scraper.
* This module when run parses the rss.xml links by the respective news feed into dictionaries having keys 'feed' and 'entries'
* the parsing is done by the library [feedparser](https://pypi.org/project/feedparser/) which is included in the pygooglenews library
* the news can be accessed as follows :
```python
from pygooglenews import GoogleNews
gn = GoogleNews(lang = 'en') # obtains every news written in language english
world_news = gn.top_news('World') # filters top news under the category world
print(world_news['entries']) # prints the dictionary under key 'entries'
```
```python
  top_news(category)
  ```
  accepts only the following categories :
  - World
  - Business
  - Sports
  - Nation
  - Science
  - Technology
  - Health
  - Entertainment

### Future updates
- [ ] Must add icon to NEWSgram.
- [ ] Must add function to segregrate news based on time of release.
- [ ] Must add a function to make the notification more responsive.

Created by [Aditya](https://github.com/Mikeyzgoat)
