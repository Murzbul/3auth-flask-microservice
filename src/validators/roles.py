from cerberus import Validator
import logging

class Uservalidator(Validator):
    '''
    User request validator
    '''
    def __init__(self, *args, **kwargs):
        default_schema = {
            'email': {'type': 'string', 'required': True, 'empty': False},
            'password': {'type': 'string', 'required': True, 'empty': False}
        }
        kwargs['schema'] = kwargs.get('schema', default_schema)
        super(Uservalidator, self).__init__(*args, **kwargs)
