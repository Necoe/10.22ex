from main import app
from flask import render_template, abort
from services.article_service import ArticleService



@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/article/<article_id>.html')
def article_page(article_id):
    article = ArticleService().get_article(article_id)
    if article:
        return render_template('article.html',article = article)

    abort(404)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/login.html')
def login():
    return render_template('login.html')