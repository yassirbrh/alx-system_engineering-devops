# Puppet manifest to fix the Nginx issue

exec {'fix--for-nginx':
	provider => shell,
	command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx'
}

exec {'restart':
	provider => shell,
	command  => 'sudo service nginx restart'
}
