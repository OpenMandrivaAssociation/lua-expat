%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define oname luaexpat

Name:           lua-expat
Version:        1.2.0
Release:        %mkrel 1
Summary:        SAX XML parser based on expat, for lua
Group:          Development/Other
License:        MIT
URL:            http://www.keplerproject.org/luaexpat/
Source0:        http://luaforge.net/frs/download.php/2469/%{oname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  lua >= %{luaver}, lua-devel >= %{luaver}
BuildRequires:  expat-devel
Requires:       lua >= %{luaver}
%description
SAX XML parser based on expat, for lua.

%prep
%setup -q -n %{oname}-%{version}

%build
perl -pi -e 's/(CFLAGS =)/$1 -fPIC/' config
echo 'LUA_VERSION_NUM=501' >> config 
%make 

%install
rm -rf %{buildroot}
make install LUA_LIBDIR=$RPM_BUILD_ROOT%{lualibdir} LUA_DIR=$RPM_BUILD_ROOT%{luapkgdir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README  doc/us/*
%{lualibdir}/*
%{luapkgdir}/*
