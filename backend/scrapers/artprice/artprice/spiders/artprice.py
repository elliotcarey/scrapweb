import scrapy
from scrapy_djangoitem import DjangoItem
from artImmo.scrapProject.art.models import Art
import django
django.setup()

class ArtItem(DjangoItem):
    django_model = Art

class GetReview(scrapy.Spider):
    name = 'artprice'
    start_urls = ["https://fr.artprice.com/place-de-marche#!?page=3&order_by=sort_dt&order=desc"]

    def parse(self, response):
        art = ArtItem()
        art['author'] = response.xpath('//a/strong[@title]/text()').extract()        
        art['title'] = response.xpath('//a/span[@title]/text()').extract()
        art['typeart'] = response.xpath('//div[@class="tech"]/text()').extract()
        art['date'] = response.xpath('//span[@class="dates_data"]/text()').extract()
        art['price'] = response.xpath('//div[@class="price pull-left marg marg-r-10"]/text()').extract()     		

        yield art
        print (art['title'])
