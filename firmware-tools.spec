Name:           firmware-tools 
Version:        1.5.6
Release:        %mkrel 2
Summary:        Scripts and tools to manage firmware and BIOS updates
Group:          System/Kernel and hardware
License:        GPLv2+ or OSL
URL:            http://linux.dell.com/libsmbios/download/ 
Source0:        http://linux.dell.com/libsmbios/download/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python-devel
Requires:       rpm-python
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
The firmware-tools project provides tools to inventory hardware and a plugin
architecture so that different OEM vendors can provide different inventory
components. It is intended to tie to the package system to enable seamless
installation of updated firmware via your package manager, as well as provide
a framework for BIOS and firmware updates.

%prep
%setup -q

find . -type f | xargs perl -pi -e 's|#!/usr/bin/python2|#!/usr/bin/python|'

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/firmware/firmware.d/
mkdir -p %{buildroot}/%{_datadir}/firmware

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING-GPL COPYING-OSL README
%{python_sitelib}/*
%{_bindir}/*
%{_datadir}/firmware-tools/
%dir %{_sysconfdir}/firmware
%dir %{_sysconfdir}/firmware/firmware.d
%config(noreplace) %{_sysconfdir}/firmware/firmware.conf
%{_datadir}/firmware/


