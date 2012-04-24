"""
Dave Paola
April 2012

"""
import exceptions
from constants import *

class Namespace(object):
    def __init__(self, model):
        self.model = model
    def getattr(self):
        return DIRECTORY
    def readdir(self):
        return self.model.all()

class ModelInterface(object):
    @staticmethod
    def all():
        raise exceptions.NotAllowed
    def read(self):
        raise exceptions.NotAllowed
    def write(self):
        raise exceptions.NotAllowed
    def getattr(self):
        raise exceptions.NotAllowed
    def readdir(self):
        raise exceptions.NotAllowed

