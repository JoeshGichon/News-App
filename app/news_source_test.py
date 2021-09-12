import unittest
from .models import news_source

News_Source = news_source.News_Source

class NewsSourceTest:
    def setUp(self):
        self.newsSource("abc-news","ABC News","our trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com."," https://abcnews.go.com","general","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.newsSource,News_Source))

if __name__ == '__main__':
        unittest.main()