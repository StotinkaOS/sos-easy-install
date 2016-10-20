Summary: A simple GUI program that enables you to install additional software, such as Skype, Chrome, Steam, etc.
Summary(bg): Прост графичен потребителски интерфейс който позволява да се инсталира допълнителен софтуер като Skype, Chrome, Steam и др.
Name: sos-easy-install
Version: 3.2
Release: 1%{?dist}
URL: http://stotinkaos.net
License: GPLv3
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: libappstream-glib
Requires: bash
Requires: coreutils
Requires: wget
Requires: yad
Requires: yum-utils
Source0: %{name}-%{version}.tar.gz

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
mkdir -p %{buildroot}/usr/bin/%{name}-plugins
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/appdata

install -m 755 %{name} ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 %{name}-pkexec ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 global ${RPM_BUILD_ROOT}%{_bindir}/%{name}-plugins/
cp -pr plugins/ ${RPM_BUILD_ROOT}%{_bindir}/%{name}-plugins/plugins
cp -pr menu/ ${RPM_BUILD_ROOT}%{_bindir}/%{name}-plugins/menu
install -m 644 org.freedesktop.%{name}.policy ${RPM_BUILD_ROOT}%{_datadir}/polkit-1/actions/org.freedesktop.%{name}.policy
install -Dpm 644 %{name}.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
install -m 644 %{name}.appdata.xml ${RPM_BUILD_ROOT}%{_datadir}/appdata/%{name}.appdata.xml
install -Dpm 644 sos-easy-install.png ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/96x96/apps/sos-easy-install.png
install -d -m755 %{RPM_BUILD_ROOT}%{_datadir}/icons/
cp -pr sos-ei-app-icons/ ${RPM_BUILD_ROOT}%{_datadir}/icons/
install -Dpm 644 COPYING ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/COPYING

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    /usr/bin/update-desktop-database &>/dev/null ||:
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database &>/dev/null ||:

%files
%defattr(-,root,root)
%attr(755,root,root)
%doc README.md COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-pkexec
%{_bindir}/%{name}-plugins/menu
%{_bindir}/%{name}-plugins/plugins
%{_bindir}/%{name}-plugins/global
%{_datadir}/polkit-1/actions/org.freedesktop.%{name}.policy
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/96x96/apps/%{name}.png
%{_datadir}/icons/sos-ei-app-icons
%{_datadir}/licenses/%{name}/COPYING

%changelog
* Thu Oct 20 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 3.2-1
- Update to 3.2

* Wed Oct 05 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 3.1-1
- Update to 3.1

* Thu Sep 22 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 3.0-1
- Update to 3.0

* Wed Aug 17 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 2.9-1
- Update to 2.9

* Sat Jul 16 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 2.7-1
- Update to 2.7

* Sun May 15 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 2.6-1
- Update to 2.6

* Mon May 09 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 2.5-1
- Update to 2.5

* Mon Mar 28 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 2.4-1
- Update to 2.4

* Fri Mar 25 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 2.3-1
- Update to 2.3

* Tue Feb 09 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 2.2-1
- update to 2.2

* Thu Feb 04 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 2.1-1
- Initial spec

