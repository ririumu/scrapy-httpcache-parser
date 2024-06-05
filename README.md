# scrapy-httpcache-parser

Parse scrapy's http cache files
`scrapy-httpcache-parser` は Scrapy HttpCacheMiddleware の保存結果を外部利用するための parser です。

[] Downloader Middleware — Scrapy 2.11.2 documentation
https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
> This middleware provides low-level cache to all HTTP requests and responses.

たとえば以下のような `setting.py` を想定します。

```
HTTPCACHE_ENABLED = True
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
```

Scrapy を実行した結果 low-level cache は以下のように保存されています。

```
% cd .scrapy/httpcache/example_spider/c3/c3bed7b7ea39d4ee17d7bc494c02cad08162079c
% ls
meta                    request_headers
pickled_meta            response_body
request_body            response_headers
```

```python
from scrapy_http_cache_parser import ScrapyHttpCacheParser
parser = ScrapyHttpCacheParser(".scrapy/httpcache/example_spider/c3/c3bed7b7ea39d4ee17d7bc494c02cad08162079c")
result = parser.parse_cache()
print(result["meta"])
```