sudo rm -rf /etc/nginx/sites-available/default
sudo cp -p ~/default /etc/nginx/sites-available/default
#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default.conf
sudo /etc/init.d/nginx restart
gunicorn -b 0.0.0.0:8080 -c hello.py hello:app
