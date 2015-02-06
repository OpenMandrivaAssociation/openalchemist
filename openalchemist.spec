Name:		openalchemist
Version:	0.3
Release:	5
Summary:	Free clone of naturalchimie (puzzle game)
License:	GPLv2+
Group:		Games/Puzzles
URL:		http://openalchemist.sourceforge.net/index.html
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz 
BuildRequires:	clanlib0.8-devel
BuildRequires:	zip

%description
OpenAlchemist is a new game project developed with C++ language and 
Clanlib framework. 
Our goal is to reimplement the game www.naturalchimie.com with free 
softwares and with free licenses (GNU GPL for code and Creative 
Commons for graphics).

%prep
%setup -q -n %{name}-%{version}-src

%build
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make 

%install
%makeinstall_std

#Menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=OpenAlchemist
Comment=Free Clone of Naturalchimie
Exec=%{_gamesbindir}/%{name}
Icon=strategy_section
Terminal=false
Type=Application
Categories=Game;LogicGame;BlocksGame;
EOF

%files 
%defattr(-,root,root,0755)
%{_gamesbindir}/%{name}
%{_gamesbindir}/%{name}-config
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

