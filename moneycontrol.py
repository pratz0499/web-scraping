import csv
from datetime import datetime
import urllib.request
import requests
from bs4 import BeautifulSoup

url="https://m.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI"
page=urllib.request.urlopen(url)
soup=BeautifulSoup(page,'html.parser')
#print(soup.prettify())
name_box=soup.find('a',attrs={'class':'rbt_18bl'})
name=name_box.text.strip()
print(name)

price_box=soup.find(id='b_last_value')
price=price_box.text
print(price)


with open('stocks.csv','a')as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow([name,price,datetime.now()])
    
