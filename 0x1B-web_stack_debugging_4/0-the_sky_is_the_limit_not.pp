# Puppet manifest to fix the Nginx issue

exec {'Increase Limits':
	provider => shell,
	command  => 'sudo sed -i "s/\"-n 15\"/\"-n 4096\"/" /etc/default/nginx'
}

exec {'restart':
	provider => shell,
	command  => 'sudo service nginx restart'
}
