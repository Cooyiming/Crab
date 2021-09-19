import scrapy

# define our spider
class PostsSpider(scrapy.Spider):
    # 爬虫的唯一标识符
    name = "posts"

    # 请求生成器
    def start_requests(self):
        
        # present pn =121
        url = "https://tieba.baidu.com/p/5389935515"
        yield scrapy.Request(url=url,callback=self.parse)
        

    def parse(self, response):
        
        # Dev only
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
        
        
        
        #选贴器

        posts = response.xpath('//*[@id="j_p_postlist"]')
        for post in posts:
            yield{

                'level': post.xpath(''),
                'uid':post.xpath(''),
                'nickname':post.xpath(''),
                'content':post.xpath(''),
                'replycount':post.xpath(''),


            }
    
        
        
        pass
        
        
        # 下一页
        next_page = response.xpath('//*[@id="thread_theme_5"]/div[1]/ul/li[1]/a[10]/@herf').get()
        
        if next_page is not None:
            yield response.follow(next_page, self.parse)