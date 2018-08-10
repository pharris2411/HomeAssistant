#/usr/local/bin/bash

trap "kill 0" EXIT

cd /home/.homeassistant/certs

python2.7 -m SimpleHTTPServer 8000 &

certbot renew --webroot -w /home/.homeassistant/certs

