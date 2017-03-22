<?php

/////////////////////////////////////////////////////////////////////////////
// General information
/////////////////////////////////////////////////////////////////////////////

$app['basename'] = 'kibana_plugin';
$app['version'] = '1.0.1';
$app['release'] = '1';
$app['vendor'] = 'WikiSuite';
$app['packager'] = 'eGloo';
$app['license'] = 'GPLv3';
$app['license_core'] = 'LGPLv3';
$app['description'] = lang('kibana_plugin_app_description');

/////////////////////////////////////////////////////////////////////////////
// App name and categories
/////////////////////////////////////////////////////////////////////////////

$app['name'] = lang('kibana_plugin_app_name');
$app['category'] = lang('base_category_server');
$app['subcategory'] = lang('base_subcategory_directory');
$app['menu_enabled'] = FALSE;

/////////////////////////////////////////////////////////////////////////////
// Packaging
/////////////////////////////////////////////////////////////////////////////

$app['core_only'] = TRUE;

$app['core_requires'] = array(
    'app-accounts-core', 
);

$app['core_file_manifest'] = array( 
   'kibana.php' => array(
        'target' => '/var/clearos/accounts/plugins/kibana.php'
   ),
);

$app['delete_dependency'] = array();
