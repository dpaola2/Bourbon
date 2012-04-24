all: virtualenv install

virtualenv:
	virtualenv --no-site-packages .

install:
	source bin/activate && pip install -r requirements.txt

serve:
	source bin/activate && foreman start -p 5000

deploy:
	git push heroku master