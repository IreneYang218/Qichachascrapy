# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy.loader.processors import Join, MapCompose



class QichachascrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    firm_searchname = scrapy.Field()
    firm_url = scrapy.Field()
    firm_id = scrapy.Field()
    firm_name = scrapy.Field()
    #firm_phone = scrapy.Field()
    #firm_location = scrapy.Field()
    #firm_province = scrapy.Field()
    
    #base_rgcapital = scrapy.Field()
    #base_opstatus = scrapy.Field()
    #base_type = scrapy.Field()
    #base_rlcapital = scrapy.Field()
    #base_foundtime = scrapy.Field()
    #base_industry = scrapy.Field()
    #base_business = scrapy.Field()
    #base_shareholderurl = scrapy.Field()
    #base_shareholder = scrapy.Field()
    #base_shareholdershare = scrapy.Field()
    #base_shareholdercapital = scrapy.Field()
    #base_shareholdertype = scrapy.Field()
    
    #base_relationlink = scrapy.Field()

    run_grad = scrapy.Field()
    run_tax = scrapy.Field()
    run_netprofit = scrapy.Field()
    run_grossprofit = scrapy.Field()
    
    report_year = scrapy.Field()
    report16_asset = scrapy.Field()
    report16_liability= scrapy.Field()
    report16_insnum = scrapy.Field()
    #report15_asset = scrapy.Field()
    #report15_liability = scrapy.Field()
    #report15_insnum = scrapy.Field()
    #report14_asset = scrapy.Field()
    #report14_liability = scrapy.Field()
    #report14_insnum = scrapy.Field()
    
    #asset_trademark = scrapy.Field()
    #asset_patent = scrapy.Field()
    #asset_certificate = scrapy.Field()
    #asset_software = scrapy.Field()
    
    #relation_legal = scrapy.Field(
            #input_processor=MapCompose(str.strip),
            #out_processor=Join(),
            #)
    #relation_invest = scrapy.Field(
            #input_processor=MapCompose(str.strip),
            #out_processor=Join(),
            #)
    #relation_office = scrapy.Field(
            #input_processor=MapCompose(str.strip),
            #out_processor=Join(),
            #)
    
