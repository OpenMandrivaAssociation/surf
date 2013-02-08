%define		_enable_libtoolize	%{nil}

Name:		surf
Version:	1.0.6
Summary:	Tool to visualize some real algebraic geometry
Release:	2
Source0:	http://downloads.sourceforge.net/project/surf/surf/%{version}/%{name}-%{version}.tar.gz
URL:		http://surf.sourceforge.net/
License:	GPL
Group:		Sciences/Mathematics

BuildRequires:	flex
BuildRequires:	cups-devel
BuildRequires:	gmp-devel
BuildRequires:	gtk+-devel
BuildRequires:	jpeg-devel
BuildRequires:	libxmu-devel
BuildRequires:	tiff-devel
BuildRequires:	zlib-devel


%description
surf is a tool to visualize some real algebraic geometry:
plane algebraic curves, algebraic surfaces and hyperplane sections of surfaces.
surf is script driven and has (optionally) a nifty GUI using the Gtk widget
set.

%prep
%setup -q

%build
%configure2_5x \
	--with-gmp=%{_prefix}				\
	--with-gtk=%{_prefix}				\
	--with-x

%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/surf
%{_mandir}/man1/surf.1.*
%dir %{_datadir}/surf
%{_datadir}/surf/surf.xpm


%changelog
* Tue Sep 13 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.6-1mdv2012.0
+ Revision: 699660
- fixed BRs, config and make macros
- new version 1.0.6

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-4mdv2011.0
+ Revision: 615041
- the mass rebuild of 2010.1 packages

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 1.0.5-3mdv2010.1
+ Revision: 503628
- rebuild for new gmp

* Sun Aug 23 2009 Funda Wang <fwang@mandriva.org> 1.0.5-2mdv2010.0
+ Revision: 419818
- rebuild for new libjpeg v7

* Fri Aug 14 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.0.5-1mdv2010.0
+ Revision: 416247
- Import surf version 1.0.5.
  The surf program is the default singular plotting interface to sagemath.
- surf

