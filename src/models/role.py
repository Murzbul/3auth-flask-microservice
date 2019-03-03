from db import db
import datetime

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    cannonical_name = db.Column(db.String(45), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    enabled = db.Column(db.Boolean())
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __init__(self, name, cannonical_name, description):
        self.name = name
        self.cannonical_name = cannonical_name
        self.description = description
        self.enabled = 1

    @classmethod
    def find_by_name(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_cannonical_name(cls, cannonical_name):
        return cls.query.filter_by(cannonical_name=cannonical_name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
