#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
if ! dpkg -l | grep -q nginx; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
sudo echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx restart
exit 0
