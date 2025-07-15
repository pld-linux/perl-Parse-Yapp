#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Parse
%define		pnam	Yapp
Summary:	Parse::Yapp Perl module - Yet Another Perl Parser compiler
Summary(pl.UTF-8):	Moduł Perla Parse::Yapp - jeszcze jeden kompilator parserów perlowych
Name:		perl-Parse-Yapp
Version:	1.21
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Parse/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	69584d5b0f0304bb2a23cffcd982c5de
Patch0:		%{name}-man.patch
URL:		http://search.cpan.org/dist/Parse-Yapp/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse::Yapp (Yet Another Perl Parser compiler) compiles yacc-like LALR
grammars to generate Perl OO parser modules.

%description -l pl.UTF-8
Parse::Yapp (Yet Another Perl Parser compiler - jeszcze jeden
kompilator perlowych analizatorów składniowych) kompiluje gramatyki
LALR w stylu narzędzia yacc, aby wygenerować analizatory w postaci
obiektowo zorientowanych modułów Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

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
%doc Changes
%attr(755,root,root) %{_bindir}/yapp
%{perl_vendorlib}/Parse/Yapp.pm
%{perl_vendorlib}/Parse/Yapp
%{_mandir}/man1/yapp.1p*
%{_mandir}/man3/Parse::Yapp.3*
