# Generated from C:/Users/Admin/Desktop/aaa/Algoritmia.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,192,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,4,0,46,8,0,11,0,12,0,47,1,0,1,0,1,1,1,1,3,1,54,
        8,1,1,1,1,1,1,1,1,1,1,2,4,2,61,8,2,11,2,12,2,62,1,3,5,3,66,8,3,10,
        3,12,3,69,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,80,8,4,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,3,8,94,8,8,1,9,1,9,1,
        9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,109,8,10,
        1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,5,12,119,8,12,10,12,12,12,
        122,9,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,15,1,15,1,16,1,16,1,16,5,16,141,8,16,10,16,12,16,144,9,16,
        1,17,1,17,1,17,5,17,149,8,17,10,17,12,17,152,9,17,1,18,1,18,1,18,
        5,18,157,8,18,10,18,12,18,160,9,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,179,
        8,19,1,20,1,20,3,20,183,8,20,1,20,1,20,1,21,4,21,188,8,21,11,21,
        12,21,189,1,21,0,0,22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,0,4,1,0,6,7,2,0,11,11,15,19,1,0,20,21,1,0,22,24,
        196,0,45,1,0,0,0,2,51,1,0,0,0,4,60,1,0,0,0,6,67,1,0,0,0,8,79,1,0,
        0,0,10,81,1,0,0,0,12,85,1,0,0,0,14,88,1,0,0,0,16,93,1,0,0,0,18,95,
        1,0,0,0,20,98,1,0,0,0,22,110,1,0,0,0,24,116,1,0,0,0,26,123,1,0,0,
        0,28,128,1,0,0,0,30,135,1,0,0,0,32,137,1,0,0,0,34,145,1,0,0,0,36,
        153,1,0,0,0,38,178,1,0,0,0,40,180,1,0,0,0,42,187,1,0,0,0,44,46,3,
        2,1,0,45,44,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,
        49,1,0,0,0,49,50,5,0,0,1,50,1,1,0,0,0,51,53,5,32,0,0,52,54,3,4,2,
        0,53,52,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,1,0,0,56,57,
        3,6,3,0,57,58,5,2,0,0,58,3,1,0,0,0,59,61,5,33,0,0,60,59,1,0,0,0,
        61,62,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,5,1,0,0,0,64,66,3,8,
        4,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,7,
        1,0,0,0,69,67,1,0,0,0,70,80,3,10,5,0,71,80,3,12,6,0,72,80,3,14,7,
        0,73,80,3,20,10,0,74,80,3,22,11,0,75,80,3,24,12,0,76,80,3,18,9,0,
        77,80,3,26,13,0,78,80,3,28,14,0,79,70,1,0,0,0,79,71,1,0,0,0,79,72,
        1,0,0,0,79,73,1,0,0,0,79,74,1,0,0,0,79,75,1,0,0,0,79,76,1,0,0,0,
        79,77,1,0,0,0,79,78,1,0,0,0,80,9,1,0,0,0,81,82,5,33,0,0,82,83,5,
        3,0,0,83,84,3,30,15,0,84,11,1,0,0,0,85,86,5,4,0,0,86,87,5,33,0,0,
        87,13,1,0,0,0,88,89,5,5,0,0,89,90,3,16,8,0,90,15,1,0,0,0,91,94,5,
        30,0,0,92,94,3,30,15,0,93,91,1,0,0,0,93,92,1,0,0,0,94,17,1,0,0,0,
        95,96,7,0,0,0,96,97,3,30,15,0,97,19,1,0,0,0,98,99,5,8,0,0,99,100,
        3,30,15,0,100,101,5,1,0,0,101,102,3,6,3,0,102,108,5,2,0,0,103,104,
        5,9,0,0,104,105,5,1,0,0,105,106,3,6,3,0,106,107,5,2,0,0,107,109,
        1,0,0,0,108,103,1,0,0,0,108,109,1,0,0,0,109,21,1,0,0,0,110,111,5,
        10,0,0,111,112,3,30,15,0,112,113,5,1,0,0,113,114,3,6,3,0,114,115,
        5,2,0,0,115,23,1,0,0,0,116,120,5,32,0,0,117,119,3,30,15,0,118,117,
        1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,25,1,
        0,0,0,122,120,1,0,0,0,123,124,5,33,0,0,124,125,5,11,0,0,125,126,
        5,11,0,0,126,127,3,30,15,0,127,27,1,0,0,0,128,129,5,12,0,0,129,130,
        5,11,0,0,130,131,5,33,0,0,131,132,5,13,0,0,132,133,3,30,15,0,133,
        134,5,14,0,0,134,29,1,0,0,0,135,136,3,32,16,0,136,31,1,0,0,0,137,
        142,3,34,17,0,138,139,7,1,0,0,139,141,3,34,17,0,140,138,1,0,0,0,
        141,144,1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,33,1,0,0,0,144,
        142,1,0,0,0,145,150,3,36,18,0,146,147,7,2,0,0,147,149,3,36,18,0,
        148,146,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,
        151,35,1,0,0,0,152,150,1,0,0,0,153,158,3,38,19,0,154,155,7,3,0,0,
        155,157,3,38,19,0,156,154,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,
        0,158,159,1,0,0,0,159,37,1,0,0,0,160,158,1,0,0,0,161,162,5,21,0,
        0,162,179,3,38,19,0,163,164,5,25,0,0,164,165,3,30,15,0,165,166,5,
        26,0,0,166,179,1,0,0,0,167,179,5,31,0,0,168,179,5,33,0,0,169,179,
        5,32,0,0,170,171,5,33,0,0,171,172,5,13,0,0,172,173,3,30,15,0,173,
        174,5,14,0,0,174,179,1,0,0,0,175,176,5,27,0,0,176,179,5,33,0,0,177,
        179,3,40,20,0,178,161,1,0,0,0,178,163,1,0,0,0,178,167,1,0,0,0,178,
        168,1,0,0,0,178,169,1,0,0,0,178,170,1,0,0,0,178,175,1,0,0,0,178,
        177,1,0,0,0,179,39,1,0,0,0,180,182,5,28,0,0,181,183,3,42,21,0,182,
        181,1,0,0,0,182,183,1,0,0,0,183,184,1,0,0,0,184,185,5,29,0,0,185,
        41,1,0,0,0,186,188,3,30,15,0,187,186,1,0,0,0,188,189,1,0,0,0,189,
        187,1,0,0,0,189,190,1,0,0,0,190,43,1,0,0,0,14,47,53,62,67,79,93,
        108,120,142,150,158,178,182,189
    ]

class AlgoritmiaParser ( Parser ):

    grammarFileName = "Algoritmia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|:'", "':|'", "'<-'", "'<?>'", "'<w>'", 
                     "'(:)'", "'<:>'", "'if'", "'else'", "'while'", "'<'", 
                     "'8'", "'['", "']'", "'='", "'/='", "'>'", "'<='", 
                     "'>='", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", 
                     "'#'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "INT", "ID_MAYUS", 
                      "ID_MINUSCULA", "WS", "COMMENT" ]

    RULE_programa = 0
    RULE_procedimiento = 1
    RULE_parametros = 2
    RULE_instrucciones = 3
    RULE_instruccion = 4
    RULE_asignacion = 5
    RULE_lectura = 6
    RULE_escritura = 7
    RULE_escritura_item = 8
    RULE_reproduccion = 9
    RULE_condicional = 10
    RULE_while = 11
    RULE_llamada_proc = 12
    RULE_addlista = 13
    RULE_poplista = 14
    RULE_expr = 15
    RULE_comparacion = 16
    RULE_aritmetica = 17
    RULE_termino = 18
    RULE_factor = 19
    RULE_lista = 20
    RULE_elementos_lista = 21

    ruleNames =  [ "programa", "procedimiento", "parametros", "instrucciones", 
                   "instruccion", "asignacion", "lectura", "escritura", 
                   "escritura_item", "reproduccion", "condicional", "while", 
                   "llamada_proc", "addlista", "poplista", "expr", "comparacion", 
                   "aritmetica", "termino", "factor", "lista", "elementos_lista" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    STRING=30
    INT=31
    ID_MAYUS=32
    ID_MINUSCULA=33
    WS=34
    COMMENT=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AlgoritmiaParser.EOF, 0)

        def procedimiento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgoritmiaParser.ProcedimientoContext)
            else:
                return self.getTypedRuleContext(AlgoritmiaParser.ProcedimientoContext,i)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = AlgoritmiaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.procedimiento()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
                    break

            self.state = 49
            self.match(AlgoritmiaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedimientoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_MAYUS(self):
            return self.getToken(AlgoritmiaParser.ID_MAYUS, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(AlgoritmiaParser.InstruccionesContext,0)


        def parametros(self):
            return self.getTypedRuleContext(AlgoritmiaParser.ParametrosContext,0)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_procedimiento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedimiento" ):
                listener.enterProcedimiento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedimiento" ):
                listener.exitProcedimiento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedimiento" ):
                return visitor.visitProcedimiento(self)
            else:
                return visitor.visitChildren(self)




    def procedimiento(self):

        localctx = AlgoritmiaParser.ProcedimientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_procedimiento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(AlgoritmiaParser.ID_MAYUS)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 52
                self.parametros()


            self.state = 55
            self.match(AlgoritmiaParser.T__0)
            self.state = 56
            self.instrucciones()
            self.state = 57
            self.match(AlgoritmiaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_MINUSCULA(self, i:int=None):
            if i is None:
                return self.getTokens(AlgoritmiaParser.ID_MINUSCULA)
            else:
                return self.getToken(AlgoritmiaParser.ID_MINUSCULA, i)

        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = AlgoritmiaParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.match(AlgoritmiaParser.ID_MINUSCULA)
                self.state = 62 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==33):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgoritmiaParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(AlgoritmiaParser.InstruccionContext,i)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = AlgoritmiaParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instrucciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 12884907504) != 0):
                self.state = 64
                self.instruccion()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(AlgoritmiaParser.AsignacionContext,0)


        def lectura(self):
            return self.getTypedRuleContext(AlgoritmiaParser.LecturaContext,0)


        def escritura(self):
            return self.getTypedRuleContext(AlgoritmiaParser.EscrituraContext,0)


        def condicional(self):
            return self.getTypedRuleContext(AlgoritmiaParser.CondicionalContext,0)


        def while_(self):
            return self.getTypedRuleContext(AlgoritmiaParser.WhileContext,0)


        def llamada_proc(self):
            return self.getTypedRuleContext(AlgoritmiaParser.Llamada_procContext,0)


        def reproduccion(self):
            return self.getTypedRuleContext(AlgoritmiaParser.ReproduccionContext,0)


        def addlista(self):
            return self.getTypedRuleContext(AlgoritmiaParser.AddlistaContext,0)


        def poplista(self):
            return self.getTypedRuleContext(AlgoritmiaParser.PoplistaContext,0)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = AlgoritmiaParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instruccion)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.lectura()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.escritura()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.condicional()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 74
                self.while_()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 75
                self.llamada_proc()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 76
                self.reproduccion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 77
                self.addlista()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 78
                self.poplista()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_MINUSCULA(self):
            return self.getToken(AlgoritmiaParser.ID_MINUSCULA, 0)

        def expr(self):
            return self.getTypedRuleContext(AlgoritmiaParser.ExprContext,0)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = AlgoritmiaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(AlgoritmiaParser.ID_MINUSCULA)
            self.state = 82
            self.match(AlgoritmiaParser.T__2)
            self.state = 83
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LecturaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_MINUSCULA(self):
            return self.getToken(AlgoritmiaParser.ID_MINUSCULA, 0)

        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_lectura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLectura" ):
                listener.enterLectura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLectura" ):
                listener.exitLectura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLectura" ):
                return visitor.visitLectura(self)
            else:
                return visitor.visitChildren(self)




    def lectura(self):

        localctx = AlgoritmiaParser.LecturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(AlgoritmiaParser.T__3)
            self.state = 86
            self.match(AlgoritmiaParser.ID_MINUSCULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscrituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def escritura_item(self):
            return self.getTypedRuleContext(AlgoritmiaParser.Escritura_itemContext,0)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_escritura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscritura" ):
                listener.enterEscritura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscritura" ):
                listener.exitEscritura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscritura" ):
                return visitor.visitEscritura(self)
            else:
                return visitor.visitChildren(self)




    def escritura(self):

        localctx = AlgoritmiaParser.EscrituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_escritura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(AlgoritmiaParser.T__4)
            self.state = 89
            self.escritura_item()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Escritura_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AlgoritmiaParser.STRING, 0)

        def expr(self):
            return self.getTypedRuleContext(AlgoritmiaParser.ExprContext,0)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_escritura_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscritura_item" ):
                listener.enterEscritura_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscritura_item" ):
                listener.exitEscritura_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscritura_item" ):
                return visitor.visitEscritura_item(self)
            else:
                return visitor.visitChildren(self)




    def escritura_item(self):

        localctx = AlgoritmiaParser.Escritura_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_escritura_item)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.match(AlgoritmiaParser.STRING)
                pass
            elif token in [21, 25, 27, 28, 31, 32, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReproduccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(AlgoritmiaParser.ExprContext,0)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_reproduccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReproduccion" ):
                listener.enterReproduccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReproduccion" ):
                listener.exitReproduccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReproduccion" ):
                return visitor.visitReproduccion(self)
            else:
                return visitor.visitChildren(self)




    def reproduccion(self):

        localctx = AlgoritmiaParser.ReproduccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_reproduccion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 96
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(AlgoritmiaParser.ExprContext,0)


        def instrucciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgoritmiaParser.InstruccionesContext)
            else:
                return self.getTypedRuleContext(AlgoritmiaParser.InstruccionesContext,i)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = AlgoritmiaParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(AlgoritmiaParser.T__7)
            self.state = 99
            self.expr()
            self.state = 100
            self.match(AlgoritmiaParser.T__0)
            self.state = 101
            self.instrucciones()
            self.state = 102
            self.match(AlgoritmiaParser.T__1)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 103
                self.match(AlgoritmiaParser.T__8)
                self.state = 104
                self.match(AlgoritmiaParser.T__0)
                self.state = 105
                self.instrucciones()
                self.state = 106
                self.match(AlgoritmiaParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(AlgoritmiaParser.ExprContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(AlgoritmiaParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = AlgoritmiaParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(AlgoritmiaParser.T__9)
            self.state = 111
            self.expr()
            self.state = 112
            self.match(AlgoritmiaParser.T__0)
            self.state = 113
            self.instrucciones()
            self.state = 114
            self.match(AlgoritmiaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Llamada_procContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_MAYUS(self):
            return self.getToken(AlgoritmiaParser.ID_MAYUS, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgoritmiaParser.ExprContext)
            else:
                return self.getTypedRuleContext(AlgoritmiaParser.ExprContext,i)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_llamada_proc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada_proc" ):
                listener.enterLlamada_proc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada_proc" ):
                listener.exitLlamada_proc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada_proc" ):
                return visitor.visitLlamada_proc(self)
            else:
                return visitor.visitChildren(self)




    def llamada_proc(self):

        localctx = AlgoritmiaParser.Llamada_procContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_llamada_proc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(AlgoritmiaParser.ID_MAYUS)
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 117
                    self.expr() 
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddlistaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_MINUSCULA(self):
            return self.getToken(AlgoritmiaParser.ID_MINUSCULA, 0)

        def expr(self):
            return self.getTypedRuleContext(AlgoritmiaParser.ExprContext,0)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_addlista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddlista" ):
                listener.enterAddlista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddlista" ):
                listener.exitAddlista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddlista" ):
                return visitor.visitAddlista(self)
            else:
                return visitor.visitChildren(self)




    def addlista(self):

        localctx = AlgoritmiaParser.AddlistaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_addlista)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(AlgoritmiaParser.ID_MINUSCULA)
            self.state = 124
            self.match(AlgoritmiaParser.T__10)
            self.state = 125
            self.match(AlgoritmiaParser.T__10)
            self.state = 126
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PoplistaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_MINUSCULA(self):
            return self.getToken(AlgoritmiaParser.ID_MINUSCULA, 0)

        def expr(self):
            return self.getTypedRuleContext(AlgoritmiaParser.ExprContext,0)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_poplista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPoplista" ):
                listener.enterPoplista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPoplista" ):
                listener.exitPoplista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPoplista" ):
                return visitor.visitPoplista(self)
            else:
                return visitor.visitChildren(self)




    def poplista(self):

        localctx = AlgoritmiaParser.PoplistaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_poplista)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(AlgoritmiaParser.T__11)
            self.state = 129
            self.match(AlgoritmiaParser.T__10)
            self.state = 130
            self.match(AlgoritmiaParser.ID_MINUSCULA)
            self.state = 131
            self.match(AlgoritmiaParser.T__12)
            self.state = 132
            self.expr()
            self.state = 133
            self.match(AlgoritmiaParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparacion(self):
            return self.getTypedRuleContext(AlgoritmiaParser.ComparacionContext,0)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = AlgoritmiaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.comparacion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgoritmiaParser.AritmeticaContext)
            else:
                return self.getTypedRuleContext(AlgoritmiaParser.AritmeticaContext,i)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_comparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)




    def comparacion(self):

        localctx = AlgoritmiaParser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.aritmetica()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1017856) != 0):
                self.state = 138
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1017856) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 139
                self.aritmetica()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgoritmiaParser.TerminoContext)
            else:
                return self.getTypedRuleContext(AlgoritmiaParser.TerminoContext,i)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_aritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAritmetica" ):
                listener.enterAritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAritmetica" ):
                listener.exitAritmetica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAritmetica" ):
                return visitor.visitAritmetica(self)
            else:
                return visitor.visitChildren(self)




    def aritmetica(self):

        localctx = AlgoritmiaParser.AritmeticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_aritmetica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.termino()
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 146
                    _la = self._input.LA(1)
                    if not(_la==20 or _la==21):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 147
                    self.termino() 
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgoritmiaParser.FactorContext)
            else:
                return self.getTypedRuleContext(AlgoritmiaParser.FactorContext,i)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = AlgoritmiaParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.factor()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0):
                self.state = 154
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 155
                self.factor()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(AlgoritmiaParser.FactorContext,0)


        def expr(self):
            return self.getTypedRuleContext(AlgoritmiaParser.ExprContext,0)


        def INT(self):
            return self.getToken(AlgoritmiaParser.INT, 0)

        def ID_MINUSCULA(self):
            return self.getToken(AlgoritmiaParser.ID_MINUSCULA, 0)

        def ID_MAYUS(self):
            return self.getToken(AlgoritmiaParser.ID_MAYUS, 0)

        def lista(self):
            return self.getTypedRuleContext(AlgoritmiaParser.ListaContext,0)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = AlgoritmiaParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_factor)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(AlgoritmiaParser.T__20)
                self.state = 162
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(AlgoritmiaParser.T__24)
                self.state = 164
                self.expr()
                self.state = 165
                self.match(AlgoritmiaParser.T__25)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.match(AlgoritmiaParser.INT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 168
                self.match(AlgoritmiaParser.ID_MINUSCULA)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 169
                self.match(AlgoritmiaParser.ID_MAYUS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 170
                self.match(AlgoritmiaParser.ID_MINUSCULA)
                self.state = 171
                self.match(AlgoritmiaParser.T__12)
                self.state = 172
                self.expr()
                self.state = 173
                self.match(AlgoritmiaParser.T__13)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 175
                self.match(AlgoritmiaParser.T__26)
                self.state = 176
                self.match(AlgoritmiaParser.ID_MINUSCULA)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 177
                self.lista()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementos_lista(self):
            return self.getTypedRuleContext(AlgoritmiaParser.Elementos_listaContext,0)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
            else:
                return visitor.visitChildren(self)




    def lista(self):

        localctx = AlgoritmiaParser.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(AlgoritmiaParser.T__27)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15470690304) != 0):
                self.state = 181
                self.elementos_lista()


            self.state = 184
            self.match(AlgoritmiaParser.T__28)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elementos_listaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgoritmiaParser.ExprContext)
            else:
                return self.getTypedRuleContext(AlgoritmiaParser.ExprContext,i)


        def getRuleIndex(self):
            return AlgoritmiaParser.RULE_elementos_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementos_lista" ):
                listener.enterElementos_lista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementos_lista" ):
                listener.exitElementos_lista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementos_lista" ):
                return visitor.visitElementos_lista(self)
            else:
                return visitor.visitChildren(self)




    def elementos_lista(self):

        localctx = AlgoritmiaParser.Elementos_listaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_elementos_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 186
                self.expr()
                self.state = 189 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 15470690304) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





