# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter
from mysql import connector


# 将歌手信息保存入数据库
class SingerMysqlPipeline:
    def open_spider(self, spider):
        self.db_cnx = connector.connect(**spider.settings.get("MYSQL_CONFIG"))
        self.db_cursor = self.db_cnx.cursor()
        

    def process_item(self, item, spider):
        sql = "INSERT INTO singer (singer_name, Singer_nationality, Singer_birthday, Song_name) VALUES (%s, %s, %s, %s)"
        data = (item['Singer_name'], item['Singer_nationality'], item['Singer_birthday'], item['Song_name'])
        self.db_cursor.execute(sql, data)
        return item

    def close_spider(self, spider):
        self.db_cnx.commit()
        self.db_cursor.close()
        self.db_cnx.close()
        
# 将歌曲信息保存入数据库
class MusicMysqlPipeline:
    def open_spider(self, spider):
        self.db_cnx = connector.connect(**spider.settings.get("MYSQL_CONFIG"))
        self.db_cursor = self.db_cnx.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO music ( music_name, music_writer, music_composer, music_lyric ) VALUES ( %s, %s, %s, %s);"
        data = (item['Song_name'], item['Song_writer'], item['Song_composer'], item['Song_lyricist'])
        self.db_cursor.execute(sql, data)
        return item

    def close_spider(self, spider):
        self.db_cnx.commit()
        self.db_cursor.close()
        self.db_cnx.close()
        
# 将专辑信息保存入数据库
class AlbumMysqlPipeline:
    def open_spider(self, spider):
        self.db_cnx = connector.connect(**spider.settings.get("MYSQL_CONFIG"))
        self.db_cursor = self.db_cnx.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO album ( album_name, album_release_time, album_company )VALUES ( %s, %s, %s);"
        data = (item['Album_name'], item['Album_release_time'], item['Album_company'])
        self.db_cursor.execute(sql, data)
        return item

    def close_spider(self, spider):
        self.db_cnx.commit()
        self.db_cursor.close()
        self.db_cnx.close()

        
# 将歌手信息保存到json文件中
class SingerJsonPipeline:
    def open_spider(self, spider):
        self.file = open('singer.json', 'wb')
        self.exporter = JsonItemExporter(self.file, ensure_ascii=False)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.file.close()
        file = open('singer.json', 'a')
        file.write("]")
        file.close()
        # self.file.write("]")
        # self.file.close()

# 将歌曲信息保存到json文件中
class MusicJsonPipeline:
    def open_spider(self, spider):
        self.file = open('music.json', 'wb')
        self.exporter = JsonItemExporter(self.file, ensure_ascii=False)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.file.write("]")
        self.file.close()

# 将专辑信息保存到json文件中
class AlbumJsonPipeline:
    def open_spider(self, spider):
        self.file = open('Album.json', 'wb')
        self.exporter = JsonItemExporter(self.file, ensure_ascii=False)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.file.write("]")
        self.file.close()
        
