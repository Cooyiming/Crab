# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from logging import _levelToName
import scrapy


class CrabItem(scrapy.Item):
    # define the fields for your item here like:    A = scrapy.Field(*arg)
    
    # Post main info
    # metadata
    pid = scrapy.Field()
    user_id = scrapy.Field()
    comment_num = scrapy.Field()
    user_name = scrapy.Field()
    level = scrapy.Field()
    #content
    content = scrapy.Field()
    
    # Reply main info
    reply_content = scrapy.Field()




class ReplyItem(CrabItem):
    #  Detailed reply info extracted from r_m & r_c
    floor_num = scrapy.Field()
    spid = scrapy.Field()
    user_name = scrapy.Field()
    user_nickname = scrapy.Field()
    content = scrapy.Field()
    
