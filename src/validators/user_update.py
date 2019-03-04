import logging
import bcrypt

from cerberus import Validator

from models.user import User

class UserUpdateValidator(Validator):
    '''
    UserUpdate request validator
    '''
    def __init__(self, *args, **kwargs):
        default_schema = {
            'password': {'type': 'string', 'required': False, 'empty': False},
            'new_password': {'type': 'string', 'required': False, 'empty': False},
            're_new_password': {'type': 'string', 'required': False, 'empty': False},
            'first_name': {'type': 'string', 'required': False, 'empty': False},
            'last_name': {'type': 'string', 'required': False, 'empty': False},
            'phone_number': {'type': 'string', 'required': False, 'empty': False},
            'date_of_birth': {'birth': True, 'required': False, 'empty': False}
        }
        kwargs['schema'] = kwargs.get('schema', default_schema)
        super(UserUpdateValidator, self).__init__(*args, **kwargs)

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

    def is_password_valid(self, payload_password, encrypted_password):
        success = False

        if bcrypt.checkpw(payload_password.encode('utf8'), encrypted_password.encode('utf8')):
            success = True

        return success
