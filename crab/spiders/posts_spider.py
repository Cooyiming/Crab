from typing import ContextManager
import scrapy
#from scrapy import signals

import json,re









# define our spider
class PostsSpider(scrapy.Spider):
    # 爬虫的唯一标识符
    name = "posts"
    allowed_domains = ['tieba.baidu.com']
    @classmethod
    # 请求生成器
    def start_requests(self):
        
        # present pn =121
        url = "https://tieba.baidu.com/p/5389935515?pn=1"
        yield scrapy.Request(url=url,callback=self.parse)
        

    def parse(self, response):
        
        # Dev only
        #page = response.url.split("/")[-2]
        #filename = f'quotes-{page}.html'
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log(f'Saved file {filename}')
        
        #选贴器
        posts = response.xpath('//*[@id="j_p_postlist"]//div')
        """
            posts:
            //*[@id="j_p_postlist"]/div[1]
            //*[@id="j_p_postlist"]/div[1]
            //*[@id="j_p_postlist"]/div[2]

            author:

            content:
            //*[@id="post_content_141129758205"]
                image:
                //*[@id="post_content_141134307009"]/img

            reply:
            //*[@id="j_p_postlist"]/div[1]/div[2]/div[1]/cc
        """
        
        for post in posts:
            pid = post.xpath('.@data-pid').get()
            metadata = post.xpath('.@data-field').getall()                       #TODO:
            content = post.xpath('.//*[@class="d_post_content j_d_post_content "]/descendant::*')
            #                     //*[@id="j_p_postlist"]/div[10]/div[2]/div[1]
            # Metadata normalization
#TODO:
            data = json.loads(metadata)
            #data is a dictionary
            meta_author = data['author']
            meta_content = data['content']
            
            user_id = meta_author['user_id']
            comment_num = meta_content['comment_numa']
            level = meta_content['post_no']
            # Parse 'comment_num' in the metadate first
            
            yield{
                'pid':pid,
                'content':content,
                'comment_num':comment_num,
                'user_id':user_id,
                'level':level,
            }
#TODO:
            if comment_num != 0 :
                replies = post.xpath('.//*[@class="j_lzl_c_b_a core_reply_content"]/ul//li[@class="lzl_single_post j_lzl_s_p "]')
                yield{
                'reply_meta':post.xpath(''),
                'reply_content':post.xpath(''),
                }
        #下一页(But there is no end of this...)
        next_page = response.xpath('//*[@id="l_pager pager_theme_4 pb_list_pager"]/a[1ast()-1]/@herf').get()
        #tips:                      //*[@id="thread_theme_5"]/div[1]/ul/li[1]/a[9]/@herf
        this_page = response.xpath('//*[@id="l_pager pager_theme_4 pb_list_pager"]//span/text()').get()
        total_page = response.xpath('//*[@id="thread_theme_5"]/div[1]/ul/li[2]/span[2]/text()').get()
        if this_page is not total_page:
            yield response.follow(next_page, self.parse)

    def parse_details(self, response, item=None):
        if item:
            # populate more `item` fields
            return item
        else:
            self.logger.warning('No item received for %s', response.url)