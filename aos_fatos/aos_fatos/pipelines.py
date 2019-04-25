from scrapy.utils.project import get_project_settings
import pyodbc
settings = get_project_settings()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AosFatosPipeline(object):
    def process_item(self, item, spider):

        # insert
        cursor = self.cnxn.cursor()
        cursor.execute('''
                        INSERT INTO TabelaTeste(title,date,quote_text,status,url)
                        VALUES(?,?,?,?,?)
                    ''', item['title'],item['date'],item['quote_text'], item['status'],item['url'])
        return item

    def open_spider(self, spider):
        server = settings.get('SERVER')
        database = settings.get('DATA_BASE')
        username = settings.get('USER_NAME')
        password = settings.get('PASSWORD')
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    def close_spider(self, spider):
        self.cnxn.commit()
        self.cnxn.close()
