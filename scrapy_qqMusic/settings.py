# Scrapy settings for scrapy_qqMusic project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy_qqMusic"

SPIDER_MODULES = ["scrapy_qqMusic.spiders"]
NEWSPIDER_MODULE = "scrapy_qqMusic.spiders"


# 使用UserAgent来生成USER_AGENT
from fake_useragent import UserAgent
USER_AGENT = UserAgent().random

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapy_qqMusic (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapy_qqMusic.middlewares.ScrapyqqmusicSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "scrapy_qqMusic.middlewares.ScrapyqqmusicDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapy_qqMusic.pipelines.ScrapyqqmusicPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# pipeline优先级设置
# 注：这个写在spider里面似乎会出现未知特性
DOWNLOAD_DELAY =  1
# 这里只开启一个用于debug
ITEM_PIPELINES = { 
    # "scrapy_qqMusic.pipelines.SingerMysqlPipeline":404, # 歌手MySQL管道 
    "scrapy_qqMusic.pipelines.SingerJsonPipeline":403, # 歌手JSON管道 
    # "scrapy_qqMusic.pipelines.MusicMysqlPipeline": 402, # 歌曲MySQL管道 
    # "scrapy_qqMusic.pipelines.MusicJsonPipeline": 401, # 歌曲JSON管道 
    # "scrapy_qqMusic.pipelines.AlbumMysqlPipeline": 400, # 专辑MySQL管道 
    # "scrapy_qqMusic.pipelines.AlbumJsonPipeline": 399, # 专辑JSON管道 
        }

# 要爬取的歌手mid
singer_mid = [
  '001z2JmX09LLgL', #汪苏泷
  '0025NhlN2yWrP4', #周杰伦
  '000c2vQb13oq5I' #hanser
]

# 数据库配置
MYSQL_CONFIG = {
    'host': '101.42.22.211',
    'port': '3306',
    'user': 'student',
    'password': 'Ambow99(',
    'database': 'sms'
}