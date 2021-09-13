from app.models import news_source
from flask import render_template
from app import app
from .request import get_news_sources,get_news_articles

@app.route("/")
def index():
    title="Home"
    news_sources = get_news_sources()
    return render_template("index.html", title=title,news_sources=news_sources)

@app.route("/articles")
def article():
    title="articles"
    news_articles = get_news_articles()
    print(news_articles)
    return render_template("articles.html",title=title,news_articles=news_articles)