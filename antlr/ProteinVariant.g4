grammar ProteinVariant;

import HUGOLexer;

mutation: gene WS prefix=AA number_or_range suffix=AA;

gene: GENE;

number_or_range: number (('-' | '_') number)?;

number: INT;

WS: [ \t]+ -> skip;

AA: [ARNDCQEGHILKMFPSTWYVUO*];
INT: [0-9]+;
