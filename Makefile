# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = GentooPolicyGuide
SOURCEDIR     = .
BUILDDIR      = _build

all: html $(BUILDDIR)/html/combined.html

$(BUILDDIR)/html/combined.html: singlehtml
	cp $(BUILDDIR)/singlehtml/index.html $@

.PHONY: all Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
