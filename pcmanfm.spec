#define _disable_ld_no_undefined 1

# git snapshot
%global snapshot 1
%if 0%{?snapshot}
	%global commit		e6b422b2003126b2116d26cf09f6e6244f1bb41f
	%global commitdate	20230917
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	PCMan File Manager
Name:		pcmanfm
Version:	1.3.2
Release:	3
License:	GPLv2+
Group:		File tools
Url:		https://pcmanfm.sourceforge.net/
#Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.xz
Source0:	https://github.com/lxde/pcmanfm/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz
Patch0:		pcmanfm-0.9.8-mdv-default-config.patch
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.18.0
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libfm) >= 1.2.5
BuildRequires:	pkgconfig(libfm-gtk3) >= 1.0.1
BuildRequires:  pkgconfig(libfm-extra)
BuildRequires:	pkgconfig(pango) >= 1.20.0
BuildRequires:	pkgconfig(x11)
Requires:	shared-mime-info
Requires:	gnome-icon-theme
Suggests:	gvfs
Conflicts:	lxde-common < 0.5.5

%description
PCMan File Manager is an extremely fast and lightweight file manager which
features tabbed browsing and user-friendly interface.

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/xdg/%{name}/default/pcmanfm.conf
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-desktop-pref.desktop
%{_mandir}/man1/%{name}.1*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
autoreconf -fiv
%configure \
	-with-gtk=3 \
	%{nil}
%make_build

%install
%make_install

rm -r %{buildroot}%{_includedir}

# locales
%find_lang %{name}

# clean .desktop file
desktop-file-install \
	--vendor="" \
	--remove-category="Application" \
	--add-category="System;FileTools" \
	--remove-mime-type="x-directory/normal" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

