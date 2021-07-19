import scrapy

class BrandsSpider(scrapy.Spider):
    name = 'paintbrands'
    start_url = ['https://www.michaels.com/paint-and-painting-supplies/fine-art-paint/845160979']

    def parse(self, response):
        for products in response.css('div.product-tile'):
            yield {
                'nameBrand' : products.css('a.name-link::text').get(),
            }