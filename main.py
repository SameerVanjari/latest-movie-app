from flask import Flask, render_template, request
import scrape_bot

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = scrape_bot.get_movies
    return render_template('index.html', movies=movies)