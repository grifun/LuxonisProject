# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class SrealityPipeline:
    def __init__(self):
        # DB connection info
        hostname = 'db'
        username = 'username_test'
        password = 'password_test'
        database = 'SREALITY'

        # Connect to DB
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cursor = self.connection.cursor()
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            id serial PRIMARY KEY, 
            title text,
            images text
        )
        """)

    def process_item(self, item, spider):
        self.cursor.execute(""" insert into sales (title, images) values (%s,%s)""", (
            item["title"],
            item["image_urls"]
        ))
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()