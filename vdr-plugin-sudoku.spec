
%define plugin	sudoku
%define name	vdr-plugin-%plugin
%define version	0.3.5
%define rel	2

Summary:	VDR plugin: Sudoku - generate and solve Number Place puzzles
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://toms-cafe.de/vdr/sudoku/
Source:		http://toms-cafe.de/vdr/sudoku/vdr-%plugin-%version.tgz
# Fixes build (04/2008)
Patch0:		sudoku-0.2.1-makefile.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
'Sudoku' is a VDR plugin to generate and solve Number Place puzzles, so called
Sudokus.

A Sudoku puzzle consists of 9 x 9 cells subdivided into 9 regions with 3 x 3
cells. The rules are simple. There have to be the numbers from 1 to 9 in every
row, column and region. In the beginning some numbers are given. These cells
are painted with cyan background color. The aim of the puzzle is to find the
missing numbers. There is only one solution of a Sudoku puzzle.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build
%make -C tools CXXFLAGS="%optflags %ldflags"

%install
%vdr_plugin_install
%makeinstall -C tools

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%{_bindir}/sudoku_generator
%{_mandir}/man1/sudoku_generator.1*



%changelog
* Sun Aug 15 2010 Anssi Hannula <anssi@mandriva.org> 0.3.5-1mdv2011.0
+ Revision: 569840
- new version
- drop unneeded hunk from makefile.patch

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.3.4-2mdv2011.0
+ Revision: 401088
- rebuild for new VDR

* Tue Jul 14 2009 Anssi Hannula <anssi@mandriva.org> 0.3.4-1mdv2010.0
+ Revision: 395758
- new version
- include sudoku_generator tool

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.2.1-3mdv2009.1
+ Revision: 359370
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.2.1-2mdv2009.0
+ Revision: 197982
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.2.1-1mdv2009.0
+ Revision: 197727
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- fix makefile for build (P0)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.3-6mdv2008.1
+ Revision: 145207
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.3-5mdv2008.1
+ Revision: 103217
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.3-4mdv2008.0
+ Revision: 50051
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.3-3mdv2008.0
+ Revision: 42134
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.3-2mdv2008.0
+ Revision: 22703
- rebuild for new vdr


* Tue Feb 27 2007 Anssi Hannula <anssi@mandriva.org> 0.1.3-1mdv2007.0
+ Revision: 126273
- 0.1.3

* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-10mdv2007.1
+ Revision: 90976
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-9mdv2007.1
+ Revision: 74087
- rebuild for new vdr
- Import vdr-plugin-sudoku

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-8mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-7mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-6mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-5mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-4mdv2007.0
- rebuild for new vdr

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-3mdv2007.0
- rebuild for new vdr

* Sat Jun 03 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-2mdv2007.0
- fix URL

* Sat Jun 03 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-1mdv2007.0
- initial Mandriva release

