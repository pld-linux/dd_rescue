Summary:	Data copying in presence of I/O errors
Summary(pl.UTF-8):	Kopiowanie danych z błędami we/wy
Name:		dd_rescue
Version:	1.42
Release:	1
License:	GPL v2 or v3
Group:		Applications/System
Source0:	http://www.garloff.de/kurt/linux/ddrescue/%{name}-%{version}.tar.gz
# Source0-md5:	5974a513ce4e279ae0e6c54e1597cc11
URL:		http://www.garloff.de/kurt/linux/ddrescue/
BuildRequires:	autoconf
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
%setup -q -n %{name}

%build
%{__autoconf}
%{__autoheader}
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmldflags} -DHAVE_CONFIG_H" \
	CFLAGS_OPT='$(CFLAGS)' \

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLDIR=$RPM_BUILD_ROOT%{_bindir} \
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
%{_mandir}/man1/dd_rescue.1*
