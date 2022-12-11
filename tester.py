import  requests
from bs4 import BeautifulSoup as bs
from xmltojson import parse

url = 'https://www.youtube.com/watch?v=MAu1fPqlivk'
response = requests.get(url)
soup = bs(response.content, "html.parser")
# result = parse(soup)
print(soup)
