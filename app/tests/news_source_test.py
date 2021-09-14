import unittest
from app.models import News_Source

class NewsSourceTest:
    '''
    Test Class to test the behaviour of the News_Source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.newsSource = News_Source("abc-news","ABC News","our trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com."," https://abcnews.go.com","general","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.newsSource,News_Source))