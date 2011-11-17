source printenv/bin/activate

nohup unoconv -l &
nohup ./manage.py runworker &
nohup gunicorn -w 2 application:app &
