import scrapy
from scrapy.selector import HtmlXPathSelector
import urlparse


class Art(scrapy.Item):
    author = scrapy.Field()    
    title = scrapy.Field()
    typeart = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()



class GetReview(scrapy.Spider):
    name = 'liveauction'
    start_urls = ["https://new.liveauctioneers.com/search?parameters=%7B%22pageSize%22:120,%22page%22:1,%22sort%22:%22-popularity%22,%22status%22:%22online%22,%22category_id%22:%2210%22%7D"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        art = Art()      
        art['title'] = response.xpath('//a[@class="item-title___3zS_6"]/span/text()').extract()
        art['date'] = response.xpath('//span[@class="card-date___3dU5s"]/span/text()').extract()
        art['price'] = response.xpath('//span[@class="item-current-bid___j1nna"]/span/text()').extract()     		

        yield art
