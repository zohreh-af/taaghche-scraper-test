from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "myCrawler"
    allowed_domins = ["taaghche.com"]
    start_urls = ["https://taaghche.com/"]
    rules = (
        Rule(LinkExtractor(allow=('/category/',)), callback='parse_item', follow=True),
    ).header_container__xofsz