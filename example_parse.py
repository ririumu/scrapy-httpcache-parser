from http_cache_parser import HttpCacheParser
from pathlib import Path
from pprint import pprint
from bs4 import BeautifulSoup

glob = Path(".scrapy").glob("httpcache/*/*/*/")
page_dir_list = list(glob)

for page_dir in page_dir_list:
    extractor = HttpCacheParser(page_dir)
    result = extractor.extract()
    soup = BeautifulSoup(result["response_body"], features="lxml")
    if soup.title:
        print(str(soup.title) + " - " + result["meta"]["url"])
