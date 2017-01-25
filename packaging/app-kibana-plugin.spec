
Name: app-kibana-plugin
Epoch: 1
Version: 1.0.0
Release: 1%{dist}
Summary: Kibana Policies - Core
License: LGPLv3
Group: ClearOS/Libraries
Packager: eGloo
Vendor: Marc Laporte
Source: app-kibana-plugin-%{version}.tar.gz
Buildarch: noarch

%description
Kibana Policies provide access control for the Kibana app.

%package core
Summary: Kibana Policies - Core
Requires: app-base-core
Requires: app-accounts-core

%description core
Kibana Policies provide access control for the Kibana app.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/kibana_plugin
cp -r * %{buildroot}/usr/clearos/apps/kibana_plugin/

install -D -m 0644 packaging/kibana.php %{buildroot}/var/clearos/accounts/plugins/kibana.php

%post core
logger -p local6.notice -t installer 'app-kibana-plugin-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/kibana_plugin/deploy/install ] && /usr/clearos/apps/kibana_plugin/deploy/install
fi

[ -x /usr/clearos/apps/kibana_plugin/deploy/upgrade ] && /usr/clearos/apps/kibana_plugin/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-kibana-plugin-core - uninstalling'
    [ -x /usr/clearos/apps/kibana_plugin/deploy/uninstall ] && /usr/clearos/apps/kibana_plugin/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/kibana_plugin/packaging
%dir /usr/clearos/apps/kibana_plugin
/usr/clearos/apps/kibana_plugin/deploy
/usr/clearos/apps/kibana_plugin/language
/var/clearos/accounts/plugins/kibana.php
