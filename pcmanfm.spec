%define _disable_ld_no_undefined 1

Summary:	PCMan File Manager
Name:		pcmanfm
Version:	1.2.5
Release:	3
License:	GPLv2+
Group:		File tools
Url:		http://pcmanfm.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.xz
Patch0:		pcmanfm-0.9.8-mdv-default-config.patch
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.18.0
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libfm) >= 1.2.5
BuildRequires:	pkgconfig(libfm-gtk) >= 1.0.1
BuildRequires:	pkgconfig(pango) >= 1.20.0
BuildRequires:	pkgconfig(x11)
Requires:	shared-mime-info
Requires:	gnome-icon-theme
Suggests:	gvfs
Conflicts:	lxde-common < 0.5.5

%description
PCMan File Manager is an extremely fast and lightweight file manager which
features tabbed browsing and user-friendly interface.

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

rm -r %{buildroot}%{_includedir}

%find_lang %{name}

# clean .desktop file
desktop-file-install \
	--vendor="" \
	--remove-category="Application" \
	--add-category="System;FileTools" \
	--remove-mime-type="x-directory/normal" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/xdg/%{name}/default/pcmanfm.conf
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-desktop-pref.desktop
%{_mandir}/man1/%{name}.1*
