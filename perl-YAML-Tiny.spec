#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	YAML
%define	pnam	Tiny
Summary:	YAML::Tiny - Read/Write YAML files with as little code as possible
Summary(pl.UTF-8):	YAML::Tiny - odczyt i zapis plików YAML z użyciem jak najmniejszego kodu
Name:		perl-YAML-Tiny
Version:	1.76
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/YAML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0ba27f37b09d84720a4f257fae7045f7
URL:		https://metacpan.org/dist/YAML-Tiny
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl-File-Temp >= 0.19
BuildRequires:	perl-JSON-PP
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Test-Simple >= 0.88
%endif
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
