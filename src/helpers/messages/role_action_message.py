import  logging

from helpers.messages.message import Message

class RoleActionMessage(Message):
    """docstring for RoleActionMessage."""
    def __init__(self):
        super(RoleActionMessage, self).__init__()

    def update(self, roleActions):
        if roleActions:
            self.data.update({'roleActions':[]})

            for roleAction in roleActions:
                self.data["roleActions"].append({
                    'message': f'Action {roleAction.action.name} has set in Role {roleAction.role.name}'
                })
        else:
            self.data.update({
                'message': f'There is no action to assign a role'
            })
