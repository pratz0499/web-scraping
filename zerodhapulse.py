import urllib.request
import requests
from bs4 import BeautifulSoup
user_agent ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

urls=["https://pulse.zerodha.com/"]
headers={'User-Agent':user_agent,}

data=[]
request=urllib.request.Request(url,None,headers)
response=urllib.request.urlopen(request)
datum=response.read()

soup=BeautifulSoup(datum,'html.parser')
#head_box=soup.find('h2',attrs={'class':'title'})
head_box=soup.select('.title')
for i in head_box:
  head=i.text.strip()
  data.append(head)
for news in data:
  print(news)
#soup.select('.title')
#soup1=BeautifulSoup('<h2 class="title"</h2>')
#print(soup1.prettify())
#tag=soup1.h2
#tag.contents
