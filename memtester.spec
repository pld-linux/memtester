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

Copyright (C) 1999 Simon Kirby. Version 2 Copyright © 1999 Charles
Cazabon.
Memtest is a utility for testing the memory in a PC to determine if it
is faulty. The original source was by Simon Kirby <sim@stormix.com>. I
have by this time completely rewritten the original source, and added
many additional tests to help catch borderline memory. I also rewrote
the original tests (which catch mainly memory bits which are stuck
permanently high or low) so that they run approximately an order of
magnitude faster.



%description -l pl

memtest jest programem s³u¿±cym do testowania pamiêci PC, oraz okre¶lenia
czy jest sprawna, czy te¿ nie.

%prep
%setup -q -n memtester-%{date}

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
make

%install
install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/doc/memtester-%{date}
install -s memtest $RPM_BUILD_ROOT/usr/bin
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
/usr/bin/memtest


%changelog

* Fri Nov 19 1999 £ukasz Tr±biñski <lukasz@lt.wsisiz.edu.pl>
- Make a spec file
