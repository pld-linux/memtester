Summary:	Userspace utility to test for faulty memory subsystem
Summary(pl.UTF-8):	Narzędzie do testowania podsystemu pamięci
Name:		memtester
Version:	4.0.8
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://pyropus.ca/software/memtester/old-versions/%{name}-%{version}.tar.gz
# Source0-md5:	a4971ed1ccaf5b2e2148fd66b0eb7363
URL:		http://pyropus.ca/software/memtester/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memtester is a userspace utility to test for memory subsytem errors.
It performs various types of tests to check for many possible error
kinds. Running as root is prefferred, but not a must.

%description -l pl.UTF-8
Memtester jest programem testującym podsystem pamięci, działającym w
przestrzeni użytkownika. Wykonuje wiele różnych rodzajów testów
wyłapujących różne typy błędów. Najlepiej jest uruchomić go z
użytkownika root, ale nie jest to wymagane.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install memtester $RPM_BUILD_ROOT%{_bindir}
install memtester.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG README README.tests
%attr(755,root,root) %{_bindir}/memtester
%{_mandir}/man8/*
