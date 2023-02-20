from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.http import FormRequest
import re
from itemadapter import ItemAdapter

import schedule
import time

import openpyxl

SCRAPER_API_KEY = "" 
PROXY = f"http://scraperapi.country_code=us.device_type=desktop:{SCRAPER_API_KEY}@proxy-server.scraperapi.com:8001 "
URL = "https://www.quora.com/qemail/tc?al_imp=eyJ0eXBlIjogMzMsICJoYXNoIjogIjEzOTA3MTgyNzY2MjcxNzIzODJ8MXwxfDM5MDM3MTkxOSJ9&al_pri=1&aoid=zAGnk0HMhfU&aoty=2&aty=4&cp=1&et=2&id=9911ccb58f1a400d842ec2fe10301bc0&q_aid=4CTrKSowbWA&uid=VOFXbF6MshZ"


SELECTORS = {
	"player_name" : '//div[@id="player-general-info"]/div[1]/span[1]/text()',
    "team_name" : '//div[@id="player-general-info"]/div[1]/span/a/text()',
}
class TestScrapy(scrapy.Spider):
	name="TEST"
	custom_settings={
		# "ITEM_PIPELINES": {
		# 	'__main__.XLSXPipeline': 100
		# 	},
		"DOWNLOADER_MIDDLEWARES" : {
			'__main__.CustomProxyMiddleware': 350,
			'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
		},
		"CONCURRENT_REQUESTS":32
	}

	def start_requests(self):
		yield scrapy.Request(url=URL,callback=self.parse)
	
	def parse(self,response):
		print(response.text)

	# def clean(self,value):
	# 	new_str = re.sub(r'[\t\n\r]',"",value)
	# 	return new_str

	# def remainAlpabet(self, value):

	# 	value_1 = re.sub(r'[^a-zA-Z]',"",value)
	# 	return value_1

	# def remainAlpabetNumeric(self, value):

	# 	value_1 = re.sub(r'[^a-zA-Z0-9]',"",value)
	# 	return value_1

class Item(scrapy.Item):
    player_link = scrapy.Field()

class CustomProxyMiddleware:
    def process_request(self, request, spider):
        request.meta["proxy"] = PROXY


class XLSXPipeline(object):
    wb = None
    ws = None

    def open_spider(self, spider):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active

        self.ws.append(FIELDNAMES)
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        self.ws.append([
        	adapter.get("player_link"),
        	])

        return item

    def close_spider(self, spider):
        self.wb.save('output.xlsx')



def start_crawl():
	print("Start Crawling...")
	configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
	runner = CrawlerRunner()
	d = runner.crawl(TestScrapy)
	d.addBoth(lambda _: reactor.stop())
	reactor.run()

start_crawl()