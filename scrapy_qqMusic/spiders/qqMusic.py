# -*- coding: utf-8 -*- 
import scrapy 
from scrapy import Request
from scrapy_qqMusic.items import MusicItem 
import requests
 # 创建爬虫类
 
class qqMusicSpider(scrapy.Spider): 
    # 爬虫名称 
    name = "qqMusic" 
    # 允许爬取的域名 
    allowed_domains = ["y.qq.com"] 
    # 起始URL列表 
    # start_urls = ["https://y.qq.com/n/ryqq/singer_list"] 
    singer_page = "https://y.qq.com/n/ryqq/singer/{singer_mid}"
    
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
    
    
    # TODO 按照具体情况调节，目前所有子方法都需要重写
    
    # 解析函数 
    def parse(self): 
        # 解析歌手页URL 
        #content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a::attr('href')
        singer_page = Request.get(self.singer_page.format(singer_mid=self.settings.get('singer_mid')))
        yield singer_page
        exit()
        
        
        
        # for subject_url in response.css("#app > div > div.main > div.mod_singer_list > ul > a::attr('href')").getall():
            # yield scrapy.Request(url=subject_url, callback=self.parse_singer)
        # response.css("#app > div > div.main > div.mod_singer_list > ul").getall(): 
            # yield scrapy.Request(url=singer_url, callback=self.parse_singer) 
        # 解析下一页URL 
        # next_url_param = response.css("#content > div > div.paginator > a.next::attr('href')").get() 
        # yield scrapy.Request(url=self.start_urls[0] + next_url_param) 
        
        pass
    
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