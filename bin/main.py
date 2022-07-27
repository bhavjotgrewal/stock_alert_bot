from window.window import Window
from processor.processor import Processor
from scraper.scraper import CanadaComputersScraper, MemoryExpressScraper, NeweggScraper, Scraper
from scraper.product_loader import Loader
import time
from datetime import datetime

HEADERS = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                        'like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

def main():

    w = Window()
    loader = Loader()

    productsCanadaComp = loader.load_data(r"C:\Users\65rgr\Documents\Projects\stock_alert_bot\in-stock-alert\data\Canada_Computer_list.txt")
    productsMemex = loader.load_data(r"C:\Users\65rgr\Documents\Projects\stock_alert_bot\in-stock-alert\data\Memex_list.txt")
    productsNewegg = loader.load_data(r"C:\Users\65rgr\Documents\Projects\stock_alert_bot\in-stock-alert\data\Newegg_list.txt")

    stores = {}

    stores[CanadaComputersScraper] = [productsCanadaComp, 'Canada Computers']
    stores[MemoryExpressScraper] = [productsMemex, 'Memory Express']
    stores[NeweggScraper] = [productsNewegg, 'Newegg']

    while True:

        for scraper in stores:

            processor = Processor(stores[scraper][0], scraper)
            scraped = processor.multiprocess_scraping()

            w.fill(stores[scraper][1], 'N/A', scraped)
            w.display()

if __name__ == "__main__":

    main()