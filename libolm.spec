%global appname olm

Name: libolm
Version: 3.0.0
Release: 1%{?dist}

Summary: Double Ratchet cryptographic library
License: ASL 2.0
URL: https://git.matrix.org/git/%{appname}/about/

Source0: https://git.matrix.org/git/%{appname}/snapshot/%{appname}-%{version}.tar.bz2

BuildRequires: gcc-c++
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
sed -i 's@$(PREFIX)/lib@%{_libdir}@g' Makefile

%build
%set_build_flags
%make_build

%install
%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%ldconfig_scriptlets

%files
%license LICENSE
%doc *.rst docs/*.rst
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{appname}
%{_libdir}/%{name}.so

%changelog
* Sat Jan 05 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.0-1
- Updated to version 3.0.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.2-1
- Initial SPEC release.
