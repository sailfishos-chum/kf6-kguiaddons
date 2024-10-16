%global  kf_version 6.6.0

Name:		kf6-kguiaddons
Version: 6.6.0
Release:	0%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with various classes on top of QtGui
License:	BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
URL:		https://invent.kde.org/frameworks/kguiaddons
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:	cmake
BuildRequires:	clang
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-plasma-wayland-protocols-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  qt6-qttools-devel

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       qt6-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6 -DWITH_X11=OFF -DWITH_WAYLAND=ON
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kde-geo-uri-handler
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6GuiAddons.so.*
%{_kf6_datadir}/applications/*-handler.desktop

%files devel
%{_kf6_includedir}/KGuiAddons/
%{_kf6_libdir}/libKF6GuiAddons.so
%{_kf6_libdir}/cmake/KF6GuiAddons/
%{_qt6_docdir}/*.tags
%{_kf6_libdir}/pkgconfig/KF6GuiAddons.pc


%files doc
%{_qt6_docdir}/*.qch
