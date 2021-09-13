from app import app
import urllib.request,json
from .models import news_source,news_articles

api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]
base_url2 = app.config["ARTICLE_API_BASE_URL"]

News_Source=news_source.News_Source
News_Articles=news_articles.News_Articles

def get_news_sources():
    get_news_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_sources_url) as url:
        get_news_sources_data = url.read()
        get_news_sources_response = json.loads(get_news_sources_data)

        news_source_results = None

        if get_news_sources_response['sources']:
            news_source_results_list = get_news_sources_response['sources']
            news_source_results = process_results(news_source_results_list)

        return news_source_results

def process_results(news_sources_list):
    news_sources_results = []
    for news_source_item in news_sources_list:
        id = news_source_item.get('id')
        name = news_source_item.get('name')
        description = news_source_item.get('description')
        url = news_source_item.get('url')
        category = news_source_item.get('category')
        language=news_source_item.get("language")
        country=news_source_item.get("country")

        if category:
            news_source_object=News_Source(id,name,description,url,category,language,country)
            news_sources_results.append(news_source_object)

    return news_sources_results

def get_news_articles():
    get_news_articles_url = base_url2.format(api_key)

    with urllib.request.urlopen(get_news_articles_url) as url:
        get_news_articles_data = url.read()
        get_news_articles_response = json.loads(get_news_articles_data)

        news_articles_results = None

        if get_news_articles_response['articles']:
            news_articles_results_list = get_news_articles_response['articles']
            news_articles_results = process_results2(news_articles_results_list)

        return news_articles_results

def process_results2(news_articles_list):
    news_articles_results = []
    for news_article_item in news_articles_list:
        source = news_article_item.get('source')
        author = news_article_item.get('author')
        title = news_article_item.get('title')
        url = news_article_item.get('url')
        urlToImage = news_article_item.get('urlToImage')
        publishedAt=news_article_item.get("publishedAt")
        content=news_article_item.get("content")

        if source:
            id = news_article_item.get('id')
            name = news_article_item.get('name')

            news_articles_object=News_Articles(id,name,author,title,url,urlToImage,publishedAt,content)
            news_articles_results.append(news_articles_object)

    return news_articles_results

        