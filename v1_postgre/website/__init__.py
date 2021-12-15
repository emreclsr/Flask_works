from flask import Flask
from flask_login.utils import login_required
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager

app = Flask(__name__)
app.config["SECRET_KEY"] = "verysecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:111995@localhost/notepad"
db = SQLAlchemy(app)
#DB_NAME = "notepad.db"



def create_app():
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "verysecretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:111995@localhost/notepad"
    db.init_app(app)"""

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    #create_database(app)


    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

"""
def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Datebase!")"""

