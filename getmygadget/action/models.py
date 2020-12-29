from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests


class ScrapTrend(ABC):
    @abstractmethod
    def fetch(self):
        pass


class Web1(ScrapTrend):
    url = "https://ajkerdeal.com/en/category/gadgets"

    def fetch(self):
        response = requests.get(self.url)

        data = response.text
        soup = BeautifulSoup(data, 'html.parser')

        products = soup.find_all('div', {'class': 'deal-info-container'})
        return products
