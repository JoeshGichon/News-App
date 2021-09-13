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
    bbc_news_articles = get_news_articles("bbc-news")
    a=get_news_articles("abc-news-au")
    b = get_news_articles("aftenposten")
    c=get_news_articles("al-jazeera-english")
    d=get_news_articles("associated-press")
    e=get_news_articles("bloomberg")
    f=get_news_articles("cbs-news")
    g=get_news_articles("cnn-es")
    h=get_news_articles("crypto-coins-news")
    i=get_news_articles("financial-post")
    return render_template("articles.html",title=title,bbc_news_articles=bbc_news_articles,a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h,i=i)