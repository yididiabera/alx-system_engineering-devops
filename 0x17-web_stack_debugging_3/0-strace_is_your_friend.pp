# Replaces "phpp with "php" in the file "var/www/html/wp-settings.php"

exec {'fix-wordpress':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
    path    => ['/bin', '/usr/bin'],
}
