Summary:	Data copying in presence of I/O errors
Summary(pl.UTF-8):	Kopiowanie danych z błędami we/wy
Name:		dd_rescue
Version:	1.99.13
Release:	1
License:	GPL v2 or v3
Group:		Applications/System
Source0:	http://www.garloff.de/kurt/linux/ddrescue/%{name}-%{version}.tar.bz2
# Source0-md5:	5b2d31e8e13b17ca99f5453de705f9b9
URL:		http://www.garloff.de/kurt/linux/ddrescue/
BuildRequires:	autoconf >= 2.50
BuildRequires:	lzo-devel >= 2.07
BuildRequires:	openssl-devel
Requires:	lzo >= 2.07
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dd_rescue helps, when nobody else will: Your disk has crashed and you
try to copy it over to another one. Standard Un*x tools like cp, cat,
dd will abort on every I/O error. dd_rescue won't.

%description -l pl.UTF-8
dd_rescue pomaga tam, gdzie nic innego nie pomoże: kiedy dysk padnie i
próbujemy go skopiować na inny. Standardowe narzędzia uniksowe takie
jak cp, cat, dd kończą działanie na każdym błędzie we/wy. dd_rescue
tego nie robi.

%prep
%setup -q

%build
%{__autoconf}
%{__autoheader}
%configure
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}" \
	EXTRA_LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLDIR=$RPM_BUILD_ROOT%{_bindir} \
	LIB=%{_lib} \
	INSTALLFLAGS= \
	INSTASROOT=

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.dd_rescue
%attr(755,root,root) %{_bindir}/dd_rescue
%attr(755,root,root) %{_libdir}/libddr_MD5.so
%attr(755,root,root) %{_libdir}/libddr_crypt.so
%attr(755,root,root) %{_libdir}/libddr_hash.so
%attr(755,root,root) %{_libdir}/libddr_null.so
%attr(755,root,root) %{_libdir}/libddr_lzo.so
%{_mandir}/man1/dd_rescue.1*
%{_mandir}/man1/ddr_crypt.1*
%{_mandir}/man1/ddr_lzo.1*
