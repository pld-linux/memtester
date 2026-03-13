Summary:	Userspace utility to test for faulty memory subsystem
Summary(pl.UTF-8):	Narzędzie do testowania podsystemu pamięci
Name:		memtester
Version:	4.7.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://pyropus.ca/software/memtester/old-versions/%{name}-%{version}.tar.gz
# Source0-md5:	a9d5e85a37696087b7c17a45ef017ded
URL:		https://pyropus.ca/software/memtester/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memtester is a userspace utility to test for memory subsystem errors.
It performs various types of tests to check for many possible error
kinds. Running as root is preferred, but not a must.

%description -l pl.UTF-8
Memtester jest programem testującym podsystem pamięci, działającym w
przestrzeni użytkownika. Wykonuje wiele różnych rodzajów testów
wyłapujących różne typy błędów. Najlepiej jest uruchomić go z
użytkownika root, ale nie jest to wymagane.

%prep
%setup -q

# Fix conf-cc and conf-ld to use our compiler flags and not strip binary
echo '%{__cc} %{rpmcflags} -DPOSIX -D_POSIX_C_SOURCE=200809L -D_FILE_OFFSET_BITS=64 -DTEST_NARROW_WRITES -c' > conf-cc
echo '%{__cc} %{rpmldflags}' > conf-ld

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install memtester $RPM_BUILD_ROOT%{_bindir}
cp -p memtester.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGELOG README README.tests
%attr(755,root,root) %{_bindir}/memtester
%{_mandir}/man8/memtester.8*
