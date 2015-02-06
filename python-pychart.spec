%define oname	pychart

Name: 	 	python-%{oname}
Summary:	Python library for data graphs and charts 	

Version: 	1.39
Release: 	9
Source0:	http://download.gna.org/pychart/PyChart-%{version}.tar.bz2
URL:		http://home.gna.org/pychart/
License:	GPLv2+
Group:		Sciences/Mathematics
BuildRequires:	python-devel
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



