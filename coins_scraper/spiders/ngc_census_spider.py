from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "ngc_census"

    start_urls = [
            "https://www.ngccoin.com/census/world/germany-states-1871-1925/sc-144/5m/",
    ]
    
    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall()
            }
        
        for row in response.css("div.pinned"):
            pass