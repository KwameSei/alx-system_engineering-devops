# Creating a puppet file in /tmp
file { 'random file':
  path    => '/tmp/school',
  mode    => '0744',
  owner   => www-data,
  group   => www-data,
  content => 'I love Puppet'
}
