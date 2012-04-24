"""
Dave Paola
April 2012

"""
import exceptions, constants

class Namespace(object):
    def __init__(self, model):
        self.model = model
    def getattr(self):
        return DIRECTORY
    def readdir(self):
        return self.model.all()

class Model(object):
    def read(self):
        raise exceptions.NotAllowed
    def write(self):
        raise exceptions.NotAllowed
    def getattr(self):
        raise exceptions.NotAllowed
    def readdir(self):
        raise exceptions.NotAllowed

