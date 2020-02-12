# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field
from scrapy.loader.processors import TakeFirst, Join, Compose


class WebScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Article(Item):
    title = Field(output_processor=TakeFirst())
    publish_date = Field(output_processor=TakeFirst())
    content = Field(
        output_processor=Compose(lambda v: filter(None, v), Join(''))
    )
    image_urls = Field()
    links = Field()
