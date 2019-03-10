import datetime
import logging

from db import db

from sqlalchemy.orm import sessionmaker, relationship, backref

# from models.role import Role
# from models.role_action import RoleAction

class Action(db.Model):
    __tablename__ = 'actions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    refer_action = db.Column(db.String(255), nullable=False)
    enabled = db.Column(db.Boolean())
    created = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    updated = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)

    # roles = db.relationship("Role", secondary="RoleAction", viewonly=True)

    def __init__(self, name, refer_action):
        self.name = name
        self.refer_action = refer_action
        self.enabled = 1

    def __repr__(self):
        return f'<Action {self.name}>'

    @classmethod
    def find_by_name(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_refer_action(cls, refer_action):
        return cls.query.filter_by(refer_action=refer_action).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.updated = datetime.datetime.now()
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
