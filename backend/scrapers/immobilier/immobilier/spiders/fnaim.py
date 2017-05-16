import scrapy
import urlparse


class Immo(scrapy.Item):
    typeImo = scrapy.Field()    
    place = scrapy.Field()
    size = scrapy.Field()
    price = scrapy.Field()



class GetReview(scrapy.Spider):
    name = 'fnaim'
    start_urls = ["http://www.fnaim.fr/17-acheter.htm?localites=%5B%7B%22label%22%3A%22PARIS+%2875%29%22%2C%22value%22%3A%22PARIS+%2875%29%22%2C%22id%22%3A%2275%22%2C%22type%22%3A%222%22%7D%5D&TRANSACTION=1&TYPE%5B%5D=6&SURFACE_MIN=&PRIX_MAX=&idtf=17&submit=Rechercher"]
    def parse(self, response):
        immo = Immo()
        immo['typeImo'] = response.xpath('//div[@class="js-block-responsive"]/p[2]/text()').extract() 
        immo['size'] = response.xpath('//footer/ul/li[@class="picto surface"]/b/text()').extract()        
        immo['place'] = response.xpath('//p[@class="picto lieu"]/a/text()').extract()       
        immo['price'] = response.xpath('//div[@class="js-block-responsive"]/h4/text()').extract()     		

        yield immo
