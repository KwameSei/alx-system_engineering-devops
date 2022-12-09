# Killing process 'killmenow'

exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
  path     => '/usr/local/bin/:/bin/'
}
