from application import db, login_manager
from flask_login import UserMixin
<<<<<<< HEAD
import datetime
from datetime import datetime
=======
>>>>>>> 5c6991cbb528d1f245f7c02808de9252d8b2eced

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'User: ', self.first_name, ' ', self.last_name, '\r\n',
            'Title: ', self.title, '\r\n', self.content
            ])

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
<<<<<<< HEAD

    posts = db.relationship('Posts', backref='author', lazy=True)



    def __repr__(self):
        return ''.join([
            'UserID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])
        


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
=======
    
    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])
>>>>>>> 5c6991cbb528d1f245f7c02808de9252d8b2eced
