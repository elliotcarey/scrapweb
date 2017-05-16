import scrapy
import urlparse


class Immo(scrapy.Item):
    typeImo = scrapy.Field()    
    size = scrapy.Field()
    charac = scrapy.Field()
    price = scrapy.Field()



class GetReview(scrapy.Spider):
    name = 'seloger'
    start_urls = ["http://www.seloger.com/list.htm?org=advanced_search&idtt=2&idtypebien=7,8,9,10,11,12&div=2238&tri=initial&naturebien=1,2,4"]

    def parse(self, response):
        immo = Immo()
        immo['typeImo'] = response.xpath('//div[@class="title"]/a/text()').extract() 
        immo['size'] = response.xpath('//div[@class="properties"]/ul/li[1]/text()').extract()       
        immo['charac'] = response.xpath('//div[@class="properties"]/ul/li[2]/text()').extract()
        immo['price'] = response.xpath('//div[@class="price same_price"]/a/text()').extract()     		

        yield immo
