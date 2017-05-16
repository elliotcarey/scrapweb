import scrapy
import urlparse


class Art(scrapy.Item):
    author = scrapy.Field()    
    title = scrapy.Field()
    typeart = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()



class GetReview(scrapy.Spider):
    name = 'salesroom'
    start_urls = ["https://www.the-saleroom.com/fr-fr/search-filter?mastercategorycode=FIA&type=Oil%20painting"]

    def parse(self, response):
        art = Art()
        art['title'] = response.xpath('//div[@class="lot-single"]/div/h1/a/text()').extract()
        art['date'] = response.xpath('//div[@class="lot-single"]/aside/ul/li/strong/text()').extract()
        art['price'] = response.xpath('//div[@class="lot-single"]/aside/ul/li[@class="estimate"]/strong/text()').extract()     		

        yield art