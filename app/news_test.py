import unittest
from models import source
from models import article
Source=source.Source
Article=article.Article

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behavior of the source class.
    '''

    def setUp(self):
        '''
        set up method that will run before every test 
        '''
        self.new_source=Source("abc","Abc news","this gives timely news","https://www.aljazeera.com/news/","private",)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behavior of the article class.
    '''
    def setUp(self):
        self.new_article=Article("John","mountain goes to the lake", "HEY" ,"the 2022 endpoint","https://www.standardmedia.co.ke/politics/article/2001389638/inside-railas-talks-with-central-elders","2020-2-2","Done deal")

    def  test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))




if __name__=='__main__':
    unittest.main()