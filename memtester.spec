Summary:	Userspace utility to test for faulty memory subsystem
Summary(pl):	Narz�dzie do testowania podsystemu pami�ci
Name:		memtester
Version:	4.0.5
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://pyropus.ca/software/memtester/%{name}-%{version}.tar.gz
# Source0-md5:	f6328b4863caf8f2013489c82c26cd1d
URL:		http://pyropus.ca/software/memtester/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memtester is a userspace utility to test for memory subsytem errors.
It performs various types of tests to check for many possible error
kinds. Running as root is prefferred, but not a must.

%description -l pl
Memtester jest programem testuj�cym podsystem pami�ci, dzia�aj�cym w
przestrzeni u�ytkownika. Wykonuje wiele r�nych rodzaj�w test�w
wy�apuj�cych r�ne typy b��d�w. Najlepiej jest uruchomi� go z
u�ytkownika root, ale nie jest to wymagane.

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
%doc README README.tests
%attr(755,root,root) %{_bindir}/memtester
%{_mandir}/man8/*
