# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoinsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TypeItem(scrapy.Item):
    country_name = scrapy.Field()
    denomination = scrapy.Field()
    population = scrapy.Field()
    link = scrapy.Field()
    extracted_at = scrapy.Field()
    
class CountryItem(scrapy.Item):
    country_name = scrapy.Field()
    link = scrapy.Field()
    last_updated_at = scrapy.Field()

class CensusItem(scrapy.Item):
    denomination = scrapy.Field()
    designation = scrapy.Field()
    total_number = scrapy.Field()
    pr_ag_base = scrapy.Field()
    pr_ag_star = scrapy.Field()
    g_base = scrapy.Field()
    g_star = scrapy.Field()
    vg_base = scrapy.Field()
    vg_star = scrapy.Field()
    forty_base = scrapy.Field()
    forty_star = scrapy.Field()
    forty_five_base = scrapy.Field()
    forty_five_star = scrapy.Field()
    forty_five_plus = scrapy.Field()
    forty_five_plus_star = scrapy.Field()
    fifty_base = scrapy.Field()
    fifty_star = scrapy.Field()
    fifty_plus = scrapy.Field()
    fifty_plus_star = scrapy.Field()
    fifty_three_base = scrapy.Field()
    fifty_three_star = scrapy.Field()
    fifty_three_plus = scrapy.Field()
    fifty_three_plus_star = scrapy.Field()
    fifty_five_base = scrapy.Field()
    fifty_five_star = scrapy.Field()
    fifty_five_plus = scrapy.Field()
    fifty_five_plus_star = scrapy.Field()
    fifty_eight_base = scrapy.Field()
    fifty_eight_star = scrapy.Field()
    fifty_eight_plus = scrapy.Field()
    fifty_eight_plus_star = scrapy.Field()
    sixty_base = scrapy.Field()
    sixty_star = scrapy.Field()
    sixty_plus = scrapy.Field()
    sixty_plus_star = scrapy.Field()
    sixty_one_base = scrapy.Field()
    sixty_one_star = scrapy.Field()
    sixty_one_plus = scrapy.Field()
    sixty_one_plus_star = scrapy.Field()
    sixty_two_base = scrapy.Field()
    sixty_two_star = scrapy.Field()
    sixty_two_plus = scrapy.Field()
    sixty_two_plus_star = scrapy.Field()
    sixty_three_base = scrapy.Field()
    sixty_three_star = scrapy.Field()
    sixty_three_plus = scrapy.Field()
    sixty_three_plus_star = scrapy.Field()
    sixty_four_base = scrapy.Field()
    sixty_four_star = scrapy.Field()
    sixty_four_plus = scrapy.Field()
    sixty_four_plus_star = scrapy.Field()
    sixty_five_base = scrapy.Field()
    sixty_five_star = scrapy.Field()
    sixty_five_plus = scrapy.Field()
    sixty_five_plus_star = scrapy.Field()
    sixty_six_base = scrapy.Field()
    sixty_six_star = scrapy.Field()
    sixty_six_plus = scrapy.Field()
    sixty_six_plus_star = scrapy.Field()
    sixty_seven_base = scrapy.Field()
    sixty_seven_star = scrapy.Field()
    sixty_seven_plus = scrapy.Field()
    sixty_seven_plus_star = scrapy.Field()
    sixty_eight_base = scrapy.Field()
    sixty_eight_star = scrapy.Field()
    sixty_eight_plus = scrapy.Field()
    sixty_eight_plus_star = scrapy.Field()
    sixty_nine_base = scrapy.Field()
    sixty_nine_star = scrapy.Field()
    seventy_base = scrapy.Field()
    seventy_star = scrapy.Field()
    origin = scrapy.Field()
    last_updated_at = scrapy.Field()

class DetailsCensusItem(scrapy.Item):
    denomination = scrapy.Field()
    designation = scrapy.Field()
    num_pr_ag_details = scrapy.Field()
    num_g_details = scrapy.Field()
    num_vg_details = scrapy.Field()
    num_f_details = scrapy.Field()
    num_vf_details = scrapy.Field()
    num_xf_details = scrapy.Field()
    num_au_details = scrapy.Field()
    num_unc_details = scrapy.Field()
    origin = scrapy.Field()
    last_updated_at = scrapy.Field()
