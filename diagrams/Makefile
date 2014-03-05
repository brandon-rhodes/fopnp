
FORMAT = png
DENSITY = 240
DENSITY = 96

DIAG_SOURCES = $(wildcard *.diag)
DIAG_IMAGES = $(patsubst %.diag, %.$(FORMAT), $(DIAG_SOURCES))

DOT_SOURCES = $(wildcard *.dot)
DOT_IMAGES = $(patsubst %.dot, %.$(FORMAT), $(DOT_SOURCES))

NWDIAG_SOURCES = $(wildcard *.nwdiag)
NWDIAG_IMAGES = $(patsubst %.nwdiag, %.$(FORMAT), $(NWDIAG_SOURCES))

all: $(DIAG_IMAGES) $(DOT_IMAGES) $(NWDIAG_IMAGES)

$(DIAG_IMAGES): %.$(FORMAT): %.diag fixup.py Makefile
	seqdiag -f $(HOME)/.fonts/Inconsolata.otf -Tsvg $(OPTIONS) $<
	python fixup.py $*.svg
	convert -density $(DENSITY) $*.svg $*.$(FORMAT)

$(DOT_IMAGES): %.$(FORMAT): %.dot Makefile
	dot -Tsvg $(OPTIONS) $< > $*.svg
	convert -density $(DENSITY) $*.svg $*.$(FORMAT)

$(NWDIAG_IMAGES): %.$(FORMAT): %.nwdiag Makefile
	nwdiag -f $(HOME)/.fonts/Inconsolata.otf -Tsvg $(OPTIONS) $<
	convert -density $(DENSITY) $*.svg $*.$(FORMAT)
