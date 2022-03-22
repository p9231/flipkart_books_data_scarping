import scrapy
from ..items import FlipkartBooksItem

class FlipkartSpiderSpider(scrapy.Spider):
    name = 'flipkart_spider'
    start_urls = ['https://www.flipkart.com/search?q=books&sid=bks&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=books%7CBooks&requestId=7801d899-8fb5-468a-9360-bc99e2720825&as-searchtext=books&page=1']

    def parse(self, response):
        items = FlipkartBooksItem()


