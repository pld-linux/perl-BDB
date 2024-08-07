#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pnam	BDB
Summary:	BDB - Asynchronous Berkeley DB access
Summary(pl.UTF-8):	BDB - asynchroniczny dostęp do Berkeley DB
Name:		perl-BDB
Version:	1.92
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/%{pnam}-%{version}.tar.gz
# Source0-md5:	2be2ce3cf9457d7775a32f3006abc2c0
URL:		https://metacpan.org/dist/BDB
BuildRequires:	db-devel >= 4.3
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-common-sense
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BDB - Asynchronous Berkeley DB access.

%description -l pl.UTF-8
BDB - asynchroniczny dostęp do Berkeley DB.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/BDB.pm
%dir %{perl_vendorarch}/auto/BDB
%attr(755,root,root) %{perl_vendorarch}/auto/BDB/BDB.so
%{_mandir}/man3/BDB.3pm*
