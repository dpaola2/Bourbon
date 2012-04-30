#!/usr/bin/env python
from migrate.versioning.shell import main
import os

if __name__ == '__main__':
    main(debug='False', url=os.environ.get('HEROKU_SHARED_POSTGRESQL_IVORY_URL'), repository='migrations')
