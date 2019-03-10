from cerberus import Validator
import logging

from models.role import Role

class RoleValidator(Validator):
    '''
    Role request validator
    '''
    def __init__(self, *args, **kwargs):
        default_schema = {
            'name': {'type': 'string', 'required': True, 'empty': False},
            'cannonical_name': {'type': 'string', 'required': True, 'empty': False},
            'description': {'type': 'string', 'required': False, 'empty': False}
        }
        kwargs['schema'] = kwargs.get('schema', default_schema)
        super(RoleValidator, self).__init__(*args, **kwargs)

    def role_is_exist(self, cannonical_name):
        success = False

        role = Role.find_by_cannonical_name(cannonical_name)

        if role:
            success = True

        return success
