%define clname	cloop
%define minver	1

Summary:	Utilities for the creation and extraction of compressed loop images
Name:		%{clname}-utils
Version:	2.625
Release:	12
License:	GPLv2
Group:		File tools
Url:		http://debian-knoppix.alioth.debian.org/sources/
Source0:	http://debian-knoppix.alioth.debian.org/sources/%{clname}_%{version}-%{minver}.tar.gz
Patch0:		cloop-2.06-write-to-file-ASAP.patch
Patch1:		mkfile-cloop.patch
Patch2:		cloop_2.625-gcc43.patch
BuildRequires:	pkgconfig(zlib)

%description
%{summary}.

%prep
%setup -qn %{clname}-%{version}
%autopatch -p1

%build
%make utils

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 create_compressed_fs %{buildroot}/usr/bin
install -m 755 extract_compressed_fs %{buildroot}/usr/bin

%files
%doc CHANGELOG README
%{_bindir}/create_compressed_fs
%{_bindir}/extract_compressed_fs

