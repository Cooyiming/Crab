import scrapy

# define our spider
class PostsSpider(scrapy.Spider):
    # 爬虫的唯一标识符
    name = "posts"

    # 请求生成器
    def start_requests(self):
        
        pn =121
        url = "https://tieba.baidu.com/p/5389935515"
        yield scrapy.Request(url=url,callback=self.parse)
        

    def parse(self, response):
        
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
