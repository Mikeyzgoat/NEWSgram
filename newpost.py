from pygooglenews import GoogleNews
from plyer import notification
import time
# gn will be a dictionary holding all news posted in english
gn = GoogleNews(lang='en')
# top news will be filtered from gn dictionary
tech_top = gn.top_news()


# creating a function to remove duplicate news feeds


def rem_dupes(stories):
    for i in range(len(stories)):
        if stories[i] not in stories[i + 1:]:
            stories.append(stories[i])


# filtering title from all entries
stories = []


def defnotif():
    stories = []

    for item in tech_top['entries']:
        stories.append(item.title)

    rem_dupes(stories)
    stories = sorted(stories)
    return stories
# creating the push notfiication function


def sendnotif(stories):
    read_txt = "Read more.."
    for item in range(len(stories)):
        if len(stories[item]) <= 64:
            notification.notify(
                title=stories[item], message=read_txt, app_icon=None, timeout=15, toast=False)
            time.sleep(60)
        else:
            continue
    defnotif()


sendnotif(defnotif())
