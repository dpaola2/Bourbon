from sqlalchemy import *
from migrate import *

meta = MetaData()

posts = Table(
    'posts', meta,
    Column('id', Integer, primary_key = True),
    Column('text', Text)
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    posts.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    posts.drop()
