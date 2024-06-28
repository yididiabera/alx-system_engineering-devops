#!/usr/bin/pup
# Installs an especific version of flask
package {'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
