# -*- coding: utf-8 -*-

# Scrapy settings for Qichachascrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import csv

BOT_NAME = 'Qichachascrapy'

SPIDER_MODULES = ['Qichachascrapy.spiders']
NEWSPIDER_MODULE = 'Qichachascrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Qichachascrapy (+http://www.yourdomain.com)'

COOKIE = {'UM_distinctid': '162747f3abe5f0-0b1e48b0b24c33-5f19331c-100200-162747f3abf24b', 
          ' zg_did': '%7B%22did%22%3A%20%22162747f3ae4fc-0e81e0aff36142-5f19331c-100200-162747f3ae5f%22%7D', 
          ' _uab_collina': '152237300875136550697094', 
          ' PHPSESSID': '7lggoqctv9qbci8kqi2scl7a52', 
          ' hasShow': '1', 
          ' Hm_lvt_3456bee468c83cc63fb5147f119f1075': '1524490907,1524534480,1524551949,1524634460', 
          ' acw_tc': 'AQAAAAuvGXSdDwsA2i5QblYLV07Wc12r', 
          ' _umdata': '6AF5B463492A874D282D74A7456AABC269B84B9E90D2920A9B174617448C023918BF4804957EB855CD43AD3E795C914CD1A80B15B5B3C7110FFFB1006F8D12AE', 
          ' CNZZDATA1254842228': '703573870-1522371699-https%253A%252F%252Fwww.baidu.com%252F%7C1524638139', 
          ' zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f': '%7B%22sid%22%3A%201524641144058%2C%22updated%22%3A%201524641176230%2C%22info%22%3A%201524543123189%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%22c4bf5220cbbcc85887d6a00a74151d9c%22%7D', 
          ' Hm_lpvt_3456bee468c83cc63fb5147f119f1075': '1524641176'}
                              
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Qichachascrapy.middlewares.QichachascrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'Qichachascrapy.middlewares.MyCustomDownloaderMiddleware': 543,
'Qichachascrapy.middlewares.RandomUserAgent': 1
}

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Qichachascrapy.pipelines.QichachascrapyPipeline': 300,
#}
FEED_FORMAT: csv
FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_FIELDS =["firm_searchname", 
                     "firm_url","firm_id", "firm_name", #"firm_phone",
                     #"firm_location", "firm_province",
                     #"base_rgcapital", "base_rlcapital", 
                     #"base_opstatus", "base_type","base_foundtime",
                     #"base_industry", "base_business","base_shareholder",
                     #"base_shareholdershare", "base_shareholdercapital","base_shareholdertype", 
                     "run_grad", "run_tax", "run_netprofit", "run_grossprofit",
                     "report_year", "report16_asset", #"report15_asset", "report14_asset",
                     "report16_liability", #"report15_liability", "report14_liability",
                     "report16_insnum" #"report15_insnum", "report14_insnum",
                     #"asset_trademark", "asset_patent", "asset_certificate", "asset_software",
                     #"relation_legal", "relation_invest", "relation_office"
                     ]

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
LOG_ENABLED = True
LOG_FILE = "log.txt"
LOG_LEVEL = "INFO"