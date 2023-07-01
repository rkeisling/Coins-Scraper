from pathlib import Path

import scrapy
import datetime
import time
import re


class NgcTypeCensusSpider(scrapy.Spider):
    name = "ngc_type_census"

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
        
        # links_list = []
        
        # for link in alphabetical_links:
        #     sub_dict = {"alpha_link": link.css("::href").get(),
        #                 "name_of_category": link.css("div span:nth-child(1)::text").get(),
        #                 "num_results_in_category": link.css("div span::nth-child(1)::text").get()}
            
        #     links_list.append(sub_dict)
        
        # request = scrapy.Request(
        #     response.request.url + "data",
        #     callback=self.parse_details,
        #     cb_kwargs={"links_list": links_list}
        # )
        
        # yield request

        
                    
    def parse_further_links(self, response):
        # extract data from these dudes
        # can't just follow link because the page is too advanced (no links to follow)
        details = response.css("div.subcategory-list div")
        
        print(details[0])
        
        letter = details.css("::attr(parent-name)").get()
        base_url = details.css("::attr(base-url)").get()
        
        url_to_follow = "https://ngccoin.com" + base_url + letter + "/" + "subcategories"
        print(url_to_follow)
        
        yield response.follow(url_to_follow, self.parse_more_sublinks)
        

    def parse_more_sublinks(self, response):
        links_from_subcategory = response.css("div.subcategory-list div a")
        
        for link in links_from_subcategory:
            yield {
                "country_name": link.css("::text").get(),
                "link": link.css("::attr(href)").get()
            }