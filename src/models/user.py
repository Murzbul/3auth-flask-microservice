from db import db
import datetime
import bcrypt

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication fields
    email = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    # User fields
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    date_of_birth = db.Column(db.Date(), nullable=False)
    google_auth_ref = db.Column(db.String(50), nullable=False)
    enabled = db.Column(db.Boolean())
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __init__(self, email, password, first_name, last_name, phone_number, date_of_birth, google_auth_ref):
        self.email = email
        self.password = bcrypt.hashpw(password, bcrypt.gensalt())
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.google_auth_ref = google_auth_ref
        self.enabled = 1

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
