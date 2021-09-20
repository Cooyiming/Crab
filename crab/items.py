# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from logging import _levelToName
import scrapy


class CrabItem(scrapy.Item):
    # define the fields for your item here like:
    level = scrapy.Field()
    uid = scrapy.Field()
    nickname = scrapy.Field()
    content = scrapy.Field()
    image = scrapy.Field()
    replycount = scrapy.Field()




    pass
