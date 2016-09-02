#!/bin/bash
cd /var/www/www.lichess4545.com/
export PYTHONPATH=/var/www/www.lichess4545.com/
/var/www/www.lichess4545.com/env/bin/gunicorn --capture-output --error-logfile /var/log/heltour/error-api.log -t 60 -w 2 -b 127.0.0.1:8880  heltour.live_api_wsgi:application

