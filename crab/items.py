# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from logging import _levelToName
import scrapy


class CrabItem(scrapy.Item):
    # define the fields for your item here like:
    metadata = scrapy.Field()
    post_content = scrapy.Field()
    comment_num = scrapy.Field()
    reply_content = scrapy.Field()
class PostItem(CrabItem):
    uid = scrapy.Field()
    pid = scrapy.Field()
    username = scrapy.Field()
    level = post_no =scrapy.Field()
    content = scrapy.Field()
    pass

class ReplyItem(CrabItem):
    sid = scrapy.Field()
    username = scrapy.Field()
    content = scrapy.Field()
