Name:           gnome-shell
Version:        3.8.4
Release:        31%{?dist}
Summary:        Window management and application launching for GNOME

Group:          User Interface/Desktops
License:        GPLv2+
Provides:       desktop-notification-daemon
URL:            http://live.gnome.org/GnomeShell
#VCS:           git:git://git.gnome.org/gnome-shell
Source0:        http://download.gnome.org/sources/gnome-shell/3.8/%{name}-%{version}.tar.xz
Source1:	org.gnome.shell.gschema.override

# Replace Epiphany with Firefox in the default favourite apps list
Patch1: gnome-shell-favourite-apps-firefox.patch
Patch2: gnome-shell-favourite-apps-yelp.patch
Patch3: gnome-shell-favourite-apps-terminal.patch
Patch4: gnome-shell-favourite-apps-empathy.patch

Patch10: 0001-popupMenu-Fix-removing-the-active-menu-from-PopupMen.patch
Patch11: 0001-catch-more-errors-on-extensions-enable-and-disable.patch

Patch20: 0001-main-allow-session-mode-to-be-specified-in-the-envir.patch

Patch30: 0001-network-Do-not-use-timestamp-to-identify-connections.patch
Patch31: 0001-network-Don-t-disable-switch-in-wifi-section-while-c.patch

Patch40: fix-remote-search-provider-loading.patch

Patch50: fix-background-leaks.patch

Patch60: 0001-main-Actually-respect-hasWorkspaces.patch
Patch61: 0001-main-Close-runDialog-as-necessary-on-session-mode-ch.patch
Patch62: 0001-keyring-Don-t-unregister-the-prompt-when-disabled.patch
Patch63: 0002-keyring-Cancel-active-prompts-on-disable.patch

Patch70: 0001-screenshot-Extend-ScreenshotArea-parameter-validatio.patch
Patch71: 0002-screencast-Fix-disabling-screencasts-via-session-mod.patch
Patch72: 0003-screencast-Validate-parameters-of-ScreencastArea.patch

Patch80: 0001-shellDBus-Add-a-DBus-method-to-load-a-single-extensi.patch
Patch81: 0002-extensions-Add-a-SESSION_MODE-extension-type.patch

Patch90: 0001-panel-add-an-icon-to-the-ActivitiesButton.patch

Patch99: login-screen-backport.patch
Patch100: gdm-support-pre-authenticated-logins-from-oVirt.patch
Patch101: dont-load-user-list-when-disabled.patch

%define clutter_version 1.13.4
%define gnome_bluetooth_version 3.5.5
%define gobject_introspection_version 0.10.1
%define gjs_version 1.35.4
%define mutter_version 3.8.3
%define eds_version 3.5.3
%define gnome_desktop_version 3.7.90
%define gnome_menus_version 3.5.3
%define json_glib_version 0.13.2
%define gsettings_desktop_schemas_version 3.7.4
%define caribou_version 0.4.8
%define libcroco_version 0.6.8
%define telepathy_logger_version 0.2.6

## Needed when we re-autogen
BuildRequires:  autoconf >= 2.53
BuildRequires:  automake >= 1.10
BuildRequires:  gnome-common >= 2.2.0
BuildRequires:  libtool >= 1.4.3
BuildRequires:  caribou-devel >= %{caribou_version}
BuildRequires:  chrpath
BuildRequires:  clutter-devel >= %{clutter_version}
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  evolution-data-server-devel >= %{eds_version}
BuildRequires:  gcr-devel
BuildRequires:  gjs-devel >= %{gjs_version}
BuildRequires:  glib2-devel
BuildRequires:  gnome-menus-devel >= %{gnome_menus_version}
BuildRequires:  gobject-introspection >= %{gobject_introspection_version}
BuildRequires:  json-glib-devel >= %{json_glib_version}
BuildRequires:  upower-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  libnm-gtk-devel
BuildRequires:  NetworkManager-glib-devel
BuildRequires:  polkit-devel
BuildRequires:  startup-notification-devel
BuildRequires:  telepathy-glib-devel
BuildRequires:  telepathy-logger-devel >= %{telepathy_logger_version}
# for screencast recorder functionality
BuildRequires:  gstreamer1-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libcanberra-devel
BuildRequires:  libcroco-devel >= %{libcroco_version}

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
Requires:       gnome-desktop3 >= %{gnome_desktop_version}
Requires:       gnome-menus%{?_isa} >= %{gnome_menus_version}
# wrapper script uses to restart old GNOME session if run --replace
# from the command line
Requires:       gobject-introspection%{?_isa} >= %{gobject_introspection_version}
Requires:       gjs%{?_isa} >= %{gjs_version}
# needed for loading SVG's via gdk-pixbuf
Requires:       librsvg2%{?_isa}
# needed as it is now split from Clutter
Requires:       json-glib%{?_isa} >= %{json_glib_version}
Requires:       mutter%{?_isa} >= %{mutter_version}
Requires:       upower%{?_isa}
Requires:       polkit%{?_isa} >= 0.100
Requires:       gnome-desktop3%{?_isa} >= %{gnome_desktop_version}
Requires:       gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires:       libcroco%{?_isa} >= %{libcroco_version}
Requires:       telepathy-logger%{?_isa} >= %{telepathy_logger_version}
# needed for schemas
Requires:       at-spi2-atk%{?_isa}
# needed for on-screen keyboard
Requires:       caribou%{?_isa} >= %{caribou_version}
# needed for the user menu
Requires:       accountsservice-libs%{?_isa}
Requires:       gdm-libs%{?_isa}
Requires:       clutter%{?_isa} >= %{clutter_version}
# needed for screen recording
Requires:       gstreamer1-plugins-good

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
%setup -q
%patch1 -p1 -b .firefox
%patch2 -p1 -b .yelp
%patch3 -p1 -b .terminal
%patch4 -p1 -b .empathy

%patch10 -p1 -b .fix-popup-menu-manager-exception
%patch11 -p1 -b .catch-extension-errors

%patch20 -p1 -b .main-allow-session-mode-to-be-specified-in-the-envir

%patch30 -p1 -b .fix-stuck-network-icon
%patch31 -p1 -b .keep-wifi-switch

%patch40 -p1 -b .fix-remote-search-provider-loading

%patch50 -p1 -b .fix-background-leaks

%patch60 -p1 -b .support-has-workspaces
%patch61 -p1 -b .close-run-dialog-on-lock
%patch62 -p1 -b .prevent-fallback-keyring-dialog
%patch63 -p1 -b .cancel-keyring-dialog-on-lock

%patch70 -p1 -b .validate-screenshot-params
%patch71 -p1 -b .fix-disable-screencasts
%patch72 -p1 -b .validate-screencast-params

%patch80 -p1
%patch81 -p1

%patch90 -p1 -b .panel-add-an-icon-to-the-ActivitiesButton

%patch99 -p1 -b .login-screen-backport
%patch100 -p1 -b .gdm-support-pre-authenticated-logins-from-oVirt
%patch101 -p1 -b .dont-load-user-list-when-disabled

%build
autoreconf -f
(if ! test -x configure; then NOCONFIGURE=1 ./autogen.sh; fi;
 %configure --disable-static --disable-compile-warnings)
make V=1 %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf %{buildroot}/%{_libdir}/mozilla/plugins/*.la

desktop-file-validate %{buildroot}%{_datadir}/applications/gnome-shell.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/gnome-shell-extension-prefs.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/evolution-calendar.desktop

cp %{SOURCE1} %{buildroot}/%{_datadir}/glib-2.0/schemas

%find_lang %{name}

%ifnarch s390 s390x ppc ppc64 ppc64p7
# The libdir rpath breaks nvidia binary only folks, so we remove it.
# See bug 716572
# skip on s390(x), workarounds a chrpath issue
chrpath -r %{_libdir}/gnome-shell:%{_libdir}/gnome-bluetooth $RPM_BUILD_ROOT%{_bindir}/gnome-shell
chrpath -r %{_libdir}/gnome-bluetooth $RPM_BUILD_ROOT%{_libdir}/gnome-shell/libgnome-shell.so
%endif

%preun
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas &> /dev/null ||:

%posttrans
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas &> /dev/null ||:

%files -f %{name}.lang
%doc COPYING README
%{_bindir}/gnome-shell
%{_bindir}/gnome-shell-extension-tool
%{_bindir}/gnome-shell-perf-tool
%{_bindir}/gnome-shell-extension-prefs
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/glib-2.0/schemas/*.override
%{_datadir}/applications/gnome-shell.desktop
%{_datadir}/applications/gnome-shell-extension-prefs.desktop
%{_datadir}/applications/evolution-calendar.desktop
%{_datadir}/gnome-control-center/keybindings/50-gnome-shell-screenshot.xml
%{_datadir}/gnome-control-center/keybindings/50-gnome-shell-system.xml
%{_datadir}/gnome-shell/
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
%{_libdir}/gnome-shell/
%{_libexecdir}/gnome-shell-calendar-server
%{_libexecdir}/gnome-shell-perf-helper
%{_libexecdir}/gnome-shell-hotplug-sniffer
# Co own these directories instead of pulling in GConf
# after all, we are trying to get rid of GConf with these files
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/gnome-shell-overrides.convert
%{_mandir}/man1/%{name}.1.gz
# exclude as these should be in a devel package for st etc
%exclude %{_datadir}/gtk-doc

%files browser-plugin
%{_libdir}/mozilla/plugins/*.so

%changelog
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
