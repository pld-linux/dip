Summary:	Handles the connections needed for dialup IP links
Summary(pl):	Obs�uga po��cze� wdzwanianych
Name:		dip
Version:	3.3.7o
Release:	15
License:	GPL
Group:		Applications/Communications
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/serial/%{name}337o-uri.tgz
Patch0:		%{name}-3.3.7o-misc.patch
Patch1:		%{name}-3.3.7o-suffix.patch
Patch2:		%{name}-3.3.7o-fsstnd.patch
Patch3:		%{name}-3.3.7o-glibc.patch
Patch4:		%{name}-3.3.7o-sparc.patch
Patch5:		%{name}-3.3.7o-andor.patch
Patch6:		%{name}-arm.patch
Patch7:		%{name}-3.3.7o-skey.patch
Patch8:		%{name}-3.3.7o-jbj.patch
Patch9:		%{name}-3.3.7o-timeout.patch
Patch10:	%{name}-3.3.7o-lockfile.patch
Patch11:	%{name}-3.3.7o-asm.patch
Patch12:	%{name}-3.3.7o-db.patch
Patch13:	%{name}-3.3.7o-types.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dip is a modem dialer. Dip handles the connections needed for dialup
IP links like SLIP or PPP. Dip can handle both incoming and outgoing
connections, using password security for incoming connections. Dip is
useful for setting up PPP and SLIP connections, but isn't required for
either. Netcfg uses dip for setting up SLIP connections.

Install dip if you need a utility which will handle dialup IP
connections.

%description -l pl
Dip jest narz�dziem do dzwonienia za pomoc� modemu. Obs�uguje
po��czenia IP takie jak SLIP czy PPP. Dip obs�uguje zar�wno po��czenia
przychodz�ce jak i wychodz�ce, przy czym bezpiecze�stwo po��cze�
przychodz�cych opiera si� na has�ach. Mo�na wykorzysta� dip do
ustawienia po��cze� PPP i SLIP, ale nie jest do tego niezb�dny. Netcfg
u�ywa dip do ustawienia po��cze� SLIP. Nale�y zainstalowa� dip je�li
potzrbuje si� narz�dzia do obs�ugi modemowych po��cze� IP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p0
%patch5 -p1 -b .andor
%patch3 -p1 -b .glibc
%patch6 -p1 -b .arm
%patch7 -p0 -b .skey
%patch8 -p1 -b .jbj
%patch9 -p1 -b .timeout
%patch10 -p1 -b .lockfile
%patch11 -p1 -b .asm
%patch12 -p1 -b .db
%patch13 -p1 -b .types

%build
%{__make} depend
(cd skey; make clean; make linux)
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/sbin,%{_mandir}/man8}

install -c dip $RPM_BUILD_ROOT%{_sbindir}
ln -sf dip $RPM_BUILD_ROOT%{_sbindir}/diplogin

install dip.8 $RPM_BUILD_ROOT%{_mandir}/man8
echo ".so dip.8" > $RPM_BUILD_ROOT%{_mandir}/man8/diplogin.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0755,root,uucp) %{_sbindir}/dip
%attr(755,root,root) %{_sbindir}/diplogin
%{_mandir}/man8/*
