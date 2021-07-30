Summary:	A unix pager optimized for psql
Name:		pspg
Version:	5.3.1
Release:	1
License:	BSD
URL:		https://github.com/okbob/%{name}
Source:		https://github.com/okbob/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: ncurses-devel 
BuildRequires: readline-devel
BuildRequires: pkgconfig(libpq)

%description
pspg is a unix pager optimized for psql. It can freeze rows, freeze
columns, and lot of color themes are included.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc README.md LICENSE
%{_bindir}/*
