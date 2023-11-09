# Fixing the issue in wordpress website
exec { 'Fix Wordpress Issue':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
