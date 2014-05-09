%define		_enable_libtoolize	%{nil}

Name:		surf
Version:	1.0.6
Summary:	Tool to visualize some real algebraic geometry
Release:	4
Source0:	http://downloads.sourceforge.net/project/surf/surf/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.module.in
URL:		http://surf.sourceforge.net/
License:	GPL

BuildRequires:	flex-devel
BuildRequires:	cups-devel
BuildRequires:	gmp-devel
BuildRequires:	gtk+-devel
BuildRequires:	jpeg-devel
BuildRequires:	libxmu-devel
BuildRequires:	tiff-devel
BuildRequires:	zlib-devel
Requires:	environment-modules

%description
surf is a tool to visualize some real algebraic geometry:
plane algebraic curves, algebraic surfaces and hyperplane sections of surfaces.
surf is script driven and has (optionally) a nifty GUI using the Gtk widget
set.

%prep
%setup -q
# Avoid extra directory and install binary and xpm file in same directory
sed -i 's|^\(pkgdatadir = $(datadir)\)/@PACKAGE@|\1|' Makefile.in
sed -i 's|/surf\(/surf\.xpm\)|\1|' gtkgui/showAbout.cc
chmod -x gtkgui/PrintImageDialog.{cc,h}

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS=$CFLAGS

%configure2_5x \
	--bindir=%{_libdir}/%{name}			\
	--datadir=%{_libdir}/%{name}			\
	--with-gmp=%{_prefix}				\
	--with-gtk=%{_prefix}				\
	--with-x

%make

%install
%makeinstall_std

# Based on 4ti2.spec
mkdir -p $RPM_BUILD_ROOT%{_datadir}/Modules/modulefiles
sed 's#@BINDIR@#'%{_libdir}/%{name}'#g;' < %{SOURCE1} > \
    $RPM_BUILD_ROOT%{_datadir}/Modules/modulefiles/%{name}-%{_arch} 

%files
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%doc NEWS
%doc README
%doc TODO
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/Modules/modulefiles/%{name}-%{_arch}
