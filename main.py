from bs4 import BeautifulSoup
import requests

url_date_start = ""
url_date_end = ""


def find_files(url):
    soup = BeautifulSoup(requests.get(url).text)
    hrefs = []
    for a in soup.find_all('a'):
        hrefs.append(a['href'])
    return hrefs


def download(url):
    r = requests.get(url)
    with open('1.xml', 'wb') as f:
        f.write(r.content)

while(True):
    url_begin = "https://office.gemotest.ru/"
    url_middle = ""
    url_end = ""
    
    list_of_links = find_files(url_begin + url_date_start + url_middle + url_date_end + url_end)
    end = list_of_links[0].replace("×tamp", "&timestamp")
    download("https://office.gemotest.ru" + end)
    time.sleep(60*60*24)
