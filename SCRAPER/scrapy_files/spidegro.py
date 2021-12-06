import scrapy
from scrapy.crawler import CrawlerProcess

class allegro_spidegro(scrapy.Spider):
    name = 'spidegro'

    start_urls = [
        f"https://allegro.pl/listing?string=nintendo%20switch"
    ]

    def parse(self, response):
        item_class_list = response.xpath('//div/h2/a/@class').getall()
        item_class_name = min(item_class_list[1:], key=lambda word: len(word))
        price_class_name = response.xpath("//div/span[contains(., ',')]/@class").get()

        for item, price in zip(
            response.xpath(f'//div/h2/a[contains(@class, "{item_class_name}")]'),
            response.css(f'span[class="{price_class_name}"]')
        ):
            yield {
                'title': item.xpath('text()').get(),
                'link': item.xpath('@href').get(),
                'price': int(price.xpath('text()').get().replace(' ', '').replace(',', ''))
            }
        next_page = response.css("a[rel='next']").xpath('@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

process.crawl(allegro_spidegro)
process.start()