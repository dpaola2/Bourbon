"""
Dave Paola
April 2012

"""
import os, stat
import exceptions
from constants import *

class Directory(object):
    def __init__(self, model_list):
        assert type(model_list) == list, "Argument must be a list of Bourbon models."
        self.model_list = model_list
    def readdir(self):
        return self.model_list
    def stat(self):
        return Stat.as_dir().as_dict()

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

class Stat(object):
    def __init__(self):    
        self.st_mode = 0
        self.st_ino = 0
        self.st_dev = 0
        self.st_nlink = 0
        self.st_uid = 0
        self.st_gid = 0
        self.st_size = 0
        self.st_atime = 0
        self.st_mtime = 0
        self.st_ctime = 0    

    @staticmethod
    def as_dir():
        st = Stat()
        st.st_mode = stat.S_IFDIR | 0755
        st.st_nlink = 2
        return st

    @staticmethod
    def as_file(size):
        st = Stat()
        st.st_mode = stat.S_IFREG | 0777
        st.st_nlink = 1
        st.st_size = size
        return st

    def as_dict(self):
        d = dict()
        keys = (
            'st_mode', 'st_ino', 'st_dev',
            'st_nlink', 'st_uid', 'st_gid',
            'st_size', 'st_atime', 'st_mtime',
            'st_ctime'
        )
        for key in keys:
            d[key] = getattr(self, key)
        return d

