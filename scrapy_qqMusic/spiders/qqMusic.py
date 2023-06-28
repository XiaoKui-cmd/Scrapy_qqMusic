# -*- coding: utf-8 -*- 
import scrapy 
from scrapy_qqMusic.items import MusicItem 
 # 创建爬虫类
 
class qqMusicSpider(scrapy.Spider): 
    # 爬虫名称 
    name = "qqMusic" 
    # 允许爬取的域名 
    allowed_domains = ["https://y.qq.com"] 
    # 起始URL列表 
    start_urls = ["https://y.qq.com/n/ryqq/singer_list"] 
     # 自定义设置 
    custom_settings = { 
        "DOWNLOAD_DELAY": 1, # 下载延迟 
        "ITEM_PIPELINES": { # 管道设置 
            "scrapy_qqMusic.pipelines.SingerMysqlPipeline":None, # 歌手MySQL管道 
            "scrapy_qqMusic.pipelines.SingerJsonPipeline":402, # 歌手JSON管道 
            "scrapy_qqMusic.pipelines.MusicMysqlPipeline": None, # 歌曲MySQL管道 
            "scrapy_qqMusic.pipelines.MusicJsonPipeline": 400, # 歌曲JSON管道 
            "scrapy_qqMusic.pipelines.AlbumMysqlPipeline": None, # 专辑MySQL管道 
            "scrapy_qqMusic.pipelines.AlbumJsonPipeline": 396, # 专辑JSON管道 
        }     
    } 
    
    # TODO 按照具体情况调节，目前所有css选择器都需要重写
    
     # 解析函数 
    def parse(self, response): 
        # 解析歌手URL 
        for singer_url in response.css("#app > div > div.main > div.mod_singer_list > ul").getall(): 
            yield scrapy.Request(url=singer_url, callback=self.parse_singer) 
         # 解析下一页URL 
        next_url_param = response.css("#content > div > div.paginator > a.next::attr('href')").get() 
        yield scrapy.Request(url=self.start_urls[0] + next_url_param) 
     # 解析歌手函数 
    def parse_singer(self, response): 
        selector = response.css("#info") 
        item = MusicItem() 
        item["Singer_name"] = response.css("#content > h1 > span.name::text").get() 
        item["Singer_nationality"] = selector.css("span:nth-of-type(1) > span.attrs > a::text").get() 
        item["Singer_birthday"] = selector.css("span:nth-of-type(2) > span.attrs > a::text").get() 
         # 返回歌手信息 
        yield item 
         # 解析歌曲URL 
        for music_url in response.css("a[href*='music.douban.com/subject/']::attr('href')").getall(): 
            yield scrapy.Request(url=music_url, callback=self.parse_music) 
     # 解析歌曲函数 
    def parse_music(self, response): 
        selector = response.css("#info") 
        item = MusicItem() 
        item["Singer_name"] = response.css("#content > h1 > span.name::text").get() 
        item["Singer_nationality"] = selector.css("span:nth-of-type(1) > span.attrs > a::text").get() 
        item["Singer_birthday"] = selector.css("span:nth-of-type(2) > span.attrs > a::text").get() 
         # 返回歌曲信息 
        yield item 
         # 解析专辑URL 
        for album_url in response.css("a[href*='music.douban.com/subject/']::attr('href')").getall(): 
            yield scrapy.Request(url=album_url, callback=self.parse_album) 
     # 解析专辑函数 
    def parse_album(self, response): 
        selector = response.css("#info") 
        item = MusicItem() 
        item["Singer_name"] = response.css("#content > h1 > span.name::text").get() 
        item["Singer_nationality"] = selector.css("span:nth-of-type(1) > span.attrs > a::text").get() 
        item["Singer_birthday"] = selector.css("span:nth-of-type(2) > span.attrs > a::text").get() 
         # 返回专辑信息 
        yield item