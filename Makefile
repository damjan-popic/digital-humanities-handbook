.PHONY: install install-authoring serve indexes manuscripts scholarly-work-samples archival-friction-packet contested-models-packet text-nlp-validation text-nlp-validation-models check build preview clean

install:
	python -m pip install -r requirements.txt

install-authoring:
	python -m pip install -r requirements-authoring.txt

serve:
	mkdocs serve

indexes:
	python scripts/build_workflow_index.py
	python scripts/check_translation_coverage.py --output release/translation-coverage.md

manuscripts:
	python scripts/build_review_manuscripts.py

scholarly-work-samples:
	python scripts/build_scholarly_work_documents.py --repo-root .
	python scripts/build_scholarly_work_workbook.py --repo-root .
	python scripts/build_scholarly_work_snapshot.py --repo-root .

archival-friction-packet:
	python scripts/build_archival_friction_packet.py --repo-root .

contested-models-packet:
	python scripts/build_contested_models_packet.py

text-nlp-validation:
	python scripts/build_text_nlp_validation.py
	python scripts/check_text_nlp_validation.py

# Optional: downloads/uses heavyweight model resources and is deliberately not
# part of ordinary CI or the Pages build.
text-nlp-validation-models:
	python teaching-data/text-nlp-validation/run_optional_models.py --output .cache/text-nlp-validation-models --resources-dir .cache/classla-resources --download

check: indexes manuscripts
	python scripts/check_handbook.py
	python scripts/check_technical_foundations.py
	python scripts/check_scholarly_work_foundations.py
	python scripts/check_scholarly_work_samples.py
	python scripts/build_archival_friction_packet.py --repo-root . --check
	python scripts/check_archival_friction.py
	python scripts/build_contested_models_packet.py --check
	python scripts/check_contested_models.py
	python scripts/build_text_nlp_validation.py --check
	python scripts/check_text_nlp_validation.py
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
