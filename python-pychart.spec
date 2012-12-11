%define oname	pychart

Name: 	 	python-%{oname}
Summary:	Python library for data graphs and charts 	
Version: 	1.39
Release: 	8
Source0:	http://download.gna.org/pychart/PyChart-%{version}.tar.bz2
URL:		http://home.gna.org/pychart/
License:	GPLv2+
Group:		Sciences/Mathematics
%{py_requires -d}
BuildArch:	noarch
Obsoletes:	pychart
Provides:	pychart

%description
PyChart is a Python library for creating high quality Encapsulated Postscript,
PDF, PNG, or SVG charts. It currently supports line plots, bar plots,
range-fill plots, and pie charts. Because it is based on Python, you can make
full use of Python's scripting power.

%prep
%setup -q -n PyChart-%{version}
chmod 644 `find -type f`

%install
python setup.py install --root=%{buildroot} --compile --optimize=2

%files
%doc README demos doc
%{py_puresitedir}/%{oname}
%{py_puresitedir}/PyChart-%{version}-py%{py_ver}.egg-info



%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 1.39-7mdv2011.0
+ Revision: 594079
- rebuild
- rebuild

* Tue May 19 2009 Jérôme Brenier <incubusss@mandriva.org> 1.39-5mdv2010.0
+ Revision: 377438
- remove version/release from obsoletes/provides (mdk pakage still here)

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.39-4mdv2009.1
+ Revision: 323948
- rebuild

* Fri Sep 12 2008 Adam Williamson <awilliamson@mandriva.org> 1.39-3mdv2009.0
+ Revision: 284028
- obsolete / provide old name

* Fri Sep 12 2008 Adam Williamson <awilliamson@mandriva.org> 1.39-2mdv2009.0
+ Revision: 284024
- rename spec file
- package egg-info file
- don't package COPYING
- clean macros
- update URL
- new license policy
- tabs not spaces
- rename to match python policy
- drop unnecessary defines
- rename to conform to python policy

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import pychart

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

