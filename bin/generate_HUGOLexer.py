import json
import requests
import sys

def get_latest_hugo_symbol_list():
    res = requests.get(
        "https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/locus_types/gene_with_protein_product.json")

    return [x['symbol'] for x in res.json()['response']['docs']]


def generate_lexer(output_file):
    gene_names = get_latest_hugo_symbol_list()

    with open(output_file, "w") as f:
        f.write("lexer grammar HUGOLexer;\n\n")
        f.write("GENE: " + " | ".join(f"'{gene_name}'" for gene_name in gene_names) + ";\n")


if __name__ == "__main__":
    generate_lexer(sys.argv[1])