CURSORDIR=$(HOME)/.icons/default/cursors
BUILDDIR=../cursors_old


#Define here the animation cursor directories
ANIMATED_CURSORS:=



##################################################################
#find all the cursors

conffiles = $(wildcard *.conf)
cursorfiles:= $(foreach conffile,$(conffiles),$(BUILDDIR)/$(subst ./,,$(subst .conf,,$(conffile))))
cursornames:= $(foreach conffile,$(conffiles),$(subst ./,,$(subst .conf,,$(conffile))))
animcursorfiles:=$(foreach animationfile,$(ANIMATED_CURSORS),$(BUILDDIR)/$(animationfile))
animcursornames:=$(ANIMATED_CURSORS)

CURSORS = $(cursorfiles)
CURSORNAMES= $(cursornames)
ANIMATIONS= $(animcursorfiles)
ANIMATIONNAMES=$(animcursornames)




.PHONY: all


all: $(CURSORS) $(ANIMATIONS)

install: all
	cp -Rf $(BUILDDIR)/* $(CURSORDIR)

#Normal Cursors
define CURSOR_template
$(BUILDDIR)/$(1): $(1).png $(1).conf
	xcursorgen $(1).conf $(BUILDDIR)/$(1)
endef

$(foreach cursor,$(CURSORNAMES),$(eval $(call CURSOR_template,$(cursor))))


#Animated Cursors
define ANIMCURSOR_template
$(BUILDDIR)/$(1):  $(1)/$(1).conf $(1)/*.png
	xcursorgen $(1)/$(1).conf $(BUILDDIR)/$(1)
endef

$(foreach anim,$(ANIMATIONNAMES),$(eval $(call ANIMCURSOR_template,$(anim))))
