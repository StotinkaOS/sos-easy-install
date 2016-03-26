Summary: A simple GUI program that enables you to install additional software, such as Skype, Chrome, Steam, etc.
Summary(bg): Прост графичен потребителски интерфейс който позволява да се инсталира допълнителен софтуер като Skype, Chrome, Steam и др.
Name: sos-easy-install
Version: 2.3
Release: 1%{?dist}
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
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

install -m 755 %{name} ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 %{name}-pkexec ${RPM_BUILD_ROOT}%{_bindir}
install -m 644 org.freedesktop.%{name}.policy ${RPM_BUILD_ROOT}%{_datadir}/polkit-1/actions/org.freedesktop.%{name}.policy
install -Dpm 644 %{name}.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
install -Dpm 644 sosEI-header.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/sosEI-header.png
install -Dpm 644 sos-easy-install.png ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/96x96/apps/sos-easy-install.png
install -d -m755 %{RPM_BUILD_ROOT}%{_datadir}/icons/
cp -pr sos-ei-app-icons/ ${RPM_BUILD_ROOT}%{_datadir}/icons/
install -Dpm 644 COPYING ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/COPYING 

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
%{_bindir}/%{name}-pkexec
%{_datadir}/polkit-1/actions/org.freedesktop.%{name}.policy
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/sosEI-header.png
%{_datadir}/icons/hicolor/96x96/apps/%{name}.png
%{_datadir}/icons/sos-ei-app-icons
%{_datadir}/licenses/%{name}/COPYING

%changelog
* Fri Mar 25 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 2.3-1
- Update to 2.3

* Tue Feb 09 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 2.2-1
- update to 2.2

* Thu Feb 04 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 2.1-1
- Initial spec
