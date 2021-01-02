from abc import ABC,abstractmethod
from bs4 import BeautifulSoup
import requests
import re

class ScrapSearch(ABC):
    @abstractmethod
    def fetch(self):
        pass

class Web1(ScrapSearch):
    url = "https://www.startech.com.bd/product/search?search="

    def addSearch(self,search):
        search = search.replace(" ", "%20")
        self.url = self.url + search

    def fetch(self):
        name = []
        price = []
        link = []
        img = []
        response = requests.get(self.url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')

        products = soup.find_all('div', {'class': 'product-thumb'})

        for p in products:
            name.append(p.find('h4', {'class': 'product-name'}).text)
            temp = p.find('div', {'class': 'price'}).text
            temp = re.sub('\W+', '', temp)
            price.append(temp)
            link.append(p.find('a').get('href'))
            img.append(p.find('img').get('src'))

        return name,price,link,img

class Web2(ScrapSearch):
    url = "https://ucc-bd.com/catalogsearch/result//?q="

    def addSearch(self,search):
        search = search.replace(" ", "%20")
        self.url = self.url + search

    def fetch(self):
        name = []
        price = []
        link = []
        img = []
        response = requests.get(self.url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')

        products = soup.find_all('li', {'class': 'item product product-item'})

        for p in products:
            name.append(p.find('h2', {'class': 'product-name product-item-name'}).text)
            temp = p.find('span', {'class': 'price'}).text
            temp = re.sub('\W+', '', temp)
            temp = temp[:-2]
            price.append(temp)
            link.append(p.find('a', {'class': 'product-item-link'}).get('href'))
            img.append(p.find('img').get('data-src'))

        return name,price,link,img