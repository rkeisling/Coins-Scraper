from pathlib import Path

import scrapy
import datetime
import re


class NgcCountriesSpider(scrapy.Spider):
    # recommend to run with:
    # scrapy crawl ncg_countries -O ngc_countries.json
    
    name = "ngc_countries"

    start_urls = [
            "https://www.ngccoin.com/census/"
        ]
    
    def parse(self, response):
        alphabetical_links = response.xpath('//a[starts-with(@href, "/census/world/")]')
        filtered_links = []
        
        pattern = r"^/census/world/(?!$)(?!.*(?:china|canada|australia|south-africa|great-britain|mexico|russia|poland|germany)).*$"
        for link in alphabetical_links:
            href = link.xpath('@href').get()
            if re.match(pattern, href) and href != "/census/world/":
                    filtered_links.append(link)

        
        yield from response.follow_all(filtered_links, self.parse_further_links)
         
    def parse_further_links(self, response):
        details = response.css("div.subcategory-list div")
        
        letter = details.css("::attr(parent-name)").get()
        base_url = details.css("::attr(base-url)").get()
        
        url_to_follow = "https://ngccoin.com" + base_url + letter + "/" + "subcategories"
        
        yield response.follow(url_to_follow, self.parse_more_sublinks)
        
    def parse_more_sublinks(self, response):
        links_from_subcategory = response.css("div.subcategory-list div a")
        
        for link in links_from_subcategory:
            yield {
                "country_name": link.css("::text").get(),
                "link": link.css("::attr(href)").get(),
                "last_updated_at": str(datetime.datetime.now())
            }