bind = "0.0.0.0:80"
workers = 16
accesslog = "/var/log/gunicorn.access.log"
errorlog = "/var/log/gunicorn.error.log"
capture_output = True
loglevel = "info"
