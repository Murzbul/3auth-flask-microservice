import logging
from datetime import datetime, timedelta

from flask_jwt_extended import ( jwt_required, create_access_token )
from flask_restful import Resource
from flask import request

from validators.session import SessionValidator
from validators.login import LoginValidator

from helpers.messages.type_message import FactoryTypeMessage
from helpers.messages.login_message import LoginMessage

from models.session import Session
from models.user import User

class SessionResource(Resource):

    def post(self):

        loginMessage = LoginMessage()

        validator = LoginValidator()
        success = validator.validate(request.json)

        email = request.json.get("email",None)
        password = request.json.get("password",None)

        if not success:
            loginMessage.errors = validator.errors
            loginMessage.statusCode = 400
            loginMessage.send()

        user = User.find_by_email(email)

        if not user:
            loginMessage.errors = 'User invalid'
            loginMessage.statusCode = 401
            loginMessage.send()

        success = validator.is_password_valid(password, user.password)

        if success and user.enabled:
            loginMessage.update(user)
            loginMessage.statusCode = 200
            loginMessage.success = True
        else:
            loginMessage.errors = 'Invalid credentials or user disabled'
            loginMessage.statusCode = 401
            loginMessage.send()

        # Identity can be any data that is json serializable
        time = timedelta(seconds=3600)
        expired = datetime.now() + time
        access_token = create_access_token(identity=user.email, expires_delta=time)
        last_login = None
        loginMessage.data.update({'access_token': access_token})

        old_session = Session.find_by_email(user.email)

        if old_session:
            last_login = old_session.created
            old_session.delete()

        session = Session(access_token, email, last_login, expired)
        session.save()

        return loginMessage.send()
