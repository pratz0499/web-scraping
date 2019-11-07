import csv
from datetime import datetime
import urllib.request
import requests
from bs4 import BeautifulSoup
import traceback

def get_name(body):
    return body.find('span', {'class':'jcn'}).a.string

def get_phone_number(body):
    num_dict={}
    num_dict['icon-dc'] = '+'
    num_dict['icon-fe'] = '('
    num_dict['icon-ji'] = '9'
    num_dict['icon-yz'] = '1'
    num_dict['icon-hg'] = ')'
    num_dict['icon-ba'] = '-'
    num_dict['icon-rq'] = '5'
    num_dict['icon-wx'] = '2'
    num_dict['icon-vu'] = '3'
    num_dict['icon-nm'] = '7'
    num_dict['icon-ts'] = '4'
    num_dict['icon-acb'] = '0'
    num_dict['icon-po'] = '6'
    num_dict['icon-lk'] = '8'
    phone = ''
    try:
        p_tag = body.find('p', {'class':'contact-info'})
        # print(type(p_tag))
        span = p_tag.find('span')
        sp_list = span.findAll('span')
        for i in sp_list:
            num=i.attrs['class'][1]
            phone += num_dict[num]
        return phone
    except AttributeError:
        print(traceback.format_exc())
        return ''

def get_rating(body):
    rating = 0.0
    text = body.find('span', {'class':'star_m'})
    if text is not None:
        for item in text:
            rating += float(item['class'][0][1:])/10

    return rating

def get_rating_count(body):
    text = body.find('span', {'class':'rt_count'}).string

    rating_count =''.join(i for i in text if i.isdigit())
    return rating_count

def get_address(body):
    return body.find('span', {'class':'mrehover'}).text.strip()

def get_location(body):
    text = body.find('a', {'class':'rsmap'})
    if text == None:
        return
    text_list = text['onclick'].split(",")
    
    latitutde = text_list[3].strip().replace("'", "")
    longitude = text_list[4].strip().replace("'", "")
    
    return latitutde + ", " + longitude
def get_article(url_string):
    # headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'en-US,en;q=0.9',
    # 'cache-control': 'max-age=0',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-site': 'none',
    # 'sec-fetch-user': '?1',
    # 'upgrade-insecure-requests': 1,
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    while(True):
        try:
            req = urllib.request.Request(url_string,None,headers)
            response = urllib.request.urlopen(req)
            break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return 'Invalid'
            else:
                pass
        except:
            pass
    return response.read()
page_number=1
details_count=1


with open("D:\\Organised\\Projects\\DBMS\\customer_details.csv","w") as out_file:
    fields = ['Name','Phone','Rating','Rating Count','Address','Location']
    csvwriter = csv.DictWriter(out_file, fieldnames=fields)
    csvwriter.writeheader()
    while True:

        if page_number>2:
            break
        print("here")
        url="https://www.justdial.com/Bangalore/Estate-Agents-in-Sarakki-Nagar/nct-10192623/page-%s"%(page_number)
        text = get_article(url)
        #print(text)
        soup = BeautifulSoup(text, "html.parser")
        details = soup.find_all('li', {'class': 'cntanr'})
        #print(details)
        #break
        for i in details:
            dictionary_details={}
            name=get_name(i)
            phone=get_phone_number(i)
            print(phone)
            rating=get_rating(i)
            count=get_rating_count(i)
            address=get_address(i)
            location=get_location(i)

            if name != None:
                dictionary_details['Name'] = name
            if phone != None:
                print('getting phone number')
                dictionary_details['Phone'] = phone
            if rating != None:
                dictionary_details['Rating'] = rating
            if count != None:
                dictionary_details['Rating Count'] = count
            if address != None:
                dictionary_details['Address'] = address
            if location != None:
                dictionary_details['Address'] = location

            csvwriter.writerow(dictionary_details)
            print("#" + str(details_count) + " " , dictionary_details)
            details_count += 1

        
        page_number += 1
    out_file.close()
