from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


class Players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(30), nullable=False)
    player_age = db.Column(db.Integer, nullable=False)
    player_team = db.Column(db.String(30), nullable=False)
    id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    player_stat = db.relationship('Stats', backref='stat', lazy=True)
  

    def __repr__(self):
        return ''.join([
            'Player: ', self.player_name, ' ', '\r\n',
            'Team: ', self.player_team, '\r\n'
            ])

class Stats(db.Model):

    stat_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer,db.ForeignKey('players.player_id'), nullable=False)
    goals = db.Column(db.Integer, nullable=False, default=0)
    assists = db.Column(db.Integer, nullable=False, default=0)
    chances = db.Column(db.Integer, nullable=False, default=0)
    shots = db.Column(db.Integer, nullable=False, default=0)
    minutes = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    
    def __repr__(self):
        return ''.join(['Player: ', str(Players.player_name), '\r\n', 'Date: ', str(self.date)])

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    player = db.relationship('Players', backref='author', lazy=True)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])