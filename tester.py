import  requests
from bs4 import BeautifulSoup as bs
import pandas as pd

df = pd.read_excel('Zee Music Company.xlsx')
for url in df['youtube link']:
 response = requests.get(f"http://127.0.0.1:5000/{url}")
 data = requests.json()
 print(data)

