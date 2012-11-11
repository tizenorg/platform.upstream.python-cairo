Name:           python-cairo
Version:        1.10.0
Release:        0
Summary:        Python Bindings for Cairo
License:        LGPL-2.1+ or MPL-1.1
Group:          Development/Libraries/Python
# FIXME: on update, check if we still need to manually compile the byte-code in %%install
Url:            http://www.cairographics.org/
Source:         py2cairo-%{version}.tar.bz2
BuildRequires:  cairo-devel
BuildRequires:  fdupes
BuildRequires:  python-devel

%description
Python bindings for cairo.

%package devel
Summary:        Headers for python-cairo
Group:          Development/Libraries/C and C++
Requires:       %name = %{version}
Requires:       cairo-devel
Requires:       python-devel

%description devel
Headers for python-cairo

%prep
%setup -n py2cairo-%{version}

%build
export CFLAGS='%{optflags}'
./waf configure --prefix=%{_prefix} --libdir=%{_libdir}
./waf build

%install
./waf install --destdir=%{buildroot}
# waf is broken and generated byte-code that references the build root, see http://code.google.com/p/waf/issues/detail?id=986
%py_compile %{buildroot}/%{py_sitedir}
%py_compile -O %{buildroot}/%{py_sitedir}
%fdupes %{buildroot}/%{py_sitedir}

%files
%defattr(-,root,root)
%doc COPYING COPYING-*
%{python_sitearch}/cairo/

%files devel
%defattr(-,root,root)
%{_includedir}/pycairo/
%{_libdir}/pkgconfig/pycairo.pc

%changelog