import os 
from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
from model import rand_headlines, fetch_results

app = Flask(__name__)
load_dotenv()
api_key = os.getenv("API_KEY")

@app.route('/')
@app.route('/index')
def index():
    current = rand_headlines(api_key)
    return render_template("index.html", title="Homepage", headlines=current)

@app.route('/search', methods=["GET", "POST"])
def results():
    topics = []
    if "entertainment-box" in request.form:
        topics.append("entertainment")
    if "sports-box" in request.form:
        topics.append("sports")
    if "tech-box" in request.form:
        topics.append("technology")
    results = fetch_results(topics, request.form['query'], api_key)
    return render_template('search.html', query=request.form['query'], results=results, title="Search Results")

if __name__ == '__main__':
    app.run()