from . import db

class Quote:
    '''
    Quotes class to define quote objects
    '''

    def __init__(self,id,author,quote,permalink):
        self.id =id
        self.author = author
        self.quote = quote
        self.permalink = "http://quotes.stormconsultancy.co.uk/quotes/16/" + permalink
    
    



# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255))

#     def __repr__(self):
#         return f'User {self.username}'


