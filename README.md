# scrapy-httpcache-parser

`scrapy-httpcache-parser` is a parser that enables 
external use of data from Scrapy HttpCacheMiddleware.

Consider the following `settings.py`.

```py
HTTPCACHE_ENABLED = True
HTTPCACHE_DIR     = 'httpcache'
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
```

In this case, crawler's low-level caches is saved 
as a collection of files like this.

```
% cd .scrapy/httpcache/example_spider/c3/c3bed7b7ea39d4ee17d7bc494c02cad08162079c
% ls
meta                    request_headers
pickled_meta            response_body
request_body            response_headers
```

Using `scrapy-httpcache-parser`, you can use 
this low-level cache as a cohesive Python object.

```py
from scrapy_httpcache_parser import ScrapyHttpCacheParser
parser = ScrapyHttpCacheParser(".scrapy/httpcache/example_spider/c3/c3bed7b7ea39d4ee17d7bc494c02cad08162079c")
result = parser.parse_cache()
print(result["meta"])
```

[] Downloader Middleware — Scrapy 2.11.2 documentation  
https://docs.scrapy.org/en/latest/topics/downloader-middleware.html  
> This middleware provides low-level cache to all HTTP requests and responses.  
