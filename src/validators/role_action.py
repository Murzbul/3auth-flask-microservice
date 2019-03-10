from cerberus import Validator
import logging

class RoleActionValidator(Validator):
    '''
    Role has action request validator
    '''
    def __init__(self, *args, **kwargs):
        default_schema = {
            'role_id': {'type': 'list', 'schema': {'type': 'integer'}, 'required': True, 'empty': False},
            'action_id': {'type': 'list', 'schema': {'type': 'integer'}, 'required': True, 'empty': False}
        }
        kwargs['schema'] = kwargs.get('schema', default_schema)
        super(RoleActionValidator, self).__init__(*args, **kwargs)
