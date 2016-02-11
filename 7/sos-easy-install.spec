Summary: A simple GUI program that enables you to install additional software, such as Skype, Chrome, Steam, etc.
Summary(bg): Прост графичен потребителски интерфейс който позволява да се инсталира допълнителен софтуер като Skype, Chrome, Steam и др.
Name: sos-easy-install
Version: 2.2
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
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

install -m 755 %{name} ${RPM_BUILD_ROOT}%{_bindir}
install -Dpm 644 %{name}.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
install -Dpm 644 sosEI-header.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/sosEI-header.png
install -Dpm 644 sos-easy-install.png ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/48x48/apps/sos-easy-install.png
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

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%defattr(-,root,root)
%attr(755,root,root) 
%doc README.md COPYING
%{_bindir}/%{name}
%{_sbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/sosEI-header.png
%{_datadir}/icons/hicolor/48x48/apps/sos-easy-install.png
%{_datadir}/icons/sos-ei-app-icons
%{_datadir}/licenses/%{name}/COPYING
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/security/console.apps/%{name}

%changelog
* Tue Feb 09 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 2.2-1
- update to 2.2

* Thu Feb 04 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 2.1-1
- Initial spec
