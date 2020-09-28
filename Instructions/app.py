from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo  
import marsscrape 

app = Flask(__name__)

mongo = PyMongo(app, url="mongodb://localhost:27017/nasa_db

@app.route("/")
def home():

    mars_data = mongo.nasa_db.marsarticles.find_one()

    return render_template("marsfacts.html", marsdata=mars_data)

@app.route("/scrape")
def scrape():

    mars_scrape=(marsscrape.scrape_info()

    mongo.nasa_db.marsarticles.update({}, mars_scrape, upsert=True)

    return redirect("/") 

if __name__=="__main__":
    app.run(debug=True)

