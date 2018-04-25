# -*- coding: utf-8 -*-
import scrapy
import csv
import re
import copy
from urllib.parse import urljoin
from scrapy.http import Request
from Qichachascrapy.items import QichachascrapyItem
from scrapy.conf import settings

class QichachaSpider(scrapy.Spider):
    name = "Qichacha"
    allowed_domains = ["qichacha.com"]
    start_urls = []
    cookie = settings['COOKIE']
    headers = {
    'Host': "www.qichacha.com",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Accept-Encoding': "gzip, deflate",
    'Content-Type': "application/x-www-form-urlencoded",
    'Connection': "keep-alive",
    #User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    
    #response.mate 深浅拷贝问题要尤其注意
    
    def start_requests(self):
        item =  QichachascrapyItem()
        with open (("maoyi.csv"),"rU", newline = '') as f:
            for line in csv.reader(f):
                #print(line)
                item['firm_searchname'] = line[0]
                request = Request('http://www.qichacha.com/search?key='+line[0],
                                  headers=self.headers, 
                                  cookies= self.cookie,
                                  callback = self.parse,
                                  meta = {'key': copy.deepcopy(item)},
                                  dont_filter=True)
                #request.meta['key'] = item
                print (item)
                yield request

    def parse(self, response):
        item=response.meta['key'].copy()
        print (item)
        _firm_url=response.xpath('//a[@class="ma_h1"]/@href').extract_first()
        if _firm_url is not None:
            firm_url =urljoin(response.url,_firm_url)
            item['firm_url']= firm_url
            match_obj=re.match('.*?([a-zA-Z0-9]{10,})',_firm_url)
            item['firm_id']=match_obj.group(1)
            request = scrapy.Request(firm_url,
                                     headers= self.headers,
                                     cookies= self.cookie,
                                     meta = {'key':item},
                                     callback = self.parse_base,
                                     dont_filter = True)
            
            yield request
            print (item)
        else: 
            f = open('nocompany.txt', 'a')
            f.write(item['firm_searchname'])
            f.write('\n')
            f.close()
            yield item

    def parse_base(self,response):
        print (response.url)
        item = response.meta['key'].copy()
        item['firm_name'] = response.xpath('//div[@class = "row title"]/h1/text()').extract()[0].strip()
        #item['firm_phone'] = response.xpath('//span[@style="color: #000;"]/text()').extract()[0].strip()
        #item['firm_location'] =response.xpath('//html//div[@class="container m-t-md"]//tr[10]/td[2]/text()').extract()[0].strip()
        #item['firm_province'] = response.xpath('//section[@id = "Cominfo"]/table[@class = "ntable"][2]//tr[7]/td[2]/text()').extract()[0].strip()#checking mismatch
        #item['base_rgcapital'] = response.xpath('//section[@id = "Cominfo"]/table[@class = "ntable"][2]//tr[1]/td[2]/text()').extract()[0].strip()
        #item['base_rlcapital'] = response.xpath('//html//tr[1]/td[4]/text()').extract()[0].strip()
        #item['base_opstatus'] =response.xpath('//section[@id = "Cominfo"]/table[@class = "ntable"][2]//tr[2]/td[2]/text()').extract()[0].strip()
        #item['base_foundtime'] = response.xpath('//html//section[@id="Cominfo"]//tr[2]/td[4]/text()').extract()[0].strip()
        #item['base_type'] =response.xpath('//html//div[@class="container m-t-md"]//tr[5]/td[2]/text()').extract()[0].strip()
        #item['base_industry'] = response.xpath('//html//tr[5]/td[4]/text()').extract()[0].strip()
        #item['base_business'] =response.xpath('//td[@colspan="3"]//text()').extract()[5].strip()
        #if response.xpath('//html//section[@id="Sockinfo"]//tr[2]/td[2]/a[1]/@href').extract_first() is not None:
            #_shareholderurl = response.xpath('//html//section[@id="Sockinfo"]//tr[2]/td[2]/a[1]/@href').extract()[0]
            #print (_shareholderurl)
            #item['base_shareholderurl'] = urljoin(response.url, _shareholderurl)
            #item['base_shareholder'] = response.xpath('//html//section[@id="Sockinfo"]//tr[2]/td[2]/a[1]/text()').extract()
            #item['base_shareholdershare'] = response.xpath('//html//section[@id="Sockinfo"]//tr[2]/td[3]/text()').extract()[0].strip()
            #item['base_shareholdercapital'] = response.xpath('//html//section[@id="Sockinfo"]//tr[2]/td[4]/text()').extract()[0].strip()
            #item['base_shareholdertype'] = response.xpath('//html//tr[2]/td[6]/text()').extract()
        #else: 
            #item['base_shareholderurl'] = None
            #f = open('noshareholder.txt', 'a')
            #f.write(response.url)
            #f.write('\n')
            #f.close()
        print(item)
        run_url='http://www.qichacha.com/company_getinfos?unique={0}&companyname={1}&tab=run' #from guapier on github
        request_run = scrapy.Request(run_url.format(item['firm_id'],item['firm_name'].encode('utf-8')), 
                                     headers = self.headers,
                                     cookies = self.cookie,
                                     meta = {'key':item, 'dont_redirect': True},
                                     callback = self.parse_run,
                                     dont_filter = True)
        yield request_run
    
    def parse_run(self,response):
        #from scrapy.shell import inspect_response
        #inspect_response(response, self)
        print (response.url)
        item = response.meta['key'].copy()
        if response.xpath('//section[@id="V3_cwzl"]//table[@class="ntable"]//tr/td//text()').extract_first() is not None:
            item['run_grad'] = response.xpath('//section[@id="V3_cwzl"]//table[@class="ntable"]//tr[1]/td[2]/text()').extract()[0].strip()
            item['run_tax'] = response.xpath('//section[@id="V3_cwzl"]//table[@class="ntable"]//tr[1]/td[4]/text()').extract()[0].strip()
            item['run_netprofit'] = response.xpath('//section[@id="V3_cwzl"]//table[@class="ntable"]//tr[2]/td[2]/text()').extract()[0].strip()
            item['run_grossprofit'] = response.xpath('//section[@id="V3_cwzl"]//table[@class="ntable"]//tr[2]/td[4]/text()').extract()[0].strip()
        
        report_url= 'http://www.qichacha.com/company_getinfos?unique={0}&companyname={1}&tab=report'
        request_report = scrapy.Request(report_url.format(item['firm_id'],item['firm_name'].encode('utf-8')),
                                        headers = self.headers,
                                        cookies = self.cookie,
                                        meta = {'key':item, 'dont_redirect': True},
                                        callback = self.parse_report,
                                        dont_filter = True)
        yield request_report
    
    def parse_report(self, response):
        #from scrapy.shell import inspect_response
        #inspect_response(response, self)
        print(response.url)
        item = response.meta['key'].copy() 
        if response.xpath('//html//div[@id="0"]//text()').extract_first() is not None:
            item['report_year'] = response.xpath('//span[contains(@class,"font-15 text-dark")][contains(text(),"年度报告")]/text()').extract()[0].strip()
        if response.xpath('//html//div[@id="0"]/table//td[contains(text(),"资产总额")]/parent::*/td/text()').extract_first() is not None:
            item['report16_asset'] = response.xpath('//html//div[@id="0"]/table//td[contains(text(),"资产总额")]/parent::*/td/text()').extract()[1].strip()#using extract_first to aviod missing value
        if response.xpath('//html//div[@id="0"]/table//td[contains(text(),"负债总额")]/parent::*/td/text()').extract_first() is not None:
            item['report16_liability'] = response.xpath('//html//div[@id="0"]/table//td[contains(text(),"负债总额")]/parent::*/td/text()').extract()[3].strip()
        if response.xpath('//html//div[@id="0"]/table//td[contains(text(),"城镇职工基本养老保险")]/parent::*/td//text()').extract_first() is not None:
            item['report16_insnum'] = response.xpath('//html//div[@id="0"]/table//td[contains(text(),"城镇职工基本养老保险")]/parent::*/td//text()').extract()[1].strip()
        
        #if response.xpath('//html//div[@id="1"]/table//td[contains(text(),"资产总额")]/parent::*/td/text()').extract_first() is not None:
            #item['report15_asset'] = response.xpath('//html//div[@id="1"]/table//td[contains(text(),"资产总额")]/parent::*/td/text()').extract()[1].strip()
        #if response.xpath('///html//div[@id="1"]/table//td[contains(text(),"负债总额")]/parent::*/td/text()').extract_first() is not None:
            #item['report15_liability'] = response.xpath('//html//div[@id="1"]/table//td[contains(text(),"负债总额")]/parent::*/td/text()').extract()[3].strip()
        #if response.xpath('//html//div[@id="1"]/table//td[contains(text(),"城镇职工基本养老保险")]/parent::*/td//text()').extract_first() is not None:
            #item['report15_insnum'] = response.xpath('//html//div[@id="1"]/table//td[contains(text(),"城镇职工基本养老保险")]/parent::*/td//text()').extract()[1].strip()
        
        #if response.xpath('//html//div[@id="2"]/table//td[contains(text(),"资产总额")]/parent::*/td/text()').extract_first() is not None:
            #item['report14_asset'] = response.xpath('//html//div[@id="2"]/table//td[contains(text(),"资产总额")]/parent::*/td/text()').extract()[1].strip()
        #if response.xpath('//html//div[@id="2"]/table//td[contains(text(),"负债总额")]/parent::*/td/text()').extract_first() is not None:
            #item['report14_liability'] = response.xpath('//html//div[@id="2"]/table//td[contains(text(),"负债总额")]/parent::*/td/text()').extract()[3].strip()
        #if response.xpath('//html//div[@id="2"]/table//td[contains(text(),"城镇职工基本养老保险")]/parent::*/td//text()').extract_first() is not None:
            #item['report14_insnum'] = response.xpath('//html//div[@id="2"]/table//td[contains(text(),"城镇职工基本养老保险")]/parent::*/td//text()').extract()[1].strip()
        
        #asset_url = 'http://www.qichacha.com/company_getinfos?unique={0}&companyname={1}&tab=assets'
        #request_asset = scrapy.Request(asset_url.format(item['firm_id'],item['firm_name'].encode('utf-8')),
                                       #headers = self.headers,
                                       #cookies = self.cookie,
                                       #meta = {'key':item, 'dont_redirect': True},
                                       #callback = self.parse_asset,
                                       #dont_filter = True)
        #yield request_asset
        return item
        print (item)
        
    
    #def parse_asset(self, response):
        #from scrapy.shell import inspect_response
        #inspect_response(response, self)
        #print (response.url)
        #item = response.meta['key']
        #item['asset_trademark'] = response.xpath('//section[@id="shangbiaolist"]/div[@class="tcaption"]/span/text()').extract()
        #item['asset_patent'] = response.xpath('//section[@id="zhuanlilist"]/div[@class="tcaption"]/span/text()').extract()
        #item['asset_certificate'] = response.xpath('//section[@id="zhengshulist"]/div[@class="tcaption"]/span/text()').extract()
        #item['asset_software'] = response.xpath('//section[@id="rjzzqlist"]/div[@class="tcaption"]/span/text()').extract()
        #if item['base_shareholderurl'] is not None:
            #request_relation = scrapy.Request(item['base_shareholderurl'],
                                              #headers = self.headers,
                                              #cookies = self.cookie,
                                              #meta = {'key':item, 'dont_redirect': True},
                                              #callback = self.parse_relation,
                                              #dont_filter = True)
            #yield request_relation
        #else: 
            #return item
            #print(item)
        
    #def parse_relation(self, response):
        #from scrapy.shell import inspect_response
        #inspect_response(response, self)
        #print (response.url)
        #item = response.meta['key'].copy()
        #item['relation_legal'] = response.xpath('//html//div[@id="legal"]//tr/td[2]//text()').extract()
        #item['relation_invest'] = response.xpath('//html//div[@id="invest"]//tr/td[2]//text()').extract()
        #item['relation_office'] = response.xpath('//html//div[@id="postOffice"]//tr/td[2]//text()').extract()
        #return item
        #print(item)
        
    
        
        
    

        
        
        
        
        

    
