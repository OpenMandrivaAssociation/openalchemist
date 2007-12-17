Name:          openalchemist
Version:       0.2
Release:       %mkrel 2
Summary:       Free clone of naturalchimie
License:       GPL
Group:         Games/Strategy
Url:           http://openalchemist.sourceforge.net/index.html
Source:        %name-%version-src.tar.gz 
Patch0:        %name-%version-fix-build.patch
Patch1:        %name-%version-fixMakefile.patch

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
rm -rf %buildroot

%setup -q -n %name-%version-src
%patch0 -p0
%patch1 -p0

%build

%make 

%install
make DESTDIR=%buildroot install

#XDG Menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=OpenAlchemist
Comment= Free Clone of Naturalchimie
Exec=%{_bindir}/%name/%{name} 
Icon=strategy_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Puzzles;Game;LogicGame;BlocksGame;
EOF

%clean
rm -rf %buildroot


