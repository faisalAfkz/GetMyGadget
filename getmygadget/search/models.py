from abc import ABC,abstractmethod
from bs4 import BeautifulSoup
import requests
import re
import json
import urllib3

numOfProduct = 20
timeout = 3

class ScrapSearch(ABC):
    @abstractmethod
    def fetch(self):
        pass

class Web1(ScrapSearch):
    url = "https://www.startech.com.bd/product/search?sort=p.price&order=ASC&search="

    def addSearch(self,search):
        search = search.replace(" ", "%20")
        self.url = self.url + search

    def fetch(self):
        name = []
        price = []
        link = []
        img = []
        response = requests.get(self.url,timeout = timeout)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')

        products = soup.find_all('div', {'class': 'product-thumb'})
        products = products[:numOfProduct]
        for p in products:
            button = p.find('div', {'class': 'cart-btn'}).text
            button = button.lstrip().rstrip()

            if button == 'Buy Now':
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
        response = requests.get(self.url,timeout = timeout)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')

        products = soup.find_all('li', {'class': 'item product product-item'})
        products = products[:numOfProduct]

        for p in products:
            name.append(p.find('h2', {'class': 'product-name product-item-name'}).text)
            temp = p.find('span', {'class': 'price'}).text
            temp = re.sub('\W+', '', temp)
            temp = temp[:-2]
            price.append(temp)
            link.append(p.find('a', {'class': 'product-item-link'}).get('href'))
            img.append(p.find('img').get('data-src'))

        return name,price,link,img

class Web3(ScrapSearch):
    url = "https://www.daraz.com.bd/catalog/?q="

    def addSearch(self,search):
        search = search.replace(" ", "%20")
        self.url = self.url + search

    def fetch(self):
        name = []
        price = []
        link = []
        img = []

        response = requests.get(self.url,timeout = timeout)
        soup = BeautifulSoup(response.content, 'html.parser')
        script = soup.find_all('script')[3]
        script = str(script)
        script = script[24:-9]
        data = json.loads(script)
        products = data['mods']['listItems']
        products = products[:numOfProduct]
        for p in products:
            name.append(p['name'])
            temp = p['priceShow']
            temp = re.sub('\W+', '', temp)
            price.append(temp)
            link.append(p['productUrl'])
            img.append(p['image'])

        return name,price,link,img

class Web4(ScrapSearch):
    url = "https://www.ryanscomputers.com/api/search?keyword="

    def addSearch(self,search):
        search = search.replace(" ", "%2520")
        self.url = self.url + search + "&returnType=searchPageHTML"

    def fetch(self):
        name = []
        price = []
        link = []
        img = []
        response = requests.get(self.url,timeout = timeout)
        response.close()
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')

        products = soup.find_all('div', {'class': 'product-box'})
        products = products[:numOfProduct]
        for p in products:
            temp = p.find('div', {'class': 'product-content-info'})
            name.append(temp.find('a').text)
            price.append(p.find('span',{'class':'price'}).text)
            link.append(p.find('a').get('href'))
            img.append(p.find('img').get('src'))

        return name, price, link, img

class Web5(ScrapSearch):
    search = ''

    def addSearch(self,search):
        search = search.replace(" ", "%20")
        self.search = search

    def fetch(self):
        name = []
        price = []
        link = []
        img = []
        MAX_VALUES_PER_FACET = 10  # no. of result show per page
        page_no = 0  # default page no.
        URL = 'https://eza2j926q5-3.algolianet.com/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser%20(lite)%3B%20react%20(16.13.1)%3B%20react-instantsearch%20(5.7.0)%3B%20JS%20Helper%20(2.28.1)&x-algolia-application-id=EZA2J926Q5&x-algolia-api-key=ca9abeea06c16b7d531694d6783a8f04'  # API URL for querying
        urllib3.disable_warnings()

        form_data = {
            "requests": [{"indexName": "products", "params": "query=" + self.search + "&maxValuesPerFacet=" + str(
                MAX_VALUES_PER_FACET) + "&page=" + str(
                page_no) + "&highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&facets=%5B%22price%22%2C%22category_name%22%2C%22brand_name%22%2C%22shop_name%22%2C%22color%22%5D&tagFilters="}]
        }

        # form_data which is dynamic and creates new set of results and send back
        response = requests.post(URL, json=form_data, verify=False)  # requests for data using POST and JSON form data

        result = json.loads(response.text)  # load json data result
        products = result['results'][0]['hits']
        products = products[:numOfProduct]
        for p in products:
            if p['discounted_price'] != "0.00":
                name.append(p['name'])
                temp = p['discounted_price']
                if temp is None :
                    temp = p['price']
                temp = str(int(float(temp)))
                price.append(temp)
                temp = "https://evaly.com.bd/products/"
                link.append(temp + p['slug'])
                img.append(p['product_image'])

        return name, price, link, img