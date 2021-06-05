import unittest
from models import source
from models import article
Source=source.Source
article=article.Article

class SourceTest(unnittest.TestCase):
    '''
    Test class to test the behavior of the source class.
    '''

    def setUp(self):
        '''
        set up method that will rrun before every test 
        '''
        self.new_source=Source("abc","Abc news","this gives timely news","https://www.aljazeera.com/news/","private",)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


# class ArticleTest(unnittest.TestCase):
#     '''
#     Test class to test the behavior of the article class.
#     '''




if __name__=='__main__':
    unittest.main()