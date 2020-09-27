#!/usr/bin/env bash
cd ~/
#mkdir -p web
#cd web && mkdir -p uploads public etc
#cd public && mkdir -p js css img && cd ..

sudo rm /etc/nginx/sites-available/default
sudo cp -p ~/web/etc/default /etc/nginx/sites-available/default
#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default.conf
sudo /etc/init.d/nginx restart
gunicorn -c ~/web/etc/gunicorn-django.conf ask.wsgi:application

