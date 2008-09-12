%define name	pychart
%define version 1.39
%define release %mkrel 2

Name: 	 	%{name}
Summary:	Python library for data graphs and charts 	
Version: 	%{version}
Release: 	%{release}

Source:		http://download.gna.org/pychart/PyChart-%{version}.tar.bz2
URL:		http://www.hpl.hp.com/personal/Yasushi_Saito/pychart/
License:	GPL
Group:		Sciences/Mathematics
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel
BuildArch:	noarch

%description
PyChart is a Python library for creating high quality Encapsulated Postscript,
PDF, PNG, or SVG charts. It currently supports line plots, bar plots,
range-fill plots, and pie charts. Because it is based on Python, you can make
full use of Python's scripting power.

%prep
%setup -q -n PyChart-%version
chmod 644 `find -type f`

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README demos doc COPYING
%python_sitelib/%name

