import requests
import json
import webbrowser
from bs4 import BeautifulSoup


def get_articles(response):
    """
    Get Article headings from GET request response.

    Parameters
    ----------
    response_text : requests.Response
       GET request response from The Economist weekly link 

    Returns
    -------
    articles : dict { heading : articles[] }
    """

    articles = {}
    soup = BeautifulSoup(response.text, 'lxml')

    # Find articles in sections LEADERS and BRIEFING
    SECTIONS_CLASS_1 = 'layout-weekly-edition-section ds-layout-grid'
    ARTICLES_CLASS_1 = 'teaser__headline teaser__headline--sc3'

    sections1 = soup.find_all('section', attrs={"class": SECTIONS_CLASS_1})

    for section in sections1:
        if section.h2.text == 'Leaders':
            articles['Leaders'] = \
                section.find_all(attrs={'class': ARTICLES_CLASS_1})
        elif section.h2.text == 'Briefing':
            articles['Briefing'] = \
                section.find_all(attrs={'class': ARTICLES_CLASS_1})

    # Find articles in other sections
    SECTIONS_CLASS_2 = \
        'layout-weekly-edition-section layout-weekly-edition-section--cols ds-layout-grid'
    ARTICLES_CLASS_2 = 'teaser__headline teaser__headline--sc1'

    sections2 = soup.find_all('section', attrs={"class": SECTIONS_CLASS_2 })
    for section in sections2:
        if section.h2.text == 'Britain':
            articles['Britain'] = \
                section.find_all(attrs={"class": ARTICLES_CLASS_2})
        elif section.h2.text == 'Europe':
            articles['Europe'] = \
                section.find_all(attrs={"class": ARTICLES_CLASS_2})
        elif section.h2.text == 'United States':
            articles['United States'] = \
                section.find_all(attrs={"class": ARTICLES_CLASS_2})
        elif section.h2.text == 'Middle East & Africa':
            articles['Middle East & Africa'] = \
                section.find_all(attrs={"class": ARTICLES_CLASS_2})
        elif section.h2.text == 'The Americas':
            articles['The Americas'] = \
                section.find_all(attrs={"class": ARTICLES_CLASS_2})
        elif section.h2.text == 'Asia':
            articles['Asia'] = \
                section.find_all(attrs={"class": ARTICLES_CLASS_2})
        elif section.h2.text == 'China':
            articles['China'] = \
                section.find_all(attrs={"class": ARTICLES_CLASS_2})
        elif section.h2.text == 'International':
            articles['International'] = \
                section.find_all(attrs={"class": ARTICLES_CLASS_2})
        elif section.h2.text == 'Special report':
            articles['Special report'] = \
                section.find_all(attrs={"class": ARTICLES_CLASS_2})
        elif section.h2.text == 'Business':
            articles['Business'] = \
                section.find_all(attrs={"class": ARTICLES_CLASS_2})
        elif section.h2.text == 'Finance & economics':
            articles['Finance & economics'] = \
                section.find_all(attrs={"class": ARTICLES_CLASS_2})
        elif section.h2.text == 'Science & technology':
            articles['Science & technology'] = \
                section.find_all(attrs={"class": ARTICLES_CLASS_2})
        elif section.h2.text == 'Graphic detail':
            articles['Graphic detail'] = \
                section.find_all(attrs={"class": ARTICLES_CLASS_2})

    return articles


def add_to_things(articles):
    """
    Adds articles to Things 3.

    Parameters
    ----------
    articles : dict { heading : articles[] }

    Returns
    -------
    None
    """

    # Add "The world this week"
    webbrowser.open('things:///add?title='
                    'Politics%20this%20week&list=The%20Economist')
    webbrowser.open('things:///add?title='
                    'Business%20this%20week&list=The%20Economist')

    # Add the other sections
    for heading, section in articles.items():
        for article in section:
            title = article.text.replace(" ", "%20")
            title = title.replace("’", "'")
            url = (f'things:///add?title={title}'
                   f'&list=The%20Economist&heading={things_heading(heading)}')
            webbrowser.open(url)


def things_heading(economist_heading):
    """Returns headings formated for Things 3"""
    
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


def main():
    url = input('The Weekly Economist Link: ')

    # Sends a GET request to the url provided
    response = requests.get(url)

    # Gets articles from the response
    articles = get_articles(response)

    # Add the articles to Things 3
    add_to_things(articles)

if __name__ == '__main__':
    main()
