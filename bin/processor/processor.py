from multiprocessing import Process, Queue, Manager
import multiprocessing
from typing import List

from scraper.scraper import Scraper, ScraperStrategy

class Processor():

    def __init__(self, product_list: List[str], scraper_strategy: ScraperStrategy) -> None:
        self.product_list = product_list
        self.scraper_strategy = scraper_strategy
        self.headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                        'like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

    def update_scraper(self, scraper) -> None:
        self.scraper_strategy = scraper

    def multiprocess_scraping(self):

        scraper = Scraper("", self.scraper_strategy, self.headers)

        for product_link in self.product_list:

            scraper.update_link(product_link)

            Process(target=scraper.scrape(), args=()).start()

        return scraper.scrapes
