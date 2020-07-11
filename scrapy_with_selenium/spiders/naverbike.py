# -*- coding: utf-8 -*-
import scrapy


class NaverbikeSpider(scrapy.Spider):
    name = 'naverbike'
    allowed_domains = ['auto.naver.com/bike/mainList.nhn']
    start_urls = ['http://auto.naver.com/bike/mainList.nhn']
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_with_selenium.middlewares.ScrapyWithSeleniumDownloaderMiddleware': 100
        }
    }

    def parse(self, response):
        print(response.text)
        # print(response.text)
