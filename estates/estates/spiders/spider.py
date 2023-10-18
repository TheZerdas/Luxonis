import scrapy
import json
import re
from estates.settings import DATABASE_URI
import psycopg2
import requests
from scrapy.crawler import CrawlerProcess


class FlatSpider(scrapy.Spider):
    name = 'estates'
    allowed_domains = ['sreality.cz']
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=0&per_page=500']
   
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
   
    def parse(self, response, **kwargs):
        response_json = response.json()
        # converting the response body of the HTTP response into a dictionary object 
        for flat in response_json.get('_embedded').get('estates'):
            title = flat.get('name')
            image_url = flat.get('_links').get('images')[0].get('href')
            yield (
                {
                    # replace any whitespace characters with a single space character
                    'title': re.sub(r'\s', ' ', title),
                    # image_url is retrieving the URL of the first image associated with the flat
                    'image_url': image_url,
                }
            )
            # Save to PostgreSQL
            conn = psycopg2.connect(DATABASE_URI)
            # allows to execute SQL commands and retrieve data from the PostgreSQL database connected to 
            # `conn`. The cursor object provides methods like `execute()` to execute SQL queries and 
            # `fetchone()` or `fetchall()` to retrieve the results of the query.
            cursor = conn.cursor()

            try:
                #cursor.execute("""DELETE FROM flats_data
                #    WHERE (SELECT COUNT(*) FROM flats_data) > 500;""")
                cursor.execute("""CREATE TABLE IF NOT EXISTS flats_data (
                    title VARCHAR(255),
                    image_url VARCHAR(2083)
                );
                """)
                
                cursor.execute(
                    "INSERT INTO flats_data (title, image_url) VALUES (%s, %s)", (title, image_url)
                )
                conn.commit()
            except Exception as e:
                print(f"Error inserting data into the database: {e}")
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
        