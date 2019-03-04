import  logging

from helpers.messages.message import Message

class UserMessage(Message):
    """docstring for UserMessage."""
    def __init__(self):
        super(UserMessage, self).__init__()

    def update(self, user):
        self.data.update({
            'id':user.id,
            'email':user.email,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'phone_number':user.phone_number,
            'date_of_birth':str(user.date_of_birth),
            'created':str(user.created),
            'updated':str(user.updated)
        })

    def update_list(self, users):
        self.data.update({'users':[]})

        for user in users:
            self.data['users'].append({
                'id':user.id,
                'email':user.email,
                'first_name':user.first_name,
                'last_name':user.last_name,
                'phone_number':user.phone_number,
                'date_of_birth':str(user.date_of_birth),
                'created':str(user.created),
                'updated':str(user.updated)
            })
