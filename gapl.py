import pandas as pd
import requests
import urllib.request
from bs4 import BeautifulSoup

user_agent ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url="https://www.justdial.com/Bangalore/Automobile-Part-Manufacturers/nct-10028195"
headers={'User-Agent':user_agent,}

request=urllib.request.Request(url,None,headers)
response=urllib.request.urlopen(request)
data=response.read()
soup=BeautifulSoup(data,'html.parser')
#soup.select('.lng_cont_name')
df=pd.DataFrame({'col':['companyname']})
for i in soup.select('lng_cont_name'):
  df.append(i)
  print(df,'\n')
