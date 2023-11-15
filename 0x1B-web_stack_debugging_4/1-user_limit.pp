#Manifest to configure the OS to increase the number of the files opened

exec {'Increase Limits':
     provider => shell,
     command  => 'sudo sed -i "s/nofile 4/nofile 4000/" /etc/security/limits.conf && sudo sed -i "s/nofile 5/nofile 5000/" /etc/security/limits.conf'
}
