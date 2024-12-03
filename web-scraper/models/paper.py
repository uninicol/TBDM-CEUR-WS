class Paper:
    def __init__(self, url, title, pages, author):
        self.url = url
        self.title = title
        self.pages = pages
        self.author = author
    
    def to_dict(self):
        return {
            "url": self.url,
            "title": self.title,
            "pages": self.pages,
            "author": self.author,
        }
