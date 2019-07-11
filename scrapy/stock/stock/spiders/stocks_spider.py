import scrapy
from influxdb import InfluxDBClient
from time import time
import pdb
import random
class StockSpider(scrapy.Spider):
  companyList = ["MSFT", "FB", "AMZN", "GOOGL", "AAPL", "INTC", "NKE", "SBUX", "EBAY", "WMT", "AMD"]  
  name = "stock"
  start_urls = ['https://finance.yahoo.com/quote/']
  db = InfluxDBClient ("localhost", 8086);
  def parse(self, response):
      for company in self.companyList:
          link = self.start_urls[0] + company + '/'
          print(link)
          yield scrapy.Request(link, callback = self.crawStock, meta = {'companyName' : company})
  def crawStock(self, response): 
      companyName = response.meta.get('companyName')
      self.db.switch_database("stock")
      price = response.xpath('//div[@id="quote-header-info"]/div[@class="My(6px) Pos(r) smartphone_Mt(6px)"]/div//span/text()').extract()[0]
      growth = response.xpath('//div[@id="quote-header-info"]/div[@class="My(6px) Pos(r) smartphone_Mt(6px)"]/div//span/text()').extract()[1]
      json = [{
        "measurement": companyName,
        "time": int(time()) * 1000000000,
        "fields": {
        "price": str(price),
        "growth": str((growth))
        }
      }]
      self.db.write_points(json)
        