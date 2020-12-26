
from abc import ABC,abstractmethod
from bs4 import BeautifulSoup
import requests

class ScrapTrend(ABC):
    @abstractmethod
    def fetch(self):
        pass

class Web1(ScrapTrend):
    url = "https://ajkerdeal.com/en/category/gadgets"


    def fetch(self):
        name = ['']
        price = ['']
        link = ['']
        img = ['']
        response = requests.get(self.url)

        data = response.text
        soup = BeautifulSoup(data, 'html.parser')

        products = soup.find_all('div', {'class': 'deal-info-container'})
        for p in products:
            name.append(p.find('span', {'class': 'deal-title-container'}).text)
            price.append(p.find('span', {'class': 'deal-price-container'}).text)
            img.append(p.find('img', {'class': 'deal_image'}).get('src'))
            link.append(p.find('a').get('href'))
        return name,price,link,img


