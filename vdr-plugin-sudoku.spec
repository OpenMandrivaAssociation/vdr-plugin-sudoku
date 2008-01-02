
%define plugin	sudoku
%define name	vdr-plugin-%plugin
%define version	0.1.3
%define rel	5

Summary:	VDR plugin: Sudoku - generate and solve Number Place puzzles
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://toms-cafe.de/vdr/sudoku/
Source:		http://toms-cafe.de/vdr/sudoku/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
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

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


