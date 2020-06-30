virtualenv venv
source venv/bin/activate
pip install -r requirements-dev.txt
python manage.py migrate
python manage.py loaddata ./core/fixtures/preapproved.json
