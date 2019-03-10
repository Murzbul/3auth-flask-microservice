from cerberus import Validator
import logging

class ActionUpdateValidator(Validator):
    '''
    User request validator
    '''
    def __init__(self, *args, **kwargs):
        default_schema = {
            'name': {'type': 'string', 'required': False, 'empty': False},
            'refer_action': {'type': 'string', 'required': False, 'empty': False}
        }
        kwargs['schema'] = kwargs.get('schema', default_schema)
        super(ActionUpdateValidator, self).__init__(*args, **kwargs)
