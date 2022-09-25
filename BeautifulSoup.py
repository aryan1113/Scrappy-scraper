import urllib3
from bs4 import BeautifulSoup
url = "https://www.youtube.com/watch?v=b8m9zhNAgKs&list=RDZaWdMrmEhDA&index=13"
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, "lxml")
print(soup.find('title').text)