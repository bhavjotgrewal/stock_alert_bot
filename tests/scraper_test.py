from sre_constants import ASSERT
import unittest

from bin.scraper.scraper import CanadaComputersScraper, MemoryExpressScraper, NeweggScraper, Scraper

HEADERS = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                        'like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

class TestScraper(unittest.TestCase):

    def test_in_stock_CANADA_COMP(self):

        scraper = Scraper('C:\\Users\\65rgr\Documents\\Projects\\stock_alert_bot\\in-stock-alert\\tests\data\\Canada_Computers_in_stock.html', CanadaComputersScraper, HEADERS)
        scraper.scrape()
        self.assertEqual(scraper.scrapes[0], ['ASUS TUF Gaming GeForce RTX 3080 Ti OC Edition', True])

    def test_out_of_stock_CANADA_COMP(self):

        scraper = Scraper('C:\\Users\\65rgr\Documents\\Projects\\stock_alert_bot\\in-stock-alert\\tests\data\\Canada_Computers_out_of_stock.html', CanadaComputersScraper, HEADERS)
        scraper.scrape()
        self.assertEqual(scraper.scrapes[0], ['Patriot Burst 240GB  SSD', False])

    def test_in_stock_NEWEGG(self):

        scraper = Scraper('C:\\Users\\65rgr\Documents\\Projects\\stock_alert_bot\\in-stock-alert\\tests\data\\Newegg_in_stock.html', NeweggScraper, HEADERS)
        scraper.scrape()
        self.assertEqual(scraper.scrapes[0], ['MSI Ventus GeForce RTX 3050 Video Card RTX 3050 Ventus 2X 8G OC', True])

    def test_out_of_stock_NEWEGG(self):

        scraper = Scraper('C:\\Users\\65rgr\Documents\\Projects\\stock_alert_bot\\in-stock-alert\\tests\data\\Newegg_out_of_stock.html', NeweggScraper, HEADERS)
        scraper.scrape()
        self.assertEqual(scraper.scrapes[0], ['Newest ASUS 15.6" FHD High Performance Gaming Laptop, AMD 2nd Gen Quad Core Ryzen 5 3550H upto 3.7GHz, 8GB RAM, 1024GB SSD, NVIDIA GeForce GTX 1050, Backlit Keyboard, Windows 10', False])

    def test_in_stock_MEMORY_EXPRESS(self):

        scraper = Scraper('C:\\Users\\65rgr\Documents\\Projects\\stock_alert_bot\\in-stock-alert\\tests\data\\Memory_in_stock.html', MemoryExpressScraper, HEADERS)
        scraper.scrape()
        self.assertEqual(scraper.scrapes[0], ['MSI GeForce RTX 3060 VENTUS 2X 12GB PCI-E  w/ HDMI, Triple D', True, '10'])

    def test_out_of_stock_MEMORY_EXPRESS(self):

        scraper = Scraper('C:\\Users\\65rgr\Documents\\Projects\\stock_alert_bot\\in-stock-alert\\tests\data\\Memory_out_of_stock.html', MemoryExpressScraper, HEADERS)
        scraper.scrape()
        self.assertEqual(scraper.scrapes[0], ['MSI GeForce RTX 3060 Ti VENTUS 2X OC LHR 8GB PCI-E  w/ HDMI, Triple D', False, '0'])

if __name__ == '__main__':
    unittest.main()