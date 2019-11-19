Name:           tripleo-ciscoaci
Version:        13.0
Release:        %{?release}%{!?release:1}
Summary:        Files for ACI tripleO patch
License:        ASL 2.0
Group:          Applications/Utilities
Source0:        tripleo-ciscoaci.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       createrepo

%define debug_package %{nil}

%description
This package contains files that are required for patch tripleO to support ACI

%prep
%setup -q -n tripleo-ciscoaci

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/ciscoaci-tripleo-heat-templates
mkdir -p $RPM_BUILD_ROOT/var/www/html
cp -r docker $RPM_BUILD_ROOT/opt/ciscoaci-tripleo-heat-templates
cp -r puppet $RPM_BUILD_ROOT/opt/ciscoaci-tripleo-heat-templates
cp -r tools $RPM_BUILD_ROOT/opt/ciscoaci-tripleo-heat-templates
cp nodepre.yaml $RPM_BUILD_ROOT/opt/ciscoaci-tripleo-heat-templates
cp -r  rpms $RPM_BUILD_ROOT/var/www/html/acirepo
createrepo $RPM_BUILD_ROOT/var/www/html/acirepo

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/opt/ciscoaci-tripleo-heat-templates
/var/www/html/acirepo

