# -*- coding: utf-8 -*-
#programer : Parinaz Soltanzadeh
#output ha dar ghaleb name,price,imagelink dar 3 file items.json , items.csv , items.xml gharar dade shode ast.
import scrapy
from ..items import AmazonscrapyItem

class AmazonspiderSpider(scrapy.Spider):
    name = 'amazonspider'
    page_number = 2
    #allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108&dc&qid=1591103901&rnid=13896617011&ref=sr_nr_n_2']

    def parse(self, response):
        items = AmazonscrapyItem()
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_price = response.css('.a-price span').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
'''
agar bekhahim chand safhe ra scrap konim
        next_page = 'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108&dc&page=' + str(AmazonspiderSpider.page_number) + '&qid=1591103904'
        if AmazonspiderSpider.page_number <= 142:
            AmazonspiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
'''

