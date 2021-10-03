from typing import ContextManager
import scrapy
#from scrapy import signals

import json,re
# define our spider
class PostsSpider(scrapy.Spider):
    # 爬虫的唯一标识符
    name = "posts"
    allowed_domains = ['tieba.baidu.com']
    # 请求生成器
    #def start_requests(self):

        # present pn =121
    #    url = "https://tieba.baidu.com/p/5389935515?pn=1"
    #    yield scrapy.Request(url=url,callback=self.parse)
    start_urls = ["https://tieba.baidu.com/p/5389935515?pn=1",]

    def parse(self, response):

        # Dev only
            #page = response.url.split("/")[-2]
            #filename = f'quotes-{page}.html'
            #with open(filename, 'wb') as f:
            #    f.write(response.body)
            #self.log(f'Saved file {filename}')
        
        #选贴器
        posts = response.xpath('//*[@id="j_p_postlist"]/div[@class="l_post l_post_bright j_l_post clearfix  "]')
        # Return a list of selectors
                
        for post in posts:
            #Defult root node here is  
            pid = int(post.xpath('@data-pid').get())        # 返回str->返回int
            metadata = post.xpath('@data-field').getall()   # 返回List
                                                            # example:['{"key1":value1}']                                                     
          
            content_raw = post.xpath('./div[2]/div[1]/cc/div[2]/*|./div[2]/div[1]/cc/div[2]/text()').extract()
        # Post info wrapper(已完成)
            # Metadata normalization
            data = json.loads(metadata[0])
            #data is a dictionary
            meta_author = data['author']
            meta_content = data['content']

            user_id = int(meta_author['user_id'])
            comment_num = meta_content['comment_num']
            level = meta_content['post_no']
            # Parse 'comment_num' in the metadate first

#TODO:      Post content wrapper


            yield{
                'pid':pid,
                'level':level,
                'comment_num':comment_num,
                'user_id':user_id,
                'content':content_raw,
            }
    #TODO:  Reply wrapper TODO:
            if comment_num != 0 :
            #    replies = post.xpath('.//*[@class="j_lzl_c_b_a core_reply_content"]/ul//li[@class="lzl_single_post j_lzl_s_p "]')
            #    yield{
            #    'reply_meta':post.xpath(''),
            #    'reply_content':post.xpath(''),
            #    }
                pass
        


        #下一页(已完成)
        this_page = response.xpath('//*[@id="thread_theme_5"]/div[1]/ul/li[1]/span/text()').extract()
        tp = int(this_page[0])
        np = str(tp+1)
        next_page = "https://tieba.baidu.com/p/5389935515?pn=" + np
        total_page = response.xpath('//*[@id="thread_theme_5"]/div[1]/ul/li[2]/span[2]/text()').extract()
        if this_page is not total_page:
            yield response.follow(next_page, self.parse)
    
