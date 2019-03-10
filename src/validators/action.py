import logging

from cerberus import Validator

from models.action import Action


class ActionValidator(Validator):
    '''
    User request validator
    '''
    def __init__(self, *args, **kwargs):
        default_schema = {
            'name': {'type': 'string', 'required': True, 'empty': False},
            'refer_action': {'type': 'string', 'required': True, 'empty': False}
        }
        kwargs['schema'] = kwargs.get('schema', default_schema)
        super(ActionValidator, self).__init__(*args, **kwargs)

    def action_is_exist(self, refer_action):
        success = False

        action = Action.find_by_refer_action(refer_action)

        if action:
            success = True

        return success
