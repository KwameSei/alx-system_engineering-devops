# Fixing apache 500 response error
# Changing phpp in apache to php

exec { 'fix-phpp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/';
}
