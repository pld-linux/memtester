%define date 19991116
Summary:	Utility to test for faulty memory
Summary(pl):	Program do testowania pamiêci
Name:		memtester
Version:	%{date}
Release:	1
Copyright:	GNU
Group:		Utility/System
Group(pl):	Narzedzia/System		
Source:		memtester-%{date}.tar.gz
URL:		http://www.qcc.sk.ca/~charlesc/software/memtester/
BuildRoot:	/tmp/%{name}-%{version}-root

%description

Memtest is a utility for testing the memory in a PC to determine if it
is faulty.

%description -l pl

Memtest jest programem s³u¿±cym do testowania pamiêci PC, oraz okre¶lenia
czy jest sprawna, czy te¿ nie.

%prep
%setup -q -n memtester-%{date}

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
make

%install
install -d $RPM_BUILD_ROOT/usr/sbin
install -d $RPM_BUILD_ROOT/usr/doc/memtester-%{date}
install -s memtest $RPM_BUILD_ROOT/usr/sbin
install ABOUT $RPM_BUILD_ROOT/usr/doc/memtester-%{date}
install README.tests $RPM_BUILD_ROOT/usr/doc/memtester-%{date}
install CHANGELOG $RPM_BUILD_ROOT/usr/doc/memtester-%{date}
install TODO $RPM_BUILD_ROOT/usr/doc/memtester-%{date}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc {TODO,CHANGELOG,README.tests,ABOUT}
%defattr(755, root, root)
/usr/sbin/memtest


%changelog

* Sat Nov 20 1999 £ukasz Tr±biñski <lukasz@lt.wsisiz.edu.pl>
- change location memtest to /usr/sbin

* Fri Nov 19 1999 £ukasz Tr±biñski <lukasz@lt.wsisiz.edu.pl>
- Make a spec file
