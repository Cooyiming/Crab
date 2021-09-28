from scrapy import cmdline

cmdline.execute('scrapy crawl posts -o tieba.json'.split())