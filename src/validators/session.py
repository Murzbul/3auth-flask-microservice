from cerberus import Validator
import logging

class SessionValidator(Validator):
    '''
    Session request validator
    '''
    def __init__(self, *args, **kwargs):
        default_schema = {
            'token': {'type': 'string', 'required': True, 'empty': False},
            'email': {'type': 'string', 'required': True, 'empty': False},
            'last_login': {'type': 'string', 'required': True, 'empty': False},
            'expired': {'type': 'string', 'required': True, 'empty': False}
        }
        kwargs['schema'] = kwargs.get('schema', default_schema)
        super(SessionValidator, self).__init__(*args, **kwargs)
