%define		_enable_libtoolize	%{nil}

Name:		surf
Version:	1.0.6
Summary:	Tool to visualize some real algebraic geometry
Release:	3
Source0:	http://downloads.sourceforge.net/project/surf/surf/%{version}/%{name}-%{version}.tar.gz
URL:		http://surf.sourceforge.net/
License:	GPL
Group:		Sciences/Mathematics

BuildRequires:	flex-devel
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
%{_bindir}/surf
%{_mandir}/man1/surf.1.*
%dir %{_datadir}/surf
%{_datadir}/surf/surf.xpm
