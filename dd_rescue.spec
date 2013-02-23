Summary:	Data copying in presence of I/O errors
Summary(pl.UTF-8):	Kopiowanie danych z błędami we/wy
Name:		dd_rescue
Version:	1.32
Release:	1
License:	GPL v2 or v3
Group:		Applications/System
Source0:	http://www.garloff.de/kurt/linux/ddrescue/%{name}-%{version}.tar.gz
# Source0-md5:	5d2d88cf8932b8baed5c6d8c35c8db69
URL:		http://www.garloff.de/kurt/linux/ddrescue/
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
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D dd_rescue $RPM_BUILD_ROOT%{_bindir}/dd_rescue

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.dd_rescue
%attr(755,root,root) %{_bindir}/dd_rescue
