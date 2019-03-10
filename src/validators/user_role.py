from cerberus import Validator
import logging

class UserRoleValidator(Validator):
    '''
    User has role request validator
    '''
    def __init__(self, *args, **kwargs):
        default_schema = {
            'user_id': {'type': 'list', 'schema': {'type': 'integer'}, 'required': True, 'empty': False},
            'role_id': {'type': 'list', 'schema': {'type': 'integer'}, 'required': True, 'empty': False}
        }
        kwargs['schema'] = kwargs.get('schema', default_schema)
        super(UserRoleValidator, self).__init__(*args, **kwargs)
