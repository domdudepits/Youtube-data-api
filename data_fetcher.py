from requests_html import HTMLSession 
from bs4 import BeautifulSoup as bs

def scrap(url):
 views = ''
 pdate = ''
 session = HTMLSession()
 response = session.get(url)
 soup = bs(response.html.html, "html.parser")


 views = soup.find("meta", itemprop="interactionCount")['content']
 pdate = soup.find("meta", itemprop="datePublished")['content']
 result = {"Views": views, "Date Published": pdate}
 return result
