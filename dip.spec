Summary:	Handles the connections needed for dialup IP links
Summary(pl):	Obs³uga po³±czeñ wdzwanianych
Name:		dip
Version:	3.3.7o
Release:	16
License:	GPL
Group:		Applications/Communications
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/serial/%{name}337o-uri.tgz
# Source0-md5:	45fc2a9abbcb3892648933cadf7ba090
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
Requires(post,preun):	grep
Requires(preun):	fileutils
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
Dip jest narzêdziem do dzwonienia za pomoc± modemu. Obs³uguje
po³±czenia IP takie jak SLIP czy PPP. Dip obs³uguje zarówno po³±czenia
przychodz±ce jak i wychodz±ce, przy czym bezpieczeñstwo po³±czeñ
przychodz±cych opiera siê na has³ach. Mo¿na wykorzystaæ dip do
ustawienia po³±czeñ PPP i SLIP, ale nie jest do tego niezbêdny. Netcfg
u¿ywa dip do ustawienia po³±czeñ SLIP. Nale¿y zainstalowaæ dip je¶li
potzrbuje siê narzêdzia do obs³ugi modemowych po³±czeñ IP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p0
%patch5 -p1
%patch3 -p1
%patch6 -p1
%patch7 -p0
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
%{__make} depend
cd skey
%{__make} clean
%{__make} linux
cd ..
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install -c dip $RPM_BUILD_ROOT%{_sbindir}
ln -sf dip $RPM_BUILD_ROOT%{_sbindir}/diplogin

install dip.8 $RPM_BUILD_ROOT%{_mandir}/man8
echo ".so dip.8" > $RPM_BUILD_ROOT%{_mandir}/man8/diplogin.8

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f /etc/shells ]; then
	echo "/usr/sbin/diplogin" > /etc/shells
else
	if ! grep -q '^/usr/sbin/diplogin$' /etc/shells; then
		echo "/usr/sbin/diplogin" >> /etc/shells
	fi
fi

%preun
if [ "$1" = "0" ]; then
	umask 022
	grep -v /usr/sbin/diplogin /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%files
%defattr(644,root,root,755)
%attr(755,root,uucp) %{_sbindir}/dip
%attr(755,root,root) %{_sbindir}/diplogin
%{_mandir}/man8/*
