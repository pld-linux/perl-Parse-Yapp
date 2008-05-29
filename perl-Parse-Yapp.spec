#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Parse
%define		pnam	Yapp
Summary:	Parse::Yapp Perl module
Summary(cs.UTF-8):	Modul Parse::Yapp pro Perl
Summary(da.UTF-8):	Perlmodul Parse::Yapp
Summary(de.UTF-8):	Parse::Yapp Perl Modul
Summary(es.UTF-8):	Módulo de Perl Parse::Yapp
Summary(fr.UTF-8):	Module Perl Parse::Yapp
Summary(it.UTF-8):	Modulo di Perl Parse::Yapp
Summary(ja.UTF-8):	Parse::Yapp Perl モジュール
Summary(ko.UTF-8):	Parse::Yapp 펄 모줄
Summary(nb.UTF-8):	Perlmodul Parse::Yapp
Summary(pl.UTF-8):	Moduł Perla Parse::Yapp
Summary(pt.UTF-8):	Módulo de Perl Parse::Yapp
Summary(pt_BR.UTF-8):	Módulo Perl Parse::Yapp
Summary(ru.UTF-8):	Модуль для Perl Parse::Yapp
Summary(sv.UTF-8):	Parse::Yapp Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Parse::Yapp
Summary(zh_CN.UTF-8):	Parse::Yapp Perl 模块
Name:		perl-Parse-Yapp
Version:	1.05
Release:	33
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

%description -l pl.UTF-8
Moduł Perla Parse::Yapp - jeszcze jedno narzędzie do tworzenia
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
