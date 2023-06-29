# -*- coding: utf-8 -*- 
import scrapy 
from scrapy_qqMusic.items import MusicItem 
import re
 # 创建爬虫类
 
class qqMusicSpider(scrapy.Spider): 
    # 爬虫名称 
    name = "qqMusic" 
    # 允许爬取的域名 
    allowed_domains = ["y.qq.com"] 
    # 起始URL列表 
    # start_urls = ["https://y.qq.com/n/ryqq/singer/0025NhlN2yWrP4"] 
    start_urls = [  "https://y.qq.com/n/ryqq/singer/0025NhlN2yWrP4", "https://y.qq.com/n/ryqq/singer/001z2JmX09LLgL"]
    
    # 将start_urls中所有的内容都分别给parse方法来处理
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_items)
    
    
    # 这里是要传到items中的各种信息
    def parse_items(self, response): 
        item = MusicItem()
        # 歌手名
        item["Singer_name"] = response.css("#app > div > div.main > div.mod_data > div.data__cont > div.data__name > h1::text").get()
        # 歌手国籍
        item["Singer_nationality"] = response.css("#popup_data_detail > div > p:nth-child(5)::text").get().replace("国籍：", "")
        # 歌手生日(处理生日真不是一件容易事)
        birthday_row = [birthday for birthday in response.css("#popup_data_detail > div > p").getall() if "生日" in birthday][0]
        item["Singer_birthday"] = birthday_row[birthday_row.find('：') + 1:birthday_row.find('</p>')]
        # 歌曲名(此处为歌手页热门歌曲)
        item["Song_name"] = response.css("#app > div > div.main > div:nth-child(2) > div.mod_songlist > ul.songlist__list > li > a::attr('href')").getall()
        # item["Song_writer"] = response.css("#app").get()
        # item["Song_composer"] = response.css("#app").get()
        # item["Album_name"] = response.css("#app").get()
        # item["Album_release_time"] = response.css("#app").get()
        # item["Album_company"] = response.css("#app").get()

        # # debug用
        # print("\n这里是parse拿到的页面数据：\n\n",
        #       "singer_name:",item["Singer_name"],
        #       "Singer_nationality:",item["Singer_nationality"],
        #       "Singer_birthday:",item["Singer_birthday"],
        #       "Song_name:",item["Song_name"],
        #       "Song_writer:",item["Song_writer"],
        #       "Song_writer:",item["Song_writer"],
        #       "Song_composer:",item["Song_composer"],
        #       "Album_name:",item["Album_name"],
        #       "Album_release_time:",item["Album_release_time"],
        #       "\n")
        yield item
    
    def parse_song(self, response):
        song_page = response.css("#app > div > div.main > div:nth-child(2) > div.mod_songlist > ul.songlist__list > li:nth-child(1)").getall()
