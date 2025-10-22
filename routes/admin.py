from routes import app

@app.route('/admin')
def admin():
    return 'Admin'