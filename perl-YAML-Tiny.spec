#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	YAML
%define	pnam	Tiny
Summary:	YAML::Tiny - Read/Write YAML files with as little code as possible
#Summary(pl.UTF-8):	
Name:		perl-YAML-Tiny
Version:	1.34_01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AD/ADAMK/YAML-Tiny-1.34_01.tar.gz
# Source0-md5:	2db2b514cce2570be1e9fa234e81bc5d
URL:		http://search.cpan.org/dist/YAML-Tiny/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAML::Tiny is a perl class for reading and writing YAML-style files,
written with as little code as possible, reducing load time and memory
overhead.

# %description -l pl.UTF-8
# TODO

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
%doc Changes
%{perl_vendorlib}/YAML/*.pm
%{_mandir}/man3/*
