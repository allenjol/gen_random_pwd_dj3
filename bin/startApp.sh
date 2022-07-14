#!/bin/bash
# *****************************
# * Author: Allen_Jol
# * Date  : 2022/07/12 12:45:05
# *****************************

uwsgi --ini /data/bin/uwsgi.ini
nginx -c /etc/nginx/opssite.conf -g 'daemon off;'
