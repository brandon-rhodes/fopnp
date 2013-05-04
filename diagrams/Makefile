
FORMAT = png
DIAG_SOURCES = $(wildcard *.diag)
DIAG_IMAGES = $(patsubst %.diag, %.$(FORMAT), $(DIAG_SOURCES))

all: $(DIAG_IMAGES)

$(DIAG_IMAGES): %.$(FORMAT): %.diag fixup.py Makefile
	seqdiag -f $(HOME)/.fonts/Inconsolata.otf -Tsvg $(OPTIONS) $<
	python fixup.py $*.svg
	convert -density 240 $*.svg $*.$(FORMAT)
