from requests import get
from bs4 import BeautifulSoup as bs


def scrap(url):
 views = ''
 pdate = ''
 response = get(url)
 soup = bs(response.content, "html.parser")


 views = soup.find("meta", itemprop="interactionCount")['content']
 pdate = soup.find("meta", itemprop="datePublished")['content']
 result = {"Views": views, "Date Published": pdate, "Title": 'title'}
 return result
