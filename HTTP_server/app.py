import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Connect to the PostgreSQL database and fetch the scraped data
    conn = psycopg2.connect(host="db", dbname="postgres", user="postgres",
                                password="1234", port=5432)
    cursor = conn.cursor()
    cursor.execute("SELECT title, image_url FROM flats_data")
    data = cursor.fetchall()
    conn.close()
    
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)