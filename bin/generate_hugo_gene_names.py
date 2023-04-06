import requests
import sys
import json


def get_latest_hugo_symbol_list():
    res = requests.get(
        "https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/locus_types/gene_with_protein_product.json"
    )

    return [x["symbol"] for x in res.json()["response"]["docs"]]


TEMPLATE = """
HUGO_GENE_NAMES = {genenamelist}
"""


def generate_code(output_fn, gene_names):
    with open(output_fn, "w") as f:
        f.write(TEMPLATE.replace("{genenamelist}", json.dumps(gene_names)))


if __name__ == "__main__":
    gene_names = get_latest_hugo_symbol_list()
    generate_code(sys.argv[1], gene_names=gene_names)
