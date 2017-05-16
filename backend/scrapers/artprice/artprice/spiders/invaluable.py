import scrapy
from scrapy.selector import HtmlXPathSelector
import urlparse


class Art(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()



class GetReview(scrapy.Spider):
    name = 'invaluable'
    start_urls = ["http://www.invaluable.com/drawings/cc-X40D0LU64C/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        art = Art()      
        art['title'] = response.xpath('//div[@class="lot-tile-title"]/a/text()').extract()
        art['date'] = response.xpath('//p[@class="date-location"]/text()').extract()
        art['price'] = response.xpath('//p[@class="current-bid"]/text()').extract()     		

        yield art
