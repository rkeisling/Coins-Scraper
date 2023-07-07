from pathlib import Path

import scrapy
import datetime
import time


class NgcDetailsCensusSpider(scrapy.Spider):
    name = "ngc_details_census"

    start_urls = [
            "https://www.ngccoin.com/details-census/world/germany-states-1871-1925/sc-144/5m/",
            "https://www.ngccoin.com/details-census/world/germany-states-1871-1925/sc-144/10m/",
            "https://www.ngccoin.com/details-census/world/germany-states-1871-1925/sc-144/20m/",
            "https://www.ngccoin.com/details-census/world/germany-states-1871-1925/sc-144/2m/",
            "https://www.ngccoin.com/details-census/world/germany-states-1871-1925/sc-144/3m/",
            "https://www.ngccoin.com/details-census/world/germany-states-1871-1925/sc-144/g5m/"
        ]
    
    def parse(self, response):
        broad_detail_row = response.css('div.details-census div.pinned table tbody tr.ms')

        broad_dict = {}
        counter = 0
        
        for row in broad_detail_row:
            name = row.css('td span span.merged::text').get()
            if name is None:
                name = row.css('td.total-cell span:nth-child(1)::text').get()
            denom = row.css('td:nth-child(2)::text').get()
            desig = row.css('td:nth-child(3)::text').get()
            total_num = row.css('td.census-only::text').get().replace(",", "").replace(" ", "")
            origin = response.request.url
            counter += 1
            
            if name == "Total":
                name = name + " - " + desig
            
            sub_dict = {}
            
            sub_dict[counter] = {"name": name,
                                 "denomination": denom,
                                 "designation": desig,
                                 "total_number": total_num,
                                 "origin": origin,
                                 "index": counter}
            
            broad_dict.update(sub_dict)

        request = scrapy.Request(
            response.request.url + "data",
            callback=self.parse_details,
            cb_kwargs={"broad_dict": broad_dict}
        )
        
        yield request

        
                    
    def parse_details(self, response, broad_dict):
        narrow_detail_row = response.css('body table tbody tr.ms')
        
        narrow_dict = {}
        counter = 0
        
        for row in narrow_detail_row:
            num_pr_ag_details = row.css('td.grade-PrAg::text').get() or 0
            num_g_details = row.css('td.grade-G::text').get() or 0
            num_vg_details = row.css('td.grade-VG::text').get() or 0
            num_f_details = row.css('td.grade-F::text').get() or 0
            num_vf_details = row.css('td.grade-VF::text').get() or 0
            num_xf_details = row.css('td.grade-XF::text').get() or 0
            num_au_details = row.css('td.grade-AU::text').get() or 0
            num_unc_details = row.css('td.grade-UNC::text').get() or 0
            
            counter += 1
            
            sub_dict = {}
            
            sub_dict[counter] = {"num_pr_ag_details": num_pr_ag_details,
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
        
        split_url = response.request.url.split("/")
        
        type_name = split_url[-5].upper()
        
        denom = split_url[-3].upper()
        
        # dictionary comprehension method
        # is faster than the nested loops
        yield { f"{type_name} - {denom}" : { broad_dict[k]["name"]: {"denomination": broad_dict[k]["denomination"],
                                                                     "designation": broad_dict[k]["designation"],
                                                                     "total_number": broad_dict[k]["total_number"],
                                                                     "num_pr_ag_details": narrow_dict[k]["num_pr_ag_details"],
                                                                     "num_g_details": narrow_dict[k]["num_g_details"],
                                                                     "num_vg_details": narrow_dict[k]["num_vg_details"],
                                                                     "num_f_details": narrow_dict[k]["num_f_details"],
                                                                     "num_vf_details": narrow_dict[k]["num_vf_details"],
                                                                     "num_xf_details": narrow_dict[k]["num_xf_details"],
                                                                     "num_au_details": narrow_dict[k]["num_au_details"],
                                                                     "num_unc_details": narrow_dict[k]["num_unc_details"],
                                                                     "origin": broad_dict[k]["origin"],
                                                                     "last_updated_at": str(datetime.datetime.now())} for k in keys if broad_dict[k]["index"] == narrow_dict[k]["index"]}}
