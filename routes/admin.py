from main import app

@app.route('/create_article.html')
def create_article():
    return "create article"