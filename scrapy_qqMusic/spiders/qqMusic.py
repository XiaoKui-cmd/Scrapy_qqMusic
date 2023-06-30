import scrapy
from scrapy import Selector,Request
from scrapy_qqMusic.items import MusicItem
from urllib.parse import urljoin

class QqmusicSpider(scrapy.Spider):
    name = 'qqMusic'
    allowed_domains = ['qqmusic.com', 'y.qq.com']
    start_urls = ['https://y.qq.com/n/ryqq/singer/003Nz2So3XXYek','https://y.qq.com/n/ryqq/singer/001BLpXF2DyJe2' ]
    sencond_url=['https://y.qq.com']

    # 歌手部分
    def parse(self, response):
        sel = Selector(response)
        items = MusicItem()
        # 歌手名
        items['Singer_name'] = sel.css(
            '#app > div > div.main > div.mod_data > div.data__cont > div.data__name > h1.data__name_txt::text').extract_first()
        items['Singer_nationality'] = sel.css('#popup_data_detail > div > p:nth-child(5)::text').extract_first()
        # 歌手生日
        birthday_row = [birthday for birthday in response.css("#popup_data_detail > div > p").getall() if "生日" in birthday][0]
        items["Singer_birthday"] = birthday_row[birthday_row.find('：') + 1:birthday_row.find('</p>')]
        print(items['Singer_name'], items['Singer_nationality'], items['Singer_birthday'])
        yield items
        # 找所有的专辑的url
        list_iteams=sel.css('#app > div > div.main > div:nth-child(2) > div.mod_songlist > ul.songlist__list > li')
        detail_urls = sel.css(' div.songlist__album > a::attr(href)').extract()
        # 拿到所有专辑的url
        for detail_url in detail_urls:
            url = response.urljoin(detail_url)
            yield Request(url=url, callback=self.parse_Albums)
        # 找所有的歌曲的url
        Song_iteams=sel.css(' div > div.songlist__songname > span > a::attr(href)').extract()
        # 拿到所有歌曲的url
        for Song_iteam in  Song_iteams:
            url2 = response.urljoin(Song_iteam)
            yield  Request(url=url2,callback=self.parse_Songs)

    # 专辑部分
    def parse_Albums(self, response):
        sel = Selector(response)
        items = MusicItem()
        # 专辑名
        items['Album_name'] = sel.css(
            '#app > div > div.main > div.mod_data > div > div.data__name > h1.data__name_txt::text').extract()
        # 专辑发布时间
        items['Album_release_time'] = sel.css(
            '#app > div > div.main > div.mod_data > div > ul > li:nth-of-type(3)::text').extract()
        # 专辑唱片公司
        items['Album_company'] = sel.css(
            '#app > div > div.main > div.mod_data > div > ul > li:nth-of-type(4)::text').extract()
        print(items['Album_name'], items['Album_release_time'], items['Album_company'])
        return items
    # 歌曲部分
    def parse_Songs(self, response):
        sel=Selector(response)
        items = MusicItem()
        # 歌曲名
        items['Song_name']=sel.css(
            '#app > div > div.main > div.mod_data > div > div.data__name > h1.data__name_txt::text').extract_first()
        
        items['Song_lyricist'] = sel.css(
            '#app > div > div.main > div.mod_data > div > div.data__name > h1.data__name_txt::text').extract_first()
        print(items['Song_name'], items['Song_lyricist'])
        return items
