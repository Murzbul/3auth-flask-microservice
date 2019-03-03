from db import db
import datetime

class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(612), nullable=False, unique=True)
    email = db.Column(db.String(244), nullable=False, unique=True)
    last_login = db.Column(db.DateTime, nullable=False)
    expired = db.Column(db.DateTime, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)

    def __init__(self, token, email, last_login, expired):
        self.token = token
        self.email = email
        self.last_login = last_login
        self.expired = expired

    @classmethod
    def find_by_token(cls, token):
        return cls.query.filter_by(token=token).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
