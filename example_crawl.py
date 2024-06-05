from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse
import logging
import json


class ExampleSpider(CrawlSpider):
    name = "example_spider"
    rules = [Rule(LinkExtractor(), callback="parse_item")]
    start_urls = ["https://www.iana.org/"]
    allowed_domains = [urlparse(url).netloc for url in start_urls]

    def parse_item(self, response):
        item = {
            "content": len(response.text),
            "url": response.url,
        }
        self.log(f"Item scraped: {item['url']}", level=logging.INFO)
        yield item


class ExamplePipeline(object):
    def open_spider(self, spider):
        logging.debug(spider)
        self.file = open("items.jsonl", "w")

    def close_spider(self, spider):
        logging.debug(spider)
        self.file.close()

    def process_item(self, item, spider):
        logging.debug(spider)
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


settings = {
    "USER_AGENT": "Mozilla/5.0",
    "ITEM_PIPELINES": {ExamplePipeline: 100},
    "DOWNLOAD_DELAY": 1,
    "LOG_LEVEL": "INFO",
    "HTTPCACHE_ENABLED": True,
    "HTTPCACHE_DIR": "httpcache",
}


if __name__ == "__main__":
    process = CrawlerProcess(settings=settings)
    process.crawl(ExampleSpider)
    process.start()
