%include	/usr/lib/rpm/macros.perl
%define	pdir	Parse
%define	pnam	Yapp
Summary:	Parse::Yapp perl module
Summary(pl):	Modu³ perla Parse::Yapp
Name:		perl-Parse-Yapp
Version:	1.05
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse::Yapp - Yet Another Perl Parser compiler.

%description -l pl
Modu³ perla Parse::Yapp - jeszcze jedno narzêdzie do tworzenia
parserów perlowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/yapp
%{perl_sitelib}/Parse/Yapp.pm
%{perl_sitelib}/Parse/Yapp
%{_mandir}/man[13]/*
