from pathlib import Path

import scrapy


class NgcDetailsCensusSpider(scrapy.Spider):
    name = "ngc_details_census"

    start_urls = [
            "https://www.ngccoin.com/details-census/world/germany-states-1871-1925/sc-144/5m/"
        ]
    
    def parse(self, response):
        page_title = response.css('div.sticky-header header h1::text').get() + response.css('div.sticky-header header h1 span::text').get()
        broad_detail_row = response.css('div.details-census div.pinned table tbody tr.ms')

        # loops through each row, returns the first number in the row that isn't blank
        # for row in narrow_detail_row:
        #     print(row.css('td::text').get())
        
        # loops through, returns the data in the first column for each row
        # for r in narrow_detail_row:
        #     print(row.xpath('./td[0]//text()').get())
        
        # loops through, returns the name of the coin
        # for row in broad_detail_row:
        #     first_data = row.css('td span span.merged').xpath('.//text()')
        #     print(first_data.get())

        broad_dict = {}
        counter = 0
        
        # biggun
        for row in broad_detail_row:
            name = row.css('td span span.merged::text').get()
            if name is None:
                print("name was null! name: " + str(name))
                print("Attempting to get new name...")
                name = row.css('td.total-cell span:nth-child(1)::text').get()
                print("New name: " + str(name))
            denom = row.css('td:nth-child(2)::text').get()
            desig = row.xpath('//td[3]/text()').get()
            total_num = row.css('td.census-only::text').get()
            counter += 1
            
            sub_dict = {}
            
            sub_dict[counter] = {"name": name,
                                 "denomination": denom,
                                 "designation": desig,
                                 "total_number": total_num,
                                 "index": counter}
            
            broad_dict.update(sub_dict)

        # print("Broad dictionary: " + str(broad_dict))
        
        request = scrapy.Request(
            "https://www.ngccoin.com/details-census/world/germany-states-1871-1925/sc-144/5m/data",
            callback=self.parse_details,
            cb_kwargs=broad_dict
        )
        
        yield request

        
                    
    def parse_details(self, response, broad_dict):
        narrow_detail_row = response.css('body table tbody tr.ms')
        
        narrow_dict = {}
        counter = 0
        
        for row in narrow_detail_row:
            num_pr_ag_details = row.css('td.grade-PrAg::text').get()
            if (num_pr_ag_details is None):
                num_pr_ag_details = 0
            num_g_details = row.css('td.grade-G::text').get()
            if (num_g_details is None):
                num_g_details = 0
            num_vg_details = row.css('td.grade-VG::text').get()
            if (num_vg_details is None):
                num_vg_details = 0
            num_f_details = row.css('td.grade-F::text').get()
            if (num_f_details is None):
                num_f_details = 0
            num_vf_details = row.css('td.grade-VF::text').get()
            if (num_vf_details is None):
                num_vf_details = 0
            num_xf_details = row.css('td.grade-XF::text').get()
            if (num_xf_details is None):
                num_xf_details = 0
            num_au_details = row.css('td.grade-AU::text').get()
            if (num_au_details is None):
                num_au_details = 0
            num_unc_details = row.css('td.grade-UNC::text').get()
            if (num_unc_details is None):
                num_unc_details = 0
            
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
        
        print("Narrow dictionary: " + str(narrow_dict))
        
        # keys = set(broad_dict.keys()) & set(narrow_dict.keys())
        
        # trying to figure out how to do this dictionary comprehension
        # master = {broad_dict["name"]: {"denomination": broad_dict["denomination"],
        #                                "designation": broad_dict["designation"],
        #                                "total_number": broad_dict["total_number"],
        #                                "num_pr_ag_details": narrow_dict["num_pr_ag_details"],
        #                                "num_g_details": narrow_dict["num_g_details"],
        #                                "num_vg_details": narrow_dict["num_vg_details"],
        #                                "num_f_details": narrow_dict["num_f_details"],
        #                                "num_vf_details": narrow_dict["num_vf_details"],
        #                                "num_xf_details": narrow_dict["num_xf_details"],
        #                                "num_au_details": narrow_dict["num_au_details"],
        #                                "num_unc_details": narrow_dict["num_unc_details"]} for k in keys if broad_dict[k]["index"] == narrow_dict[k]["index"]}
        
        # print("Master dictionary: " + str(master))
        
        for broad_key, broad_value in broad_dict.items():
            for narrow_key, narrow_value in narrow_dict.items():
                if broad_key == narrow_key:
                    yield { broad_value["name"]: {"denomination": broad_value["denomination"],
                            "designation": broad_value["designation"],
                            "total_number": broad_value["total_number"],
                            "num_pr_ag_details": narrow_value["num_pr_ag_details"],
                            "num_g_details": narrow_value["num_g_details"],
                            "num_vg_details": narrow_value["num_vg_details"],
                            "num_f_details": narrow_value["num_f_details"],
                            "num_vf_details": narrow_value["num_vf_details"],
                            "num_xf_details": narrow_value["num_xf_details"],
                            "num_au_details": narrow_value["num_au_details"],
                            "num_unc_details": narrow_value["num_unc_details"]} }