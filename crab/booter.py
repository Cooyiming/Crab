from scrapy import cmdline

cmdline.execute('scrapy crawl crab -o tieba.json'.split())