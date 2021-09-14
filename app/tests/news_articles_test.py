import unittest
from app.models import News_Articles

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News_article class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = News_Articles("The Associated Press","Man attacked by alligator in Hurricane Ida's floodwaters","https://abcnews.go.com/US/wireStory/man-attacked-alligator-hurricane-idas-floodwaters-79746310","https://s.abcnews.com/images/GMA/210831_gma_zee_0713_hpMain_16x9_992.jpg","2021-08-31T15:39:13Z","SLIDELL, La. -- A man was attacked by a large alligator while walking through floodwaters from Hurricane Ida and is now missing, a Louisiana sheriff said.\r\nThe 71-year-old mans wife told sheriffs dep… [+1041 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,News_Articles))