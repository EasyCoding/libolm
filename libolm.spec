%global appname olm

Name: libolm
Version: 2.2.2
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
%doc *.rst docs/*
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{appname}
%{_libdir}/%{name}.so

%changelog
