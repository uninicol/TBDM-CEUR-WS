class Paper:
    def __init__(self, url, title, pages, author, abstract=None, keywords=None, content=None, volume_id=None):
        self.url = url
        self.title = title
        self.pages = pages
        self.author = author
        self.abstract = abstract
        self.keywords = keywords
        self.content = content
        self.volume_id = volume_id

    def to_dict(self):
        return self.__dict__
