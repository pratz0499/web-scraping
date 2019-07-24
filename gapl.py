import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException


user_agent ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,}
CompanyName=[]
url="https://www.justdial.com/Bangalore/Automobile-Part-Manufacturers/nct-10028195"

driver=webdriver.Chrome("D:\\Downloads\\chromedriver.exe")
driver.get(url)
soup=BeautifulSoup(driver.page_source,"lxml")
#ActionChains(drivers).move_to_element(drivers.find_element_by_tag_name("h2")).click().perform()

cn=driver.find_elements_by_tag_name("h2")
ActionChains(driver).move_to_element(driver.find_element_by_xpath("//a[@rel='next']")).click().perform()


while True:
	try:
		elements=driver.find_elements_by_tag_name("h2")
		ActionChains(driver).move_to_element(driver.find_element_by_xpath("//a[@rel='next']")).click().perform()
		soup=BeautifulSoup(driver.page_source,"lxml")
		cn=soup.select(".lng_cont_name")
		for i in cn:
			x=i.text.strip()
			CompanyName.append(x)
	except WebDriverException:
		time.sleep(5)
