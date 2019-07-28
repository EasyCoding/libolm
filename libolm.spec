%global appname olm

Name: libolm
Version: 3.0.0
Release: 3%{?dist}

Summary: Double Ratchet cryptographic library
License: ASL 2.0
URL: https://git.matrix.org/git/%{appname}/about/

Source0: https://git.matrix.org/git/%{appname}/snapshot/%{appname}-%{version}.tar.bz2

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
An implementation of the Double Ratchet cryptographic ratchet in C++.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{appname}-%{version} -p1
mkdir -p %{_target_platform}

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DOLM_TESTS=ON \
    ..
popd
%ninja_build -C %{_target_platform}

%check
pushd %{_target_platform}/tests
    ctest --output-on-failure
popd

%install
%ninja_install -C %{_target_platform}

%files
%license LICENSE
%doc *.rst docs/*.rst
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{appname}
%{_libdir}/%{name}.so
%{_libdir}/cmake/Olm

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.0-1
- Updated to version 3.0.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.2-1
- Initial SPEC release.
