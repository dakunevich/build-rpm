Name:           HelloWorld
Version:        1.0 
Release:        1%{?dist}
Summary:        Hello World Script
Group:          Miscellaneous

License:        License text
#URL:            
Source0:        HelloWorld-1.0.tar.gz
BuildArch:      noarch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

AutoReq:        no

%description
This is a text describing what the Package is meant for


%prep

%setup -q

#%autosetup


%build
#%configure
#%make_build


%install
rm -rf $RPM_BUILD_ROOT
#%make_install
#install -d -m 0755 $RPM_BUILD_ROOT/opt/HelloWorld
#install -m 0755 HelloWorld.sh $RPM_BUILD_ROOT/opt/HelloWorld/*
mkdir -p $RPM_BUILD_ROOT/opt/HelloWorld
cp -r ./* $RPM_BUILD_ROOT/opt/HelloWorld/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir /opt/HelloWorld

%defattr(-,root,root,-)

#%license add-license-file-here
#%doc add-docs-here

/opt/HelloWorld/*

%changelog
* Sun Mar 17 2019 DzmitryA
- 
