%define clname      cloop
%define clver       2.06
%define clminorver  1
%define release     %mkrel 1

Name:		%{clname}-utils
Version:	%{clver}
Release:	%{release}
Summary:	Utilities for the creation and extraction of compressed loop images
License:	GPL
Group:		File tools
URL:		http://debian-knoppix.alioth.debian.org/sources/
Source0:	http://debian-knoppix.alioth.debian.org/sources/%{clname}_%{clver}-%{clminorver}.tar.bz2
Patch0:		cloop-2.06-write-to-file-ASAP.patch
Patch1:		mkfile-cloop.patch
Patch2:		cloop-2.06-x86-64-build-fix.patch
BuildRequires:	zlib-devel
%description
%{summary}

%prep
%setup -q -n %{clname}-%{clver}
%patch0 -p1 -b .write
%patch1 -b .cflags
%patch2 -p1 -b .x86-64

%build
%make utils

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

