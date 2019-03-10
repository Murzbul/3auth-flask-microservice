import datetime
import logging

from db import db


class UserRole(db.Model):
    __tablename__ = 'users_has_roles'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)

    user = db.relationship("User", backref=db.backref("UserRole", cascade="all, delete-orphan" ))
    role = db.relationship("Role", backref=db.backref("UserRole", cascade="all, delete-orphan" ))

    def __init__(self, user=None, role=None):
        self.user = user
        self.role =  role

    def __repr__(self):
        return f'<UserRole {self.user.name} - {self.role.name}>'

    @classmethod
    def find_by_ids(cls, user_id, role_id):
        return cls.query.filter_by(user_id=user_id, role_id=role_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
