from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "myCrawler"
    allowed_domins = ["taaghche.com"]
    start_urls = ["https://taaghche.com/"]
    rules = (
        Rule(LinkExtractor(allow=('/category/',)), callback='parse_item',),
    #    Rule(LinkExtractor(allow=('/category/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B1%D9%85%D8%A7%D9%86/')),)
    )
    def pars_item(self,response):
        yield{
            "title": response.css(".bookCard_bookTitle__ELp4O div::text").get(),
            "auther": response.css(".bookCard_bookAuthor__myAZB::text").get(),
            "price": response.css(".bookCard_price__zOAwb::text").get()

        }