%define version 1.1
%define release %mkrel 7

Name: python-mcrypt
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Summary: Comprehensive Python interface to the mcrypt library
License: GPL
Group: Development/Python
Url: http://labix.org/python-mcrypt
Requires: python 
BuildRequires: python-devel
BuildRequires: libmcrypt-devel


%description
Python-mcrypt is a comprehensive Python interface to the mcrypt library, which
provides a uniform interface to several symmetric encryption algorithms.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root %buildroot

%files
%doc LICENSE NEWS AUTHORS
%py_platsitedir/mcrypt.so
%py_platsitedir/python_mcrypt-*info




%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.1-7mdv2010.0
+ Revision: 442311
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.1-6mdv2009.0
+ Revision: 259702
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.1-5mdv2009.0
+ Revision: 247510
- rebuild

* Tue Feb 19 2008 Thierry Vignaud <tv@mandriva.org> 1.1-3mdv2008.1
+ Revision: 172399
- fix file list
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sat Apr 15 2006 Couriousous <couriousous@mandriva.org> 1.1-2mdk
- rebuild

* Sat Mar 19 2005 Couriousous <couriousous@mandrake.org> 1.1-1mdk
- First Mandrakelinux release

