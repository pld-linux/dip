Summary: Handles the connections needed for dialup IP links.
Name: dip
Version: 3.3.7o
Release: 14
Copyright: GPL
Group: Applications/Communications
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/serial/dip337o-uri.tgz
Patch: dip-3.3.7o-misc.patch
Patch1: dip-3.3.7o-suffix.patch
Patch2: dip-3.3.7o-fsstnd.patch
Patch3: dip-3.3.7o-glibc.patch
Patch4: dip-3.3.7o-sparc.patch
Patch5: dip-3.3.7o-andor.patch
Patch6: dip-arm.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dip is a modem dialer.  Dip handles the connections needed for dialup
IP links like SLIP or PPP.  Dip can handle both incoming and outgoing
connections, using password security for incoming connections.  Dip is
useful for setting up PPP and SLIP connections, but isn't required for
either.  Netcfg uses dip for setting up SLIP connections.

Install dip if you need a utility which will handle dialup IP
connections.

%description -l pl
Dip jest narz�dziem do dzwonienia za pomoc� modemu. Obs�uguje po��czenia 
IP takie jak SLIP czy PPP. Dip obs�uguje zar�wno po��czenia przychodz�ce 
jak i wychodz�ce, przy czym bezpiecze�stwo po��cze� przychodz�cych
opiera si� na has�ach. Mo�na wykorzysta� dip do ustawienia po��cze� PPP
i SLIP, ale nie jest do tego niezb�dny. Netcfg u�ywa dip do ustawienia
po��cze� SLIP.
Nale�y zainstalowa� dip je�li potzrbuje si� narz�dzia do obs�ugi modemowych 
po��cze� IP.

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
%patch4 -p0
%patch5 -p1 -b .andor
%patch3 -p1 -b .glibc
%patch6 -p1 -b .arm

%build
make depend
(cd skey; make clean; make linux)
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{sbin,man/man8}

install -c -s dip $RPM_BUILD_ROOT/usr/sbin
ln -sf dip $RPM_BUILD_ROOT/usr/sbin/diplogin
install -c -m 0444 dip.8 $RPM_BUILD_ROOT/usr/man/man8
ln -sf dip.8 $RPM_BUILD_ROOT/usr/man/man8/diplogin.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0755,root,uucp)	/usr/sbin/dip
/usr/sbin/diplogin
/usr/man/man8/dip.8
/usr/man/man8/diplogin.8
