import logging

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)

from config.config import dictConfig, string_config_db

from resources.user import UserResource, UserIdResource, UserListResource
from resources.role import RoleResource, RoleIdResource, RoleListResource
from resources.action import ActionResource, ActionIdResource, ActionListResource
from resources.assign import AssignActionToRoleResource, AssignRoleToUserResource
from resources.session import SessionResource

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = string_config_db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 20
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 5
app.config['SQLALCHEMY_POOL_RECYCLE'] = 1500
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jwt-secret-string'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

api = Api(app)

jwt = JWTManager(app)

api.add_resource(SessionResource, '/session')

api.add_resource(UserResource, '/user')
api.add_resource(UserIdResource, '/user/<int:id>')
api.add_resource(UserListResource, '/users')

api.add_resource(RoleResource, '/role')
api.add_resource(RoleIdResource, '/role/<int:id>')
api.add_resource(RoleListResource, '/roles')

api.add_resource(ActionResource, '/action')
api.add_resource(ActionIdResource, '/action/<int:id>')
api.add_resource(ActionListResource, '/actions')

api.add_resource(AssignActionToRoleResource, '/assign_action_role')
api.add_resource(AssignRoleToUserResource, '/assign_role_user')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=5001, debug=True)
