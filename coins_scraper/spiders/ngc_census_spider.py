from pathlib import Path

import scrapy
import datetime
import json
import os
import time

def get_types(filename):
        current_dir = os.getcwd()
        print(current_dir)
        json_file_path = os.path.abspath(os.path.join(current_dir, filename))
        with open(json_file_path) as fin:
            return json.loads(fin.read())

class NgcCensusSpider(scrapy.Spider):
    name = "ngc_census"

    start_urls = [
            each["link"] for each in get_types("ngc_types_test_run.json")
        ]
    
    def parse(self, response):
        broad_detail_row = response.css('div.census div.pinned table tbody tr.ms')

        broad_dict = {}
        counter = 0
        start = time.time()
        
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

        end = time.time()
        print("Gathering broad rows took: " + str(end - start))

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
        
        start = time.time()
        
        for row in narrow_detail_row:
            pr_ag_base = row.css('td:nth-child(1)::text').get() or 0
            pr_ag_star = row.css('td:nth-child(2)::text').get() or 0
            g_base = row.css('td:nth-child(3)::text').get() or 0
            g_star = row.css('td:nth-child(4)::text').get() or 0
            vg_base = row.css('td:nth-child(5)::text').get() or 0
            vg_star = row.css('td:nth-child(6)::text').get() or 0
            f_base = row.css('td:nth-child(7)::text').get() or 0
            f_star = row.css('td:nth-child(8)::text').get() or 0
            vf_base = row.css('td:nth-child(9)::text').get() or 0
            vf_star = row.css('td:nth-child(10)::text').get() or 0
            forty_base = row.css('td:nth-child(11)::text').get() or 0
            forty_star = row.css('td:nth-child(12)::text').get() or 0
            forty_five_base = row.css('td:nth-child(13)::text').get() or 0
            forty_five_star = row.css('td:nth-child(14)::text').get() or 0
            forty_five_plus = row.css('td:nth-child(15)::text').get() or 0
            forty_five_plus_star = row.css('td:nth-child(16)::text').get() or 0
            fifty_base = row.css('td:nth-child(17)::text').get() or 0
            fifty_star = row.css('td:nth-child(18)::text').get() or 0
            fifty_plus = row.css('td:nth-child(19)::text').get() or 0
            fifty_plus_star = row.css('td:nth-child(20)::text').get() or 0
            fifty_three_base = row.css('td:nth-child(21)::text').get() or 0
            fifty_three_star = row.css('td:nth-child(22)::text').get() or 0
            fifty_three_plus = row.css('td:nth-child(23)::text').get() or 0
            fifty_three_plus_star = row.css('td:nth-child(24)::text').get() or 0
            fifty_five_base = row.css('td:nth-child(25)::text').get() or 0
            fifty_five_star = row.css('td:nth-child(26)::text').get() or 0
            fifty_five_plus = row.css('td:nth-child(27)::text').get() or 0
            fifty_five_plus_star = row.css('td:nth-child(28)::text').get() or 0
            fifty_eight_base = row.css('td:nth-child(29)::text').get() or 0
            fifty_eight_star = row.css('td:nth-child(30)::text').get() or 0
            fifty_eight_plus = row.css('td:nth-child(31)::text').get() or 0
            fifty_eight_plus_star = row.css('td:nth-child(32)::text').get() or 0
            sixty_base = row.css('td:nth-child(33)::text').get() or 0
            sixty_star = row.css('td:nth-child(34)::text').get() or 0
            sixty_plus = row.css('td:nth-child(35)::text').get() or 0
            sixty_plus_star = row.css('td:nth-child(36)::text').get() or 0
            sixty_one_base = row.css('td:nth-child(37)::text').get() or 0
            sixty_one_star = row.css('td:nth-child(38)::text').get() or 0
            sixty_one_plus = row.css('td:nth-child(39)::text').get() or 0
            sixty_one_plus_star = row.css('td:nth-child(40)::text').get() or 0
            sixty_two_base = row.css('td:nth-child(41)::text').get() or 0
            sixty_two_star = row.css('td:nth-child(42)::text').get() or 0
            sixty_two_plus = row.css('td:nth-child(43)::text').get() or 0
            sixty_two_plus_star = row.css('td:nth-child(44)::text').get() or 0
            sixty_three_base = row.css('td:nth-child(45)::text').get() or 0
            sixty_three_star = row.css('td:nth-child(46)::text').get() or 0
            sixty_three_plus = row.css('td:nth-child(47)::text').get() or 0
            sixty_three_plus_star = row.css('td:nth-child(48)::text').get() or 0
            sixty_four_base = row.css('td:nth-child(49)::text').get() or 0
            sixty_four_star = row.css('td:nth-child(50)::text').get() or 0
            sixty_four_plus = row.css('td:nth-child(51)::text').get() or 0
            sixty_four_plus_star = row.css('td:nth-child(52)::text').get() or 0
            sixty_five_base = row.css('td:nth-child(53)::text').get() or 0
            sixty_five_star = row.css('td:nth-child(54)::text').get() or 0
            sixty_five_plus = row.css('td:nth-child(55)::text').get() or 0
            sixty_five_plus_star = row.css('td:nth-child(56)::text').get() or 0
            sixty_six_base = row.css('td:nth-child(57)::text').get() or 0
            sixty_six_star = row.css('td:nth-child(58)::text').get() or 0
            sixty_six_plus = row.css('td:nth-child(59)::text').get() or 0
            sixty_six_plus_star = row.css('td:nth-child(60)::text').get() or 0
            sixty_seven_base = row.css('td:nth-child(61)::text').get() or 0
            sixty_seven_star = row.css('td:nth-child(62)::text').get() or 0
            sixty_seven_plus = row.css('td:nth-child(63)::text').get() or 0
            sixty_seven_plus_star = row.css('td:nth-child(64)::text').get() or 0
            sixty_eight_base = row.css('td:nth-child(65)::text').get() or 0
            sixty_eight_star = row.css('td:nth-child(66)::text').get() or 0
            sixty_eight_plus = row.css('td:nth-child(67)::text').get() or 0
            sixty_eight_plus_star = row.css('td:nth-child(68)::text').get() or 0
            sixty_nine_base = row.css('td:nth-child(69)::text').get() or 0
            sixty_nine_star = row.css('td:nth-child(70)::text').get() or 0
            seventy_base = row.css('td:nth-child(71)::text').get() or 0
            seventy_star = row.css('td:nth-child(72)::text').get() or 0
            
            counter += 1
            
            sub_dict = {}
            
            sub_dict[counter] = {"pr_ag_base": pr_ag_base,
                                 "pr_ag_star": pr_ag_star,
                                 "g_base": g_base,
                                 "g_star": g_star,
                                 "vg_base": vg_base,
                                 "vg_star": vg_star,
                                 "f_base": f_base,
                                 "f_star": f_star,
                                 "vf_base": vf_base,
                                 "vf_star": vf_star,
                                 "forty_base": forty_base,
                                 "forty_star": forty_star,
                                 "forty_five_base": forty_five_base,
                                 "forty_five_star": forty_five_star,
                                 "forty_five_plus": forty_five_plus,
                                 "forty_five_plus_star": forty_five_plus_star,
                                 "fifty_base": fifty_base,
                                 "fifty_star": fifty_star,
                                 "fifty_plus": fifty_plus,
                                 "fifty_plus_star": fifty_plus_star,
                                 "fifty_three_base": fifty_three_base,
                                 "fifty_three_star": fifty_three_star,
                                 "fifty_three_plus": fifty_three_plus,
                                 "fifty_three_plus_star": fifty_three_plus_star,
                                 "fifty_five_base": fifty_five_base,
                                 "fifty_five_star": fifty_five_star,
                                 "fifty_five_plus": fifty_five_plus,
                                 "fifty_five_plus_star": fifty_five_plus_star,
                                 "fifty_eight_base": fifty_eight_base,
                                 "fifty_eight_star": fifty_eight_star,
                                 "fifty_eight_plus": fifty_eight_plus,
                                 "fifty_eight_plus_star": fifty_eight_plus_star,
                                 "sixty_base": sixty_base,
                                 "sixty_star": sixty_star,
                                 "sixty_plus": sixty_plus,
                                 "sixty_plus_star": sixty_plus_star,
                                 "sixty_one_base": sixty_one_base,
                                 "sixty_one_star": sixty_one_star,
                                 "sixty_one_plus": sixty_one_plus,
                                 "sixty_one_plus_star": sixty_one_plus_star,
                                 "sixty_two_base": sixty_two_base,
                                 "sixty_two_star": sixty_two_star,
                                 "sixty_two_plus": sixty_two_plus,
                                 "sixty_two_plus_star": sixty_two_plus_star,
                                 "sixty_three_base": sixty_three_base,
                                 "sixty_three_star": sixty_three_star,
                                 "sixty_three_plus": sixty_three_plus,
                                 "sixty_three_plus_star": sixty_three_plus_star,
                                 "sixty_four_base": sixty_four_base,
                                 "sixty_four_star": sixty_four_star,
                                 "sixty_four_plus": sixty_four_plus,
                                 "sixty_four_plus_star": sixty_four_plus_star,
                                 "sixty_five_base": sixty_five_base,
                                 "sixty_five_star": sixty_five_star,
                                 "sixty_five_plus": sixty_five_plus,
                                 "sixty_five_plus_star": sixty_five_plus_star,
                                 "sixty_six_base": sixty_six_base,
                                 "sixty_six_star": sixty_six_star,
                                 "sixty_six_plus": sixty_six_plus,
                                 "sixty_six_plus_star": sixty_six_plus_star,
                                 "sixty_seven_base": sixty_seven_base,
                                 "sixty_seven_star": sixty_seven_star,
                                 "sixty_seven_plus": sixty_seven_plus,
                                 "sixty_seven_plus_star": sixty_seven_plus_star,
                                 "sixty_eight_base": sixty_eight_base,
                                 "sixty_eight_star": sixty_eight_star,
                                 "sixty_eight_plus": sixty_eight_plus,
                                 "sixty_eight_plus_star": sixty_eight_plus_star,
                                 "sixty_nine_base": sixty_nine_base,
                                 "sixty_nine_star": sixty_nine_star,
                                 "seventy_base": seventy_base,
                                 "seventy_star": seventy_star,
                                 "index": counter}
    
            narrow_dict.update(sub_dict)
            
        end = time.time()
        print("Gathering detailed rows took: " + str(end - start))
        
        keys = set(broad_dict.keys()) & set(narrow_dict.keys())
        
        split_url = response.request.url.split("/")
        
        type_name = split_url[-5].upper()
        
        denom = split_url[-3].upper()
        
        # dictionary comprehension method
        # is faster than the nested loops
        yield { f"{type_name} - {denom}" : { broad_dict[k]["name"]: {"denomination": broad_dict[k]["denomination"],
                                                                     "designation": broad_dict[k]["designation"],
                                                                     "total_number": broad_dict[k]["total_number"],
                                                                     "pr_ag_base": narrow_dict[k]["pr_ag_base"],
                                                                     "pr_ag_star": narrow_dict[k]["pr_ag_star"],
                                                                     "g_base": narrow_dict[k]["g_base"],
                                                                     "g_star": narrow_dict[k]["g_star"],
                                                                     "vg_base": narrow_dict[k]["vg_base"],
                                                                     "vg_star": narrow_dict[k]["vg_star"],
                                                                     "f_base": narrow_dict[k]["f_base"],
                                                                     "f_star": narrow_dict[k]["f_star"],
                                                                     "vf_base": narrow_dict[k]["vf_base"],
                                                                     "vf_star": narrow_dict[k]["vf_star"],
                                                                     "forty_base": narrow_dict[k]["forty_base"],
                                                                     "forty_star": narrow_dict[k]["forty_star"],
                                                                     "forty_five_base": narrow_dict[k]["forty_five_base"],
                                                                     "forty_five_star": narrow_dict[k]["forty_five_star"],
                                                                     "forty_five_plus": narrow_dict[k]["forty_five_plus"],
                                                                     "forty_five_plus_star": narrow_dict[k]["forty_five_plus_star"],
                                                                     "fifty_base": narrow_dict[k]["fifty_base"],
                                                                     "fifty_star": narrow_dict[k]["fifty_star"],
                                                                     "fifty_plus": narrow_dict[k]["fifty_plus"],
                                                                     "fifty_plus_star": narrow_dict[k]["fifty_plus_star"],
                                                                     "fifty_three_base": narrow_dict[k]["fifty_three_base"],
                                                                     "fifty_three_star": narrow_dict[k]["fifty_three_star"],
                                                                     "fifty_three_plus": narrow_dict[k]["fifty_three_plus"],
                                                                     "fifty_three_plus_star": narrow_dict[k]["fifty_three_plus_star"],
                                                                     "fifty_five_base": narrow_dict[k]["fifty_five_base"],
                                                                     "fifty_five_star": narrow_dict[k]["fifty_five_star"],
                                                                     "fifty_five_plus": narrow_dict[k]["fifty_five_plus"],
                                                                     "fifty_five_plus_star": narrow_dict[k]["fifty_five_plus_star"],
                                                                     "fifty_eight_base": narrow_dict[k]["fifty_eight_base"],
                                                                     "fifty_eight_star": narrow_dict[k]["fifty_eight_star"],
                                                                     "fifty_eight_plus": narrow_dict[k]["fifty_eight_plus"],
                                                                     "fifty_eight_plus_star": narrow_dict[k]["fifty_eight_plus_star"],
                                                                     "sixty_base": narrow_dict[k]["sixty_base"],
                                                                     "sixty_star": narrow_dict[k]["sixty_star"],
                                                                     "sixty_plus": narrow_dict[k]["sixty_plus"],
                                                                     "sixty_plus_star": narrow_dict[k]["sixty_plus_star"],
                                                                     "sixty_one_base": narrow_dict[k]["sixty_one_base"],
                                                                     "sixty_one_star": narrow_dict[k]["sixty_one_star"],
                                                                     "sixty_one_plus": narrow_dict[k]["sixty_one_plus"],
                                                                     "sixty_one_plus_star": narrow_dict[k]["sixty_one_plus_star"],
                                                                     "sixty_two_base": narrow_dict[k]["sixty_two_base"],
                                                                     "sixty_two_star": narrow_dict[k]["sixty_two_star"],
                                                                     "sixty_two_plus": narrow_dict[k]["sixty_two_plus"],
                                                                     "sixty_two_plus_star": narrow_dict[k]["sixty_two_plus_star"],
                                                                     "sixty_three_base": narrow_dict[k]["sixty_three_base"],
                                                                     "sixty_three_star": narrow_dict[k]["sixty_three_star"],
                                                                     "sixty_three_plus": narrow_dict[k]["sixty_three_plus"],
                                                                     "sixty_three_plus_star": narrow_dict[k]["sixty_three_plus_star"],
                                                                     "sixty_four_base": narrow_dict[k]["sixty_four_base"],
                                                                     "sixty_four_star": narrow_dict[k]["sixty_four_star"],
                                                                     "sixty_four_plus": narrow_dict[k]["sixty_four_plus"],
                                                                     "sixty_four_plus_star": narrow_dict[k]["sixty_four_plus_star"],
                                                                     "sixty_five_base": narrow_dict[k]["sixty_five_base"],
                                                                     "sixty_five_star": narrow_dict[k]["sixty_five_star"],
                                                                     "sixty_five_plus": narrow_dict[k]["sixty_five_plus"],
                                                                     "sixty_five_plus_star": narrow_dict[k]["sixty_five_plus_star"],
                                                                     "sixty_six_base": narrow_dict[k]["sixty_six_base"],
                                                                     "sixty_six_star": narrow_dict[k]["sixty_six_star"],
                                                                     "sixty_six_plus": narrow_dict[k]["sixty_six_plus"],
                                                                     "sixty_six_plus_star": narrow_dict[k]["sixty_six_plus_star"],
                                                                     "sixty_seven_base": narrow_dict[k]["sixty_seven_base"],
                                                                     "sixty_seven_star": narrow_dict[k]["sixty_seven_star"],
                                                                     "sixty_seven_plus": narrow_dict[k]["sixty_seven_plus"],
                                                                     "sixty_seven_plus_star": narrow_dict[k]["sixty_seven_plus_star"],
                                                                     "sixty_eight_base": narrow_dict[k]["sixty_eight_base"],
                                                                     "sixty_eight_star": narrow_dict[k]["sixty_eight_star"],
                                                                     "sixty_eight_plus": narrow_dict[k]["sixty_eight_plus"],
                                                                     "sixty_eight_plus_star": narrow_dict[k]["sixty_eight_plus_star"],
                                                                     "sixty_nine_base": narrow_dict[k]["sixty_nine_base"],
                                                                     "sixty_nine_star": narrow_dict[k]["sixty_nine_star"],
                                                                     "seventy_base": narrow_dict[k]["seventy_base"],
                                                                     "seventy_star": narrow_dict[k]["seventy_star"],
                                                                     "origin": broad_dict[k]["origin"],
                                                                     "last_updated_at": str(datetime.datetime.now())} for k in keys if broad_dict[k]["index"] == narrow_dict[k]["index"]}}
        