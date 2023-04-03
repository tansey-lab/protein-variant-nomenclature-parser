import sys
from antlr4 import *

from protein_variant_nomenclature_parser.generated.ProteinVariantLexer import ProteinVariantLexer
from protein_variant_nomenclature_parser.generated.ProteinVariantParser import ProteinVariantParser
from protein_variant_nomenclature_parser.generated.ProteinVariantListener import ProteinVariantListener

class ProteinVariantExtractListener(ProteinVariantListener):
    def __init__(self):
        self.result = []

    def exitGene(self, ctx):
        self.result.append(ctx.getText())

    def exitProteinVariant(self, ctx):
        self.result.extend([
            ctx.prefix.text,
            self.parse_number_or_range(ctx.number_or_range()),
            ctx.suffix.text
        ])

    def parse_number_or_range(self, ctx):
        numbers = [int(number.text) for number in ctx.number()]
        if len(numbers) == 1:
            return numbers[0]
        else:
            return numbers

def parse_ProteinVariant_string(input_string):
    input_stream = InputStream(input_string)
    lexer = ProteinVariantLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ProteinVariantParser(token_stream)
    tree = parser.ProteinVariant()

    listener = ProteinVariantExtractListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.result
