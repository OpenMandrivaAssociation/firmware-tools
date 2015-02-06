Name:		firmware-tools
Version:	2.1.14
Release:	3
Summary:	Scripts and tools to manage firmware and BIOS updates
Group:		System/Kernel and hardware
License:	GPLv2+
URL:		http://linux.dell.com/libsmbios/download/ 
Source0:	http://linux.dell.com/libsmbios/download/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	python-devel
Requires:	python-rpm
BuildArch:	noarch

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
%configure2_5x

%make

%install
%makeinstall_std
mkdir -p %{buildroot}/%{_sysconfdir}/firmware/firmware.d/
mkdir -p %{buildroot}/%{_datadir}/firmware

%files
%doc COPYING-GPL COPYING-OSL README
%{python_sitelib}/*
%{_sbindir}/*
%{_datadir}/firmware-tools/
%dir %{_sysconfdir}/firmware
%dir %{_sysconfdir}/firmware/firmware.d
%config(noreplace) %{_sysconfdir}/firmware/firmware.conf
%{_datadir}/firmware/
