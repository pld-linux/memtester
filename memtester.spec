%define date 19991116
Summary:	Utility to test for faulty memory
Summary(pl):	Program do testowania pamiêci
Name:		memtester
Version:	%{date}
Release:	1
Copyright:	GNU
Group:		Utility/System
Group(pl):	Narzêdzia/System		
Source:		memtester-%{date}.tar.gz
URL:		http://www.qcc.sk.ca/~charlesc/software/memtester/
Exclusivearch:	%{ix86}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Memtest is a utility for testing the memory in a PC to determine if it is
faulty.

%description -l pl
Memtest jest programem s³u¿±cym do testowania pamiêci PC, oraz okre¶lenia
czy jest sprawna, czy te¿ nie.

%prep
%setup -q -n memtester-%{date}

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}
install -s memtest $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf ABOUT README.tests CHANGELOG TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{sbindir}/memtest
