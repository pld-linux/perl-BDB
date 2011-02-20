#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	BDB
Summary:	BDB - Asynchronous Berkeley DB access
Name:		perl-BDB
Version:	1.88
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{pnam}-%{version}.tar.gz
# Source0-md5:	64ef414a55a49edf78302a80b3871b94
URL:		http://search.cpan.org/dist/BDB/
BuildRequires:	db-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BDB - Asynchronous Berkeley DB access.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/BDB.pm
%dir %{perl_vendorarch}/auto/BDB
%attr(755,root,root) %{perl_vendorarch}/auto/BDB/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/BDB/*.so
%{_mandir}/man3/*
