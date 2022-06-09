from app import *

class UserData(db.Model):
    token = db.Column(db.String, unique=True, primary_key=True)
    username=db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    api_key = db.Column(db.String, default=True)
    api_count = db.Column(db.Integer, default=0)
    name = db.Column(db.String, default="User")
    country = db.Column(db.String)
    def __repr__(self):
        return f'<UserData {self.username}>'


class Shorten_Links(db.Model):
    shorten_link = db.Column(db.String, unique=True, primary_key=True)
    destination_link = db.Column(db.String, nullable=False)
    user_token = db.Column(db.String, nullable=False)
    click_count = db.Column(db.Integer, default = 0 , nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    def __repr__(self):
        return f'<Shorten_Links {self.link}>'

db.create_all()
# db.drop_all()