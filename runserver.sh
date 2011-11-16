source printenv/bin/activate

./manage.py runworker &
gunicorn -w 2 application:app &
