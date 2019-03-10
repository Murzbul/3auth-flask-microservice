import  logging

from helpers.messages.message import Message

class UserRoleMessage(Message):
    """docstring for UserRoleMessage."""
    def __init__(self):
        super(UserRoleMessage, self).__init__()

    def update(self, userRoles):
        if userRoles:
            self.data.update({'userRoles':[]})

            for userRole in userRoles:
                self.data["userRoles"].append({
                'message': f'Role {userRole.role.name} has set in User {userRole.user.email}'
                })
        else:
            self.data.update({
            'message': f'There is no role to assign a user'
            })
