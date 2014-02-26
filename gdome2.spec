%define major 0
%define libname  %mklibname gdome %{major}
%define devname %mklibname -d gdome

Summary:	A DOM level2 library for accessing XML files
Name:		gdome2
Version:	0.8.1
Release:	11
License:	LGPLv2.1+
Group:		System/Libraries
URL:		http://gdome2.cs.unibo.it
Source0:	http://gdome2.cs.unibo.it/tarball/%{name}-%{version}.tar.bz2
Patch0:		gdome2-0.8.1-gdome-config_lib64.diff
Patch1:		gdome2-0.8.1-fix-str-fmt.patch
Patch2:		gdome2-0.8.1-libxml2.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
Libgdome is a DOM C library developed for the Gnome project. It's a DOM level2
implementation. Libgdome supports "Core", "XML", "Events" and "MutationEvents"
modules. It's based on libxml2.

%package -n	%{libname}
Summary:	A DOM level2 library for accessing XML files
Group:		System/Libraries

%description -n	%{libname}
A fast, light and complete DOM level2 implementation based on libxml2.

%files -n %{libname}
%{_libdir}/libgdome.so.%{major}*

#----------------------------------------------------------------------------

%package -n	%{devname}
Summary:	DOM level2 library for accessing XML files
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package contains the header files and static libraries for
developing with libgdome.

%files -n %{devname}
%doc AUTHORS MAINTAINERS ChangeLog README COPYING COPYING.LIB
%{_bindir}/gdome-config
%{_datadir}/aclocal/gdome2.m4
%{_includedir}/*
%{_libdir}/pkgconfig/gdome2.pc
%{_libdir}/libgdome.so
%{_libdir}/*.sh
%{_mandir}/man1/gdome-config.1*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
autoreconf -fi
%configure2_5x \
	--disable-static \
	--disable-glib-1

%make

%install
%makeinstall_std

