%include	/usr/lib/rpm/macros.perl
%define		pdir	Parse
%define		pnam	Yapp
Summary:	Parse::Yapp Perl module
Summary(cs):	Modul Parse::Yapp pro Perl
Summary(da):	Perlmodul Parse::Yapp
Summary(de):	Parse::Yapp Perl Modul
Summary(es):	M�dulo de Perl Parse::Yapp
Summary(fr):	Module Perl Parse::Yapp
Summary(it):	Modulo di Perl Parse::Yapp
Summary(ja):	Parse::Yapp Perl �⥸�塼��
Summary(ko):	Parse::Yapp �� ����
Summary(no):	Perlmodul Parse::Yapp
Summary(pl):	Modu� Perla Parse::Yapp
Summary(pt):	M�dulo de Perl Parse::Yapp
Summary(pt_BR):	M�dulo Perl Parse::Yapp
Summary(ru):	������ ��� Perl Parse::Yapp
Summary(sv):	Parse::Yapp Perlmodul
Summary(uk):	������ ��� Perl Parse::Yapp
Summary(zh_CN):	Parse::Yapp Perl ģ��
Name:		perl-Parse-Yapp
Version:	1.05
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-man.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse::Yapp - Yet Another Perl Parser compiler.

%description -l pl
Modu� Perla Parse::Yapp - jeszcze jedno narz�dzie do tworzenia
parser�w perlowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL
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
