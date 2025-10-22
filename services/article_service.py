from routes import db
from models.article import Article


class ArticleServices:
    def get_articles(self,id):

        return db.session.get(Article,id)