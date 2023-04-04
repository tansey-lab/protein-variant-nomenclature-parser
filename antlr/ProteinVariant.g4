grammar ProteinVariant;

import HUGOLexer;

mutation: gene WS? amino_acid_or_stop WS? number_or_range WS? amino_acid_or_stop;

gene: GENE;

number_or_range: number (('-' | '_') number)?;

amino_acid_or_stop: AMINO_ACID | STOP_CODON;

number: INT;

WS: [> \t]+ -> skip;

INT: [0-9]+;

AMINO_ACID: [ARNDCQEGHILKMFPSTWYVUO]+;

STOP_CODON: '*';
