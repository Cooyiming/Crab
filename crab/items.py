# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from logging import _levelToName
import scrapy


class CrabItem(scrapy.Item):
    # define the fields for your item here like:    A = scrapy.Field(*arg)
    # Post main info
    metadata = scrapy.Field()
    content = scrapy.Field()
    comment_num = scrapy.Field()
    # Reply main info
    reply_meta = scrapy.Field()
    reply_content = scrapy.Field()


class PostItem(CrabItem):
    # Detailed post info extracted from m & c
    user_id = scrapy.Field()
    user_name = scrapy.Field()
    user_nickname = scrapy.Field()
    level = post_no =scrapy.Field()
    content = scrapy.Field()

class ReplyItem(CrabItem):
    #  Detailed reply info extracted from r_m & r_c
    floor_num = scrapy.Field()
    spid = scrapy.Field()
    user_name = scrapy.Field()
    user_nickname = scrapy.Field()
    content = scrapy.Field()
    
