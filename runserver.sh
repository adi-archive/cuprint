source printenv/bin/activate

nohup ./manage.py runworker &
nohup gunicorn -w 2 application:app &
