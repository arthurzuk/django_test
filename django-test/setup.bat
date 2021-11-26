pip install -r requirements.txt

python manage.py migrate
python manage.py ensure_adminuser --username=admin --email=admin@example.com --password=admin
python manage.py runserver