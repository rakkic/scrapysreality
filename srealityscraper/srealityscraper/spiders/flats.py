import scrapy
import json
from srealityscraper.items import FlatItem

class FlatSpider(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&sort=0&per_page=' + str(100) + '&page='+str(x)+''for x in range(1, 6)]

    def parse(self, response):
         jsonresponse = response.json() # json objekat response
         for item in jsonresponse["_embedded"]['estates']: # from the obj we take keys
             yield scrapy.Request( 'https://www.sreality.cz/api' + item['_links']['self']['href'] ,
                          callback=self.parse_flat) # sends http request and calls parse_float on response

    def parse_flat(self, response):
        jsonresponse = response.json()
        flat = FlatItem()
        flat['title'] = jsonresponse['name']['value']

        for images in jsonresponse['_embedded']['images']:
            if images['_links']['dynamicDown']: # if we have a dynamic field - link
                tmp = images['_links']['dynamicDown']['href'].replace('{width}', '400')
                tmp = tmp.replace('{height}', '300')
                flat['image_urls'] = tmp
                break # one image

        yield flat