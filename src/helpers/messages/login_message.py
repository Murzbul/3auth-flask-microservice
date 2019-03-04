from helpers.messages.message import Message

class LoginMessage(Message):
    """docstring for LoginMessage."""
    def __init__(self):
        super(LoginMessage, self).__init__()

    def update(self, user):
        self.data.update({'email':user.email})
