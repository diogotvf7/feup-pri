class Article:
    def __init__(self, title, authors, date, body):
        self.title = title
        self.authors = authors
        self.date = date
        self.body = body

    def __str__(self):
        return f"Title: {self.title}\nAuthors: {self.authors}\nDate: {self.date}\nBody: {self.body}"