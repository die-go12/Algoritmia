grammar Algoritmia;

programa:
    procedimiento+ EOF
    ;

procedimiento:

    ID_MAYUS parametros? '|:' instrucciones ':|'
    ;

parametros:
    ID_MINUSCULA+
    ;


instrucciones:
    instruccion*
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

asignacion:
    ID_MINUSCULA '<-' expr
    ;

lectura:
    '<?>' ID_MINUSCULA
    ;

escritura:
    '<w>' escritura_item
    ;

escritura_item:
      STRING
    | expr
    ;

reproduccion:
    ( '(:)' | '<:>' ) expr
    ;

condicional:
    'if' expr '|:' instrucciones ':|'
    ( 'else' '|:' instrucciones ':|' )?
    ;

while:
    'while' expr '|:' instrucciones ':|'
    ;

llamada_proc:
    ID_MAYUS expr*
    ;

addlista:
    ID_MINUSCULA '<' '<' expr
    ;

poplista:
    '8' '<' ID_MINUSCULA '[' expr ']'
    ;

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
      '-' factor
    | '(' expr ')'
    | INT
    | ID_MINUSCULA
    | ID_MAYUS
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


STRING:
    '"' (~["\r\n] | '\\' .)* '"'
    ;

INT:
    [0-9]+
    ;

ID_MAYUS:
    [A-Z][A-Za-z0-9_]*
    ;

ID_MINUSCULA:
    [a-z_][A-Za-z0-9_]*
    ;


WS:
    [ \t\r\n]+ -> skip
    ;

COMMENT:
    '###' .*? '###' -> skip
    ;