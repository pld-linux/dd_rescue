Summary:	Data copying in presence of I/O errors
Summary(pl):	Kopiowanie danych z b³êdami we/wy
Name:		dd_rescue
Version:	1.03
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.garloff.de/kurt/linux/ddrescue/%{name}-%{version}.tar.gz
# Source0-md5:	9057d5c0b4b107cbcd7db06b4c48dd60
URL:		http://www.garloff.de/kurt/linux/ddrescue/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dd_rescue helps, when nobody else will: Your disk has crashed and you
try to copy it over to another one. Standard Un*x tools like cp, cat,
dd will abort on every I/O error. dd_rescue won't.

%description -l pl
dd_rescue pomaga tam, gdzie nic innego nie pomo¿e: kiedy dysk padnie i
próbujemy go skopiowaæ na inny. Standardowe narzêdzia uniksowe takie
jak cp, cat, dd koñcz± dzia³anie na ka¿dym b³êdzie we/wy. dd_rescue
tego nie robi.

%prep
%setup -q -n %{name}

%build
rm -f missing
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D dd_rescue $RPM_BUILD_ROOT%{_bindir}/dd_rescue

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.dd_rescue
%attr(755,root,root) %{_bindir}/*
