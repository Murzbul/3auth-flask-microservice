import datetime
import logging

from db import db

# from sqlalchemy.orm import sessionmaker, relationship, backref


# from models.action import Action
# from models.role_action import RoleAction


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    cannonical_name = db.Column(db.String(45), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=True)
    enabled = db.Column(db.Boolean())
    created = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    updated = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)

    def __init__(self, name, cannonical_name, description):
        self.name = name
        self.cannonical_name = cannonical_name
        self.description = description
        self.enabled = 1

    def __repr__(self):
            return f'<Role {self.name}>'

    @classmethod
    def find_by_cannonical_name(cls, cannonical_name):
        return cls.query.filter_by(cannonical_name=cannonical_name).first()

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
