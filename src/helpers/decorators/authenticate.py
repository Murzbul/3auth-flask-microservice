import logging

from flask import request, abort, jsonify
from flask_jwt_extended import ( jwt_required, get_jwt_identity  )

from functools import wraps

from models.action import Action
from models.user import User


def Authenticate(action):

    @jwt_required
    @wraps(action)
    def wrapper(*args, **kwargs):
        email = get_jwt_identity()
        user = User.find_by_email(email)
        success = Action.find_by_refer_action(request.url_rule)
        logging.info(user)

        if not success:
            abort(401, {"message":"No tiene authorization"})
        # logging.info(kwargss["action_name"])
        # logging.info(_kwgargs__class__.__name__)
        # url = request.url.strip('http://127.0.0.1:5001')
        # logging.info(request.url_root)
        # if url == "user":
        # abort(401, {"hola":"error"})
        # return action
        return action(*args, **kwargs)
    return wrapper
