GENERATED_FILES_DIR = protein_variant_nomenclature_parser/generated

protein_variant_nomenclature_parser/generated: antlr/HUGOLexer.g4
	cd antlr && antlr -Dlanguage=Python3 ProteinVariant.g4 HUGOLexer.g4 -o ../$(GENERATED_FILES_DIR) -package protein_variant_nomenclature_parser
	touch protein_variant_nomenclature_parser/generated/__init__.py

antlr/HUGOLexer.g4:
	python bin/generate_HUGOlexer.py antlr/HUGOLexer.g4

clean:
	rm -rf $(GENERATED_FILES_DIR) antlr/HUGOLexer.g4
