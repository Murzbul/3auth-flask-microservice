import datetime
import logging

from db import db


class RoleAction(db.Model):
    __tablename__ = 'roles_has_actions'
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)
    action_id = db.Column(db.Integer, db.ForeignKey('actions.id'), primary_key=True)

    role = db.relationship("Role", backref=db.backref("RoleAction", cascade="all, delete-orphan" ))
    action = db.relationship("Action", backref=db.backref("RoleAction", cascade="all, delete-orphan" ))

    def __init__(self, role=None, action=None):
        self.role = role
        self.action =  action

    def __repr__(self):
        return f'<RoleAction {self.role.name} - {self.action.name}>'

    @classmethod
    def find_by_ids(cls, role_id, action_id):
        return cls.query.filter_by(role_id=role_id, action_id=action_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
