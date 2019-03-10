import logging
import bcrypt
import datetime

from flask_jwt_extended import ( jwt_required, get_jwt_identity  )
from flask_restful import Resource
from flask import request

from models.role_action import RoleAction
from models.user_role import UserRole
from models.role import Role
from models.action import Action
from models.user import User


from validators.role_action import RoleActionValidator
from validators.user_role import UserRoleValidator

from helpers.messages.role_action_message import RoleActionMessage
from helpers.messages.user_role_message import UserRoleMessage

class AssignActionToRoleResource(Resource):

    def post(arg):

        roleActionMessage = RoleActionMessage()

        validator = RoleActionValidator()
        success = validator.validate(request.json)

        roleActions = []

        if not success:
            roleActionMessage.errors = validator.errors
            roleActionMessage.statusCode = 400
            roleActionMessage.send()

        try:
            actions_id = request.json.get("action_id",None)
            roles_id = request.json.get("role_id",None)

            for role_id in roles_id:
                for action_id in actions_id:

                    action = Action.find_by_id(action_id)
                    role = Role.find_by_id(role_id)

                    roleAction = RoleAction.find_by_ids(role_id, action_id)

                    if action and role and roleAction == None:
                        roleAction = RoleAction( role, action )
                        roleAction.save()
                        roleActions.append(roleAction)

        except Exception as e:
            roleActionMessage.errors = str(e.orig) + ' - ' +  e.statement
            roleActionMessage.statusCode = 500
            roleActionMessage.send()

        if roleActions:
            roleActionMessage.update(roleActions)
            roleActionMessage.statusCode = 201
            roleActionMessage.success = True
        else:
            roleActionMessage.update(userRoles)
            roleActionMessage.statusCode = 400
            roleActionMessage.success = False

        return roleActionMessage.send()


class AssignRoleToUserResource(Resource):

    def post(arg):
        userRoleMessage = UserRoleMessage()

        validator = UserRoleValidator()
        success = validator.validate(request.json)

        userRoles = []

        if not success:
            userRoleMessage.errors = validator.errors
            userRoleMessage.statusCode = 400
            userRoleMessage.send()

        try:
            users_id = request.json.get("user_id",None)
            roles_id = request.json.get("role_id",None)

            for user_id in users_id:
                for role_id in roles_id:

                    user = User.find_by_id(user_id)
                    role = Role.find_by_id(role_id)

                    userRole = UserRole.find_by_ids(role_id, user_id)

                    if user and role and userRole == None:
                        userRole = UserRole( user, role )
                        userRole.save()
                        userRoles.append(userRole)

        except Exception as e:
            logging.info(e)
            userRoleMessage.errors = str(e.orig) + ' - ' +  e.statement
            userRoleMessage.statusCode = 500
            userRoleMessage.send()
            pass

        if userRoles:
            userRoleMessage.update(userRoles)
            userRoleMessage.statusCode = 201
            userRoleMessage.success = True
        else:
            userRoleMessage.update(userRoles)
            userRoleMessage.statusCode = 400
            userRoleMessage.success = False

        return userRoleMessage.send()
