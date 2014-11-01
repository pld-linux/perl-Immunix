%include	/usr/lib/rpm/macros.perl
Summary:	Deprecated Immunix Perl modules from AppArmor suite
Summary(pl.UTF-8):	Przestarzałe moduły Perla Immunix ze zbioru oprogramowania AppArmor
Name:		perl-Immunix
Version:	2.9.0
Release:	1
Epoch:		1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://launchpad.net/apparmor/2.9/%{version}/+download/apparmor-%{version}.tar.gz
# Source0-md5:	daaeb859452f793abfdafd33f88d3e90
Source1:	Ycp.pm
URL:		http://apparmor.wiki.kernel.org/
BuildRequires:	rpm-perlprov
Requires:	perl-DBD-SQLite >= 1.08
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(ycp)'

%description
Deprecated Immunix Perl modules from AppArmor suite.

%description -l pl.UTF-8
Przestarzałe moduły Perla Immunix ze zbioru oprogramowania AppArmor.

%prep
%setup -q -n apparmor-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C deprecated/utils install \
	DESTDIR=$RPM_BUILD_ROOT
#	PERLDIR=$RPM_BUILD_ROOT%{perl_vendorlib}/Immunix

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{perl_vendorlib}/Immunix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Immunix
%{perl_vendorlib}/Immunix/*.pm
