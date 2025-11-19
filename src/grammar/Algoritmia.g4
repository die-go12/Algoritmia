grammar Algoritmia;

// ---------- Estructura principal ----------

programa:
    (NEWLINE)* (procedimiento (NEWLINE)+)+ EOF
    ;

procedimiento:
    ID_MAYUS parametros? '|:' NEWLINE+ instrucciones ':|'
    ;

parametros:
    ID_MINUSCULA+
    ;

// ---------- Instrucciones ----------

instrucciones:
    (instruccion (NEWLINE)+)*
    ;

instruccion
    : asignacion
    | lectura
    | escritura
    | condicional
    | while
    | llamada_proc
    | reproduccion
    | addlista
    | poplista
    ;

// asignacion
asignacion:
    ID_MINUSCULA '<-' expr
    ;

// lectura
lectura:
    '<?>' ID_MINUSCULA
    ;

// escritura
escritura:
    '<w>' escritura_item+
    ;

escritura_item:
    STRING
  | expr
    ;

// reproduccion
reproduccion:
    (('(:)' | '<:>') expr+)
    ;

// condicional
condicional:
    'if' expr '|:' NEWLINE+ instructions_block ':|'
    ( 'else' '|:' NEWLINE+ instructions_block ':|' )?
    ;

instructions_block:
    (instruccion (NEWLINE)+)*
    ;

// while
while:
    'while' expr '|:' NEWLINE+ instructions_block ':|'
    ;

// llamada a procedimiento
llamada_proc:
    ID_MAYUS expr*
    ;

// append en listas
addlista:
    ID_MINUSCULA '<<' expr
    ;

// pop de listas
poplista:
    '8<' ID_MINUSCULA '[' expr ']'
    ;

// ---------- Expresiones ----------

expr:
    comparacion
    ;

comparacion:
    aritmetica (('=' | '/=' | '<' | '>' | '<=' | '>=') aritmetica)*
    ;

aritmetica:
    termino (('+' | '-') termino)*
    ;

termino:
    factor (('*' | '/' | '%') factor)*
    ;

factor:
      '(' expr ')'
    | INT
    | ID_MINUSCULA
    | ID_MAYUS               // notas o constantes
    | ID_MINUSCULA '[' expr ']'
    | '#' ID_MINUSCULA
    | lista
    ;

lista:
    '{' elementos_lista? '}'
    ;

elementos_lista:
    expr+
    ;

// ---------- Lexer ----------

STRING:
    '"' (~["\r\n] | '\\' .)* '"'
    ;

INT:
    [0-9]+
    ;

ID_MAYUS:
    [A-Z][A-Za-z0-9_]*      // Procedimientos y notas musicales
    ;

ID_MINUSCULA:
    [a-z_][A-Za-z0-9_]*     // Variables
    ;

WS:
    [ \t]+ -> skip
    ;

NEWLINE:
    ('\r'? '\n' | '\r')+
    ;

COMMENT:
    '###' .*? '###' -> skip
    ;
