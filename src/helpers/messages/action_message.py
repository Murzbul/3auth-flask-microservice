import  logging

from helpers.messages.message import Message

class ActionMessage(Message):
    """docstring for ActionMessage."""
    def __init__(self):
        super(ActionMessage, self).__init__()

    def update(self, role):
        self.data.update({
            'id':role.id,
            'name':role.name,
            'refer_action':role.refer_action,
            'created':str(role.created),
            'updated':str(role.updated)
        })

    def update_list(self, roles):
        self.data.update({'roles':[]})

        for role in roles:
            self.data['roles'].append({
                'id':role.id,
                'name':role.name,
                'refer_action':role.refer_action,
                'created':str(role.created),
                'updated':str(role.updated)
            })
