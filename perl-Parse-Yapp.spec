%include	/usr/lib/rpm/macros.perl
Summary:	Parse-Yapp perl module
Summary(pl):	Modu³ perla Parse-Yapp
Name:		perl-Parse-Yapp
Version:	1.04
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Parse/Parse-Yapp-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse-Yapp - Yet Another Perl Parser compiler.

%description -l pl
Modu³ perla Parse-Yapp.

%prep
%setup -q -n Parse-Yapp-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/yapp
%{perl_sitelib}/Parse/Yapp.pm
%{perl_sitelib}/Parse/Yapp
%{_mandir}/man[13]/*
