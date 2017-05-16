import scrapy
import urlparse


class Immo(scrapy.Item):
    typeImo = scrapy.Field()    
    place = scrapy.Field()
    size = scrapy.Field()
    price = scrapy.Field()



class GetReview(scrapy.Spider):
    name = 'avendre'
    start_urls = ["https://www.avendrealouer.fr/recherche.html?pageIndex=1&sortPropertyName=ReleaseDate&sortDirection=Descending&searchTypeID=1&typeGroupCategoryID=1&transactionId=1&localityIds=3-75,3-92,3-94&typeGroupIds=4,5,9,10,11,12,98&minimumPrice=100000"]
    def parse(self, response):
        immo = Immo()
        immo['typeImo'] = response.xpath('//ul[@class="mode-list"]/li/div/a/ul/li[1]/text()').extract() 
        immo['size'] = response.xpath('//ul[@class="mode-list"]/li/div/a/ul/li[2]/text()').extract()        
        immo['place'] = response.xpath('//ul[@class="mode-list"]/li/div/a/span[@class="loca"]/text()').extract()       
        immo['price'] = response.xpath('//ul[@class="mode-list"]/li/div/a/span[@class="price"]/text()').extract()     		

        yield immo
