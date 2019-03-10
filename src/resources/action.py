import logging
import bcrypt
import datetime

from flask_jwt_extended import ( jwt_required, get_jwt_identity  )
from flask_restful import Resource
from flask import request

from models.action import Action
from validators.action import ActionValidator
from validators.action_update import ActionUpdateValidator
from helpers.messages.action_message import ActionMessage

class ActionResource(Resource):

    @jwt_required
    def post(self):

        actionMessage = ActionMessage()

        validator = ActionValidator()
        success = validator.validate(request.json)

        if not success:
            actionMessage.errors = validator.errors
            actionMessage.statusCode = 400
            actionMessage.send()

        name = request.json.get("name",None)
        refer_action = request.json.get("refer_action",None)

        success = validator.action_is_exist(refer_action)

        if success:
            actionMessage.errors = "A action with that refer_action already exists"
            actionMessage.statusCode = 400
            actionMessage.send()

        action = Action(name, refer_action)
        action.save()

        actionMessage.update(action)
        actionMessage.statusCode = 201
        actionMessage.success = True

        return actionMessage.send()

class ActionIdResource(Resource):

    @jwt_required
    def get(self, id):
        actionMessage = ActionMessage()

        action = Action.find_by_id(id)

        if not action:
            actionMessage.errors = "A action with that id doesn't exist"
            actionMessage.statusCode = 404
            actionMessage.send()

        actionMessage.update(action)
        actionMessage.statusCode = 200
        actionMessage.success = True

        return actionMessage.send()

    @jwt_required
    def put(self, id):
        actionMessage = ActionMessage()

        validator = ActionUpdateValidator()
        success = validator.validate(request.json)

        if not success:
            actionMessage.errors = validator.errors
            actionMessage.statusCode = 400
            actionMessage.send()

        if not request.json:
            actionMessage.errors = "Empty data"
            actionMessage.statusCode = 400
            actionMessage.send()

        action = Action.find_by_id(id)

        if not action:
            actionMessage.errors = "A action with that id doesn't exist"
            actionMessage.statusCode = 404
            actionMessage.send()

        name = request.json.get("name", action.name)
        refer_action = request.json.get("refer_action", action.refer_action)

        action.name = name
        action.refer_action = refer_action
        action.update()

        actionMessage.update(action)
        actionMessage.statusCode = 200
        actionMessage.success = True

        return actionMessage.send()

    @jwt_required
    def delete(self, id):
        actionMessage = ActionMessage()

        action = Action.find_by_id(id)

        if not action:
            actionMessage.errors = "A action with that id doesn't exist"
            actionMessage.statusCode = 404
            actionMessage.send()

        actionMessage.update(action)
        actionMessage.statusCode = 200
        actionMessage.success = True

        action.delete()

        return actionMessage.send()

class ActionListResource(Resource):

    @jwt_required
    def get(self):
        actionMessage = ActionMessage()

        actions = Action.query.all()

        if not actions:
            actionMessage.errors = "It does not exist without action"
            actionMessage.statusCode = 404
            actionMessage.send()

        actionMessage.update_list(actions)
        actionMessage.statusCode = 200
        actionMessage.success = True

        return actionMessage.send()
