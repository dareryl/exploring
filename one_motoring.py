import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import pandas as pd
from bs4 import BeautifulSoup
import os 
import time 

os.chdir('/Users/darylchan/desktop/python/python scrapper')

folder = 'View from Ang Mo Kio Ave 1 Flyover'
if not os.path.isdir(folder): 
    os.mkdir(folder)

os.chdir(folder)


for i in range(10):
    r = requests.get('https://www.onemotoring.com.sg/content/onemotoring/home/driving/traffic_information/traffic-cameras/cte.html', verify=False)
    soup = BeautifulSoup(r.content.decode('utf-8'), 'html.parser')
    cell = soup.find_all('img')
    found = False
    for i in cell: 
        if i['alt'] == folder:
            jpeg_url = i['src'][2:]
            timestamp = jpeg_url.split('_')[2]
            found = True
            break

    if found:
        imgfile = timestamp + '.jpeg'
        with open(imgfile, 'wb') as f:
            q = requests.get('https://' + jpeg_url, verify=False)
            f.write(q.content)
            print('created ' + imgfile)


    time.sleep(120)
