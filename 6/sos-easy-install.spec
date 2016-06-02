Summary: A simple GUI program that enables you to install additional software, such as Skype, Chrome, Steam, etc.
Summary(bg): Прост графичен потребителски интерфейс който позволява да се инсталира допълнителен софтуер като Skype, Chrome, Steam и др.
Name: sos-easy-install
Version: 2.1
Release: 1%{?dist}.sos
URL: http://stotinkaos.net
License: GPLv3
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-root
Requires: bash 
Requires: coreutils 
Requires: wget 
Requires: yad
Requires: yum-utils
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

%description
%{summary}.

%description -l bg
Програма която позволява да се инсталира допълнителен софтуер като Skype, Chrome, Steam и др.., 
също така, дава възможност да настройте допълнително вашата StotinkaOS, само с няколко щраквания на мишката.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin

install -m 755 %{name} ${RPM_BUILD_ROOT}%{_bindir}
install -Dpm 644 %{name}.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
install -Dpm 644 sosEI-header.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/sosEI-header.png
install -Dpm 644 sos-Easy-Install.png ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/96x96/apps/sos-Easy-Install.png
install -d -m755 %{RPM_BUILD_ROOT}%{_datadir}/icons/
cp -pr sos-ei-app-icons/ ${RPM_BUILD_ROOT}%{_datadir}/icons/
install -Dpm 644 COPYING ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/COPYING 

# Adjust for console-helper magic
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mv ${RPM_BUILD_ROOT}%{_bindir}/%{name} ${RPM_BUILD_ROOT}%{_sbindir}/%{name}
ln -s ../bin/consolehelper ${RPM_BUILD_ROOT}%{_bindir}/%{name}
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d
cp %{name}.pam ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d/%{name}
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/security/console.apps
cp %{name}.console ${RPM_BUILD_ROOT}%{_sysconfdir}/security/console.apps/%{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%attr(755,root,root) 
%doc README.md COPYING
%{_bindir}/%{name}
%{_sbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/sosEI-header.png
%{_datadir}/icons/hicolor/96x96/apps/sos-Easy-Install.png
%{_datadir}/icons/sos-ei-app-icons
%{_datadir}/licenses/%{name}/COPYING
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/security/console.apps/%{name}

%changelog

