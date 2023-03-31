Name:		texlive-globalvals
Version:	49962
Release:	2
Summary:	Declare global variables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/globalvals
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/globalvals.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/globalvals.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows the user to declare a variable which can
then be used anywhere else in a document, including before it
was declared.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/globalvals
%doc %{_texmfdistdir}/doc/latex/globalvals

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
