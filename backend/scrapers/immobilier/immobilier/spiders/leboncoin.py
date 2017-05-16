import scrapy
import urlparse


class Immo(scrapy.Item):
    typeImo = scrapy.Field()    
    place = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()



class GetReview(scrapy.Spider):
    name = 'leboncoin'
    start_urls = ["https://www.leboncoin.fr/bureaux_commerces/offres/ile_de_france/?th=1&parrot=0&st=s&ps=7"]
    def parse(self, response):
        immo = Immo()
        immo['typeImo'] = response.xpath('//section/h2/text()').extract() 
        immo['place'] = response.xpath('//section/p[@itemprop="availableAtOrFrom"]/text()').extract()       
        immo['date'] = response.xpath('//section/aside/p[@itemprop="availabilityStarts"]/text()').extract()
        immo['price'] = response.xpath('//section/h3[@class="item_price"]/text()').extract()     		

        yield immo
