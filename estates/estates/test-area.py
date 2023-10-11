""" Taks
Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell)
and save it in the Postgresql database. Implement a simple HTTP server in python and show these 500 
items on a simple page (title and image) and put everything to single docker compose command so that 
I can just run "docker-compose up" in the Github repository and see the scraped ads on 
http://127.0.0.1:8080 page.
"""
import psycopg2
from estates.settings import DATABASE_URI


def save_to_database(self, title):
        print("start1")
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                                password="1234", port=5432)
        #conn = psycopg2.connect(DATABASE_URI)
        # `cursor = conn.cursor()` is creating a cursor object that allows us to execute SQL commands
        # and retrieve data from the PostgreSQL database connected to `conn`. The cursor object
        # provides methods like `execute()` to execute SQL queries and `fetchone()` or `fetchall()` to
        # retrieve the results of the query.
        print("start2")
        cursor = conn.cursor()
        print("start3")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS flats_data (
            id INT PRIMARY KEY,
            title VARCHAR(255),
            image_url VARCHAR(2083)
        );
        """)
        print('TABLE flat created!')
        
        #cursor.execute(
        #    "INSERT INTO flats_data (title, image_url) VALUES (%s, %s)", (title, image_url)
        #)
        conn.commit()

        cursor.close()
        conn.close()