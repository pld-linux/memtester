Summary:	Userspace utility to test for faulty memory subsystem
Summary(pl):	Narzêdzie z przestrzeniu u¿ytkownika do testowania podsystemu pamiêci
Name:		memtester
Version:	2.93.1
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
URL:		http://www.qcc.sk.ca/~charlesc/software/%{name}/
Source0:	http://www.qcc.sk.ca/~charlesc/software/%{name}/%{name}-%{version}.tar.bz2
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
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install memtest $RPM_BUILD_ROOT%{_bindir}
install memtest.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf CHANGELOG ABOUT README.tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/memtest
%{_mandir}/man1/*
