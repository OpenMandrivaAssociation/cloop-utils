%define clname      cloop
%define clver       2.625
%define clminorver  1

Name:		%{clname}-utils
Version:	%{clver}
Release:	%{mkrel 1}
Summary:	Utilities for the creation and extraction of compressed loop images
License:	GPLv2
Group:		File tools
URL:		http://debian-knoppix.alioth.debian.org/sources/
Source0:	http://debian-knoppix.alioth.debian.org/sources/%{clname}_%{clver}-%{clminorver}.tar.gz
Patch0:		cloop-2.06-write-to-file-ASAP.patch
Patch1:		mkfile-cloop.patch
Patch2:		cloop_2.625-gcc43.patch
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-root

%description
%{summary}.

%prep
%setup -q -n %{clname}-%{clver}
%patch0 -p1 -b .write
%patch1 -b .cflags
%patch2 -p1 -b .gcc43

%build
%make utils

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
install -m 755 create_compressed_fs %{buildroot}/usr/bin
install -m 755 extract_compressed_fs %{buildroot}/usr/bin

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG README
%{_bindir}/create_compressed_fs
%{_bindir}/extract_compressed_fs

