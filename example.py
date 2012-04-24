"""
Dave Paola
April, 2012

Just a sample of what a model might look like
with the intention of mapping it to a POSIX-compliant
filesystem.

"""
import bourbon

class Post(bourbon.Model):
    def read(self):
        return self.data

    def write(self, data):
        self.data = data
        self._save()
        return self.data

    def getattr(self):
        return bourbon.FILE

routes = (
    ('/', bourbon.Namespace(None)),
    ('/posts', bourbon.Namespace(Post)),
)
