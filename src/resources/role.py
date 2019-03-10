import logging
import bcrypt
import datetime

from flask_jwt_extended import ( jwt_required, get_jwt_identity  )
from flask_restful import Resource
from flask import request

from models.role import Role
from validators.role import RoleValidator
from validators.role_update import RoleUpdateValidator
from helpers.messages.role_message import RoleMessage

class RoleResource(Resource):

    @jwt_required
    def post(self):

        roleMessage = RoleMessage()

        validator = RoleValidator()
        success = validator.validate(request.json)

        if not success:
            roleMessage.errors = validator.errors
            roleMessage.statusCode = 400
            roleMessage.send()

        name = request.json.get("name",None)
        cannonical_name = request.json.get("cannonical_name",None)
        description = request.json.get("description",None)

        success = validator.role_is_exist(cannonical_name)

        if success:
            roleMessage.errors = "A role with that cannonical_name already exists"
            roleMessage.statusCode = 400
            roleMessage.send()

        role = Role(name, cannonical_name, description)
        role.save()

        roleMessage.update(role)
        roleMessage.statusCode = 201
        roleMessage.success = True

        return roleMessage.send()

class RoleIdResource(Resource):

    @jwt_required
    def get(self, id):
        roleMessage = RoleMessage()

        role = Role.find_by_id(id)

        if not role:
            roleMessage.errors = "A role with that id doesn't exist"
            roleMessage.statusCode = 404
            roleMessage.send()

        roleMessage.update(role)
        roleMessage.statusCode = 200
        roleMessage.success = True

        return roleMessage.send()

    @jwt_required
    def put(self, id):
        roleMessage = RoleMessage()

        validator = RoleUpdateValidator()
        success = validator.validate(request.json)

        if not success:
            roleMessage.errors = validator.errors
            roleMessage.statusCode = 400
            roleMessage.send()

        if not request.json:
            roleMessage.errors = "Empty data"
            roleMessage.statusCode = 400
            roleMessage.send()

        role = Role.find_by_id(id)

        if not role:
            roleMessage.errors = "A role with that id doesn't exist"
            roleMessage.statusCode = 404
            roleMessage.send()

        name = request.json.get("name", role.name)
        cannonical_name = request.json.get("cannonical_name", role.cannonical_name)
        description = request.json.get("description", role.description)

        role.name = name
        role.cannonical_name = cannonical_name
        role.description = description
        role.update()

        roleMessage.update(role)
        roleMessage.statusCode = 200
        roleMessage.success = True

        return roleMessage.send()

    @jwt_required
    def delete(self, id):
        roleMessage = RoleMessage()

        role = Role.find_by_id(id)

        if not role:
            roleMessage.errors = "A role with that id doesn't exist"
            roleMessage.statusCode = 404
            roleMessage.send()

        roleMessage.update(role)
        roleMessage.statusCode = 200
        roleMessage.success = True

        role.delete()

        return roleMessage.send()

class RoleListResource(Resource):

    @jwt_required
    def get(self):
        roleMessage = RoleMessage()

        roles = Role.query.all()

        if not roles:
            roleMessage.errors = "It does not exist without role"
            roleMessage.statusCode = 404
            roleMessage.send()

        roleMessage.update_list(roles)
        roleMessage.statusCode = 200
        roleMessage.success = True

        return roleMessage.send()
