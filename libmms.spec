Summary:	LibMMS - mms:// and mmsh:// parsing library
Name:		libmms
Version:	0.6.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.sourceforge.net/libmms/%{name}-%{version}.tar.gz
# Source0-md5:	9f63aa363deb4874e072a45850161bff
URL:		http://sourceforge.net/projects/libmms/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibMMS is mms:// and mmsh:// (Microsoft streaming protocols) parsing
library.

%package devel
Summary:	Header files for libmms library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmms library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make} \
	PKG_LIBS='$(GLIB_LIBS)'

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README README.LICENSE
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libmms
%{_pkgconfigdir}/*.pc

