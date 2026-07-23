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
	python scripts/check_technical_foundations.py
	python scripts/check_intertextuality.py
	python scripts/check_review_ecosystem.py
	python scripts/check_answers.py
	python scripts/check_projects.py
	mkdocs build --strict
	python scripts/check_rendered_ecosystem.py

build: check

preview: check
	python -m http.server 8000 --directory site

clean:
	rm -rf site .cache
