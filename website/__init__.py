from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from os import path
from flask_login import LoginManager
from flask_mail import Mail
import os



def create_app():
    #creatt the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'petesudlor'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    db.init_app(app)
    
    
    from .views import views
    from .auth import auth
    
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User
    
    with app.app_context():
        db.create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app


app = create_app()
db = SQLAlchemy(app)



def created_mail():
    app = Flask(__name__)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = "66070199@kmitl.ac.th"
    app.config['MAIL_PASSWORD'] = 'pL1brewtsa'
    mail = Mail(app)
    
    return mail


# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app = app)
#         print('Created Database !!')
