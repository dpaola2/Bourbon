DATABASE_NAME = bourbon
DATABASE_URL=postgresql://admin@localhost/$(DATABASE_NAME)
ACTIVATE = source bin/activate
ENV = DATABASE_URL=$(DATABASE_URL)
MIGRATE_PATH = migrations/manage.py
all: virtualenv install

virtualenv:
	virtualenv --no-site-packages .

install:
	$(ACTIVATE) && pip install -r requirements.txt

serve:
	$(ACTIVATE) && $(ENV) foreman start -p 5000

shell:
	$(ACTIVATE) && $(ENV) ipython

deploy:
	git push heroku master

database:
	createdb bourbon

clean:
	rm -rf bin build lib include man
	dropdb bourbon

freeze:
	$(ACTIVATE) && pip freeze > requirements.txt

migrate:
	$(ACTIVATE) && $(ENV) $(MIGRATE_PATH) upgrade

add_version_control:
	$(ACTIVATE) && $(ENV) $(MIGRATE_PATH) version_control

version:
	$(ACTIVATE) && $(ENV) $(MIGRATE_PATH) version

testmigrate:
	$(ACTIVATE) && $(ENV) $(MIGRATE_PATH) test

dbversion:
	$(ACTIVATE) && $(ENV) $(MIGRATE_PATH) db_version