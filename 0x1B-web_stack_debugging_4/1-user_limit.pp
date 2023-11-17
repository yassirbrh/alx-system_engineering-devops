#Manifest to configure the OS to increase the number of the files opened

exec {'change-os-configuration-for-holberton-user':
    provider => shell,
    command  => 'sudo sed -i "s/nofile 4/nofile 4000/" /etc/security/limits.conf'
    after    => Exec['change-os-configuration-for-holberton-user-2']
}

exec {'change-os-configuration-for-holberton-user-2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
