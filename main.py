from bs4 import BeautifulSoup
import requests

url_date_start = "03/10/2023"
url_date_end = "18/10/2023"


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


url_begin = "https://office.gemotest.ru/OrderPrint_Xml.php?DateStart="
url_middle = "&DateEnd="
url_end = "&pp=23d927e006b320a11af39d6d701cf169"

list_of_links = find_files(url_begin + url_date_start + url_middle + url_date_end + url_end)
end = list_of_links[0].replace("×tamp", "&timestamp")
download("https://office.gemotest.ru" + end)
