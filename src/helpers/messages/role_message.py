import  logging

from helpers.messages.message import Message

class RoleMessage(Message):
    """docstring for RoleMessage."""
    def __init__(self):
        super(RoleMessage, self).__init__()

    def update(self, role):
        self.data.update({
            'id':role.id,
            'name':role.name,
            'cannonical_name':role.cannonical_name,
            'description':role.description,
            'created':str(role.created),
            'updated':str(role.updated)
        })

    def update_list(self, roles):
        self.data.update({'roles':[]})

        for role in roles:
            self.data['roles'].append({
                'id':role.id,
                'name':role.name,
                'cannonical_name':role.cannonical_name,
                'description':role.description,
                'created':str(role.created),
                'updated':str(role.updated)
            })
