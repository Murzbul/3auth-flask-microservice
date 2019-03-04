import logging
import bcrypt

from cerberus import Validator

from models.user import User

class LoginValidator(Validator):
    '''
    Login validator
    '''
    def __init__(self, *args, **kwargs):
        default_schema = {
            'email': {'type': 'string', 'required': True, 'empty': False},
            'password': {'type': 'string', 'required': True, 'empty': False}
        }
        kwargs['schema'] = kwargs.get('schema', default_schema)
        super(LoginValidator, self).__init__(*args, **kwargs)

    def is_password_valid(self, payload_password, encrypted_password):
        success = False

        if bcrypt.checkpw(payload_password.encode('utf8'), encrypted_password.encode('utf8')):
            success = True

        return success
