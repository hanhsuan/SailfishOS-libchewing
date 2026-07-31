%bcond_with dynamic
Name:           libchewing
%define soname	3
Version:        0.8.5
Release:        0
Summary:        Intelligent Phonetic Input Method Library for Traditional Chinese
License:        LGPL-2.1-or-later
URL:            https://codeberg.org/chewing/libchewing
Source0:        %{name}-%{version}.tar.zst

Patch0:         0001-skip-chewing-cli-doc.patch

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  sqlite-devel
BuildRequires:  zstd

%description
Intelligent phonetic input method library for traditional Chinese.

%package devel
Summary:        Development package for libchewing
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}

%description devel
Development package for libchewing.

%package -n %{name}%{soname}
Summary:        Chewing libraries
Group:          System/Libraries
Requires:       chewing-data

%description -n %{name}%{soname}
This package contains libraries for Chewing.

%package -n chewing-data
Summary:        Data for libchewing
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n chewing-data
This package contains data files for libchewing.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%if %{with dynamic}
cmake --preset c99-release --install-prefix %{_prefix}
%else
cmake --preset c99-release --install-prefix %{_prefix} -DBUILD_SHARED_LIBS=OFF
%endif
cmake --build build

%check
cmake --build build -t test

%install
cmake --install build --prefix %{buildroot}%{_prefix}

%fdupes %{buildroot}%{_includedir}

%if %{with dynamic}
%post -n %{name}%{soname} -p /sbin/ldconfig

%postun -n %{name}%{soname} -p /sbin/ldconfig
%endif

%files -n %{name}%{soname}
%if %{with dynamic}
%{_libdir}/libchewing.so.*
%else
%{_libdir}/libchewing.a
%endif

%files -n chewing-data
%{_datadir}/%{name}/

%files devel
%{_includedir}/chewing/
%if %{with dynamic}
%{_libdir}/libchewing.so
%else
%{_libdir}/libchewing.a
%endif
%{_libdir}/pkgconfig/chewing.pc

%changelog

