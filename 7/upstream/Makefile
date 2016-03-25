PROG = sos-easy-install
VERSION = $(shell grep ^ver $(PROG) | cut -d= -f2)

all:
	@echo 'try: '
	@echo 'make install'
	@echo 'make uninstall'

install:
	@echo Copying files...
	@install -m 755 $(PROG) $(DESTDIR)/bin/$(PROG)
	@install -m 755 $(PROG)-pkexec $(DESTDIR)/bin/$(PROG)-pkexec
	@install -m 644 org.freedesktop.$(PROG).policy $(DESTDIR)//usr/share/polkit-1/actions/org.freedesktop.$(PROG).policy
	@install -Dpm 644 $(PROG).desktop $(DESTDIR)/usr/share/applications/$(PROG).desktop
	@install -Dpm 644 sosEI-header.png $(DESTDIR)/usr/share/pixmaps/sosEI-header.png
	@install -Dpm 644 $(PROG).png $(DESTDIR)/usr/share/icons/hicolor/96x96/apps/$(PROG).png
	@cp -pr sos-ei-app-icons/ $(DESTDIR)/usr/share/icons/
	@install -Dpm 644 COPYING $(DESTDIR)/usr/share/licenses/$(PROG)/COPYING 
	@echo Install complete

uninstall:
	@rm -f $(DESTDIR)/bin/$(PROG)
	@rm -f $(DESTDIR)/bin/$(PROG)-pkexec
	@rm -f $(DESTDIR)//usr/share/polkit-1/actions/org.freedesktop.$(PROG).policy
	@rm -f $(DESTDIR)/usr/share/applications/$(PROG).desktop
	@rm -f $(DESTDIR)/usr/share/pixmaps/sosEI-header.png
	@rm -f $(DESTDIR)/usr/share/icons/hicolor/96x96/apps/$(PROG).png
	@rm -rf $(DESTDIR)/usr/share/icons/sos-ei-app-icons
	@rm -f $(DESTDIR)/usr/share/licenses/$(PROG)/COPYING
	@echo Uninstall complete
