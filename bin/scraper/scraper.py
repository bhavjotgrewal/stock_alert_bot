from abc import ABC
from typing import List, Union
import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import re

class ScraperStrategy(ABC):
    
    @abstractmethod

    def scrape(self, link, headers) -> List[Union[str, bool]]:
        pass

class NeweggScraper(ScraperStrategy):

    def scrape(self, link, headers) -> List[Union[str, bool]]:

        try:
            if '.html' in link:
                with open(link, 'r', encoding='utf-8') as f:
                    contents = f.read()
                    soup = BeautifulSoup(contents, 'lxml')
            
            else:
                r = requests.get(link, headers=headers)
                soup = BeautifulSoup(r.text, 'lxml')

            name = soup.find('title').text[:-12]

            if soup.find('div', {'class': 'product-flag'}) == None:
                in_stock = True
            else:
                if 'OUT OF STOCK' in soup.find('div', {'class': 'product-flag'}).text:
                    in_stock = False
                else:
                    in_stock = True

            return [name, in_stock]

        except:
            print('connection blocked')
            pass

class MemoryExpressScraper(ScraperStrategy):

    def scrape(self, link, headers) -> List[Union[str, bool]]:

        try:
            if '.html' in link:
                with open(link, 'r', encoding='utf-8') as f:
                    contents = f.read()
                    soup = BeautifulSoup(contents, 'lxml')
            
            else:
                r = requests.get(link, headers=headers)
                soup = BeautifulSoup(r.content, 'lxml')

            name = soup.find('title').text[:-43]

            if soup.find('div',
                        {'class': 'c-capr-inventory-store'}).find(
                'span',
                {'class': 'c-capr-inventory-store__availability InventoryState_OutOfStock'}) is \
                    None:
                in_stock = True
                quantity = soup.find('div',
                                    {'class': 'c-capr-inventory-selector__details-online'}).find('div',
                                                                                                {
                                                                                                    'class': 'c-capr-inventory-store'}).find(
                    'span',
                    {'class': 'c-capr-inventory-store__availability InventoryState_InStock'}).text
                amount = re.findall(r'\b\d+\b', quantity)
            else:
                in_stock = False
                amount = [0]

            return [name, in_stock, str(amount[0])]

        except:
            print('connection blocked')
            pass

class CanadaComputersScraper(ScraperStrategy):
    
    def scrape(self, link, headers) -> List[Union[str, bool]]:
        
        try:

            if '.html' in link:
                with open(link, 'r', encoding='utf-8') as f:
                    contents = f.read()
                    soup = BeautifulSoup(contents, 'lxml')
            
            else:
                r = requests.get(link, headers=headers)
                soup = BeautifulSoup(r.content, 'lxml')
                
            soup = BeautifulSoup(contents, 'lxml')

            name = soup.find('title').text

            if 'SOLD OUT ONLINE' in soup.find('div', {'class': 'mb-0'}).text:
                in_stock = False
            else:
                in_stock = True

            return [name[:-33], in_stock]

        except:
            print('connection blocked')
            pass

class Scraper():

    def __init__(self, link, scraper_strategy: ScraperStrategy, headers: dict) -> None:

        self.link = link
        self.scraper_stragey = scraper_strategy
        self.headers = headers
        self.scrapes = []

    def update_link(self, link) -> None:
        
        self.link = link

    def update_scraper(self, scraper) -> None:

        self.scraper_stragey = scraper

    def scrape(self) -> List[Union[str, bool]]:

        result = self.scraper_stragey.scrape(self, self.link, self.headers)
        self.scrapes.append(result)