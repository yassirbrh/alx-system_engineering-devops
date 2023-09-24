# Puppet manifest to change SSH configuration file.
file_line { 'No password' :
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => '#   PasswordAuthentication no',
    replace => true
}
file_line { 'Identity file for ssh' :
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => '#   IdentityFile ~/.ssh/school',
    replace => true
}
