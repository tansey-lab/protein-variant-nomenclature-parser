protein_variant_nomenclature_parser/hugo.py:
	python bin/generate_hugo_gene_names.py protein_variant_nomenclature_parser/hugo.py

clean:
	rm -rf protein_variant_nomenclature_parser/hugo.py

test:
	python -m unittest protein_variant_nomenclature_parser/test_parser.py

install: protein_variant_nomenclature_parser/hugo.py
	pip install .

container:
	docker build --platform linux/amd64 .
