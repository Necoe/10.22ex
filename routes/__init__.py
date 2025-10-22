from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../assets',
            static_url_path='/assets')


app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:621700@localhost:5432/myblog_db'
db = SQLAlchemy(app)


from routes import admin
from routes import user