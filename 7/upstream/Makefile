PROG = sos-easy-install
VERSION = $(shell grep ^ver $(PROG) | cut -d= -f2)

all:
	@echo 'try: '
	@echo 'make install'
	@echo 'dist'
	@echo 'make uninstall'

dist:
	@echo creating dist tarball
	@tar czf $(PROG)-$(VERSION).tgz $(PROG) Makefile README.md COPYING sos-Easy-Install.png sosEI-header.png sos-easy-install.desktop sos-ei-app-icons

install:
	@echo Copying files...
	@install -m 755 $(PROG) $(DESTDIR)/bin/$(PROG)
	@install -Dpm 644 $(PROG).desktop $(DESTDIR)/usr/share/applications/$(PROG).desktop
	@install -Dpm 644 sosEI-header.png $(DESTDIR)/usr/share/pixmaps/sosEI-header.png
	@install -Dpm 644 sos-Easy-Install.png $(DESTDIR)/usr/share/icons/hicolor/48x48/apps/sos-easy-install.png
	@cp -pr sos-ei-app-icons/ $(DESTDIR)/usr/share/icons/
	@install -Dpm 644 COPYING $(DESTDIR)/usr/share/licenses/$(PROG)/COPYING 
	@echo Install complete

uninstall:
	@rm -f $(DESTDIR)/bin/$(PROG)
	@rm -f $(DESTDIR)/usr/share/applications/$(PROG).desktop
	@rm -f $(DESTDIR)/usr/share/pixmaps/sosEI-header.png
	@rm -f $(DESTDIR)/usr/share/icons/hicolor/48x48/apps/sos-easy-install.png
	@rm -rf $(DESTDIR)/usr/share/icons/sos-ei-app-icons
	@rm -f $(DESTDIR)/usr/share/licenses/$(PROG)/COPYING
	@echo Uninstall complete
