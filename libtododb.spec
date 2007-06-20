Summary:	GPE TODO Database library
Summary(pl.UTF-8):	Biblioteka bazy danych GPE TODO
Name:		libtododb
Version:	0.11
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	d3fa3b6093eefdb374a78f0fa5d2eb9a
URL:		http://gpe.linuxtogo.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libgpepimc-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	sqlite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE TODO Database library.

%description -l pl.UTF-8
Biblioteka bazy danych GPE TODO

%package devel
Summary:	Header files for libtododb
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libtododb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgpepimc-devel
Requires:	sqlite-devel

%description devel
Header files for libtododb.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libtododb.

%package static
Summary:	Static libtododb library
Summary(pl.UTF-8):	Statyczna biblioteka libtododb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtododb library.

%description static -l pl.UTF-8
Statyczna biblioteka libtododb.

%package apidocs
Summary:	libtododb API documentation
Summary(pl.UTF-8):	Dokumentacja API libtododb
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libtododb API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libtododb.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtododb.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtododb.so
%{_libdir}/libtododb.la
%{_includedir}/gpe/*.h
%{_pkgconfigdir}/libtododb.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtododb.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libtododb
