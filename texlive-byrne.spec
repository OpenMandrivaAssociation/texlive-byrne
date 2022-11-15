Name:		texlive-byrne
Version:	61943
Release:	1
Summary:	This package provides a set of tools to typeset geometric proofs in the style of Oliver Byrne's 1847 ed. of Euclid's "Elements"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/byrne
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/byrne.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/byrne.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is a LaTeX adaptation of a set of tools developed
for ConTeXt reproduction of Oliver Byrne's 1847 edition of the
first six books of Euclid's "Elements";
(https://github.com/jemmybutton/byrne-euclid). It consists of a
MetaPost library, responsible for all the drawing and a set of
LaTeX macros to conveniently use them. This package works with
LuaLaTeX and relies on luamplib v2.23.0 or higher.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/byrne
%{_texmfdistdir}/metapost/byrne
%doc %{_texmfdistdir}/doc/metapost/byrne

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
