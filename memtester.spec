Summary:	Userspace utility to test for faulty memory subsystem
Summary(pl):	Narzêdzie z przestrzeniu u¿ytkownika do testowania podsystemu pamiêci
Name:		memtester
Version:	2.93.1
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://www.qcc.sk.ca/~charlesc/software/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	3c971e11ca71cc8cd9d43b247170c243
URL:		http://www.qcc.sk.ca/~charlesc/software/memtester/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memtester is a userspace utility to test for memory subsytem errors.
It performs various types of tests to check for many possible error
kinds. Running as root is prefferred, but not a must.

%description -l pl
Memtester jest programem testuj±cym podsytem pamiêci, dzia³aj±cym w
przestrzeniu u¿ytkownika. Wykonuje wiele ró¿nych rodzajów testów
wy³apuj±cych ró¿ne typy b³êdów. Najlepiej jest uruchomiæ go z
uztkownika root, ale nie jest to wymagane.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install memtest $RPM_BUILD_ROOT%{_bindir}
install memtest.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG ABOUT README.tests
%attr(755,root,root) %{_bindir}/memtest
%{_mandir}/man1/*
