from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, desc
from utils import hash_password as hashpw

db: SQLAlchemy = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    
    uid = db.Column(db.Integer, primary_key=True)

    profile = db.relationship('UserProfile', backref='users.uid')

    username = db.Column(db.String(16))
    email = db.Column(db.String(100))
    password = db.Column(db.String(500))
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='users.uid')

    def get_id(self):
        return self.uid

    def authenticate(self, doubted_password):
        return hashpw(doubted_password) == self.password
    
    def __str__(self):
        return "<User '%s'>" % self.username
    
    def to_dict(self):
        raw_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'password'}
        raw_dict['posts'] = [p.to_dict() for p in self.posts]
        return raw_dict


class Post(db.Model):
    __tablename__ = "posts"

    post_id = db.Column(db.Integer, primary_key=True)

    published_at = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)
    
    title = db.Column(db.String(100))
    content = db.Column(db.String(2000))
    
    def __str__(self):
        return "<Post '%s'>" % self.post_id
    
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class UserProfile(db.Model):
    __tablename__ = "user_profiles"

    user_id = db.Column(db.Integer, ForeignKey('users.uid'), primary_key=True)
    
    desc = db.Column(db.Text, default="The default profile description")
    pic = db.Column(db.String(200))
