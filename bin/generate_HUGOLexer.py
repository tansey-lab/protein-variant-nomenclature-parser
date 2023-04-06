import requests
import sys
import os
from pathlib import Path


def get_latest_hugo_symbol_list():
    res = requests.get(
        "https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/locus_types/gene_with_protein_product.json"
    )

    return [x["symbol"] for x in res.json()["response"]["docs"]]


TEMPLATE = """
grammar ProteinVariant;

import HUGOLexer;

gene: {generule};

mutation: gene WS? amino_acid_or_stop WS? number_or_range WS? amino_acid_or_stop;

number_or_range: number (('-' | '_') number)?;

amino_acid_or_stop: AMINO_ACID | STOP_CODON;

number: INT;

WS: [> \t]+ -> skip;

INT: [0-9]+;

AMINO_ACID: [ARNDCQEGHILKMFPSTWYVUO]+;

STOP_CODON: '*';
"""


def generate_lexer(output_dir, gene_names, chunk_size: int = 100):
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)

    num_chunks = (len(gene_names) + chunk_size - 1) // chunk_size
    gene_name_chunks = [
        gene_names[i * chunk_size : (i + 1) * chunk_size] for i in range(num_chunks)
    ]

    lexer_rules = []
    for idx, gene_name_chunk in enumerate(gene_name_chunks):
        gene_name_chunk_quoted = [f"'{x}'" for x in gene_name_chunk]
        lexer_rules.append(f"GENE{idx}: {' | '.join(gene_name_chunk_quoted)};")

    gene_rule = " | ".join(f"GENE{i}" for i in range(num_chunks))

    with open(os.path.join(output_dir, "HUGOLexer.g4"), "w") as f:
        f.write("lexer grammar HUGOLexer;\n\n")

        f.write("\n".join(lexer_rules))

    with open(os.path.join(output_dir, "ProteinVariant.g4"), "w") as f:
        f.write(TEMPLATE.replace("{generule}", gene_rule))


if __name__ == "__main__":
    gene_names = get_latest_hugo_symbol_list()
    generate_lexer(sys.argv[1], gene_names=gene_names)
