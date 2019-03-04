import logging
from helpers.messages.type_message import FactoryTypeMessage
from flask import abort, make_response, jsonify

class Message(object):

    def __init__(self):
        self._message = None
        self._data = {}
        self._success = False
        self._errors = ''
        self._statusCode = None

    @property
    def data(self):
        return self._data

    @property
    def success(self):
        return self._success

    @property
    def errors(self):
        return self._errors

    @property
    def statusCode(self):
        return self._statusCode

    @property
    def message(self):
        return self._message

    @data.setter
    def data(self, value):
        self._data = value

    @success.setter
    def success(self, value):
        self._success = value

    @errors.setter
    def errors(self, value):
        self._errors = value

    @errors.setter
    def errors(self, value):
        self._errors = value

    @statusCode.setter
    def statusCode(self, value):
        self._statusCode = value

    def send(self):
        self._message = {
            'success': self._success,
            'data': self._data,
            'errors': self._errors,
            'status_code': self._statusCode
        }

        typeMessage = FactoryTypeMessage().create(self)
        return typeMessage.send()

    def update(self):
        pass
