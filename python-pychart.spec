%define oname	pychart

Name: 	 	python-%{oname}
Summary:	Python library for data graphs and charts 	
Version: 	1.39
Release: 	%mkrel 7
Source0:	http://download.gna.org/pychart/PyChart-%{version}.tar.bz2
URL:		http://home.gna.org/pychart/
License:	GPLv2+
Group:		Sciences/Mathematics
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README demos doc
%{py_puresitedir}/%{oname}
%{py_puresitedir}/PyChart-%{version}-py%{pyver}.egg-info

