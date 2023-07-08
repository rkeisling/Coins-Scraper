# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CoinsScraperPipeline:
    def process_item(self, item, spider):
        return item


import pymongo
import sys
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class MongoDBPipeline:
    def __init__(self, mongo_collection_name):
        conn = pymongo.MongoClient(
            settings.get('MONGO_HOST'),
            settings.get('MONGO_PORT')
        )
        self.mongodb_uri = f"{settings.get('MONGO_HOST')}:{settings.get('MONGO_PORT')}"
        db = conn[settings.get('MONGO_DB_NAME')]
        self.mongodb_db = db
        self.collection = self.mongodb_db[mongo_collection_name]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_collection_name=crawler.settings.get('MONGO_COLLECTION_NAME')
        )

    def open_spider(self, spider):
        conn = pymongo.MongoClient(
            settings.get('MONGO_HOST'),
            settings.get('MONGO_PORT')
        )
        self.client = conn

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = dict(item)
        self.collection.insert_one(data)
        return item