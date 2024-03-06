# Fix 500 error when a GET HTTP method is requested to Apache web server

file_line { 'fix_wp_settings_php':
  path    => '/var/www/html/wp-settings.php',
  line    => 'require_once( ABSPATH . WPINC . '/class-wp-locale.php' );',
  match   => '^require_once\( ABSPATH \. WPINC \. \'\/class-wp-locale\.phpp\' \);',
  replace => 'require_once( ABSPATH . WPINC . '/class-wp-locale.php' );',
}
