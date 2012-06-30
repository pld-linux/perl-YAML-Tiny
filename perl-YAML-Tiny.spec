#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	YAML
%define	pnam	Tiny
Summary:	YAML::Tiny - Read/Write YAML files with as little code as possible
Summary(pl.UTF-8):	YAML::Tiny - odczyt i zapis plików YAML z użyciem jak najmniejszego kodu
Name:		perl-YAML-Tiny
Version:	1.51
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/YAML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8e67d89a4905e797216384a89011efa9
URL:		http://search.cpan.org/dist/YAML-Tiny/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAML::Tiny is a Perl class for reading and writing YAML-style files,
written with as little code as possible, reducing load time and memory
overhead.

%description -l pl.UTF-8
YAML::Tiny to klasa Perla od odczytu i zapisu plików w stylu YAML,
napisana z użyciem jak najmniejszej ilości kodu, tym samym
zmniejszając narzut czasowy i pamięciowy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

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
%{perl_vendorlib}/YAML/Tiny.pm
%{_mandir}/man3/YAML::Tiny.3pm*
