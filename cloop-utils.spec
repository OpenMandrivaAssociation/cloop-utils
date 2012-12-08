%define clname      cloop
%define clver       2.625
%define clminorver  1

Name:		%{clname}-utils
Version:	%{clver}
Release:	%mkrel 2
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



%changelog
* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 2.625-2mdv2011.0
+ Revision: 672337
- rebuild

* Tue Dec 09 2008 Adam Williamson <awilliamson@mandriva.org> 2.625-1mdv2011.0
+ Revision: 312136
- add gcc43.patch (fix build with gcc 4.3)
- drop x86-64-build-fix.patch (no longer needed)
- new release 2.625

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 2.06-2mdv2008.1
+ Revision: 149122
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Apr 25 2007 Adam Williamson <awilliamson@mandriva.org> 2.06-1mdv2008.0
+ Revision: 18342
- 2.06 (rebuild for new era)
- clean spec
- add new patch2 (fix x86-64, fix from Andreas Jochens debian bug 288941)
- drop old patch2 (no longer needed)
- rediff patch0 and patch1


* Fri May 12 2006 Stefan van der Eijk <stefan@eijk.nu> 1.02-9mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.02-8mdk
- Rebuild

* Mon Feb 21 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.02-7mdk
- fix patch2, aka fix fix x86_64 build

* Sat Nov 27 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.02-6mdk
- Patch2: fix ppc build

* Mon Jan 12 2004 Franck Villaume <fvill@freesurf.fr> 1.02-5mdk
- add sparc support by using RPM_OPT_FLAGS support : patch1
- remove gcc as buildrequires

* Fri Oct 31 2003 Jaco Greeff <jaco@linuxminicd.org> 1.02-4mdk
- fix create_compressed_fs (broken in 3mdk) to once again make it work when
  receiving input from stdin: numblocks was wrong (!= 0, == 1), creating
  corrupted cloop images from an invalid write (which should have been ignored)
  in create_compressed_blocks (corruption reported by Avery J. Parker on the
  mklivecd list)
- update create_compressed_fs to display better help information for all options

* Tue Oct 21 2003 Pixel <pixel@mandrakesoft.com> 1.02-3mdk
- fix create_compressed_fs (estimated_numblocks was wrong in a limit case)
- fix build (using APPSONLY=1)

* Thu Oct 16 2003 Pixel <pixel@mandrakesoft.com> 1.02-2mdk
- add a patch to be memory conservative. You don't need to have enough
  ram+swap to contain the full cloop anymore. The drawback is that you need to
  give an estimated size of the non compressed file if you use stdin

* Mon Sep 01 2003 Jaco Greeff <jaco@linuxminicd.org> 1.02-1mdk
- Initial version, 1.02-1

