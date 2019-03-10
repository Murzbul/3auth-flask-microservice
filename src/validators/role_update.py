from cerberus import Validator
import logging

class RoleUpdateValidator(Validator):
    '''
    Role request validator
    '''
    def __init__(self, *args, **kwargs):
        default_schema = {
            'name': {'type': 'string', 'required': False, 'empty': False},
            'cannonical_name': {'type': 'string', 'required': False, 'empty': False},
            'description': {'type': 'string', 'required': False, 'empty': False}
        }
        kwargs['schema'] = kwargs.get('schema', default_schema)
        super(RoleUpdateValidator, self).__init__(*args, **kwargs)
