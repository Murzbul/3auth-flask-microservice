import logging

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)

from config.config import dictConfig, string_config

from resources.user import UserResource
from resources.session import SessionResource

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = string_config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jwt-secret-string'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

api = Api(app)

jwt = JWTManager(app)

api.add_resource(UserResource, '/user')
api.add_resource(SessionResource, '/session')

# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
# @app.route('/protected', methods=['GET'])
# @jwt_required
# def protected():
#     # Access the identity of the current user with get_jwt_identity
#
#     # current_user = get_jwt_identity()
#     # return jsonify(logged_in_as=current_user), 200
#
#     claims = get_jwt_claims()
#     return jsonify({
#         'hello_is': claims['hello'],
#         'foo_is': claims['foo']
#     }), 200ç¡''

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=5001, debug=True)
