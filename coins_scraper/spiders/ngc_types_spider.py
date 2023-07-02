from pathlib import Path

import scrapy
import datetime
import json
import os

def get_country_urls(filename):
        current_dir = os.getcwd()
        print(current_dir)
        json_file_path = os.path.abspath(os.path.join(current_dir, filename))
        with open(json_file_path) as fin:
            return json.loads(fin.read())

class NgcTypesSpider(scrapy.Spider):
    name = "ngc_types"

    start_urls = [
            "https://ngccoin.com" + each["link"] for each in get_country_urls("ngc_countries.json")
        ]
    
    print(start_urls)
    
    def parse(self, response):
        # exclude headers
        type_links = response.css('div.set-type:not(.set-type-header)')
        
        for type_link in type_links:
            href = type_link.css("a::attr(href)").get()
            denomination = type_link.css("a div.name::text").get()
            count = type_link.css("a div.count::text").get()
            
            country = response.request.url.rsplit("/")[-2]
            stripped_country = country.replace("/", "")
            
            yield {
                "country_name": stripped_country,
                "denomination": denomination,
                "population": count,
                "link": "https://ngccoin.com" + href,
                "extracted_at": str(datetime.datetime.now())
            }
