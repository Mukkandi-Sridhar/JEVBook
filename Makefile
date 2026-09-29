.PHONY: all fonts test figures labs listings pdf html epub book check

all: test figures labs pdf

fonts:
	bash tools/install_fonts.sh

test:
	python3 -m pytest -q

figures:
	python3 tools/build_figures.py all

labs:
	python3 tools/run_labs.py

listings:
	python3 tools/check_listings.py

pdf:
	quarto render --to pdf

html:
	quarto render --to html

epub:
	quarto render --to epub

book: pdf html epub

check: test labs listings
	python3 tools/voice_check.py chapters/*.qmd
