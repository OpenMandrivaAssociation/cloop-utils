%define clname      cloop
%define clver       1.02
%define clminorver  1
%define release     9mdk

Name:               %{clname}-utils
Version:            %{clver}
Release:            %{release}
Summary:            Utilities for the creation and extraction of compressed loop images
License:            GPL
Group:              File tools
URL:                http://www.knoppix.net/
Source0:            http://developer.linuxtag.net/knoppix/sources/%{clname}_%{clver}-%{clminorver}.tar.gz
Patch0:             cloop-1.02-write-to-file-ASAP.patch
Patch1:             mkfile-cloop.patch
Patch2:             cloop-1.02-ppc-build-fix.patch
BuildRequires:      zlib-devel
BuildRoot:          %{_tmppath}/%{name}-root
%description
%{summary}

%prep
%setup -q -n %{clname}-%{clver}
%patch0 -p1
%patch1
%patch2 -p1 -b .ppc

%build
make create_compressed_fs extract_compressed_fs APPSONLY=1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 create_compressed_fs $RPM_BUILD_ROOT/usr/bin
install -m 755 extract_compressed_fs $RPM_BUILD_ROOT/usr/bin

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG README
%{_bindir}/create_compressed_fs
%{_bindir}/extract_compressed_fs

