%bcond_with static
Name:           libchewing
Version:        0.8.5
Release:        0
Summary:        Intelligent Phonetic Input Method Library for Traditional Chinese
License:        LGPL-2.1-or-later
URL:            https://codeberg.org/chewing/libchewing
Source0:        https://codeberg.org/chewing/libchewing/releases/download/v%{version}/%{name}-%{version}.tar.zst

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
Requires:       %{name} = %{version}

%description devel
Development package for libchewing.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%if %{with static}
cmake --preset c99-release --install-prefix %{_prefix} -DBUILD_SHARED_LIBS=OFF
%else
cmake --preset c99-release --install-prefix %{_prefix}
%endif
cmake --build build

%check
cmake --build build -t test

%install
cmake --install build --prefix %{buildroot}%{_prefix}

%fdupes %{buildroot}%{_includedir}

%if %{without static}
%post -n %{name} -p /sbin/ldconfig

%postun -n %{name} -p /sbin/ldconfig
%endif

%files
%if %{with static}
%{_libdir}/libchewing.a
%else
%{_libdir}/libchewing.so.*
%endif
%{_datadir}/%{name}/

%files devel
%{_includedir}/chewing/
%if %{with static}
%{_libdir}/libchewing.a
%else
%{_libdir}/libchewing.so
%endif
%{_libdir}/pkgconfig/chewing.pc
%{_datadir}/%{name}/

%changelog

