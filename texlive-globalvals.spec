%global tl_name globalvals
%global tl_revision 49962

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Declare global variables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/globalvals
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/globalvals.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/globalvals.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows the user to declare a variable which can then be
used anywhere else in a document, including before it was declared.

