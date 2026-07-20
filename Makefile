.PHONY: install serve indexes manuscripts check build preview clean

install:
	python -m pip install -r requirements.txt

serve:
	mkdocs serve

indexes:
	python scripts/build_workflow_index.py
	python scripts/check_translation_coverage.py --output release/translation-coverage.md

manuscripts:
	python scripts/build_review_manuscripts.py

check: indexes manuscripts
	python scripts/check_handbook.py
	python scripts/check_answers.py
	python scripts/check_projects.py
	mkdocs build --strict

build: check

preview: check
	python -m http.server 8000 --directory site

clean:
	rm -rf site .cache
