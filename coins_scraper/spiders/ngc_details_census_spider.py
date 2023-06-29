from pathlib import Path

import scrapy


class NgcDetailsCensusSpider(scrapy.Spider):
    name = "ngc_details_census"

    start_urls = [
            "https://www.ngccoin.com/details-census/world/germany-states-1871-1925/sc-144/5m/",
    ]
    
    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall()
            }
        
    def parse(self, response):
        page_title = response.css('div.sticky-header header h1::text').get() + response.css('div.sticky-header header h1 span::text').get()
        narrow_detail_row = response.css('div.details-census div.scrollable table tbody tr.ms')
        broad_detail_row = response.css('div.details-census div.pinned table tbody tr.ms')

        # loops through each row, returns the first number in the row that isn't blank
        for row in narrow_detail_row:
            print(row.css('td::text').get())
        
        # loops through, returns the data in the first column for each row
        for r in narrow_detail_row:
            print(row.xpath('./td[0]//text()').get())
        
        # loops through, returns the name of the coin
        for row in broad_detail_row:
            first_data = row.css('td span span.merged').xpath('.//text()')
            print(first_data.get())

        broad_dict = {}
        narrow_dict = {}
        counter = 0
        
        # biggun
        for row in broad_detail_row:
            name = row.css('td span span.merged::text')
            denom = row.css('td[1]::text')
            desig = row.css('td[2]::text')
            total_num = row.css('td.census-only')
            counter += 1
            
            sub_dict = {"name": name,
                        "denomination": denom,
                        "designation": desig,
                        "total_number": total_num,
                        "index": counter}
            
            broad_dict.update(sub_dict)

        counter = 0
        
        for row in narrow_detail_row:
            num_pr_ag_details = row.css('td.grade-PrAg::text')
            num_g_details = row.css('td.grade-G::text')
            num_vg_details = row.css('td.grade-VG::text')
            num_f_details = row.css('td.grade-F::text')
            num_vf_details = row.css('td.grade-VF::text')
            num_xf_details = row.css('td.grade-XF::text')
            num_au_details = row.css('td.grade-AU::text')
            num_unc_details = row.css('td.grade-UNC::text')
            counter += 1
            
            sub_dict = {"num_pr_ag_details": num_pr_ag_details,
                        "num_g_details": num_g_details,
                        "num_vg_details": num_vg_details,
                        "num_f_details": num_f_details,
                        "num_vf_details": num_vf_details,
                        "num_xf_details": num_xf_details,
                        "num_au_details": num_au_details,
                        "num_unc_details": num_unc_details,
                        "index": counter}
        
            narrow_dict.update(sub_dict)
        
        
        keys = set(broad_dict.keys()) & set(narrow_dict.keys())
        
        # trying to figure out how to do this dictionary comprehension
        master = {broad_dict["name"]: {"denomination": broad_dict["denomination"],
                                       "designation": broad_dict["designation"],
                                       "total_number": broad_dict["total_number"],
                                       "num_pr_ag_details": narrow_dict["num_pr_ag_details"],
                                       "num_g_details": narrow_dict["num_g_details"],
                                       "num_vg_details": narrow_dict["num_vg_details"],
                                       "num_f_details": narrow_dict["num_f_details"],
                                       "num_vf_details": narrow_dict["num_vf_details"],
                                       "num_xf_details": narrow_dict["num_xf_details"],
                                       "num_au_details": narrow_dict["num_au_details"],
                                       "num_unc_details": narrow_dict["num_unc_details"]} for k in keys}
        
        yield {
            "page_title": page_title,
        }
        
        
"""
How do I want the output data to look?



"""
