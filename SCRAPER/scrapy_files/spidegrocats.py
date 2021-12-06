import scrapy
import json
dir = (r'C:\Users\Administrator\Desktop\rescrape\data.json')
list_with_links = []

with open(dir) as f:
    data = json.load(f)

for item in data:
    link = item.get('link')
    list_with_links.append(link)

print(list_with_links)

class allegro_spidegrocats(scrapy.Spider):
    name = 'spidegrocats'

    start_urls = list_with_links

    custom_settings = {
        'LOG_LEVEL': 'INFO',
        
    }

    def parse(self, response):
                yield {
                    'category': response.css('span[itemprop="name"]').xpath('text()').getall()[-1] 
                }



'''
response.css('span[itemprop="name"]').xpath('text()').getall() <- allegro
or
response.xpath('//a[contains(@class, "category-breadcrumbs__name")]/text()').getall() <- allegrolokalnie

https://www.tutorialspoint.com/scrapy/scrapy_following_links.htm
https://www.tutorialspoint.com/python/string_decode.htm
'''