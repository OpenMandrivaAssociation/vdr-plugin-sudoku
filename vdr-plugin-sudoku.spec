%define plugin	sudoku

Summary:	VDR plugin: Sudoku - generate and solve Number Place puzzles
Name:		vdr-plugin-%plugin
Version:	0.3.5
Release:	4
Group:		Video
License:	GPL
URL:		http://toms-cafe.de/vdr/sudoku/
Source:		http://toms-cafe.de/vdr/sudoku/vdr-%plugin-%{version}.tgz
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
%setup -q -n %plugin-%{version}
%patch0 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build
%make -C tools CXXFLAGS="%{optflags} %ldflags"

%install
%vdr_plugin_install
%makeinstall -C tools

%files -f %plugin.vdr
%doc README HISTORY
%{_bindir}/sudoku_generator
%{_mandir}/man1/sudoku_generator.1*



