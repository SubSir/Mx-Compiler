# Generated from llvm.g4 by ANTLR 4.13.2
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
        4,1,54,273,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,0,5,0,
        55,8,0,10,0,12,0,58,9,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,67,8,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,4,3,79,8,3,11,3,12,3,80,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,90,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,
        114,8,7,10,7,12,7,117,9,7,3,7,119,8,7,1,8,1,8,1,8,5,8,124,8,8,10,
        8,12,8,127,9,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,135,8,9,1,10,1,10,1,10,
        4,10,140,8,10,11,10,12,10,141,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,3,11,153,8,11,1,12,1,12,1,12,3,12,158,8,12,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,3,13,176,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,
        15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,3,16,204,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,
        19,3,19,226,8,19,1,19,1,19,1,19,1,19,1,19,1,19,4,19,234,8,19,11,
        19,12,19,235,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,
        21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,3,23,269,8,23,1,24,1,24,1,
        24,0,0,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,0,5,1,0,1,4,1,0,23,32,1,0,50,51,1,0,40,45,2,0,47,
        47,53,53,273,0,56,1,0,0,0,2,59,1,0,0,0,4,61,1,0,0,0,6,70,1,0,0,0,
        8,84,1,0,0,0,10,93,1,0,0,0,12,99,1,0,0,0,14,118,1,0,0,0,16,120,1,
        0,0,0,18,134,1,0,0,0,20,136,1,0,0,0,22,152,1,0,0,0,24,154,1,0,0,
        0,26,175,1,0,0,0,28,177,1,0,0,0,30,185,1,0,0,0,32,203,1,0,0,0,34,
        205,1,0,0,0,36,213,1,0,0,0,38,220,1,0,0,0,40,237,1,0,0,0,42,246,
        1,0,0,0,44,248,1,0,0,0,46,268,1,0,0,0,48,270,1,0,0,0,50,55,3,6,3,
        0,51,55,3,4,2,0,52,55,3,10,5,0,53,55,3,12,6,0,54,50,1,0,0,0,54,51,
        1,0,0,0,54,52,1,0,0,0,54,53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,
        56,57,1,0,0,0,57,1,1,0,0,0,58,56,1,0,0,0,59,60,7,0,0,0,60,3,1,0,
        0,0,61,62,5,5,0,0,62,63,3,2,1,0,63,64,5,51,0,0,64,66,5,6,0,0,65,
        67,3,16,8,0,66,65,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,69,5,7,
        0,0,69,5,1,0,0,0,70,71,5,8,0,0,71,72,3,2,1,0,72,73,5,51,0,0,73,74,
        5,6,0,0,74,75,3,14,7,0,75,76,5,7,0,0,76,78,5,9,0,0,77,79,3,20,10,
        0,78,77,1,0,0,0,79,80,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,82,
        1,0,0,0,82,83,5,10,0,0,83,7,1,0,0,0,84,85,5,50,0,0,85,86,5,11,0,
        0,86,87,5,12,0,0,87,89,5,9,0,0,88,90,3,16,8,0,89,88,1,0,0,0,89,90,
        1,0,0,0,90,91,1,0,0,0,91,92,5,10,0,0,92,9,1,0,0,0,93,94,5,51,0,0,
        94,95,5,11,0,0,95,96,5,13,0,0,96,97,3,2,1,0,97,98,3,48,24,0,98,11,
        1,0,0,0,99,100,5,51,0,0,100,101,5,11,0,0,101,102,5,13,0,0,102,103,
        5,14,0,0,103,104,5,53,0,0,104,105,5,15,0,0,105,106,5,16,0,0,106,
        107,5,17,0,0,107,108,5,18,0,0,108,109,5,52,0,0,109,13,1,0,0,0,110,
        115,3,18,9,0,111,112,5,19,0,0,112,114,3,18,9,0,113,111,1,0,0,0,114,
        117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,119,1,0,0,0,117,
        115,1,0,0,0,118,110,1,0,0,0,118,119,1,0,0,0,119,15,1,0,0,0,120,125,
        3,2,1,0,121,122,5,19,0,0,122,124,3,2,1,0,123,121,1,0,0,0,124,127,
        1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,17,1,0,0,0,127,125,1,
        0,0,0,128,129,3,2,1,0,129,130,5,50,0,0,130,135,1,0,0,0,131,132,3,
        2,1,0,132,133,5,51,0,0,133,135,1,0,0,0,134,128,1,0,0,0,134,131,1,
        0,0,0,135,19,1,0,0,0,136,137,5,48,0,0,137,139,5,20,0,0,138,140,3,
        22,11,0,139,138,1,0,0,0,140,141,1,0,0,0,141,139,1,0,0,0,141,142,
        1,0,0,0,142,21,1,0,0,0,143,153,3,24,12,0,144,153,3,26,13,0,145,153,
        3,28,14,0,146,153,3,32,16,0,147,153,3,34,17,0,148,153,3,36,18,0,
        149,153,3,38,19,0,150,153,3,40,20,0,151,153,3,44,22,0,152,143,1,
        0,0,0,152,144,1,0,0,0,152,145,1,0,0,0,152,146,1,0,0,0,152,147,1,
        0,0,0,152,148,1,0,0,0,152,149,1,0,0,0,152,150,1,0,0,0,152,151,1,
        0,0,0,153,23,1,0,0,0,154,155,5,21,0,0,155,157,3,2,1,0,156,158,3,
        46,23,0,157,156,1,0,0,0,157,158,1,0,0,0,158,25,1,0,0,0,159,160,5,
        22,0,0,160,161,5,3,0,0,161,162,5,51,0,0,162,163,5,6,0,0,163,164,
        3,14,7,0,164,165,5,7,0,0,165,176,1,0,0,0,166,167,5,50,0,0,167,168,
        5,11,0,0,168,169,5,22,0,0,169,170,3,2,1,0,170,171,5,51,0,0,171,172,
        5,6,0,0,172,173,3,14,7,0,173,174,5,7,0,0,174,176,1,0,0,0,175,159,
        1,0,0,0,175,166,1,0,0,0,176,27,1,0,0,0,177,178,5,50,0,0,178,179,
        5,11,0,0,179,180,3,30,15,0,180,181,3,2,1,0,181,182,3,46,23,0,182,
        183,5,19,0,0,183,184,3,46,23,0,184,29,1,0,0,0,185,186,7,1,0,0,186,
        31,1,0,0,0,187,188,5,33,0,0,188,189,5,34,0,0,189,190,5,35,0,0,190,
        204,5,48,0,0,191,192,5,33,0,0,192,193,5,4,0,0,193,194,3,46,23,0,
        194,195,5,19,0,0,195,196,5,34,0,0,196,197,5,35,0,0,197,198,5,48,
        0,0,198,199,5,19,0,0,199,200,5,34,0,0,200,201,5,35,0,0,201,202,5,
        48,0,0,202,204,1,0,0,0,203,187,1,0,0,0,203,191,1,0,0,0,204,33,1,
        0,0,0,205,206,5,50,0,0,206,207,5,11,0,0,207,208,5,36,0,0,208,209,
        3,2,1,0,209,210,5,19,0,0,210,211,5,2,0,0,211,212,7,2,0,0,212,35,
        1,0,0,0,213,214,5,37,0,0,214,215,3,2,1,0,215,216,3,46,23,0,216,217,
        5,19,0,0,217,218,5,2,0,0,218,219,7,2,0,0,219,37,1,0,0,0,220,221,
        5,50,0,0,221,222,5,11,0,0,222,225,5,38,0,0,223,226,3,2,1,0,224,226,
        5,50,0,0,225,223,1,0,0,0,225,224,1,0,0,0,226,227,1,0,0,0,227,228,
        5,19,0,0,228,229,5,2,0,0,229,230,7,2,0,0,230,233,5,19,0,0,231,232,
        5,1,0,0,232,234,3,46,23,0,233,231,1,0,0,0,234,235,1,0,0,0,235,233,
        1,0,0,0,235,236,1,0,0,0,236,39,1,0,0,0,237,238,5,50,0,0,238,239,
        5,11,0,0,239,240,5,39,0,0,240,241,3,42,21,0,241,242,3,2,1,0,242,
        243,3,46,23,0,243,244,5,19,0,0,244,245,3,46,23,0,245,41,1,0,0,0,
        246,247,7,3,0,0,247,43,1,0,0,0,248,249,5,50,0,0,249,250,5,11,0,0,
        250,251,5,46,0,0,251,252,3,2,1,0,252,253,5,14,0,0,253,254,3,46,23,
        0,254,255,5,19,0,0,255,256,5,35,0,0,256,257,5,48,0,0,257,258,5,17,
        0,0,258,259,5,19,0,0,259,260,5,14,0,0,260,261,3,46,23,0,261,262,
        5,19,0,0,262,263,5,35,0,0,263,264,5,48,0,0,264,265,5,17,0,0,265,
        45,1,0,0,0,266,269,5,50,0,0,267,269,3,48,24,0,268,266,1,0,0,0,268,
        267,1,0,0,0,269,47,1,0,0,0,270,271,7,4,0,0,271,49,1,0,0,0,17,54,
        56,66,80,89,115,118,125,134,141,152,157,175,203,225,235,268
    ]

class llvmParser ( Parser ):

    grammarFileName = "llvm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'i32'", "'ptr'", "'void'", "'i1'", "'declare'", 
                     "'('", "')'", "'define'", "'{'", "'}'", "'='", "'type'", 
                     "'global'", "'['", "'x'", "'i8'", "']'", "'c'", "','", 
                     "':'", "'ret'", "'call'", "'add'", "'sub'", "'mul'", 
                     "'sdiv'", "'srem'", "'shl'", "'ashl'", "'and'", "'or'", 
                     "'xor'", "'br'", "'label'", "'%'", "'load'", "'store'", 
                     "'getelementptr'", "'icmp'", "'eq'", "'ne'", "'slt'", 
                     "'sgt'", "'sle'", "'sge'", "'phi'", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Label", "Identifier", "Privatevariable", "Global_var", 
                      "StringLiteral", "INTEGER", "WS" ]

    RULE_module = 0
    RULE_type = 1
    RULE_function_declare = 2
    RULE_function = 3
    RULE_typedelcare = 4
    RULE_globalvariable = 5
    RULE_string_declare = 6
    RULE_params = 7
    RULE_types = 8
    RULE_parameter = 9
    RULE_basic_block = 10
    RULE_instruction = 11
    RULE_ret = 12
    RULE_call = 13
    RULE_binary_op = 14
    RULE_bin_op = 15
    RULE_branch = 16
    RULE_load = 17
    RULE_store = 18
    RULE_getelementptr = 19
    RULE_compare = 20
    RULE_cond = 21
    RULE_phi = 22
    RULE_value = 23
    RULE_constant = 24

    ruleNames =  [ "module", "type", "function_declare", "function", "typedelcare", 
                   "globalvariable", "string_declare", "params", "types", 
                   "parameter", "basic_block", "instruction", "ret", "call", 
                   "binary_op", "bin_op", "branch", "load", "store", "getelementptr", 
                   "compare", "cond", "phi", "value", "constant" ]

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
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    Label=48
    Identifier=49
    Privatevariable=50
    Global_var=51
    StringLiteral=52
    INTEGER=53
    WS=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ModuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.FunctionContext)
            else:
                return self.getTypedRuleContext(llvmParser.FunctionContext,i)


        def function_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.Function_declareContext)
            else:
                return self.getTypedRuleContext(llvmParser.Function_declareContext,i)


        def globalvariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.GlobalvariableContext)
            else:
                return self.getTypedRuleContext(llvmParser.GlobalvariableContext,i)


        def string_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.String_declareContext)
            else:
                return self.getTypedRuleContext(llvmParser.String_declareContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_module

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule" ):
                listener.enterModule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule" ):
                listener.exitModule(self)




    def module(self):

        localctx = llvmParser.ModuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251799813685536) != 0):
                self.state = 54
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 50
                    self.function()
                    pass

                elif la_ == 2:
                    self.state = 51
                    self.function_declare()
                    pass

                elif la_ == 3:
                    self.state = 52
                    self.globalvariable()
                    pass

                elif la_ == 4:
                    self.state = 53
                    self.string_declare()
                    pass


                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return llvmParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = llvmParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def types(self):
            return self.getTypedRuleContext(llvmParser.TypesContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_function_declare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declare" ):
                listener.enterFunction_declare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declare" ):
                listener.exitFunction_declare(self)




    def function_declare(self):

        localctx = llvmParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(llvmParser.T__4)
            self.state = 62
            self.type_()
            self.state = 63
            self.match(llvmParser.Global_var)
            self.state = 64
            self.match(llvmParser.T__5)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 65
                self.types()


            self.state = 68
            self.match(llvmParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def params(self):
            return self.getTypedRuleContext(llvmParser.ParamsContext,0)


        def basic_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.Basic_blockContext)
            else:
                return self.getTypedRuleContext(llvmParser.Basic_blockContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = llvmParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(llvmParser.T__7)
            self.state = 71
            self.type_()
            self.state = 72
            self.match(llvmParser.Global_var)
            self.state = 73
            self.match(llvmParser.T__5)
            self.state = 74
            self.params()
            self.state = 75
            self.match(llvmParser.T__6)
            self.state = 76
            self.match(llvmParser.T__8)
            self.state = 78 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 77
                self.basic_block()
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==48):
                    break

            self.state = 82
            self.match(llvmParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedelcareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def types(self):
            return self.getTypedRuleContext(llvmParser.TypesContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_typedelcare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedelcare" ):
                listener.enterTypedelcare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedelcare" ):
                listener.exitTypedelcare(self)




    def typedelcare(self):

        localctx = llvmParser.TypedelcareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typedelcare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(llvmParser.Privatevariable)
            self.state = 85
            self.match(llvmParser.T__10)
            self.state = 86
            self.match(llvmParser.T__11)
            self.state = 87
            self.match(llvmParser.T__8)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 88
                self.types()


            self.state = 91
            self.match(llvmParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalvariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def constant(self):
            return self.getTypedRuleContext(llvmParser.ConstantContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_globalvariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalvariable" ):
                listener.enterGlobalvariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalvariable" ):
                listener.exitGlobalvariable(self)




    def globalvariable(self):

        localctx = llvmParser.GlobalvariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_globalvariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(llvmParser.Global_var)
            self.state = 94
            self.match(llvmParser.T__10)
            self.state = 95
            self.match(llvmParser.T__12)
            self.state = 96
            self.type_()
            self.state = 97
            self.constant()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def INTEGER(self):
            return self.getToken(llvmParser.INTEGER, 0)

        def StringLiteral(self):
            return self.getToken(llvmParser.StringLiteral, 0)

        def getRuleIndex(self):
            return llvmParser.RULE_string_declare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_declare" ):
                listener.enterString_declare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_declare" ):
                listener.exitString_declare(self)




    def string_declare(self):

        localctx = llvmParser.String_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_string_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(llvmParser.Global_var)
            self.state = 100
            self.match(llvmParser.T__10)
            self.state = 101
            self.match(llvmParser.T__12)
            self.state = 102
            self.match(llvmParser.T__13)
            self.state = 103
            self.match(llvmParser.INTEGER)
            self.state = 104
            self.match(llvmParser.T__14)
            self.state = 105
            self.match(llvmParser.T__15)
            self.state = 106
            self.match(llvmParser.T__16)
            self.state = 107
            self.match(llvmParser.T__17)
            self.state = 108
            self.match(llvmParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.ParameterContext)
            else:
                return self.getTypedRuleContext(llvmParser.ParameterContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = llvmParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 110
                self.parameter()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==19:
                    self.state = 111
                    self.match(llvmParser.T__18)
                    self.state = 112
                    self.parameter()
                    self.state = 117
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.TypeContext)
            else:
                return self.getTypedRuleContext(llvmParser.TypeContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypes" ):
                listener.enterTypes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypes" ):
                listener.exitTypes(self)




    def types(self):

        localctx = llvmParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.type_()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 121
                self.match(llvmParser.T__18)
                self.state = 122
                self.type_()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def getRuleIndex(self):
            return llvmParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = llvmParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameter)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.type_()
                self.state = 129
                self.match(llvmParser.Privatevariable)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.type_()
                self.state = 132
                self.match(llvmParser.Global_var)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Label(self):
            return self.getToken(llvmParser.Label, 0)

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.InstructionContext)
            else:
                return self.getTypedRuleContext(llvmParser.InstructionContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_basic_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasic_block" ):
                listener.enterBasic_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasic_block" ):
                listener.exitBasic_block(self)




    def basic_block(self):

        localctx = llvmParser.Basic_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_basic_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(llvmParser.Label)
            self.state = 137
            self.match(llvmParser.T__19)
            self.state = 139 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 138
                self.instruction()
                self.state = 141 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1126045942022144) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ret(self):
            return self.getTypedRuleContext(llvmParser.RetContext,0)


        def call(self):
            return self.getTypedRuleContext(llvmParser.CallContext,0)


        def binary_op(self):
            return self.getTypedRuleContext(llvmParser.Binary_opContext,0)


        def branch(self):
            return self.getTypedRuleContext(llvmParser.BranchContext,0)


        def load(self):
            return self.getTypedRuleContext(llvmParser.LoadContext,0)


        def store(self):
            return self.getTypedRuleContext(llvmParser.StoreContext,0)


        def getelementptr(self):
            return self.getTypedRuleContext(llvmParser.GetelementptrContext,0)


        def compare(self):
            return self.getTypedRuleContext(llvmParser.CompareContext,0)


        def phi(self):
            return self.getTypedRuleContext(llvmParser.PhiContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = llvmParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_instruction)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.ret()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.binary_op()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.branch()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 147
                self.load()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 148
                self.store()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 149
                self.getelementptr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 150
                self.compare()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 151
                self.phi()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def value(self):
            return self.getTypedRuleContext(llvmParser.ValueContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_ret

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRet" ):
                listener.enterRet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRet" ):
                listener.exitRet(self)




    def ret(self):

        localctx = llvmParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ret)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(llvmParser.T__20)
            self.state = 155
            self.type_()
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 156
                self.value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def params(self):
            return self.getTypedRuleContext(llvmParser.ParamsContext,0)


        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = llvmParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_call)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(llvmParser.T__21)
                self.state = 160
                self.match(llvmParser.T__2)
                self.state = 161
                self.match(llvmParser.Global_var)
                self.state = 162
                self.match(llvmParser.T__5)
                self.state = 163
                self.params()
                self.state = 164
                self.match(llvmParser.T__6)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(llvmParser.Privatevariable)
                self.state = 167
                self.match(llvmParser.T__10)
                self.state = 168
                self.match(llvmParser.T__21)
                self.state = 169
                self.type_()
                self.state = 170
                self.match(llvmParser.Global_var)
                self.state = 171
                self.match(llvmParser.T__5)
                self.state = 172
                self.params()
                self.state = 173
                self.match(llvmParser.T__6)
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


    class Binary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def bin_op(self):
            return self.getTypedRuleContext(llvmParser.Bin_opContext,0)


        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.ValueContext)
            else:
                return self.getTypedRuleContext(llvmParser.ValueContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_binary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_op" ):
                listener.enterBinary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_op" ):
                listener.exitBinary_op(self)




    def binary_op(self):

        localctx = llvmParser.Binary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_binary_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(llvmParser.Privatevariable)
            self.state = 178
            self.match(llvmParser.T__10)
            self.state = 179
            self.bin_op()
            self.state = 180
            self.type_()
            self.state = 181
            self.value()
            self.state = 182
            self.match(llvmParser.T__18)
            self.state = 183
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bin_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return llvmParser.RULE_bin_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBin_op" ):
                listener.enterBin_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBin_op" ):
                listener.exitBin_op(self)




    def bin_op(self):

        localctx = llvmParser.Bin_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_bin_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8581545984) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BranchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Label(self, i:int=None):
            if i is None:
                return self.getTokens(llvmParser.Label)
            else:
                return self.getToken(llvmParser.Label, i)

        def value(self):
            return self.getTypedRuleContext(llvmParser.ValueContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_branch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBranch" ):
                listener.enterBranch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBranch" ):
                listener.exitBranch(self)




    def branch(self):

        localctx = llvmParser.BranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_branch)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(llvmParser.T__32)
                self.state = 188
                self.match(llvmParser.T__33)
                self.state = 189
                self.match(llvmParser.T__34)
                self.state = 190
                self.match(llvmParser.Label)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(llvmParser.T__32)
                self.state = 192
                self.match(llvmParser.T__3)
                self.state = 193
                self.value()
                self.state = 194
                self.match(llvmParser.T__18)
                self.state = 195
                self.match(llvmParser.T__33)
                self.state = 196
                self.match(llvmParser.T__34)
                self.state = 197
                self.match(llvmParser.Label)
                self.state = 198
                self.match(llvmParser.T__18)
                self.state = 199
                self.match(llvmParser.T__33)
                self.state = 200
                self.match(llvmParser.T__34)
                self.state = 201
                self.match(llvmParser.Label)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self, i:int=None):
            if i is None:
                return self.getTokens(llvmParser.Privatevariable)
            else:
                return self.getToken(llvmParser.Privatevariable, i)

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def getRuleIndex(self):
            return llvmParser.RULE_load

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoad" ):
                listener.enterLoad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoad" ):
                listener.exitLoad(self)




    def load(self):

        localctx = llvmParser.LoadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_load)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(llvmParser.Privatevariable)
            self.state = 206
            self.match(llvmParser.T__10)
            self.state = 207
            self.match(llvmParser.T__35)
            self.state = 208
            self.type_()
            self.state = 209
            self.match(llvmParser.T__18)
            self.state = 210
            self.match(llvmParser.T__1)
            self.state = 211
            _la = self._input.LA(1)
            if not(_la==50 or _la==51):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def value(self):
            return self.getTypedRuleContext(llvmParser.ValueContext,0)


        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def getRuleIndex(self):
            return llvmParser.RULE_store

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStore" ):
                listener.enterStore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStore" ):
                listener.exitStore(self)




    def store(self):

        localctx = llvmParser.StoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_store)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(llvmParser.T__36)
            self.state = 214
            self.type_()
            self.state = 215
            self.value()
            self.state = 216
            self.match(llvmParser.T__18)
            self.state = 217
            self.match(llvmParser.T__1)
            self.state = 218
            _la = self._input.LA(1)
            if not(_la==50 or _la==51):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetelementptrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self, i:int=None):
            if i is None:
                return self.getTokens(llvmParser.Privatevariable)
            else:
                return self.getToken(llvmParser.Privatevariable, i)

        def Global_var(self):
            return self.getToken(llvmParser.Global_var, 0)

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.ValueContext)
            else:
                return self.getTypedRuleContext(llvmParser.ValueContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_getelementptr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetelementptr" ):
                listener.enterGetelementptr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetelementptr" ):
                listener.exitGetelementptr(self)




    def getelementptr(self):

        localctx = llvmParser.GetelementptrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_getelementptr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(llvmParser.Privatevariable)
            self.state = 221
            self.match(llvmParser.T__10)
            self.state = 222
            self.match(llvmParser.T__37)
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4]:
                self.state = 223
                self.type_()
                pass
            elif token in [50]:
                self.state = 224
                self.match(llvmParser.Privatevariable)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 227
            self.match(llvmParser.T__18)
            self.state = 228
            self.match(llvmParser.T__1)
            self.state = 229
            _la = self._input.LA(1)
            if not(_la==50 or _la==51):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 230
            self.match(llvmParser.T__18)
            self.state = 233 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 231
                self.match(llvmParser.T__0)
                self.state = 232
                self.value()
                self.state = 235 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def cond(self):
            return self.getTypedRuleContext(llvmParser.CondContext,0)


        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.ValueContext)
            else:
                return self.getTypedRuleContext(llvmParser.ValueContext,i)


        def getRuleIndex(self):
            return llvmParser.RULE_compare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)




    def compare(self):

        localctx = llvmParser.CompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_compare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(llvmParser.Privatevariable)
            self.state = 238
            self.match(llvmParser.T__10)
            self.state = 239
            self.match(llvmParser.T__38)
            self.state = 240
            self.cond()
            self.state = 241
            self.type_()
            self.state = 242
            self.value()
            self.state = 243
            self.match(llvmParser.T__18)
            self.state = 244
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return llvmParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = llvmParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 69269232549888) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PhiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def type_(self):
            return self.getTypedRuleContext(llvmParser.TypeContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(llvmParser.ValueContext)
            else:
                return self.getTypedRuleContext(llvmParser.ValueContext,i)


        def Label(self, i:int=None):
            if i is None:
                return self.getTokens(llvmParser.Label)
            else:
                return self.getToken(llvmParser.Label, i)

        def getRuleIndex(self):
            return llvmParser.RULE_phi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPhi" ):
                listener.enterPhi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPhi" ):
                listener.exitPhi(self)




    def phi(self):

        localctx = llvmParser.PhiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_phi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(llvmParser.Privatevariable)
            self.state = 249
            self.match(llvmParser.T__10)
            self.state = 250
            self.match(llvmParser.T__45)
            self.state = 251
            self.type_()
            self.state = 252
            self.match(llvmParser.T__13)
            self.state = 253
            self.value()
            self.state = 254
            self.match(llvmParser.T__18)
            self.state = 255
            self.match(llvmParser.T__34)
            self.state = 256
            self.match(llvmParser.Label)
            self.state = 257
            self.match(llvmParser.T__16)
            self.state = 258
            self.match(llvmParser.T__18)
            self.state = 259
            self.match(llvmParser.T__13)
            self.state = 260
            self.value()
            self.state = 261
            self.match(llvmParser.T__18)
            self.state = 262
            self.match(llvmParser.T__34)
            self.state = 263
            self.match(llvmParser.Label)
            self.state = 264
            self.match(llvmParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Privatevariable(self):
            return self.getToken(llvmParser.Privatevariable, 0)

        def constant(self):
            return self.getTypedRuleContext(llvmParser.ConstantContext,0)


        def getRuleIndex(self):
            return llvmParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = llvmParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_value)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(llvmParser.Privatevariable)
                pass
            elif token in [47, 53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.constant()
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


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(llvmParser.INTEGER, 0)

        def getRuleIndex(self):
            return llvmParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = llvmParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            _la = self._input.LA(1)
            if not(_la==47 or _la==53):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





