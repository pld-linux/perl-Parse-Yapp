#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Parse
%define		pnam	Yapp
Summary:	Parse::Yapp Perl module
Summary(cs):	Modul Parse::Yapp pro Perl
Summary(da):	Perlmodul Parse::Yapp
Summary(de):	Parse::Yapp Perl Modul
Summary(es):	Módulo de Perl Parse::Yapp
Summary(fr):	Module Perl Parse::Yapp
Summary(it):	Modulo di Perl Parse::Yapp
Summary(ja):	Parse::Yapp Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Parse::Yapp ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Parse::Yapp
Summary(pl):	Modu³ Perla Parse::Yapp
Summary(pt):	Módulo de Perl Parse::Yapp
Summary(pt_BR):	Módulo Perl Parse::Yapp
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Parse::Yapp
Summary(sv):	Parse::Yapp Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Parse::Yapp
Summary(zh_CN):	Parse::Yapp Perl Ä£¿é
Name:		perl-Parse-Yapp
Version:	1.05
Release:	6
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7bfca736d6af36c51edf7a97111a8f3b
Patch0:		%{name}-man.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse::Yapp - Yet Another Perl Parser compiler.

%description -l pl
Modu³ Perla Parse::Yapp - jeszcze jedno narzêdzie do tworzenia
parserów perlowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
%attr(755,root,root) %{_bindir}/yapp
%{perl_vendorlib}/Parse/Yapp.pm
%{perl_vendorlib}/Parse/Yapp
%{_mandir}/man[13]/*
