from scrapy.item import Item, Field

class FlatItem(Item):
    title = Field()
    image_urls = Field()
