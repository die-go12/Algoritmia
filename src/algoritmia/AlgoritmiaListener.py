# Generated from C:/Users/Admin/Desktop/aaa/Algoritmia.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AlgoritmiaParser import AlgoritmiaParser
else:
    from AlgoritmiaParser import AlgoritmiaParser

# This class defines a complete listener for a parse tree produced by AlgoritmiaParser.
class AlgoritmiaListener(ParseTreeListener):

    # Enter a parse tree produced by AlgoritmiaParser#programa.
    def enterPrograma(self, ctx:AlgoritmiaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#programa.
    def exitPrograma(self, ctx:AlgoritmiaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#procedimiento.
    def enterProcedimiento(self, ctx:AlgoritmiaParser.ProcedimientoContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#procedimiento.
    def exitProcedimiento(self, ctx:AlgoritmiaParser.ProcedimientoContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#parametros.
    def enterParametros(self, ctx:AlgoritmiaParser.ParametrosContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#parametros.
    def exitParametros(self, ctx:AlgoritmiaParser.ParametrosContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#instrucciones.
    def enterInstrucciones(self, ctx:AlgoritmiaParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#instrucciones.
    def exitInstrucciones(self, ctx:AlgoritmiaParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#instruccion.
    def enterInstruccion(self, ctx:AlgoritmiaParser.InstruccionContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#instruccion.
    def exitInstruccion(self, ctx:AlgoritmiaParser.InstruccionContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#asignacion.
    def enterAsignacion(self, ctx:AlgoritmiaParser.AsignacionContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#asignacion.
    def exitAsignacion(self, ctx:AlgoritmiaParser.AsignacionContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#lectura.
    def enterLectura(self, ctx:AlgoritmiaParser.LecturaContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#lectura.
    def exitLectura(self, ctx:AlgoritmiaParser.LecturaContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#escritura.
    def enterEscritura(self, ctx:AlgoritmiaParser.EscrituraContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#escritura.
    def exitEscritura(self, ctx:AlgoritmiaParser.EscrituraContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#escritura_item.
    def enterEscritura_item(self, ctx:AlgoritmiaParser.Escritura_itemContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#escritura_item.
    def exitEscritura_item(self, ctx:AlgoritmiaParser.Escritura_itemContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#reproduccion.
    def enterReproduccion(self, ctx:AlgoritmiaParser.ReproduccionContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#reproduccion.
    def exitReproduccion(self, ctx:AlgoritmiaParser.ReproduccionContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#condicional.
    def enterCondicional(self, ctx:AlgoritmiaParser.CondicionalContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#condicional.
    def exitCondicional(self, ctx:AlgoritmiaParser.CondicionalContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#while.
    def enterWhile(self, ctx:AlgoritmiaParser.WhileContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#while.
    def exitWhile(self, ctx:AlgoritmiaParser.WhileContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#llamada_proc.
    def enterLlamada_proc(self, ctx:AlgoritmiaParser.Llamada_procContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#llamada_proc.
    def exitLlamada_proc(self, ctx:AlgoritmiaParser.Llamada_procContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#addlista.
    def enterAddlista(self, ctx:AlgoritmiaParser.AddlistaContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#addlista.
    def exitAddlista(self, ctx:AlgoritmiaParser.AddlistaContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#poplista.
    def enterPoplista(self, ctx:AlgoritmiaParser.PoplistaContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#poplista.
    def exitPoplista(self, ctx:AlgoritmiaParser.PoplistaContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#expr.
    def enterExpr(self, ctx:AlgoritmiaParser.ExprContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#expr.
    def exitExpr(self, ctx:AlgoritmiaParser.ExprContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#comparacion.
    def enterComparacion(self, ctx:AlgoritmiaParser.ComparacionContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#comparacion.
    def exitComparacion(self, ctx:AlgoritmiaParser.ComparacionContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#aritmetica.
    def enterAritmetica(self, ctx:AlgoritmiaParser.AritmeticaContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#aritmetica.
    def exitAritmetica(self, ctx:AlgoritmiaParser.AritmeticaContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#termino.
    def enterTermino(self, ctx:AlgoritmiaParser.TerminoContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#termino.
    def exitTermino(self, ctx:AlgoritmiaParser.TerminoContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#factor.
    def enterFactor(self, ctx:AlgoritmiaParser.FactorContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#factor.
    def exitFactor(self, ctx:AlgoritmiaParser.FactorContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#lista.
    def enterLista(self, ctx:AlgoritmiaParser.ListaContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#lista.
    def exitLista(self, ctx:AlgoritmiaParser.ListaContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#elementos_lista.
    def enterElementos_lista(self, ctx:AlgoritmiaParser.Elementos_listaContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#elementos_lista.
    def exitElementos_lista(self, ctx:AlgoritmiaParser.Elementos_listaContext):
        pass



del AlgoritmiaParser