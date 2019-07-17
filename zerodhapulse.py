import urllib.request
import csv
from datetime import datetime
from urllib.parse import unquote
import requests
from bs4 import BeautifulSoup
import pandas as pd
user_agent ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url="http://pulse.zerodha.com/"
headers={'User-Agent':user_agent,}

request=urllib.request.Request(url,None,headers)
response=urllib.request.urlopen(request)
data=response.read()
soup=BeautifulSoup(data,'html.parser')


heading=[]
news=[]
links=[]


head_box=soup.select('.title')
for i in head_box:
  head=i.text.strip()
  heading.append(head)
  
#for j in heading:
  #print(j)
  


description=soup.select('.desc')
for k in description:
  des=k.text.strip()
  news.append(des)
#for descript in news:
 # print(descript)

for h in soup.find_all('h2'):
  a=h.find('a')
  links.append(a.attrs['href'])
  
#for k in links:
  #print(k)
data = pd.DataFrame(columns=["headings","news","links"])
data["headings"]=heading
data["news"]=news
data["links"]=links
data.to_csv("news.csv",index=True)
  
  








