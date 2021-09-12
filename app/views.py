from app.models import news_source
from flask import render_template
from app import app
from .request import get_news_sources

@app.route("/")
def index():
    title="Home"
    news_sources = get_news_sources()
    return render_template("index.html", title=title,news_sources=news_sources)