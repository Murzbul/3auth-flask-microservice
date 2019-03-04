import logging
from abc import ABC, abstractmethod

from flask import abort, make_response, jsonify

class AbstractTypeMessage(ABC):

    @abstractmethod
    def send(self):
        pass

class TypeMessage200(AbstractTypeMessage):
    """docstring for TypeMessage200."""
    def __init__(self, message):
        self.message = message

    def send(self):
        return make_response(jsonify(self.message.message), 200)

class TypeMessage201(AbstractTypeMessage):
    """docstring for TypeMessage201."""
    def __init__(self, message):
        self.message = message

    def send(self):
        return make_response(jsonify(self.message.message), 201)

class TypeMessage400(AbstractTypeMessage):
    """docstring for TypeMessage400."""
    def __init__(self, message):
        self.message = message

    def send(self):
        return abort(400, self.message.errors)

class TypeMessage401(AbstractTypeMessage):
    """docstring for TypeMessage401."""
    def __init__(self, message):
        self.message = message

    def send(self):
        return abort(401, self.message.errors)

class TypeMessage404(AbstractTypeMessage):
    """docstring for TypeMessage404."""
    def __init__(self, message):
        self.message = message

    def send(self):
        return abort(404, self.message.errors)

class TypeMessage500(AbstractTypeMessage):
    """docstring for TypeMessage401."""
    def __init__(self, message):
        self.message = message

    def send(self):
        return abort(500, self.message.errors)

class FactoryTypeMessage(object):
    """docstring for FactoryTypeMessage."""

    @classmethod
    def create(cls, message):

        if message.statusCode == 200:
            typeMessage = TypeMessage200(message)

        elif message.statusCode == 201:
            typeMessage = TypeMessage201(message)

        elif message.statusCode == 400:
            typeMessage = TypeMessage400(message)

        elif message.statusCode == 401:
            typeMessage = TypeMessage401(message)

        elif message.statusCode == 404:
            typeMessage = TypeMessage404(message)

        elif message.statusCode == 500:
            typeMessage = TypeMessage401(message)

        return typeMessage
