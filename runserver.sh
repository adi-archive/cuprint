source printenv/bin/activate

nohup unoconv -l &
echo $! > pid/unoconv.pid
nohup ./manage.py runworker &
echo $! > pid/worker.pid
nohup gunicorn -w 2 application:app &
echo $! > pid/gunicorn.pid
