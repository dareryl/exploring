import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
url = "https://www.bbc.com/" 
f = open("scapped_BBC.csv", "w", encoding = "utf8", newline = '')
writer = csv.writer(f, delimiter = ',')
writer.writerow(['headline','url'])
page = requests.get(url, verify=False)
soup = BeautifulSoup(page.content, 'html.parser')
cell = soup.find_all('h3')
for row in cell: 
    headline = row.text.strip()
    url = row.find('a')
    if url:
        attr = url.get('href')
        if attr:
            if 'https://www.bbc.com' in attr: 
                writer.writerow([headline, attr])
            else: 
                writer.writerow([headline, 'https://www.bbc.com' + attr])
    else: 
        writer.writerow([headline])
f.close()
df = pd.read_csv('scapped_BBC.csv')
df
