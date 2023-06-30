# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter
from mysql import connector

# 将信息保存入数据库
class MysqlPipeline:
    def open_spider(self, spider):
        self.db_cnx = connector.connect(**spider.settings.get("MYSQL_CONFIG"))
        self.db_cursor = self.db_cnx.cursor()
        
    def process_item(self, item, spider):
        sql = "INSERT INTO singer (singer_name, singer_nationality, singer_birthday) VALUES (%s, %s, %s)"
        data = (item['Singer_name'], item['Singer_nationality'], item['Singer_birthday'])
        self.db_cursor.execute(sql, data)
        return item

    def close_spider(self, spider):
        self.db_cnx.commit()
        self.db_cursor.close()
        self.db_cnx.close()
      
        
# 将信息保存到json文件中
class JsonPipeline:
    def open_spider(self, spider):
        self.file = open('Musics.json', 'wb')
        self.exporter = JsonItemExporter(self.file, ensure_ascii=False)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.file.close()
        file = open('Musics.json', 'a')
        file.write("]")
        file.close()

