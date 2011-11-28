source printenv/bin/activate

for pidfile in pid/*.pid; do
  pid=`cat $pidfile`
  kill $pid
  rm $pidfile
done

# wait two seconds for processes to finish
sleep 2

nohup soffice -headless -accept="socket,port=2002;urp" -nofirststartwizard &
echo $! > pid/soffice.pid
nohup ./manage.py runworker &
echo $! > pid/worker.pid
nohup gunicorn -w 2 application:app &
echo $! > pid/gunicorn.pid
