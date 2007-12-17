%define version 1.1
%define release %mkrel 2

Name: python-mcrypt
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Summary: Python-mcrypt is a comprehensive Python interface to the mcrypt library
License: GPL
Group: Development/Python
Url: http://labix.org/python-mcrypt
Requires: python 
BuildRequires: libpython-devel
BuildRequires: libmcrypt-devel


%description
Python-mcrypt is a comprehensive Python interface to the mcrypt library, which
provides a uniform interface to several symmetric encryption algorithms.

%prep
%setup -q

%build
python setup.py build
%install
rm -rf %buildroot
python setup.py install --root %buildroot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE NEWS AUTHORS
%py_platsitedir/mcrypt.so

