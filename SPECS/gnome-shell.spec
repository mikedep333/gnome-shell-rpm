Name:           gnome-shell
Version:        3.26.2
Release:        5.0.1.cdc_integration%{?dist}
Summary:        Window management and application launching for GNOME

Group:          User Interface/Desktops
License:        GPLv2+
Provides:       desktop-notification-daemon
URL:            https://wiki.gnome.org/Projects/GnomeShell
#VCS:           git:git://git.gnome.org/gnome-shell
Source0:        http://download.gnome.org/sources/gnome-shell/3.26/%{name}-%{version}.tar.xz
Source1:        org.gnome.shell.gschema.override
# Fixes the Centrify issue without a dependency on the gnome-screensaver
# package.
Source20: gnome-screensaver.cdc_integration

# Replace Epiphany with Firefox in the default favourite apps list
Patch1: gnome-shell-favourite-apps-firefox.patch
Patch2: gnome-shell-favourite-apps-yelp.patch
Patch3: gnome-shell-favourite-apps-terminal.patch

# el7 build fixes
Patch5: 0001-Revert-build-Drop-autotools-support.patch
Patch6: 0002-Revert-build-Remove-included-Makefiles-as-well.patch
Patch7: 0003-build-Remove-check-for-missing-disthook.patch
Patch8: 0004-Revert-build-Use-new-mkenums_simple-function.patch

# GDM/Lock stuff
Patch10: 0001-gdm-honor-timed-login-delay-even-if-animations-disab.patch
Patch11: 0001-gdm-use-password-authentication-if-all-schemes-are-d.patch
Patch12: 0001-screenShield-unblank-when-inserting-smartcard.patch
Patch13: enforce-smartcard-at-unlock.patch
Patch14: disable-unlock-entry-until-question.patch
Patch15: allow-timed-login-with-no-user-list.patch
Patch16: 0001-data-install-process-working.svg-to-filesystem.patch
Patch17: 0001-loginDialog-make-info-messages-themed.patch
Patch18: 0001-gdm-add-AuthList-control.patch
Patch19: 0002-gdmUtil-enable-support-for-GDM-s-ChoiceList-PAM-exte.patch
Patch20: 0001-loginDialog-only-emit-session-activated-on-user-acti.patch

# Misc.
Patch30: 0001-shellDBus-Add-a-DBus-method-to-load-a-single-extensi.patch
Patch31: 0001-extensions-Add-a-SESSION_MODE-extension-type.patch
Patch32: 0001-magnifier-don-t-spew-to-console-when-focus-moves-aro.patch
Patch33: 0001-extensionSystem-Notify-about-extension-issues-on-upd.patch
Patch34: 0001-panel-add-an-icon-to-the-ActivitiesButton.patch
Patch35: 0001-app-Fall-back-to-window-title-instead-of-WM_CLASS.patch
Patch36: 0001-windowMenu-Bring-back-workspaces-submenu-for-static-.patch
Patch37: 0001-global-Allow-overriding-the-override-schema.patch
Patch38: 0001-system-don-t-throw-an-exception-if-power-off-disable.patch
Patch39: 0001-padOsd-Ensure-to-pick-pad-devices-only.patch

# Fix Centrify smartcard switch-user issue
# https://bugzilla.redhat.com/show_bug.cgi?id=1238342
# https://centrify.force.com/support/Article/KB-7415-Unable-to-unlock-screen-with-Smart-Card-on-RHEL-7/
patch50: 0001-gdm-Set-the-PAM-smartcard-service-name-for-gnome-scr.patch

%define gnome_bluetooth_version 1:3.9.0
%define gobject_introspection_version 1.45.4
%define gjs_version 1.47.0
%define mutter_version 3.25.90
%define gtk3_version 3.15.0
%define eds_version 3.13.90
%define gnome_desktop_version 3.7.90
%define json_glib_version 0.13.2
%define gsettings_desktop_schemas_version 3.21.3
%define caribou_version 0.4.8
%define libcroco_version 0.6.8
%define telepathy_logger_version 0.2.6
%define gstreamer_version 1.4.5

## Needed when we re-autogen
BuildRequires:  autoconf >= 2.53
BuildRequires:  automake >= 1.10
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  gnome-common >= 2.2.0
BuildRequires:  libtool >= 1.4.3
BuildRequires:  caribou-devel >= %{caribou_version}
BuildRequires:  chrpath
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  evolution-data-server-devel >= %{eds_version}
BuildRequires:  gcr-devel
BuildRequires:  gjs-devel >= %{gjs_version}
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection >= %{gobject_introspection_version}
BuildRequires:  json-glib-devel >= %{json_glib_version}
BuildRequires:  upower-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  libnm-gtk-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  NetworkManager-glib-devel
BuildRequires:  polkit-devel
BuildRequires:  startup-notification-devel
BuildRequires:  telepathy-glib-devel
BuildRequires:  telepathy-logger-devel >= %{telepathy_logger_version}
# for screencast recorder functionality
BuildRequires:  gstreamer1-devel >= %{gstreamer_version}
BuildRequires:  gtk3-devel >= %{gtk3_version}
BuildRequires:  gettext >= 0.19.6
BuildRequires:  libcanberra-devel
BuildRequires:  libcroco-devel >= %{libcroco_version}
%if 0%{?rhel}
BuildRequires:  python
%else
BuildRequires:  python3
%endif

# for barriers
BuildRequires:  libXfixes-devel >= 5.0
# used in unused BigThemeImage
BuildRequires:  librsvg2-devel
BuildRequires:  mutter-devel >= %{mutter_version}
BuildRequires:  pulseaudio-libs-devel
%ifnarch s390 s390x ppc ppc64 ppc64p7
BuildRequires:  gnome-bluetooth-libs-devel >= %{gnome_bluetooth_version}
%endif
BuildRequires:  control-center
# Bootstrap requirements
BuildRequires: gtk-doc gnome-common
%ifnarch s390 s390x
Requires:       gnome-bluetooth%{?_isa} >= %{gnome_bluetooth_version}
%endif
Requires:       gnome-desktop3%{?_isa} >= %{gnome_desktop_version}
# wrapper script uses to restart old GNOME session if run --replace
# from the command line
Requires:       gobject-introspection%{?_isa} >= %{gobject_introspection_version}
Requires:       gjs%{?_isa} >= %{gjs_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}
# needed for loading SVG's via gdk-pixbuf
Requires:       librsvg2%{?_isa}
# needed as it is now split from Clutter
Requires:       json-glib%{?_isa} >= %{json_glib_version}
# For $libdir/mozilla/plugins
Requires:       mozilla-filesystem%{?_isa}
Requires:       mutter%{?_isa} >= %{mutter_version}
Requires:       upower%{?_isa}
Requires:       polkit%{?_isa} >= 0.100
Requires:       gnome-desktop3%{?_isa} >= %{gnome_desktop_version}
Requires:       gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires:       libcroco%{?_isa} >= %{libcroco_version}
Requires:       telepathy-logger%{?_isa} >= %{telepathy_logger_version}
Requires:       gstreamer1%{?_isa} >= %{gstreamer_version}
# needed for schemas
Requires:       at-spi2-atk%{?_isa}
# needed for on-screen keyboard
Requires:       caribou%{?_isa} >= %{caribou_version}
# needed for the user menu
Requires:       accountsservice-libs%{?_isa}
Requires:       gdm-libs%{?_isa}
# needed for settings items in menus
Requires:       control-center
# needed by some utilities
%if 0%{?rhel}
Requires:       python%{_isa}
%else
Requires:       python3%{_isa}
%endif
# needed for the dual-GPU launch menu
#Requires:       switcheroo-control
# needed for clocks/weather integration
Requires:       geoclue2-libs%{?_isa}
Requires:       libgweather%{?_isa}

%description
GNOME Shell provides core user interface functions for the GNOME 3 desktop,
like switching to windows and launching applications. GNOME Shell takes
advantage of the capabilities of modern graphics hardware and introduces
innovative user interface concepts to provide a visually attractive and
easy to use experience.

%package browser-plugin
Summary: Browser plugin to install extensions from extensions.gnome.org
Requires: %{name} = %{version}-%{release}
Requires: mozilla-filesystem%{?_isa}

%description browser-plugin
The "GNOME Shell Integration" plugin provides integration with
Gnome Shell for live extension enabling and disabling. It can
be used only by extensions.gnome.org.

%prep
%autosetup -S git

%build
%if 0%{?rhel}
# Use Python 2
sed -i -e 's/AM_PATH_PYTHON(\[3\])/AM_PATH_PYTHON([2.5])/' configure.ac
autoreconf -fi
%endif

(if ! test -x configure; then NOCONFIGURE=1 ./autogen.sh; fi;
 %configure --disable-static --disable-compile-warnings)
make V=1 %{?_smp_mflags}

%install
%make_install

rm -rf %{buildroot}/%{_libdir}/mozilla/plugins/*.la

# Create empty directories where other packages can drop extensions
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions
mkdir -p %{buildroot}%{_datadir}/gnome-shell/search-providers

cp %{SOURCE1} %{buildroot}/%{_datadir}/glib-2.0/schemas

%find_lang %{name}

mkdir -p %{buildroot}/%{_sysconfdir}/pam.d
cp %{SOURCE20} %{buildroot}/%{_sysconfdir}/pam.d/gnome-screensaver.cdc_integration

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Shell.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/gnome-shell-extension-prefs.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/evolution-calendar.desktop

%preun
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas &> /dev/null ||:

%post
if [ ! -e "%{_sysconfdir}/pam.d/gnome-screensaver" ]; then
 cp -p %{_sysconfdir}/pam.d/gnome-screensaver.cdc_integration %{_sysconfdir}/pam.d/gnome-screensaver
 if [ -e "%{_sysconfdir}/pam.d/smartcard-auth-ac.cdc" ]; then
  echo "gnome-shell has been updated with the fix for CentrifyDC smartcard integration, gnome-screensaver does not appear to be installed, and Centrify smartcard support appers to be enabled. You need to re-apply CentrifyDC smart-card support (and log out of & back into gnome) for the fix to take effect. You can reapply it by running 'sctool -d && sctool -e', restarting the adclient service, or rebooting." > /dev/stderr
 fi
fi

%posttrans
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas &> /dev/null ||:

%files -f %{name}.lang
%license COPYING
%doc README
%{_bindir}/gnome-shell
%{_bindir}/gnome-shell-extension-tool
%{_bindir}/gnome-shell-perf-tool
%{_bindir}/gnome-shell-extension-prefs
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/glib-2.0/schemas/*.override
%{_datadir}/applications/org.gnome.Shell.desktop
%{_datadir}/applications/gnome-shell-extension-prefs.desktop
%{_datadir}/applications/evolution-calendar.desktop
%{_datadir}/applications/org.gnome.Shell.PortalHelper.desktop
%{_datadir}/gnome-control-center/keybindings/50-gnome-shell-system.xml
%{_datadir}/gnome-shell
%{_datadir}/gnome-shell/theme
%{_datadir}/gnome-shell/theme/*.svg
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.PortalHelper.service
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.PadOsd.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
# Co own directory instead of pulling in xdg-desktop-portal - we
# are providing a backend to the portal, not depending on it
%dir %{_datadir}/xdg-desktop-portal/portals/
%{_datadir}/xdg-desktop-portal/portals/gnome-shell.portal
%{_libdir}/gnome-shell/
%{_libexecdir}/gnome-shell-calendar-server
%{_libexecdir}/gnome-shell-perf-helper
%{_libexecdir}/gnome-shell-hotplug-sniffer
%{_libexecdir}/gnome-shell-portal-helper
# Co own these directories instead of pulling in GConf
# after all, we are trying to get rid of GConf with these files
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/gnome-shell-overrides.convert
%{_mandir}/man1/%{name}.1.gz
# exclude as these should be in a devel package for st etc
%exclude %{_datadir}/gtk-doc
%{_sysconfdir}/pam.d/gnome-screensaver.cdc_integration

%files browser-plugin
%{_libdir}/mozilla/plugins/*.so

%changelog
* Thu Apr 12 2018 Mike DePaulo (GFDL) - 3.26.2-5.0.1.cdc_integration
- gdm: Set the PAM smartcard service name for gnome-screensaver if we are in a user session rather than gdm
- Fixes the need for Centrify smartcard users to select "switch user" to unlock their session.
  https://bugzilla.redhat.com/show_bug.cgi?id=1238342
  https://centrify.force.com/support/Article/KB-7415-Unable-to-unlock-screen-with-Smart-Card-on-RHEL-7/
- Install /etc/pam.d/gnome-screensaver.cdc_integration and only copy it to
  /etc/pam.d/gnome-screensaver if it DNE. This avoids the dependency on the
  gnome-screensaver package, but does not conflict with it.
- If it gets copied, print out that smartcard support needs to be re-applied.

* Wed Feb 14 2018 Ray Strode <rstrode@redhat.com> - 3.26.2-5
- Make session selection bullet isn't shown on wrong item
  Resolves: #1527145

* Tue Feb 13 2018 Ray Strode <rstrode@redhat.com> - 3.26.2-4
- Fix timed login
  Resolves: #1527143

* Wed Feb 07 2018 Carlos Garnacho <cgarnach@redhat.com> - 3.26.2-3
- Fix pad device lookup from event node path
  Resolves: #1537879

* Mon Nov 13 2017 Ray Strode <rstrode@redhat.com> - 3.26.2-2
- Don't throw an exception is poweroff is disabled
  Resolves: #1512662

* Fri Nov 03 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2
- Related: #1481381

* Thu Oct 26 2017 Florian Müllner <fmuellner@redhat.com> - 3.26.1-2
- Add CLI option to specify a custom override schema
  Resolves: #1432505

* Fri Oct 06 2017 Florian Müllner <fmuellner@redhat.com> - 3.26.1-1
- Update to 3.26.1
  Resolves: #1481381

* Wed Jul 26 2017 Ray Strode <rstrode@redhat.com> - 3.22.3-18
- Support GDM ChoiceList pam extensions
  Related: #1413900

* Mon Jun 26 2017 Ray Strode <rstrode@redhat.com> - 3.22.3-17
- Fix PAM info messages in unlock screen
  Related: #1449359

* Wed Jun 14 2017 Ray Strode <rstrode@redhat.com> - 3.22.3-16
- Address race with g-s-d startup
  Related: #1450176

* Wed Jun 14 2017 Ray Strode <rstrode@redhat.com> 3.22.3-15
- Allow PAM modules to ask questions that require empty answers
  Resolves: #1448503

* Thu Jun 08 2017 Ray Strode <rstrode@redhat.com> - 3.22.3-14
- fix unlock after upgrade
  Related: #1448786
- switch from setup to autosetup -S git for easier patch maintenance

* Thu Jun 08 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-13
- Drop gnome-session-xsession dependency again
- Resolves: #1449246

* Wed Jun 07 2017 Ray Strode <rstrode@redhat.com> - 3.22.3-12
- Fix escape after password failure
  Resolves: #1446759

* Tue Jun 06 2017 Ray Strode <rstrode@redhat.com> - 3.22.3-11
- Correct typo in timed login patch
  Related: #1446762

* Wed May 31 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-10
- Fix initial visibility of network summary items
- Resolves: #1435376

* Fri Apr 28 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-9
- Re-add requirements dropped in the rebase
- Resolves: #1386959

* Wed Mar 22 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-8
- Fix some coverity warnings
- Resolves: #1386959

* Tue Mar 21 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-7
- Respect lockscreen lockdown
- Resolves: #1414898

* Tue Mar 21 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-7
- Fix previous patch after re-testing
- Resolves: #1259538

* Tue Mar 14 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-6
- Handle missing fprint service
- Resolves: #1259538

* Tue Mar 14 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-5
- Close Wifi selection dialog on screen lock
- Resolves: #1379468

* Tue Mar 14 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-4
- Keep VPN list sorted
- Resolves: #1404663

* Tue Mar 14 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-3
- Bring back workspaces submenu for static workspaces
- Resolves: #1367319

* Thu Mar 09 2017 Florian Müllner <fmuellner@redhat.com> - 3.22.3-2
- Re-add downstream patches
- Resolves: #1386959

* Thu Feb 16 2017 Kalev Lember <klember@redhat.com> - 3.22.3-1
- Update to 3.22.3
- Resolves: #1386959

* Fri Sep 09 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-53
- Improve cycle keybindings
  Resolves: #1306670

* Mon Jul 18 2016 Rui Matos <rmatos@redhat.com> - 3.14.4-52
- Require a mutter version that provides all the new APIs
  Related: rhbz#1330488

* Tue Jul 12 2016 Ray Strode <rstrode@redhat.com> - 3.14.4-51
- Backport patch to fix crash at start up
  Resolves: #1354560
  Related: #1353249

* Fri Jul 08 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-50
- Allow constructing ShellApp from AppInfo
  Related: #1353249

* Thu Jun 30 2016 Owen Taylor <otaylor@redhat.com> - 3.14.4-49
- Fix bug where maximized windows would flicker to the wrong size when
  restarting the shell (on stereo enable or otherwise)
  Resolves: #1306802

* Wed Jun 29 2016 Rui Matos <rmatos@redhat.com> - 3.14.4-48
- Handle video memory purge errors
  Resolves: #1330488

* Fri Jun 24 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-47
- Update translations
  Resolves: #1272377

* Tue May 31 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-46
- Fix cycle keybindings
  Resolves: #1306670

* Fri May 27 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-45
- Set logind's LockedHint when locked
  Resolves: #1329803

* Thu May 19 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-44
- Always show network icon when connected
  Resolves: #1100812

* Fri May 13 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-43
- Fix visibility issue in last patch
  Resolves: #1186954

* Fri May 13 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-42
- Summarize network device sections with too many devices
  Resolves: #1186954

* Fri May 13 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-41
- Fix windowless apps in switcher
  Resolves: #1329306

* Tue Apr 19 2016 Ray Strode <rstrode@redhat.com> - 3.14.4-40
- Allow timed login with no user list
  Resolves: #1301263

* Thu Mar 31 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-39
- Include translation updates
  Related: #1272377

* Fri Mar 04 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-38
- Use font-relative menu widths
  Related: #1257146

* Fri Mar 04 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-37
- Fix clicks on window-list items after dismissing context menu
  Related: #1268689

* Fri Mar 04 2016 Florian Müllner <fmuellner@redhat.com> - 3.14.4-37
- Request minimum gstreamer1 version
  Related: #1290446

* Tue Oct 13 2015 Ray Strode <rstrode@redhat.com> 3.14.4-37
- Fix Username: entry when disable-user-list is on
  Related: #1262999
  Resolves: 1270378

* Thu Oct 08 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-36
- Improve connecting to a headless shell via VNC
  Related: #1243856

* Mon Oct 05 2015 Ray Strode <rstrode@redhat.com> 3.14.4-35
- Ensure the unlock password entry is desensitized when there's
  no password being asked for (Such as when the message is just
  "Please insert smartcard")
  Resolves: #1262999

* Mon Sep 28 2015 Ray Strode <rstrode@redhat.com> 3.14.4-33
- Enforce smartcard at unlock time, if it's used to login
  Resolves: #1263759

* Thu Sep 24 2015 Matthias Clasen <mclasen@redhat.com> - 3.14.4-32
- Avoid abrt reports when the session bus is going away early
  Resolves: #1254986

* Mon Sep 21 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-31
- Notify about outdated extensions on updates
  Related: #1261552

* Fri Sep 18 2015 Ray Strode <rstrode@redhat.com> 3.14.4-30
- Another timed login update.  Makes the indicator work
  when animations are disabled.
  Related: #1252424

* Tue Sep 15 2015 Ray Strode <rstrode@redhat.com> 3.14.4-29
- Fix spew when turning on magnifier
  Resolves: #1260057

* Tue Sep 15 2015 Ray Strode <rstrode@redhat.com> 3.14.4-28
- Drop gnome-session-xsession dependency
  Resolves: #1251495

* Fri Sep 11 2015 Ray Strode <rstrode@redhat.com> 3.14.4-27
- Actually apply patch to unblank when inserting smartcard
  Related: #1201756

* Tue Aug 18 2015 Ray Strode <rstrode@redhat.com> 3.14.4-26
- Fix timed login in virtual machines
  Resolves: #1252424

* Wed Aug 05 2015 Ray Strode <rstrode@redhat.com> 3.14.4-25
- Fix user switching, which broke in 3.14.4-17
  Related: #1220023

* Thu Jul 30 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-24
- Fix some menu ornament oddities
  Related: #1174373

* Fri Jul 24 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-23
- Fix a couple more warnings when running headless
  Related: #1243856

* Thu Jul 23 2015 Ray Strode <rstrode@redhat.com> 3.14.4-22
- One more update to Next button handling
  Resolves: 1240623
  Related: #1240615
  Related: #1174373

* Wed Jul 22 2015 Ray Strode <rstrode@redhat.com> 3.14.4-21
- Make sure Next button starts out desensitized
  Resolves: 1240623
  Related: #1240615
  Related: #1174373

* Fri Jul 17 2015 Ray Strode <rstrode@redhat.com> 3.14.4-20
- set next button to next when asking for username
  Resolves: 1240615
  Related: #1174373

* Fri Jul 17 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-19
- Fix bottom tray handling when running headless
  Related: #1243856

* Thu Jul 16 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-18
- Support headless start
  Resolves: #1243856

* Wed Jul 15 2015 Ray Strode <rstrode@redhat.com> 3.14.4-17
- Fix wonkiness if user hits escape from Not Listed screen
  after typing wrong password
  Resolves: #1220023

* Fri Jul 10 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-16
- Fix user list scrolling on login screen
  Resolves: #1184802

* Wed Jul 08 2015 Milan Crha <mcrha@redhat.com> 3.14.4-15
- Rebuild against updated libical and evolution-data-server
  Related: #1209787

* Wed Jul 08 2015 Milan Crha <mcrha@redhat.com> 3.14.4-14
- Rebuild against updated libical
  Related: #1209787

* Fri Jul 03 2015 Ray Strode <rstrode@redhat.com> 3.14.4-13
- Unblank screen when a smartcard is inserted
  Resolves: #1201756

* Wed Jul 01 2015 Ray Strode <rstrode@redhat.com> 3.14.4-12
- Ensure password authentication is used if no authentication scheme is configured
- Ensure smartcard authentication is used if smartcard authentication is configured

  Related: #1174373 1034968

* Tue Jun 30 2015 Ray Strode <rstrode@redhat.com> 3.14.4-11
- Fix cancel button from Not Listed? screen
  Resolves: #1182035

* Thu Jun 25 2015 Ray Strode <rstrode@redhat.com> 3.14.4-10
- Make login banner overflow to book view at the right time
  Resolves: #1217157

* Fri Jun 12 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-9
- Make login banner message more prominent
  Resolves: rhbz#1182223

* Thu May 21 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-8
- Pass mode parameter with accelerators
  Resolves: rhbz#1028451

* Wed May 20 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-7
- Change fallback app name
  Resolves: rhbz#1125788

* Wed May 20 2015 Ray Strode <rstrode@redhat.com> 3.14.4-6
- More login screen backports
  Related: rhbz#1174373

* Thu May 14 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-5
- Fix enabling/disabling per-app notifications
  Resolves: rhbz#1051132

* Fri May 08 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-4
- Fix removal of libgsystem dependency
  Related: rhbz#1174373

* Thu May  7 2015 Matthias Clasen <mclasen@redhat.com> - 3.14.4-3
- Drop use of libgsystem
  Related: rhbz#1174373

* Thu May 07 2015 Ray Strode <rstrode@redhat.com> 3.14.4-2
- Drop chrpath weirdness
- Readd browser plugin
- Drop wayland desktop file
  Related: rhbz#1174373

* Thu May 04 2015 Florian Müllner <fmuellner@redhat.com> - 3.14.4-1
- Update to latest stable 3.14 release

* Mon May 04 2015 Florian Müllner <fmuellner@redhat.com> - 3.8.4-46
- Rebuild for eds so name bump

* Thu Nov 13 2014 Ray Strode <rstrode@redhat.com> 3.8.4-45
- Don't inform GDM about session changes that came from GDM
  Resolves: #1163474

* Wed Nov 12 2014 Ray Strode <rstrode@redhat.com> 3.8.4-44
- If password authentication is disabled and smartcard authentication is
  enabled and smartcard isn't plugged in at start up, prompt user for
  smartcard
  Resolves: #1159385

* Wed Nov 12 2014 Ray Strode <rstrode@redhat.com> - 3.8.4-43
- Support long login banner messages more effectively
  Resolves: #1110036

* Fri Oct 17 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-42
- Respect disk-writes lockdown setting
  Resolves: rhbz#1154122

* Sat Oct 11 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-41
- Disallow consecutive screenshot requests to avoid an OOM situation
  Resolves: rhbz#1154107

* Fri Oct 10 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-41
- Add option to limit app switcher to current workspace
  Resolves: rhbz#1101568

* Fri Oct 10 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-40
- Try harder to use the default calendar application
  Resolves: rhbz#1052201

* Fri Oct 10 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-40
- Update workspace switcher fix
  Resolves: rhbz#1092102

* Thu Oct 09 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-39
- Validate screenshot parameters
  Resolves: rhbz#1104694

* Thu Oct 09 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-38
- Fix shrinking workspace switcher
  Resolves: rhbz#1092102

* Thu Oct 09 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-38
- Update fix for vertical monitor layouts to upstream fix
  Resolves: rhbz#1075240

* Wed Oct 08 2014 Ray Strode <rstrode@redhat.com> 3.8.4-38
- Fix traceback introduced in 3.8.4-36 when unlocking via
  user switcher
  Related: #1101333

* Tue Oct 07 2014 Ray Strode <rstrode@redhat.com> 3.8.4-37
- Fix problems with LDAP and disable-user-list=TRUE
  Resolves: rhbz#1137041

* Mon Oct 06 2014 Ray Strode <rstrode@redhat.com> 3.8.4-36
- Fix login screen focus issue following idle
  Resolves: rhbz#1101333

* Sun Oct 05 2014 Ray Strode <rstrode@redhat.com> 3.8.4-35
- Disallow cancel from login screen before login attempt
  has been initiated.
  Resolves: rhbz#1109530

* Sun Oct 05 2014 Ray Strode <rstrode@redhat.com> 3.8.4-34
- Disallow cancel from login screen after login is already
  commencing.
  Resolves: rhbz#1079294

* Thu Jul 17 2014 Owen Taylor <otaylor@redhat.com> 3.8.4-33
- Add a patch for quadbuffer stereo suppport
  Resolves: rhbz#1108893

* Wed Apr 16 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-32
- Improve vertical monitor layouts
  Resolves: rhbz#1075240

* Wed Mar 19 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-31
- Fix some more background memory leaks
  Resolves: rhbz#1027192

* Wed Mar 12 2014 Ray Strode <rstrode@redhat.com> 3.8.4-30
- Fix automatic shield lifting when smartcard is inserted
  Resolves: #1063488

* Mon Mar 10 2014 Ray Strode <rstrode@redhat.com> 3.8.4-29
- Don't show user list if require smartcard is true
  Resolves: #1063390

* Mon Mar 10 2014 Ray Strode <rstrode@redhat.com> 3.8.4-28
- Only react to login token (not any token) when performing unlock
  Resolves: #1064972

* Sat Mar 08 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-27
- Backport background memory leak fixes
  Resolves: rhbz#1027192

* Sat Mar 08 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-26
- Do not load user list in login screen when disabled
  Resolves: rhbz#1053102

* Thu Mar 06 2014 Florian Müllner <fmuellner@redhat.com> - 3.8.4-25
- Fix loading of remote search providers
  Resolves: #1030948

* Mon Feb 17 2014 Ray Strode <rstrode@redhat.com> 3.8.4-24
- Make login banner more prominent
  Resolves: #1061996

* Wed Jan 29 2014 Ray Strode <rstrode@redhat.com> 3.8.4-23
- Fix traceback in log
  Resolves: #1034966

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.8.4-22
- Mass rebuild 2014-01-24

* Tue Jan 21 2014 Ray Strode <rstrode@redhat.com> 3.8.4-21
- Add branding next to activities button
  Resolves: #1052984

* Mon Jan 13 2014 Ray Strode <rstrode@redhat.com> 3.8.4-20
- Fix undefined variable
  Resolves: #1049897

* Wed Jan 08 2014 Ray Strode <rstrode@redhat.com> 3.8.4-19
- Allow session mode to be specified by environment variable

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.4-18
- Mass rebuild 2013-12-27

* Wed Dec  4 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.4-17
- Add gnome-terminal to favorites, remove empathy
- Resolves: #1038168

* Fri Nov 15 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.4-15
- Close run dialog on mode changes when the new session mode doesn't allow it
  Resolves: rhbz#1031142
- Prevent fallback keyring dialog to appear on lock screen

* Fri Nov  8 2013 Rui Matos <rmatos@redhat.com> - 3.8.4-14
- Add a DBus method to load a single extension
  Resolves: rhbz#1028466
- Add a SESSION_MODE extension type
  Resolves: rhbz#1028462

* Fri Nov 08 2013 Ray Strode <rstrode@redhat.com> 3.8.4-13
- Fix input regression caused by -12
  Related: #817594

* Thu Nov 07 2013 Ray Strode <rstrode@redhat.com> 3.8.4-12
- Show banner text when disable-user-list = TRUE
  Resolves: #817594

* Mon Nov 04 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.4-11
- Re-add yelp to default favorites - this downstream patch was
  accidentally dropped when rebasing on F19
  Resolves: #958196
- Fix network icon not updating
  Resolves: #1009867
- Do not hide on/off switch while connecting to wireless
  Resolves: #908829
- Fix apps menu not being disabled when open during screen lock
  Resolves: #1027501
- Be more defensive when enabling/disabling extensions
  Resolves: #1027501
- Re-enable browser plugin and move it to a subpackage
  Resolves: #972783

* Fri Nov 01 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.4-10
- Backport support for hasWorkspaces session mode property
  Resolves: #1025444
- Backport input validation of screenshot/screencast DBus methods
  Resolves: #1022491

* Thu Oct 31 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.4-9
- Backport switch to disable browser plugin
- Disable browser plugin
Resolves: #972783

* Thu Oct 31 2013 Matthias Clasen <mclasen@redhat.com> 3.8.4-8
- Add an override for always-show-log-out
- Resolves: #913566

* Tue Oct 15 2013  Vinzenz Feenstra <vfeenstr@redhat.com> 3.8.4-7
- Backport of support for pre-authenticated logins from oVirt
  Related: #854712

* Thu Aug 29 2013  Ray Strode <rstrode@redhat.com> 3.8.4-6
- Another backported ui fix
  Related: #854724

* Tue Aug 27 2013 Ray Strode <rstrode@redhat.com> 3.8.4-5
- Backport some login screen ui updates
  Related: #854724

* Thu Aug 22 2013 Ray Strode <rstrode@redhat.com> 3.8.4-4
- Backport some more smartcard related fixes
  Related: #854724

* Tue Aug 06 2013 Ray Strode <rstrode@redhat.com> 3.8.4-3
- Backport some lock screen fixes related to smartcard support
  from upstream
  Related: #854724

* Wed Jul 31 2013 Ray Strode <rstrode@redhat.com> 3.8.4-2
- Include support for smartcard authentication
  Related: #854724

* Tue Jul 30 2013 Ray Strode <rstrode@redhat.com> - 3.8.4-1
- Update to 3.8.4

* Wed Jun 26 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.3-3
- Backport upstream patch that makes a common error non-fatal

* Wed Jun 12 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.3-2
- Rebuilt against fixed cogl (#973542)

* Fri Jun 07 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.3-1
- Update to 3.8.3, drop upstreamed patches

* Wed May 22 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.2-3
- Drop the gnome-session-xsession dependency again, it
  has unwanted side-effects on eg soas

* Tue May 14 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.2-2
- Include upstream fix for bug #962876

* Mon May 13 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.2-1
- Update to 3.8.2 and drop upstreamed patches

* Tue May 07 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.1-4
- Add login-screen branding changes from gnome-3-8 branch as downstream patches

* Wed May 01 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-2
- Add missing telepathy-logger runtime dep
- Depend on gnome-session-xsession so that it gets pulled in for
  typical GNOME installs

* Tue Apr 16 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Thu Mar 28 2013 Adel Gadllah <adel.gadllah@gmail.com> - 3.8.0.1-2
- Ship the perf tool

* Wed Mar 27 2013 Ray Strode <rstrode@redhat.com> - 3.8.0.1-1
- Update to 3.8.0.1

* Tue Mar 26 2013 Florian Müllner <fmuellner@redhat.com> - 3.8.0-1
- Update to 3.8.0

* Wed Mar 26 2013 Florian Müllner <fmuellner@redhat.com>
- Drop upstreamed patch

* Wed Mar 20 2013 Ray Strode <rstrode@redhat.com> 3.7.92-2
- Fix initial setup

* Tue Mar 19 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Tue Mar 05 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Wed Feb 20 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.90-1
- Update to 3.7.90

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-2
- Rebuilt for libgcr soname bump

* Wed Feb 06 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.5-1
- Update to 3.7.5

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 3.7.4.1-2
- Rebuild for new cogl

* Thu Jan 17 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.4.1-1
- Update to 3.7.4.1

* Tue Jan 15 2013 Florian Müllner <fmuellner@redhat.com> - 3.7.4-1
- Update to 3.7.4

* Wed Jan 09 2013 Richard Hughes <hughsient@gmail.com> - 3.7.3.1-1
- Update to 3.7.3.1

* Tue Dec 18 2012 Florian Müllner <fmuellner@redhat.com> 3.7.3-1
- Update to 3.7.3

* Mon Dec 17 2012 Adam Jackson <ajax@redhat.com> 3.7.2-3
- Also don't mangle rpath on power

* Mon Dec 10 2012 Adam Jackson <ajax@redhat.com> 3.7.2-2
- Disable bluetooth on power

* Mon Nov 19 2012 Florian Müllner <fmuellner@redhat.com> - 3.7.2-1
- Update to 3.7.2

* Tue Nov 13 2012 Dan Horák <dan[at]danny.cz> - 3.7.1-2
- don't Require: gnome-bluetooth on s390(x)

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Wed Oct 31 2012 Brian Pepple <bpepple@fedoraproject.org> - 3.6.1-5
- Rebuild against latest telepathy-logger

* Thu Oct 25 2012 Milan Crha <mcrha@redhat.com> - 3.6.1-4
- Rebuild against newer evolution-data-server

* Sat Oct 20 2012 Dan Horák <dan[at]danny.cz> - 3.6.1-3
- explicit BR: control-center as it isn't brought in indirectly on s390(x)

* Thu Oct 18 2012 Florian Müllner <fmuellner@redhat.com> - 3.6.1-2
- Remove avoid-redhat-menus patch

  The standard way of supporting a desktop-specific menu layout is
  to set XDG_MENU_PREFIX (which we made gnome-session do now).

* Mon Oct 15 2012 Florian Müllner <fmuellner@redhat.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Florian Müllner <fmuellner@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Florian Müllner <fmuellner@redhat.com> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 11 2012 Florian Müllner <fmuellner@redhat.com> - 3.5.91-1
- Update dependencies

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 28 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.90-3
- Rebuild against new cogl/clutter

* Mon Aug 27 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.90-2
- Rebuild for new libcamel and synchronize gnome-bluetooth Requires with
  BuildRequires.

* Wed Aug 22 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Tue Aug 14 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.5-2
- Add Requires: gnome-bluetooth >= 3.5.5

* Mon Aug 13 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.5-1
- Update to 3.5.5

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.4-4
- Tighten runtime requires

* Thu Jul 19 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.4-3
- Add a gdm-libs dependency

* Wed Jul 18 2012 Colin Walters <walters@verbum.org> - 3.5.4-2
- Bump release

* Wed Jul 18 2012 Ray Strode <rstrode@redhat.com> 3.5.4-1
- Update to 3.5.4

* Tue Jun 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.3-2
- Rebuild against new e-d-s

* Tue Jun 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.3-1
- Update to 3.5.3

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-2
- Remove upstreamed patch

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Mon May 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 3.4.1-6
- Cherry pick F17 changes, bump build for new evo soname

* Wed May 16 2012 Owen Taylor <otaylor@redhat.com> - 3.4.1-5
- New version of unmount notification

* Tue May 15 2012 Owen Taylor <otaylor@redhat.com> - 3.4.1-4
- Add a patch to display a notification until it's safe to remove a drive (#819492)

* Fri Apr 20 2012 Owen Taylor <otaylor@redhat.com> - 3.4.1-3
- Add a patch from upstream to avoid a crash when Evolution is not installed (#814401)

* Wed Apr 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-2
- Silence glib-compile-schemas scriplets

* Wed Apr 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Thu Apr  5 2012 Owen Taylor <otaylor@redhat.com> - 3.4.0-2
- Change gnome-shell-favourite-apps-firefox.patch to also patch the JS code
  to handle the transition from mozilla-firefox.desktop to firefox.desktop.
  (#808894, reported by Jonathan Kamens)

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.92-1
- Update to 3.3.92

* Sat Mar 10 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.90-2
- Rebuild for new cogl

* Sat Feb 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.90-1
- Update to 3.3.90

* Thu Feb  9 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.5-2
- Depend on accountsservice-libs (#755112)

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Fri Jan 20 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.4-1
- Update to 3.3.4

* Thu Jan 19 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.3-2
- Rebuild for new cogl

* Thu Jan  5 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Sun Nov 27 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 3.3.2-2
- Rebuild for new clutter and e-d-s

* Wed Nov 23 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.2-1
- Update to 3.3.2

* Wed Nov 09 2011 Kalev Lember <kalevlember@gmail.com> - 3.2.1-6
- Adapt to firefox desktop file name change in F17

* Thu Nov 03 2011 Adam Jackson <ajax@redhat.com> 3.2.1-5
- Build with -Wno-error=disabled-declarations for the moment

* Wed Nov 02 2011 Brian Pepple <bpepple@fedoraproject.org> - 3.2.1-4
- Rebuld against tp-logger.

* Sun Oct 26 2011 Bruno Wolff III <bruno@wolff.to> - 3.2.1-3
- Rebuild for new evolution-data-server

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for glibc bug#747377

* Wed Oct 19 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Wed Sep 28 2011 Ray Strode <rstrode@redhat.com> 3.2.0-2
- rebuild

* Mon Sep 26 2011 Owen Taylor <otaylor@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.92-1
- Update to 3.1.92

* Fri Sep 16 2011 Kalev Lember <kalevlember@gmail.com> - 3.1.91.1-2
- Tighten dependencies by specifying the required arch (#739130)

* Wed Sep 14 2011 Owen Taylor <otaylor@redhat.com> - 3.1.91.1-1
- Update to 3.1.91.1 (adds browser plugin)
  Update Requires

* Thu Sep 08 2011 Dan Horák <dan[at]danny.cz> - 3.1.91-3
- workaround a chrpath issue on s390(x)

* Wed Sep 07 2011 Kalev Lember <kalevlember@gmail.com> - 3.1.91-2
- Replace Epiphany with Firefox in the default favourite apps

* Wed Sep  7 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.91-1
- Update to 3.1.91

* Thu Sep  1 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.90.1-2
- Require caribou

* Wed Aug 31 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.90.1-1
- Update to 3.1.90.1

* Wed Aug 31 2011 Adam Williamson <awilliam@redhat.com> - 3.1.4-3.gite7b9933
- rebuild against e-d-s

* Fri Aug 19 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.4-2.gite7b9933
- git snapshot that builds against gnome-menus 3.1.5

* Thu Aug 18 2011 Matthew Barnes <mbarnes@redhat.com> - 3.1.5-1
- Rebuild against newer eds libraries.

* Wed Jul 27 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.4-1
- Update to 3.1.4

* Wed Jul 27 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.3-4
- Rebuild

* Tue Jul 26 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.3-3
- Add necessary requires

* Mon Jul 25 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.3-2
- Rebuild

* Tue Jul  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 3.1.3-1
- Upstream 3.1.3 dev release

* Mon Jun 27 2011 Adam Williamson <awilliam@redhat.com> - 3.0.2-4
- add fixes from f15 branch (gjs dep and rpath)

* Wed Jun 22 2011 Owen Taylor <otaylor@redhat.com> - 3.0.2-3
- Add a patch from upstream to avoid g_file_get_contents()

* Fri Jun 17 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.0.2-2
- Rebuilt for new gtk3 and gnome-desktop3

* Wed May 25 2011 Owen Taylor <otaylor@redhat.com> - 3.0.2-1
- Update to 3.0.2

* Tue May 10 2011 Dan Williams <dcbw@redhat.com> - 3.0.1-4
- Fix initial connections to WPA Enterprise access points (#699014)
- Fix initial connections to mobile broadband networks

* Thu Apr 28 2011 Dan Horák <dan[at]danny.cz> - 3.0.1-3
- no bluetooth on s390(x)

* Wed Apr 27 2011 Owen Taylor <otaylor@redhat.com> - 3.0.1-2
- Add a patch from upstream to fix duplicate applications in application display

* Mon Apr 25 2011 Owen Taylor <otaylor@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Mon Apr 11 2011 Colin Walters <walters@verbum.org> - 3.0.0.2-2
- We want to use the GNOME menus which has the designed categories,
  not the legacy redhat-menus.

* Fri Apr 08 2011 Nils Philippsen <nils@redhat.com> - 3.0.0.2-1
- Update to 3.0.0.2 (fixes missing import that was preventing extensions from
  loading.)
- Update source URL

* Tue Apr  5 2011 Owen Taylor <otaylor@redhat.com> - 3.0.0.1-1
- Update to 3.0.0.1 (fixes bug where network menu could leave
  Clutter event handling stuck.)

* Mon Apr  4 2011 Owen Taylor <otaylor@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Tue Mar 29 2011 Brian Pepple <bpepple@fedoraproject.org> - 2.91.93-3
- Bump

* Tue Mar 29 2011 Brian Pepple <bpepple@fedoraproject.org> - 2.91.93-2
- Rebuild for new tp-logger

* Mon Mar 28 2011 Owen Taylor <otaylor@redhat.com> - 2.91.93-1
- Update to 2.91.93.

* Fri Mar 25 2011 Ray Strode <rstrode@redhat.com> 2.91.92-3
- Adjustments for More nm-client api changes.
- Fix VPN indicator

* Thu Mar 24 2011 Christopher Aillon <caillon@redhat.com> - 2.91.92-2
- Make activating vpn connections work from the shell indicator

* Wed Mar 23 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.92-1
- Update to 2.91.92

* Wed Mar 16 2011 Michel Salim <salimma@fedoraproject.org> - 2.91.91-2
- Fix alt-tab behavior on when primary display is not leftmost (# 683932)

* Tue Mar  8 2011 Owen Taylor <otaylor@redhat.com> - 2.91.91-1
- Update to 2.91.91

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-2
- Require upower and polkit at runtime

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-1
- Update to 2.91.90

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.6-6
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb  3 2011 Bill Nottingham <notting@redhat.com> - 2.91.6-4
- buildrequire gnome-bluetooth to fix bluetooth status icon (#674874)

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.6-3
- Rebuild against newer gtk

* Tue Feb  1 2011 Owen Taylor <otaylor@redhat.com> - 2.91.6-2
- Build-requires evolution-data-server-devel

* Tue Feb  1 2011 Owen Taylor <otaylor@redhat.com> - 2.91.6-1
- Update to 2.91.6

* Thu Jan 13 2011 Mattihas Clasen <mclasen@redhat.com> - 2.91.5-3
- Drop desktop-effects dependency

* Wed Jan 12 2011 Colin Walters <walters@verbum.org> - 2.91.5-2
- BR latest g-i, handles flags as arguments better

* Tue Jan 11 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.5-1
- Update to 2.91.5

* Sat Jan  8 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.4-1
- Update to 2.91.4
- Rebuild against new gtk

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.3-2
- Rebuild aginst new gtk

* Mon Nov 29 2010 Owen Taylor <otaylor@redhat.com> - 2.91.2-1
- Update to 2.91.3

* Thu Nov 18 2010 Owen Taylor <otaylor@redhat.com> - 2.91.2-3
- Add another memory-management crasher fix from upstream

* Mon Nov 15 2010 Owen Taylor <otaylor@redhat.com> - 2.91.2-2
- Add a patch from upstream fixing a memory-management crasher

* Tue Nov  9 2010 Owen Taylor <otaylor@redhat.com> - 2.91.2-1
- Update to 2.91.2

* Mon Nov  1 2010 Owen Taylor <otaylor@redhat.com> - 2.91.1-1
- Update to 2.91.1
- Add libcroco-devel to BuildRequires, apparently it was getting
  pulled in indirectly before
- Add libcanberra-devel and pulseaudio-libs-devel BuildRequires

* Mon Oct  4 2010 Owen Taylor <otaylor@redhat.com> - 2.91.0-1
- Update to 2.91.0
- Remove patch to disable VBlank syncing

* Thu Aug 12 2010 Colin Walters <walters@verbum.org> - 2.31.5-7
- Add patch to disable vblank syncing

* Tue Jul 13 2010 Colin Walters <walters@verbum.org> - 2.31.5-5
- Run glib-compile-schemas

* Tue Jul 13 2010 Colin Walters <walters@megatron> - 2.31.5-4
- Bless stuff in files section

* Tue Jul 13 2010 Colin Walters <walters@verbum.org> - 2.31.5-3
- Axe gnome-desktop-devel

* Tue Jul 13 2010 Adel Gadllah <adel.gadllah@gmail.com> - 2.31.5-2
- BuildRequire gnome-desktop3-devel, gtk3

* Mon Jul 12 2010 Colin Walters <walters@verbum.org> - 2.31.5-1
- New upstream version
- Drop rpath goop, shouldn't be necessary any more

* Fri Jun 25 2010 Colin Walters <walters@megatron> - 2.31.2-3
- Drop gir-repository-devel build dependency

* Fri May 28 2010 Adam Miller <maxamillion@fedoraproject.org> - 2.31.2-2
- Added new version requirements for dependencies based on upstream releases
- Added new file listings for gnome-shell-clock-preferences binary and .desktop
- Added gnome-shell man page file listing

* Wed May 26 2010 Adam Miller <maxamillion@fedoraproject.org> - 2.31.2-1
- New upstream release

* Fri Mar 26 2010 Colin Walters <walters@verbum.org> - 2.29.1-3
- Specify V=1 for build, readd smp_mflags since parallel is fixed upstream

* Thu Mar 25 2010 Adam Miller <maxamillion@fedoraproject.org> - 2.29.1-2
- Bumped for new version of mutter and clutter
- Added version requirement to gjs-devel because of dependency of build

* Wed Mar 24 2010 Adam Miller <maxamillion@fedoraproject.org> - 2.29.1-1
- Update to latest version 2.29.1

* Sun Feb 21 2010 Bastien Nocera <bnocera@redhat.com> 2.28.1-0.2.20100128git
- Require json-glib
- Rebuild for new clutter with json split out
- Fix deprecation in COGL

* Thu Jan 28 2010 Adam Miller <maxamillion@fedoraproject.org> - 2.28.1-0.1.20100128git
- New git snapshot
- Fixed Version for alphatag use

* Fri Jan 15 2010 Adam Miller <maxamillion@fedoraproject.org> - 2.28.0.20101015git-1
- Added dependency on a git build of gobject-introspect to solve some breakage
- Also went ahead and made a new git tarball

* Tue Jan 12 2010 Adam Miller <maxamillion@fedoraproject.org> - 2.28.0.20100112git-1
- New git snapshot

* Tue Dec 07 2009 Adam Miller <maxamillion@fedoraproject.org> - 2.28.0.20091206git-5
- Added libtool, glib-gettext for the libtoolize dep of git snapshot

* Mon Dec 07 2009 Adam Miller <maxamillion@fedoraproject.org> - 2.28.0.20091206git-4
- Added gnome-common needed by autogen.sh in git snapshot build

* Sun Dec 06 2009 Adam Miller <maxamillion@fedoraproject.org> - 2.28.0.20091206git-3
- Added the autotools needed to build the git snapshot to the build requires

* Sun Dec 06 2009 Adam Miller <maxamillion@fedoraproject.org> - 2.28.0.20091206git-2
- Fixed the setup naming issue with the git snapshot directory naming

* Sun Dec 06 2009 Adam Miller <maxamillion@fedoraproject.org> - 2.28.0.20091206git-1
- Update to git snapshot on 20091206

* Wed Oct  7 2009 Owen Taylor <otaylor@redhat.com> - 2.28.0-2
- Update to 2.28.0

* Tue Sep 15 2009 Owen Taylor <otaylor@redhat.com> - 2.27.3-1
- Update to 2.27.3

* Fri Sep  4 2009 Owen Taylor <otaylor@redhat.com> - 2.27.2-2
- Test for gobject-introspection version should be >= not >

* Fri Sep  4 2009 Owen Taylor <otaylor@redhat.com> - 2.27.2-1
- Update to 2.27.2
- Add an explicit dep on gobject-introspection 0.6.5 which is required 
  for the new version

* Sat Aug 29 2009 Owen Taylor <otaylor@redhat.com> - 2.27.1-4
- Fix GConf %%preun script to properly be for package removal

* Fri Aug 28 2009 Owen Taylor <otaylor@redhat.com> - 2.27.1-3
- Replace libgnomeui with gnome-desktop in BuildRequires

* Fri Aug 28 2009 Owen Taylor <otaylor@redhat.com> - 2.27.1-2
- BuildRequire intltool
- Add find_lang

* Fri Aug 28 2009 Owen Taylor <otaylor@redhat.com> - 2.27.1-1
- Update to 2.27.1
- Update Requires, add desktop-effects

* Wed Aug 12 2009 Owen Taylor <otaylor@redhat.com> - 2.27.0-4
- Add an explicit dependency on GConf2 for pre/post

* Tue Aug 11 2009 Owen Taylor <otaylor@redhat.com> - 2.27.0-3
- Add missing BuildRequires on gir-repository-devel

* Tue Aug 11 2009 Owen Taylor <otaylor@redhat.com> - 2.27.0-2
- Temporarily use a non-parallel-build until gnome-shell is fixed

* Mon Aug 10 2009 Owen Taylor <otaylor@redhat.com> - 2.27.0-1
- Initial version
