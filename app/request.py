from app.news_source_test import News_Source
from app import app
import urllib.request,json
from .models import news_source

api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]

News_Source=news_source.News_Source

def get_news_sources():
    get_news_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_sources_url) as url:
        get_news_sources_data = url.read()
        get_news_sources_response = json.loads(get_news_sources_data)

        news_source_results = None

        if get_news_sources_response['sources']:
            news_source_results_list = get_news_sources_response['sources']
            news_source_results = process_results(news_source_results)

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

        