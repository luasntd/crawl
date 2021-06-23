# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "mac"
    allowed_domains = ["hifa.vn"]
    start_urls = [
        'https://hifa.vn/cua-hang/',
    ]

    def parse(self, response):
        for book_url in response.css("div.image-none ​> a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_book_page)
        next_page = response.css("a.next page-number > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_book_page(self, response):
        item = {}
        item["title"] = product.css("h1 ::text").extract_first()
        item['category'] = response.css("div.meta-art > a ::text").extract_first()
        item['description'] = response.css("div.entry > p::text"
            ).extract_first()
        item['linksFshare'] = response.css('a.autohyperlink ::text').extract_first()
        yield item
