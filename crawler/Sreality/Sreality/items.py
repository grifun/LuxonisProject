# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SrealityItem(scrapy.Item):
    title = scrapy.Field()          #Title text of the sale offer
    images = scrapy.Field()         #Comma-separated urls of images used