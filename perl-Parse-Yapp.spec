%include	/usr/lib/rpm/macros.perl
Summary:	Parse-Yapp perl module
Summary(pl):	Modu³ perla Parse-Yapp
Name:		perl-Parse-Yapp
Version:	1.00
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Parse/Parse-Yapp-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse-Yapp - Yet Another Perl Parser compiler. 

%description -l pl
Modu³ perla Parse-Yapp.

%prep
%setup -q -n Parse-Yapp-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Parse/Yapp
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz
%attr(755,root,root) %{_bindir}/yapp
%{perl_sitelib}/Parse/Yapp.pm
%{perl_sitelib}/Parse/Yapp
%{perl_sitearch}/auto/Parse/Yapp

%{_mandir}/man[13]/*
