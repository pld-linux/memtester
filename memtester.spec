%define date 19991206
Summary:	Utility to test for faulty memory
Summary(pl):	Program do testowania pami�ci
Name:		memtester
Version:	%{date}
Release:	1
Copyright:	GNU
Group:		Utility/System
Group(pl):	Narz�dzia/System		
Source:		memtester-%{date}.tar.gz
URL:		http://www.qcc.sk.ca/~charlesc/software/memtester/
Exclusivearch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memtest is a utility for testing the memory in a PC to determine if it is
faulty.

%description -l pl
Memtest jest programem s�u��cym do testowania pami�ci PC, oraz okre�lenia
czy jest sprawna, czy te� nie.

%prep
%setup -q -n memtester-%{date}

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}
install -s memtest $RPM_BUILD_ROOT%{_sbindir}

install memtest.1 $RPM_BUILD_ROOT%{_mandir}/man1
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* ABOUT README.tests CHANGELOG TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_sbindir}/memtest
%{_mandir}/man1/*
