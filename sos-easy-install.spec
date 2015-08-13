Summary: A simple GUI program that enables you to install additional software, such as Skype, Chrome, Steam, etc.
Summary(bg): Прост графичен потребителски интерфейс който позволява да се инсталира допълнителен софтуер като Skype, Chrome, Steam и др.
Name: sos-easy-install
Version: 1.6
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
Програма която позволява да се инсталира допълнителен софтуер като Skype, Chrome, Steam и др.., също така, дава възможност да настройте допълнително вашата StotinkaOS, само с няколко щраквания на мишката.

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

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%attr(755,root,root) 
%doc README.md COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/sosEI-header.png
%{_datadir}/icons/hicolor/96x96/apps/sos-Easy-Install.png
%{_datadir}/icons/sos-ei-app-icons
%{_datadir}/licenses/%{name}/COPYING

%changelog
* Thu Aug 13 2015 Ivaylo Kuzev <ivo@stotinkaos.net> - 1.6-1
- Revert to place all dialogs at center of the screen
- Update broken Dropbox links

* Fri Aug 07 2015 Ivaylo Kuzev <ivo@stotinkaos.net> - 1.5-1
- Add autoLogin func

* Tue Aug 04 2015 Ivaylo Kuzev <ivo@stotinkaos.net> - 1.4-1
- Fix Bug with installPackage

* Mon Aug 03 2015 Ivaylo Kuzev <ivo@stotinkaos.net> - 1.3-1
- Update to version 1.3
- Add Java and Video drivers install
- Add new install dialog 

* Tue Jul 28 2015 Ivaylo Kuzev <ivo@stotinkaos.net> - 1.2-1
- Do not resize the main menu 
- Ask to remove packages
- Fix version number 
- Place all dialogs at the position where mouse cursor is
- Allow to select the text from a about dialog

* Mon Jul 27 2015 Ivaylo Kuzev <ivo@stotinkaos.net> - 1.1.1
- Fix Steam and protected multilib packages

* Sun Jul 26 2015 Ivaylo Kuzev <ivo@stotinkaos.net> - 1.0-1
- Initial spec
