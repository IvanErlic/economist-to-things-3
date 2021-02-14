import requests
from bs4 import BeautifulSoup
import json
import webbrowser


def get_articles(response_text):
    articles = {}

    soup = BeautifulSoup(response_text, 'lxml')
    sections1 = soup.find_all('section', attrs={"class": "layout-weekly-edition-section ds-layout-grid"})
    sections2 = soup.find_all('section', attrs={"class": "layout-weekly-edition-section layout-weekly-edition-section--cols ds-layout-grid"})

    for section in sections1:
        if section.h2.text == 'Leaders':
            articles['Leaders'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc3"})
        elif section.h2.text == 'Briefing':
            articles['Briefing'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc3"})

    for section in sections2:
        if section.h2.text == 'Britain':
            articles['Britain'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc1"})
        elif section.h2.text == 'Europe':
            articles['Europe'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc1"})
        elif section.h2.text == 'United States':
            articles['United States'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc1"})
        elif section.h2.text == 'Middle East & Africa':
            articles['Middle East & Africa'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc1"})
        elif section.h2.text == 'The Americas':
            articles['The Americas'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc1"})
        elif section.h2.text == 'Asia':
            articles['Asia'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc1"})
        elif section.h2.text == 'China':
            articles['China'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc1"})
        elif section.h2.text == 'International':
            articles['International'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc1"})
        elif section.h2.text == 'Special report':
            articles['Special report'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc1"})
        elif section.h2.text == 'Business':
            articles['Business'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc1"})
        elif section.h2.text == 'Finance & economics':
            articles['Finance & economics'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc1"})
        elif section.h2.text == 'Science & technology':
            articles['Science & technology'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc1"})
        elif section.h2.text == 'Graphic detail':
            articles['Graphic detail'] = \
            section.find_all(attrs={"class": "teaser__headline teaser__headline--sc1"})

    return articles

def things_heading(economist_heading):
    '''retuns heading formated for Things 3'''
    
    headings = {
        'Leaders': 'Leaders',
        'Briefing': 'Briefing',
        'Britain': 'Britain',
        'Europe': 'Europe',
        'United States': 'United States',
        'Middle East & Africa': 'Middle East %26 Africa',
        'The Americas': 'The Americas',
        'Asia': 'Asia',
        'China': 'China',
        'International': 'International',
        'Special report': 'Special Report',
        'Business': 'Business',
        'Finance & economics': 'Finance %26 Economics',
        'Science & technology': 'Science %26 Technology',
        'Graphic detail': 'Graphic Detail'
    }

    # Replace _ with %20
    headings = {k:v.replace(" ", "%20") for (k,v) in headings.items()}

    return headings.get(economist_heading)

def add_to_things(articles):

    # Add The world this week
    webbrowser.open('things:///add?title=Politics%20this%20week&list=The%20Economist')
    webbrowser.open('things:///add?title=Business%20this%20week&list=The%20Economist')

    for heading, section in articles.items():
        for article in section:
            title = article.text.replace(" ", "%20")
            title = title.replace("’", "'")
            url = \
            f'things:///add?title={title}&list=The%20Economist&heading={things_heading(heading)}'
            webbrowser.open(url)


url = input("The Weekly Economist Link: ")
response = requests.get(url)
articles = get_articles(response.text)
add_to_things(articles)
