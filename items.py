# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 歌手信息为姓名，国籍，生日
    Singer_name = scrapy.Field()
    Singer_nationality = scrapy.Field()
    Singer_birthday = scrapy.Field()
    # 歌曲信息为名称，作词，作曲，歌词
    Song_name = scrapy.Field()
    Song_writer = scrapy.Field()
    Song_composer = scrapy.Field()
    Song_lyricist = scrapy.Field()
    # 专辑信息为名称，发行时间，唱片公司
    Album_name = scrapy.Field()
    Album_release_time = scrapy.Field()
    Album_company = scrapy.Field()
    