class Config:
     NEWS_API_BASE_URL ="https://newsapi.org/v2/top-headlines/sources?apiKey={}"
     ARTICLE_API_BASE_URL="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={}"



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True