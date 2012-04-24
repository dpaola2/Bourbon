"""
Dave Paola
April, 2012

Just a sample of what a model might look like
with the intention of mapping it to a POSIX-compliant
filesystem.

"""
import bourbon
from models import Post as PostModel, Session


class Post(bourbon.ModelInterface):
    @staticmethod
    def all():
        sess = Session()
        return [post.id for post in sess.query(PostModel).all()]
    
    @staticmethod
    def open(identifier):
        self = Post()
        self.sess = Session()
        self.post = self.sess.query(PostModel).filter_by(id=identifier).scalar()
        if self.post is None:
           self.post = PostModel()
        return self

    @staticmethod
    def stat(identifier):
        post = Post.open(identifier)
        return bourbon.Stat.as_file(len(post.read())).as_dict()

    def close(self):
        self.sess.add(self.post)
        self.sess.commit()
        del self.sess
        del self.post
        return True
    
    def read(self):
        return self.post.text

    def write(self, data):
        self.post.text = data
        
    def getattr(self):
        return bourbon.FILE

root = bourbon.Directory(['posts'])
posts = bourbon.Directory(Post.all())

