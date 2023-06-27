# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter
from mysql import connector


# 将歌曲信息保存入数据库
class MusicMysqlPipeline:
    def open_spider(self, spider):
        self.db_cnx = connector.connect(**spider.settings.get("MYSQL_CONFIG"))
        self.db_cursor = self.db_cnx.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO music ( music_name, music_writer, music_composer, music_lyric ) VALUES ( %s, %s, %s, %s);"
        data = (item['name'], item['writer'], item['composer'], item['lyric'])
        self.db_cursor.execute(sql, data)
        return item

    def close_spider(self, spider):
        self.db_cnx.commit()
        self.db_cursor.close()
        self.db_cnx.close()
        
# 将歌手信息保存入数据库
class SingerMysqlPipeline:
    def open_spider(self, spider):
        self.db_cnx = connector.connect(**spider.settings.get("MYSQL_CONFIG"))
        self.db_cursor = self.db_cnx.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO singer ( singer_name, singer_rating_number ) VALUES ( %s, %s);"
        data = (item['name'], item['rating_num'])
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
        sql = "INSERT INTO album ( album_name, album_rating_number ) VALUES ( %s, %s);"
        data = (item['name'], item['rating_num'])
        self.db_cursor.execute(sql, data)
        return item

    def close_spider(self, spider):
        self.db_cnx.commit()
        self.db_cursor.close()
        self.db_cnx.close()

        
# 将歌手信息保存到json文件中
class SingerJsonPipeline:
    def open_spider(self, spider):
        self.file = open('singer.json', 'w', encoding='utf-8')
        self.exporter = JsonItemExporter(self.file, ensure_ascii=False)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.file.write("]")
        self.file.close()

# 将歌曲信息保存到json文件中
class MusicJsonPipeline:
    def open_spider(self, spider):
        self.file = open('music.json', 'w', encoding='utf-8')
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
        self.file = open('Album.json', 'w', encoding='utf-8')
        self.exporter = JsonItemExporter(self.file, ensure_ascii=False)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.file.write("]")
        self.file.close()
        
        
