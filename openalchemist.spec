Name:          openalchemist
Version:       0.2
Release:       %mkrel 5
Summary:       Free clone of naturalchimie
License:       GPLv2+
Group:         Games/Strategy
Url:           http://openalchemist.sourceforge.net/index.html
Source:        http://nchc.dl.sourceforge.net/sourceforge/openalchemist/%name-%version-src.tar.gz 
Patch0:        openalchemist-0.2-fix-build.patch
Patch1:        openalchemist-0.2-fixMakefile.patch
BuildRoot:     %{_tmppath}/%{name}-buildroot

BuildRequires: clanlib-devel >= 0.8 
BuildRequires: zip

%description
OpenAlchemist is a new game project developped with C++ language and 
Clanlib framework. 
Our goal is to reimplement the game www.naturalchimie.com with free 
softwares and with free licenses (GNU GPL for code and Creative 
Commons for graphics).

%files 
%defattr(-,root,root,0755)
%{_gamesbindir}/openalchemist/openalchemist
%{_gamesbindir}/openalchemist/skins/aqua.zip
%{_gamesbindir}/openalchemist/skins/brushed.zip
%{_datadir}/applications/mandriva-%{name}.desktop

#--------------------------------------------------------------------


%prep
%setup -q -n %name-%version-src
%patch0 -p0
%patch1 -p0

%build
%make 

%install
rm -fr %buildroot
%makeinstall_std

#XDG Menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=OpenAlchemist
Comment=Free Clone of Naturalchimie
Exec=%{_gamesbindir}/%name/%{name} 
Icon=strategy_section
Terminal=false
Type=Application
Categories=Game;LogicGame;BlocksGame;
EOF

%clean
rm -rf %buildroot
