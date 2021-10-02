import fake_useragent
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import json


class RandomUserAgent(UserAgentMiddleware):
    ua = fake_useragent.UserAgent()

    def __init__(self, user_agent=''):
        super().__init__(user_agent=user_agent)

    def process_request(self, request, spider):
        ua = fake_useragent.UserAgent()
        request.headers.setdefault('User-Agent', ua)


if __name__ == "__main__":
    #TODO:
    pass
