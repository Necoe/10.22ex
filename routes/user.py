from routes import app
from flask import render_template, abort
from services.article_service import ArticleServices


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about.html')
def about_page():
    return render_template('about.html')


@app.route('/article/<article_id>.html')
def article(article_id):
    article = ArticleServices().get_articles(article_id)

    if article:
        return render_template('article.html', article=article)

    abort(404)

    return render_template('article.html',article = article)


@app.route('/login')
def login():
    return render_template('login.html')
