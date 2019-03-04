from cerberus import Validator
import logging

from models.user import User

class UserValidator(Validator):
    '''
    User request validator
    '''
    def __init__(self, *args, **kwargs):
        default_schema = {
            'email': {'type': 'string', 'required': True, 'empty': False},
            'password': {'type': 'string', 'required': True, 'empty': False},
            'first_name': {'type': 'string', 'required': True, 'empty': False},
            'last_name': {'type': 'string', 'required': True, 'empty': False},
            'phone_number': {'type': 'string', 'required': True, 'empty': False},
            'date_of_birth': {'birth': True, 'required': True, 'empty': False}
        }
        kwargs['schema'] = kwargs.get('schema', default_schema)
        super(UserValidator, self).__init__(*args, **kwargs)

    def _validate_birth(self, birth, field, value):
            """
            The rule's arguments are validated against this schema:
            {'type': 'boolean'}
            """
            success = False
            values = value.split('-')
            message = 'Must be an valid date format: yyyy-mm-dd'

            if len(values) == 3:
                year = values[0]
                month = values[1]
                day = values[2]

                if (len(year) == 4) and (len(month) == 2) and (len(day) == 2):
                    year = int(year)
                    month = int(month)
                    day = int(day)

                    if year >= 1930 and ( month >= 1 and month <= 12) and (day >= 1 and day <= 31):
                        success = True

            if not success:
                self._error(field, message)

    def user_is_exist(self, email):
        success = False

        user = User.find_by_email(email)

        if user:
            success = True

        return success
