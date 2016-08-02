#
# ooi RPM
#

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary     : OpenStack Preemtible Instances Extension
Name        : opie
Version     : 12.0.0
Release     : 1%{?dist}
Group       : Applications/Internet
License     : ASL 2.0
URL         : https://github.com/indigo-dc/opie/
Source      : opie-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python-setuptools
BuildRequires: python-pbr
BuildRequires: python-sphinx
Requires: python
Requires: python-nova >= 2:12.0.0
Requires: python-nova < 2:13.0.0
Requires: python-pbr >= 1.8
Requires: openstack-nova-scheduler >= 12.0.0
Requires: openstack-nova-scheduler < 13.0.0
Requires: python-oslo-log >= 1.8.0
Requires: python-oslo-config >= 1:2.3.0
Requires: python-oslo-serialization >= 1.10.0
Requires: python-oslo-utils > 3.15
Requires: python-webob >= 1.2.3

%description
opie provides a set of pluggable extensions for OpenStack Compute (nova)
making possible to execute premptible instances using a modified filter
scheduler.

%prep
%setup -q -n opie-%{version}

%build
%{__python} setup.py build
%{__python} setup.py build_sphinx

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md
%doc doc/build/html
%{python_sitelib}/opie*

%changelog
* Tue Aug 2 2016 Alvaro Lopez Garcia <aloga@ifca.unican.es> 12.0.0
- Initial RPM version
