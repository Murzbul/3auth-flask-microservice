import logging
import bcrypt
import datetime

from flask_jwt_extended import ( jwt_required, get_jwt_identity  )
from flask_restful import Resource
from flask import request, Flask

from models.user import User

from validators.user import UserValidator
from validators.user_update import UserUpdateValidator

from helpers.messages.user_message import UserMessage
from helpers.decorators.authenticate import Authenticate

class UserResource(Resource):

    @jwt_required
    def post(self):

        userMessage = UserMessage()

        validator = UserValidator()
        success = validator.validate(request.json)

        if not success:
            userMessage.errors = validator.errors
            userMessage.statusCode = 400
            userMessage.send()

        email = request.json.get("email",None)
        password = request.json.get("password",None)
        first_name = request.json.get("first_name",None)
        last_name = request.json.get("last_name",None)
        phone_number = request.json.get("phone_number",None)
        date_of_birth = request.json.get("date_of_birth",None)

        success = validator.user_is_exist(email)

        if success:
            userMessage.errors = "A user with that email already exists"
            userMessage.statusCode = 400
            userMessage.send()

        user = User(email, password, first_name, last_name, phone_number, date_of_birth)
        user.save()

        userMessage.update(user)
        userMessage.statusCode = 201
        userMessage.success = True

        return userMessage.send()

class UserIdResource(Resource):

    @jwt_required
    def get(self, id):
        # For filter and pagination functionality
        # searchword = request.args.get('id', '')

        userMessage = UserMessage()

        user = User.find_by_id(id)

        if not user:
            userMessage.errors = "A user with that id doesn't exist"
            userMessage.statusCode = 404
            userMessage.send()

        userMessage.update(user)
        userMessage.statusCode = 200
        userMessage.success = True

        return userMessage.send()

    @jwt_required
    def put(self, id):
        userMessage = UserMessage()

        validator = UserUpdateValidator()
        success = validator.validate(request.json)

        if not success:
            userMessage.errors = validator.errors
            userMessage.statusCode = 400
            userMessage.send()

        if not request.json:
            userMessage.errors = "Empty data"
            userMessage.statusCode = 400
            userMessage.send()

        user = User.find_by_id(id)

        if not user:
            userMessage.errors = "A user with that id doesn't exist"
            userMessage.statusCode = 404
            userMessage.send()

        password = request.json.get("password", None)
        new_password = request.json.get("new_password", None)
        re_new_password = request.json.get("re_new_password", None)

        if password:
            if (new_password == re_new_password) and (type(new_password) == str):
                success = validator.is_password_valid(password, user.password )
                if success:
                    user.password = bcrypt.hashpw(new_password.encode('utf8'), bcrypt.gensalt())
                else:
                    userMessage.errors = "The passwords it's invalid"
                    userMessage.statusCode = 400
                    userMessage.send()
            else:
                userMessage.errors = "The passwords it's not equal"
                userMessage.statusCode = 400
                userMessage.send()

        first_name = request.json.get("first_name",user.first_name)
        last_name = request.json.get("last_name",user.last_name)
        phone_number = request.json.get("phone_number",user.phone_number)
        date_of_birth = request.json.get("date_of_birth",user.date_of_birth)

        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.date_of_birth = date_of_birth
        user.update()

        userMessage.update(user)
        userMessage.statusCode = 200
        userMessage.success = True

        return userMessage.send()

    @jwt_required
    def delete(self, id):
        userMessage = UserMessage()

        user = User.find_by_id(id)

        if not user:
            userMessage.errors = "A user with that id doesn't exist"
            userMessage.statusCode = 404
            userMessage.send()

        userMessage.update(user)
        userMessage.statusCode = 200
        userMessage.success = True

        user.delete()

        return userMessage.send()

class UserListResource(Resource):

    @jwt_required
    def get(self):
        userMessage = UserMessage()

        users = User.query.all()

        if not users:
            userMessage.errors = "It does not exist without user"
            userMessage.statusCode = 404
            userMessage.send()

        userMessage.update_list(users)
        userMessage.statusCode = 200
        userMessage.success = True
        return userMessage.send()
