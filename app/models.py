class Source:
    '''
    Class that defines sources objects
    '''
    def __init__(self,id,name,description,url,category):
        self.id=id
        self.name=name
        self.description=description
        self.url=url
        self.category=category




class Article:
    '''
    Class that defines article objects
    '''
    all_articles=[]

    def __init__(self,id,author,title,description,url,urlToImage,publishedAt,content):
        self.id=id 
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
        self.content=content