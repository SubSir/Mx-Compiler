# Generated from Mx_parser.g4 by ANTLR 4.13.2
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
        4,1,61,412,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,0,
        1,0,1,1,1,1,1,1,1,1,3,1,73,8,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,82,
        8,2,10,2,12,2,85,9,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,94,8,3,10,3,
        12,3,97,9,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,105,8,3,10,3,12,3,108,9,
        3,1,3,1,3,3,3,112,8,3,1,4,1,4,1,4,3,4,117,8,4,1,5,1,5,1,5,3,5,122,
        8,5,1,6,1,6,1,6,3,6,127,8,6,1,6,1,6,1,6,1,7,1,7,5,7,134,8,7,10,7,
        12,7,137,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        151,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        3,8,167,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,178,8,8,10,8,
        12,8,181,9,8,1,8,1,8,1,8,1,8,1,8,3,8,188,8,8,1,9,1,9,1,9,1,10,3,
        10,194,8,10,1,10,1,10,3,10,198,8,10,1,10,1,10,3,10,202,8,10,1,11,
        1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,3,14,224,8,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,5,14,234,8,14,10,14,12,14,237,9,14,1,14,1,14,
        3,14,241,8,14,1,14,1,14,1,14,1,14,1,14,5,14,248,8,14,10,14,12,14,
        251,9,14,1,14,3,14,254,8,14,1,14,1,14,1,14,1,14,3,14,260,8,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,270,8,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,4,14,303,8,14,11,14,12,14,304,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,3,14,316,8,14,1,14,1,14,1,14,1,14,5,14,322,
        8,14,10,14,12,14,325,9,14,1,15,1,15,1,16,1,16,1,17,1,17,1,17,5,17,
        334,8,17,10,17,12,17,337,9,17,1,18,1,18,1,19,1,19,1,20,1,20,1,20,
        5,20,346,8,20,10,20,12,20,349,9,20,1,21,1,21,1,21,1,21,1,21,1,21,
        3,21,357,8,21,1,22,1,22,1,23,1,23,1,23,4,23,364,8,23,11,23,12,23,
        365,1,24,1,24,1,24,1,24,1,24,1,24,3,24,374,8,24,1,25,1,25,1,25,1,
        25,1,25,1,25,3,25,382,8,25,1,26,1,26,1,26,1,26,5,26,388,8,26,10,
        26,12,26,391,9,26,3,26,393,8,26,1,26,1,26,1,27,1,27,1,27,1,27,5,
        27,401,8,27,10,27,12,27,404,9,27,1,27,1,27,1,28,1,28,3,28,410,8,
        28,1,28,0,1,28,29,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,56,0,7,1,0,41,43,1,0,39,40,1,0,
        44,45,1,0,46,48,1,0,24,25,1,0,26,31,2,0,32,34,51,51,460,0,63,1,0,
        0,0,2,68,1,0,0,0,4,77,1,0,0,0,6,111,1,0,0,0,8,113,1,0,0,0,10,121,
        1,0,0,0,12,123,1,0,0,0,14,131,1,0,0,0,16,187,1,0,0,0,18,189,1,0,
        0,0,20,193,1,0,0,0,22,203,1,0,0,0,24,205,1,0,0,0,26,207,1,0,0,0,
        28,269,1,0,0,0,30,326,1,0,0,0,32,328,1,0,0,0,34,330,1,0,0,0,36,338,
        1,0,0,0,38,340,1,0,0,0,40,342,1,0,0,0,42,356,1,0,0,0,44,358,1,0,
        0,0,46,360,1,0,0,0,48,373,1,0,0,0,50,381,1,0,0,0,52,383,1,0,0,0,
        54,396,1,0,0,0,56,409,1,0,0,0,58,62,3,2,1,0,59,62,3,4,2,0,60,62,
        3,6,3,0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,1,0,0,0,62,65,1,0,0,0,
        63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,
        0,0,1,67,1,1,0,0,0,68,69,3,48,24,0,69,70,5,51,0,0,70,72,5,49,0,0,
        71,73,3,40,20,0,72,71,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,75,
        5,50,0,0,75,76,3,14,7,0,76,3,1,0,0,0,77,78,5,1,0,0,78,79,5,51,0,
        0,79,83,5,2,0,0,80,82,3,10,5,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,
        1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,1,0,0,0,86,87,5,3,0,0,
        87,88,5,4,0,0,88,5,1,0,0,0,89,90,3,44,22,0,90,95,3,8,4,0,91,92,5,
        5,0,0,92,94,3,8,4,0,93,91,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,
        96,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,99,5,4,0,0,99,112,1,0,
        0,0,100,101,3,46,23,0,101,106,3,8,4,0,102,103,5,5,0,0,103,105,3,
        8,4,0,104,102,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,
        0,0,0,107,109,1,0,0,0,108,106,1,0,0,0,109,110,5,4,0,0,110,112,1,
        0,0,0,111,89,1,0,0,0,111,100,1,0,0,0,112,7,1,0,0,0,113,116,5,51,
        0,0,114,115,5,6,0,0,115,117,3,28,14,0,116,114,1,0,0,0,116,117,1,
        0,0,0,117,9,1,0,0,0,118,122,3,6,3,0,119,122,3,12,6,0,120,122,3,2,
        1,0,121,118,1,0,0,0,121,119,1,0,0,0,121,120,1,0,0,0,122,11,1,0,0,
        0,123,124,5,51,0,0,124,126,5,49,0,0,125,127,3,40,20,0,126,125,1,
        0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,129,5,50,0,0,129,130,3,
        14,7,0,130,13,1,0,0,0,131,135,5,2,0,0,132,134,3,16,8,0,133,132,1,
        0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,138,1,
        0,0,0,137,135,1,0,0,0,138,139,5,3,0,0,139,15,1,0,0,0,140,188,5,4,
        0,0,141,142,3,28,14,0,142,143,5,4,0,0,143,188,1,0,0,0,144,145,5,
        7,0,0,145,146,5,49,0,0,146,147,3,28,14,0,147,148,5,50,0,0,148,150,
        3,16,8,0,149,151,3,18,9,0,150,149,1,0,0,0,150,151,1,0,0,0,151,188,
        1,0,0,0,152,153,5,8,0,0,153,154,5,49,0,0,154,155,3,28,14,0,155,156,
        5,50,0,0,156,157,3,16,8,0,157,188,1,0,0,0,158,159,5,9,0,0,159,160,
        5,49,0,0,160,161,3,20,10,0,161,162,5,50,0,0,162,163,3,16,8,0,163,
        188,1,0,0,0,164,166,5,10,0,0,165,167,3,28,14,0,166,165,1,0,0,0,166,
        167,1,0,0,0,167,168,1,0,0,0,168,188,5,4,0,0,169,188,3,6,3,0,170,
        171,3,28,14,0,171,172,5,6,0,0,172,173,3,28,14,0,173,174,5,4,0,0,
        174,188,1,0,0,0,175,179,5,2,0,0,176,178,3,16,8,0,177,176,1,0,0,0,
        178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,182,1,0,0,0,
        181,179,1,0,0,0,182,188,5,3,0,0,183,184,5,11,0,0,184,188,5,4,0,0,
        185,186,5,12,0,0,186,188,5,4,0,0,187,140,1,0,0,0,187,141,1,0,0,0,
        187,144,1,0,0,0,187,152,1,0,0,0,187,158,1,0,0,0,187,164,1,0,0,0,
        187,169,1,0,0,0,187,170,1,0,0,0,187,175,1,0,0,0,187,183,1,0,0,0,
        187,185,1,0,0,0,188,17,1,0,0,0,189,190,5,13,0,0,190,191,3,16,8,0,
        191,19,1,0,0,0,192,194,3,22,11,0,193,192,1,0,0,0,193,194,1,0,0,0,
        194,195,1,0,0,0,195,197,5,4,0,0,196,198,3,24,12,0,197,196,1,0,0,
        0,197,198,1,0,0,0,198,199,1,0,0,0,199,201,5,4,0,0,200,202,3,26,13,
        0,201,200,1,0,0,0,201,202,1,0,0,0,202,21,1,0,0,0,203,204,3,28,14,
        0,204,23,1,0,0,0,205,206,3,28,14,0,206,25,1,0,0,0,207,208,3,28,14,
        0,208,27,1,0,0,0,209,210,6,14,-1,0,210,211,5,14,0,0,211,270,3,28,
        14,21,212,213,5,15,0,0,213,270,3,28,14,20,214,215,5,16,0,0,215,270,
        3,28,14,19,216,217,5,17,0,0,217,270,3,28,14,18,218,219,5,40,0,0,
        219,270,3,28,14,17,220,221,5,51,0,0,221,223,5,49,0,0,222,224,3,34,
        17,0,223,222,1,0,0,0,223,224,1,0,0,0,224,225,1,0,0,0,225,270,5,50,
        0,0,226,270,3,50,25,0,227,228,5,19,0,0,228,235,3,44,22,0,229,230,
        3,30,15,0,230,231,3,28,14,0,231,232,3,32,16,0,232,234,1,0,0,0,233,
        229,1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,
        238,1,0,0,0,237,235,1,0,0,0,238,240,3,30,15,0,239,241,3,28,14,0,
        240,239,1,0,0,0,240,241,1,0,0,0,241,242,1,0,0,0,242,243,3,32,16,
        0,243,249,1,0,0,0,244,245,3,30,15,0,245,246,3,32,16,0,246,248,1,
        0,0,0,247,244,1,0,0,0,248,251,1,0,0,0,249,247,1,0,0,0,249,250,1,
        0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,252,254,3,52,26,0,253,252,
        1,0,0,0,253,254,1,0,0,0,254,270,1,0,0,0,255,256,5,19,0,0,256,259,
        3,44,22,0,257,258,5,49,0,0,258,260,5,50,0,0,259,257,1,0,0,0,259,
        260,1,0,0,0,260,270,1,0,0,0,261,270,5,51,0,0,262,263,5,49,0,0,263,
        264,3,28,14,0,264,265,5,50,0,0,265,270,1,0,0,0,266,267,5,51,0,0,
        267,268,5,6,0,0,268,270,3,28,14,2,269,209,1,0,0,0,269,212,1,0,0,
        0,269,214,1,0,0,0,269,216,1,0,0,0,269,218,1,0,0,0,269,220,1,0,0,
        0,269,226,1,0,0,0,269,227,1,0,0,0,269,255,1,0,0,0,269,261,1,0,0,
        0,269,262,1,0,0,0,269,266,1,0,0,0,270,323,1,0,0,0,271,272,10,9,0,
        0,272,273,7,0,0,0,273,322,3,28,14,10,274,275,10,8,0,0,275,276,7,
        1,0,0,276,322,3,28,14,9,277,278,10,7,0,0,278,279,7,2,0,0,279,322,
        3,28,14,8,280,281,10,6,0,0,281,282,7,3,0,0,282,322,3,28,14,7,283,
        284,10,4,0,0,284,285,3,38,19,0,285,286,3,28,14,5,286,322,1,0,0,0,
        287,288,10,3,0,0,288,289,3,36,18,0,289,290,3,28,14,4,290,322,1,0,
        0,0,291,292,10,1,0,0,292,293,5,20,0,0,293,294,3,28,14,0,294,295,
        5,21,0,0,295,296,3,28,14,1,296,322,1,0,0,0,297,302,10,24,0,0,298,
        299,3,30,15,0,299,300,3,28,14,0,300,301,3,32,16,0,301,303,1,0,0,
        0,302,298,1,0,0,0,303,304,1,0,0,0,304,302,1,0,0,0,304,305,1,0,0,
        0,305,322,1,0,0,0,306,307,10,23,0,0,307,322,5,14,0,0,308,309,10,
        22,0,0,309,322,5,15,0,0,310,311,10,15,0,0,311,312,5,18,0,0,312,313,
        5,51,0,0,313,315,5,49,0,0,314,316,3,34,17,0,315,314,1,0,0,0,315,
        316,1,0,0,0,316,317,1,0,0,0,317,322,5,50,0,0,318,319,10,14,0,0,319,
        320,5,18,0,0,320,322,5,51,0,0,321,271,1,0,0,0,321,274,1,0,0,0,321,
        277,1,0,0,0,321,280,1,0,0,0,321,283,1,0,0,0,321,287,1,0,0,0,321,
        291,1,0,0,0,321,297,1,0,0,0,321,306,1,0,0,0,321,308,1,0,0,0,321,
        310,1,0,0,0,321,318,1,0,0,0,322,325,1,0,0,0,323,321,1,0,0,0,323,
        324,1,0,0,0,324,29,1,0,0,0,325,323,1,0,0,0,326,327,5,22,0,0,327,
        31,1,0,0,0,328,329,5,23,0,0,329,33,1,0,0,0,330,335,3,28,14,0,331,
        332,5,5,0,0,332,334,3,28,14,0,333,331,1,0,0,0,334,337,1,0,0,0,335,
        333,1,0,0,0,335,336,1,0,0,0,336,35,1,0,0,0,337,335,1,0,0,0,338,339,
        7,4,0,0,339,37,1,0,0,0,340,341,7,5,0,0,341,39,1,0,0,0,342,347,3,
        42,21,0,343,344,5,5,0,0,344,346,3,42,21,0,345,343,1,0,0,0,346,349,
        1,0,0,0,347,345,1,0,0,0,347,348,1,0,0,0,348,41,1,0,0,0,349,347,1,
        0,0,0,350,351,3,44,22,0,351,352,5,51,0,0,352,357,1,0,0,0,353,354,
        3,46,23,0,354,355,5,51,0,0,355,357,1,0,0,0,356,350,1,0,0,0,356,353,
        1,0,0,0,357,43,1,0,0,0,358,359,7,6,0,0,359,45,1,0,0,0,360,363,3,
        44,22,0,361,362,5,22,0,0,362,364,5,23,0,0,363,361,1,0,0,0,364,365,
        1,0,0,0,365,363,1,0,0,0,365,366,1,0,0,0,366,47,1,0,0,0,367,374,5,
        32,0,0,368,374,5,33,0,0,369,374,5,34,0,0,370,374,5,35,0,0,371,374,
        5,51,0,0,372,374,3,46,23,0,373,367,1,0,0,0,373,368,1,0,0,0,373,369,
        1,0,0,0,373,370,1,0,0,0,373,371,1,0,0,0,373,372,1,0,0,0,374,49,1,
        0,0,0,375,382,5,52,0,0,376,382,3,56,28,0,377,382,5,36,0,0,378,382,
        5,37,0,0,379,382,5,38,0,0,380,382,3,52,26,0,381,375,1,0,0,0,381,
        376,1,0,0,0,381,377,1,0,0,0,381,378,1,0,0,0,381,379,1,0,0,0,381,
        380,1,0,0,0,382,51,1,0,0,0,383,392,5,2,0,0,384,389,3,28,14,0,385,
        386,5,5,0,0,386,388,3,28,14,0,387,385,1,0,0,0,388,391,1,0,0,0,389,
        387,1,0,0,0,389,390,1,0,0,0,390,393,1,0,0,0,391,389,1,0,0,0,392,
        384,1,0,0,0,392,393,1,0,0,0,393,394,1,0,0,0,394,395,5,3,0,0,395,
        53,1,0,0,0,396,402,5,55,0,0,397,398,3,28,14,0,398,399,5,60,0,0,399,
        401,1,0,0,0,400,397,1,0,0,0,401,404,1,0,0,0,402,400,1,0,0,0,402,
        403,1,0,0,0,403,405,1,0,0,0,404,402,1,0,0,0,405,406,5,57,0,0,406,
        55,1,0,0,0,407,410,5,56,0,0,408,410,3,54,27,0,409,407,1,0,0,0,409,
        408,1,0,0,0,410,57,1,0,0,0,39,61,63,72,83,95,106,111,116,121,126,
        135,150,166,179,187,193,197,201,223,235,240,249,253,259,269,304,
        315,321,323,335,347,356,365,373,381,389,392,402,409
    ]

class Mx_parserParser ( Parser ):

    grammarFileName = "Mx_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'{'", "'}'", "';'", "','", 
                     "'='", "'if'", "'while'", "'for'", "'return'", "'break'", 
                     "'continue'", "'else'", "'++'", "'--'", "'!'", "'~'", 
                     "'.'", "'new'", "'?'", "':'", "'['", "']'", "'&&'", 
                     "'||'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", 
                     "'int'", "'bool'", "'string'", "'void'", "'true'", 
                     "'false'", "'null'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'<<'", "'>>'", "'&'", "'^'", "'|'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PLUS", "MINUS", 
                      "MUL", "DIV", "MOD", "LSHIFT", "RSHIFT", "AND", "XOR", 
                      "OR", "LPAREN", "RPAREN", "IDENTIFIER", "INTEGER_CONSTANT", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "FSTRING_PART1", 
                      "STRING_CONTENT", "FSTRING_PART2", "ESC", "ESC2", 
                      "FSTRING_MIDDLE_PART", "WS" ]

    RULE_program = 0
    RULE_functionDefinition = 1
    RULE_classDefinition = 2
    RULE_variableDeclaration = 3
    RULE_variableDeclarationparts = 4
    RULE_classMember = 5
    RULE_construction = 6
    RULE_functionBody = 7
    RULE_statement = 8
    RULE_elsestatement = 9
    RULE_forControl = 10
    RULE_expression1 = 11
    RULE_expression2 = 12
    RULE_expression3 = 13
    RULE_expression = 14
    RULE_square_brackets1 = 15
    RULE_square_brackets2 = 16
    RULE_expressionLists = 17
    RULE_logicOperator = 18
    RULE_relationalOperator = 19
    RULE_parameterList = 20
    RULE_parameter = 21
    RULE_type = 22
    RULE_arrayType = 23
    RULE_returnType = 24
    RULE_constant = 25
    RULE_array_constant = 26
    RULE_fstring = 27
    RULE_string_constant = 28

    ruleNames =  [ "program", "functionDefinition", "classDefinition", "variableDeclaration", 
                   "variableDeclarationparts", "classMember", "construction", 
                   "functionBody", "statement", "elsestatement", "forControl", 
                   "expression1", "expression2", "expression3", "expression", 
                   "square_brackets1", "square_brackets2", "expressionLists", 
                   "logicOperator", "relationalOperator", "parameterList", 
                   "parameter", "type", "arrayType", "returnType", "constant", 
                   "array_constant", "fstring", "string_constant" ]

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
    PLUS=39
    MINUS=40
    MUL=41
    DIV=42
    MOD=43
    LSHIFT=44
    RSHIFT=45
    AND=46
    XOR=47
    OR=48
    LPAREN=49
    RPAREN=50
    IDENTIFIER=51
    INTEGER_CONSTANT=52
    LINE_COMMENT=53
    BLOCK_COMMENT=54
    FSTRING_PART1=55
    STRING_CONTENT=56
    FSTRING_PART2=57
    ESC=58
    ESC2=59
    FSTRING_MIDDLE_PART=60
    WS=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Mx_parserParser.EOF, 0)

        def functionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.FunctionDefinitionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.FunctionDefinitionContext,i)


        def classDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ClassDefinitionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ClassDefinitionContext,i)


        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.VariableDeclarationContext,i)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = Mx_parserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251864238194690) != 0):
                self.state = 61
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 58
                    self.functionDefinition()
                    pass

                elif la_ == 2:
                    self.state = 59
                    self.classDefinition()
                    pass

                elif la_ == 3:
                    self.state = 60
                    self.variableDeclaration()
                    pass


                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(Mx_parserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnType(self):
            return self.getTypedRuleContext(Mx_parserParser.ReturnTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(Mx_parserParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(Mx_parserParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Mx_parserParser.RPAREN, 0)

        def functionBody(self):
            return self.getTypedRuleContext(Mx_parserParser.FunctionBodyContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(Mx_parserParser.ParameterListContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)




    def functionDefinition(self):

        localctx = Mx_parserParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.returnType()
            self.state = 69
            self.match(Mx_parserParser.IDENTIFIER)
            self.state = 70
            self.match(Mx_parserParser.LPAREN)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251829878456320) != 0):
                self.state = 71
                self.parameterList()


            self.state = 74
            self.match(Mx_parserParser.RPAREN)
            self.state = 75
            self.functionBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Mx_parserParser.IDENTIFIER, 0)

        def classMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ClassMemberContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ClassMemberContext,i)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_classDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDefinition" ):
                listener.enterClassDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDefinition" ):
                listener.exitClassDefinition(self)




    def classDefinition(self):

        localctx = Mx_parserParser.ClassDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(Mx_parserParser.T__0)
            self.state = 78
            self.match(Mx_parserParser.IDENTIFIER)
            self.state = 79
            self.match(Mx_parserParser.T__1)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251864238194688) != 0):
                self.state = 80
                self.classMember()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(Mx_parserParser.T__2)
            self.state = 87
            self.match(Mx_parserParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(Mx_parserParser.TypeContext,0)


        def variableDeclarationparts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.VariableDeclarationpartsContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.VariableDeclarationpartsContext,i)


        def arrayType(self):
            return self.getTypedRuleContext(Mx_parserParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = Mx_parserParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.type_()
                self.state = 90
                self.variableDeclarationparts()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 91
                    self.match(Mx_parserParser.T__4)
                    self.state = 92
                    self.variableDeclarationparts()
                    self.state = 97
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 98
                self.match(Mx_parserParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.arrayType()
                self.state = 101
                self.variableDeclarationparts()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 102
                    self.match(Mx_parserParser.T__4)
                    self.state = 103
                    self.variableDeclarationparts()
                    self.state = 108
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 109
                self.match(Mx_parserParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationpartsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Mx_parserParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_variableDeclarationparts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarationparts" ):
                listener.enterVariableDeclarationparts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarationparts" ):
                listener.exitVariableDeclarationparts(self)




    def variableDeclarationparts(self):

        localctx = Mx_parserParser.VariableDeclarationpartsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variableDeclarationparts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(Mx_parserParser.IDENTIFIER)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 114
                self.match(Mx_parserParser.T__5)
                self.state = 115
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(Mx_parserParser.VariableDeclarationContext,0)


        def construction(self):
            return self.getTypedRuleContext(Mx_parserParser.ConstructionContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(Mx_parserParser.FunctionDefinitionContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_classMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassMember" ):
                listener.enterClassMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassMember" ):
                listener.exitClassMember(self)




    def classMember(self):

        localctx = Mx_parserParser.ClassMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classMember)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.construction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.functionDefinition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Mx_parserParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(Mx_parserParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Mx_parserParser.RPAREN, 0)

        def functionBody(self):
            return self.getTypedRuleContext(Mx_parserParser.FunctionBodyContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(Mx_parserParser.ParameterListContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_construction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstruction" ):
                listener.enterConstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstruction" ):
                listener.exitConstruction(self)




    def construction(self):

        localctx = Mx_parserParser.ConstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_construction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(Mx_parserParser.IDENTIFIER)
            self.state = 124
            self.match(Mx_parserParser.LPAREN)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251829878456320) != 0):
                self.state = 125
                self.parameterList()


            self.state = 128
            self.match(Mx_parserParser.RPAREN)
            self.state = 129
            self.functionBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.StatementContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.StatementContext,i)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_functionBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBody" ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBody" ):
                listener.exitFunctionBody(self)




    def functionBody(self):

        localctx = Mx_parserParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(Mx_parserParser.T__1)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406351064883092) != 0):
                self.state = 132
                self.statement()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self.match(Mx_parserParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Mx_parserParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(Mx_parserParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(Mx_parserParser.RPAREN, 0)
        def statement(self):
            return self.getTypedRuleContext(Mx_parserParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)


    class EmptyStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)


    class AssignmentStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)


    class PrivatevariableDeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variableDeclaration(self):
            return self.getTypedRuleContext(Mx_parserParser.VariableDeclarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrivatevariableDeclaration" ):
                listener.enterPrivatevariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrivatevariableDeclaration" ):
                listener.exitPrivatevariableDeclaration(self)


    class ForStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(Mx_parserParser.LPAREN, 0)
        def forControl(self):
            return self.getTypedRuleContext(Mx_parserParser.ForControlContext,0)

        def RPAREN(self):
            return self.getToken(Mx_parserParser.RPAREN, 0)
        def statement(self):
            return self.getTypedRuleContext(Mx_parserParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)


    class BreakStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)


    class ExpressionStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)


    class BlockContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.StatementContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)


    class ContinueStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(Mx_parserParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(Mx_parserParser.RPAREN, 0)
        def statement(self):
            return self.getTypedRuleContext(Mx_parserParser.StatementContext,0)

        def elsestatement(self):
            return self.getTypedRuleContext(Mx_parserParser.ElsestatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)



    def statement(self):

        localctx = Mx_parserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = Mx_parserParser.EmptyStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(Mx_parserParser.T__3)
                pass

            elif la_ == 2:
                localctx = Mx_parserParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.expression(0)
                self.state = 142
                self.match(Mx_parserParser.T__3)
                pass

            elif la_ == 3:
                localctx = Mx_parserParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.match(Mx_parserParser.T__6)
                self.state = 145
                self.match(Mx_parserParser.LPAREN)
                self.state = 146
                self.expression(0)
                self.state = 147
                self.match(Mx_parserParser.RPAREN)
                self.state = 148
                self.statement()
                self.state = 150
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 149
                    self.elsestatement()


                pass

            elif la_ == 4:
                localctx = Mx_parserParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 152
                self.match(Mx_parserParser.T__7)
                self.state = 153
                self.match(Mx_parserParser.LPAREN)
                self.state = 154
                self.expression(0)
                self.state = 155
                self.match(Mx_parserParser.RPAREN)
                self.state = 156
                self.statement()
                pass

            elif la_ == 5:
                localctx = Mx_parserParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.match(Mx_parserParser.T__8)
                self.state = 159
                self.match(Mx_parserParser.LPAREN)
                self.state = 160
                self.forControl()
                self.state = 161
                self.match(Mx_parserParser.RPAREN)
                self.state = 162
                self.statement()
                pass

            elif la_ == 6:
                localctx = Mx_parserParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 164
                self.match(Mx_parserParser.T__9)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321000103940) != 0):
                    self.state = 165
                    self.expression(0)


                self.state = 168
                self.match(Mx_parserParser.T__3)
                pass

            elif la_ == 7:
                localctx = Mx_parserParser.PrivatevariableDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 169
                self.variableDeclaration()
                pass

            elif la_ == 8:
                localctx = Mx_parserParser.AssignmentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 170
                self.expression(0)
                self.state = 171
                self.match(Mx_parserParser.T__5)
                self.state = 172
                self.expression(0)
                self.state = 173
                self.match(Mx_parserParser.T__3)
                pass

            elif la_ == 9:
                localctx = Mx_parserParser.BlockContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 175
                self.match(Mx_parserParser.T__1)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406351064883092) != 0):
                    self.state = 176
                    self.statement()
                    self.state = 181
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 182
                self.match(Mx_parserParser.T__2)
                pass

            elif la_ == 10:
                localctx = Mx_parserParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 183
                self.match(Mx_parserParser.T__10)
                self.state = 184
                self.match(Mx_parserParser.T__3)
                pass

            elif la_ == 11:
                localctx = Mx_parserParser.ContinueStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 185
                self.match(Mx_parserParser.T__11)
                self.state = 186
                self.match(Mx_parserParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(Mx_parserParser.StatementContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_elsestatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElsestatement" ):
                listener.enterElsestatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElsestatement" ):
                listener.exitElsestatement(self)




    def elsestatement(self):

        localctx = Mx_parserParser.ElsestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_elsestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(Mx_parserParser.T__12)
            self.state = 190
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(Mx_parserParser.Expression1Context,0)


        def expression2(self):
            return self.getTypedRuleContext(Mx_parserParser.Expression2Context,0)


        def expression3(self):
            return self.getTypedRuleContext(Mx_parserParser.Expression3Context,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_forControl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForControl" ):
                listener.enterForControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForControl" ):
                listener.exitForControl(self)




    def forControl(self):

        localctx = Mx_parserParser.ForControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forControl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321000103940) != 0):
                self.state = 192
                self.expression1()


            self.state = 195
            self.match(Mx_parserParser.T__3)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321000103940) != 0):
                self.state = 196
                self.expression2()


            self.state = 199
            self.match(Mx_parserParser.T__3)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321000103940) != 0):
                self.state = 200
                self.expression3()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_expression1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression1" ):
                listener.enterExpression1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression1" ):
                listener.exitExpression1(self)




    def expression1(self):

        localctx = Mx_parserParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_expression2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression2" ):
                listener.enterExpression2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression2" ):
                listener.exitExpression2(self)




    def expression2(self):

        localctx = Mx_parserParser.Expression2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_expression3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression3" ):
                listener.enterExpression3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression3" ):
                listener.exitExpression3(self)




    def expression3(self):

        localctx = Mx_parserParser.Expression3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Mx_parserParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LogicalNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalNotExpression" ):
                listener.enterLogicalNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalNotExpression" ):
                listener.exitLogicalNotExpression(self)


    class PostfixIncrementExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixIncrementExpression" ):
                listener.enterPostfixIncrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixIncrementExpression" ):
                listener.exitPostfixIncrementExpression(self)


    class ConstantExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constant(self):
            return self.getTypedRuleContext(Mx_parserParser.ConstantContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantExpression" ):
                listener.enterConstantExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantExpression" ):
                listener.exitConstantExpression(self)


    class MuldivmodExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(Mx_parserParser.MUL, 0)
        def DIV(self):
            return self.getToken(Mx_parserParser.DIV, 0)
        def MOD(self):
            return self.getToken(Mx_parserParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMuldivmodExpression" ):
                listener.enterMuldivmodExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMuldivmodExpression" ):
                listener.exitMuldivmodExpression(self)


    class PlusminusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(Mx_parserParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(Mx_parserParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlusminusExpression" ):
                listener.enterPlusminusExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlusminusExpression" ):
                listener.exitPlusminusExpression(self)


    class ShiftExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,i)

        def LSHIFT(self):
            return self.getToken(Mx_parserParser.LSHIFT, 0)
        def RSHIFT(self):
            return self.getToken(Mx_parserParser.RSHIFT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShiftExpression" ):
                listener.enterShiftExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShiftExpression" ):
                listener.exitShiftExpression(self)


    class ArrayExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,i)

        def square_brackets1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.Square_brackets1Context)
            else:
                return self.getTypedRuleContext(Mx_parserParser.Square_brackets1Context,i)

        def square_brackets2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.Square_brackets2Context)
            else:
                return self.getTypedRuleContext(Mx_parserParser.Square_brackets2Context,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayExpression" ):
                listener.enterArrayExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayExpression" ):
                listener.exitArrayExpression(self)


    class RelationalExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,i)

        def relationalOperator(self):
            return self.getTypedRuleContext(Mx_parserParser.RelationalOperatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)


    class ConditionalExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalExpression" ):
                listener.enterConditionalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalExpression" ):
                listener.exitConditionalExpression(self)


    class PostfixDecrementExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixDecrementExpression" ):
                listener.enterPostfixDecrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixDecrementExpression" ):
                listener.exitPostfixDecrementExpression(self)


    class PrefixDecrementExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefixDecrementExpression" ):
                listener.enterPrefixDecrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefixDecrementExpression" ):
                listener.exitPrefixDecrementExpression(self)


    class VariableExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(Mx_parserParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableExpression" ):
                listener.enterVariableExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableExpression" ):
                listener.exitVariableExpression(self)


    class PrefixIncrementExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefixIncrementExpression" ):
                listener.enterPrefixIncrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefixIncrementExpression" ):
                listener.exitPrefixIncrementExpression(self)


    class NewVariableExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(Mx_parserParser.TypeContext,0)

        def LPAREN(self):
            return self.getToken(Mx_parserParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(Mx_parserParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewVariableExpression" ):
                listener.enterNewVariableExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewVariableExpression" ):
                listener.exitNewVariableExpression(self)


    class UnaryMinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(Mx_parserParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpression" ):
                listener.enterUnaryMinusExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpression" ):
                listener.exitUnaryMinusExpression(self)


    class ParenthesesExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(Mx_parserParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(Mx_parserParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesesExpression" ):
                listener.enterParenthesesExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesesExpression" ):
                listener.exitParenthesesExpression(self)


    class ExpressionListContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(Mx_parserParser.IDENTIFIER, 0)
        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)


    class MemberFunctionCallContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)

        def IDENTIFIER(self):
            return self.getToken(Mx_parserParser.IDENTIFIER, 0)
        def LPAREN(self):
            return self.getToken(Mx_parserParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(Mx_parserParser.RPAREN, 0)
        def expressionLists(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionListsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberFunctionCall" ):
                listener.enterMemberFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberFunctionCall" ):
                listener.exitMemberFunctionCall(self)


    class BitwiseNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwiseNotExpression" ):
                listener.enterBitwiseNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwiseNotExpression" ):
                listener.exitBitwiseNotExpression(self)


    class FunctionCallContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(Mx_parserParser.IDENTIFIER, 0)
        def LPAREN(self):
            return self.getToken(Mx_parserParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(Mx_parserParser.RPAREN, 0)
        def expressionLists(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionListsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)


    class AndxororExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(Mx_parserParser.AND, 0)
        def XOR(self):
            return self.getToken(Mx_parserParser.XOR, 0)
        def OR(self):
            return self.getToken(Mx_parserParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndxororExpression" ):
                listener.enterAndxororExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndxororExpression" ):
                listener.exitAndxororExpression(self)


    class LogicExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,i)

        def logicOperator(self):
            return self.getTypedRuleContext(Mx_parserParser.LogicOperatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicExpression" ):
                listener.enterLogicExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicExpression" ):
                listener.exitLogicExpression(self)


    class MemberMemberCallContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,0)

        def IDENTIFIER(self):
            return self.getToken(Mx_parserParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberMemberCall" ):
                listener.enterMemberMemberCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberMemberCall" ):
                listener.exitMemberMemberCall(self)


    class NewArrayExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Mx_parserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(Mx_parserParser.TypeContext,0)

        def square_brackets1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.Square_brackets1Context)
            else:
                return self.getTypedRuleContext(Mx_parserParser.Square_brackets1Context,i)

        def square_brackets2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.Square_brackets2Context)
            else:
                return self.getTypedRuleContext(Mx_parserParser.Square_brackets2Context,i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,i)

        def array_constant(self):
            return self.getTypedRuleContext(Mx_parserParser.Array_constantContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewArrayExpression" ):
                listener.enterNewArrayExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewArrayExpression" ):
                listener.exitNewArrayExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Mx_parserParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                localctx = Mx_parserParser.PrefixIncrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 210
                self.match(Mx_parserParser.T__13)
                self.state = 211
                self.expression(21)
                pass

            elif la_ == 2:
                localctx = Mx_parserParser.PrefixDecrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 212
                self.match(Mx_parserParser.T__14)
                self.state = 213
                self.expression(20)
                pass

            elif la_ == 3:
                localctx = Mx_parserParser.LogicalNotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 214
                self.match(Mx_parserParser.T__15)
                self.state = 215
                self.expression(19)
                pass

            elif la_ == 4:
                localctx = Mx_parserParser.BitwiseNotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 216
                self.match(Mx_parserParser.T__16)
                self.state = 217
                self.expression(18)
                pass

            elif la_ == 5:
                localctx = Mx_parserParser.UnaryMinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 218
                self.match(Mx_parserParser.MINUS)
                self.state = 219
                self.expression(17)
                pass

            elif la_ == 6:
                localctx = Mx_parserParser.FunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 220
                self.match(Mx_parserParser.IDENTIFIER)
                self.state = 221
                self.match(Mx_parserParser.LPAREN)
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321000103940) != 0):
                    self.state = 222
                    self.expressionLists()


                self.state = 225
                self.match(Mx_parserParser.RPAREN)
                pass

            elif la_ == 7:
                localctx = Mx_parserParser.ConstantExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 226
                self.constant()
                pass

            elif la_ == 8:
                localctx = Mx_parserParser.NewArrayExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 227
                self.match(Mx_parserParser.T__18)
                self.state = 228
                self.type_()
                self.state = 235
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 229
                        self.square_brackets1()
                        self.state = 230
                        self.expression(0)
                        self.state = 231
                        self.square_brackets2() 
                    self.state = 237
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 238
                self.square_brackets1()
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321000103940) != 0):
                    self.state = 239
                    self.expression(0)


                self.state = 242
                self.square_brackets2()
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 244
                        self.square_brackets1()
                        self.state = 245
                        self.square_brackets2() 
                    self.state = 251
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                self.state = 253
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 252
                    self.array_constant()


                pass

            elif la_ == 9:
                localctx = Mx_parserParser.NewVariableExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 255
                self.match(Mx_parserParser.T__18)
                self.state = 256
                self.type_()
                self.state = 259
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 257
                    self.match(Mx_parserParser.LPAREN)
                    self.state = 258
                    self.match(Mx_parserParser.RPAREN)


                pass

            elif la_ == 10:
                localctx = Mx_parserParser.VariableExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 261
                self.match(Mx_parserParser.IDENTIFIER)
                pass

            elif la_ == 11:
                localctx = Mx_parserParser.ParenthesesExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 262
                self.match(Mx_parserParser.LPAREN)
                self.state = 263
                self.expression(0)
                self.state = 264
                self.match(Mx_parserParser.RPAREN)
                pass

            elif la_ == 12:
                localctx = Mx_parserParser.ExpressionListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 266
                self.match(Mx_parserParser.IDENTIFIER)
                self.state = 267
                self.match(Mx_parserParser.T__5)
                self.state = 268
                self.expression(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 321
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = Mx_parserParser.MuldivmodExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 271
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 272
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15393162788864) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 273
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = Mx_parserParser.PlusminusExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 274
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 275
                        _la = self._input.LA(1)
                        if not(_la==39 or _la==40):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 276
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = Mx_parserParser.ShiftExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 277
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 278
                        _la = self._input.LA(1)
                        if not(_la==44 or _la==45):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 279
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = Mx_parserParser.AndxororExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 280
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 281
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 492581209243648) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 282
                        self.expression(7)
                        pass

                    elif la_ == 5:
                        localctx = Mx_parserParser.RelationalExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 283
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 284
                        self.relationalOperator()
                        self.state = 285
                        self.expression(5)
                        pass

                    elif la_ == 6:
                        localctx = Mx_parserParser.LogicExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 287
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 288
                        self.logicOperator()
                        self.state = 289
                        self.expression(4)
                        pass

                    elif la_ == 7:
                        localctx = Mx_parserParser.ConditionalExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 291
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 292
                        self.match(Mx_parserParser.T__19)
                        self.state = 293
                        self.expression(0)
                        self.state = 294
                        self.match(Mx_parserParser.T__20)
                        self.state = 295
                        self.expression(1)
                        pass

                    elif la_ == 8:
                        localctx = Mx_parserParser.ArrayExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 297
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 302 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 298
                                self.square_brackets1()
                                self.state = 299
                                self.expression(0)
                                self.state = 300
                                self.square_brackets2()

                            else:
                                raise NoViableAltException(self)
                            self.state = 304 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                        pass

                    elif la_ == 9:
                        localctx = Mx_parserParser.PostfixIncrementExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 306
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 307
                        self.match(Mx_parserParser.T__13)
                        pass

                    elif la_ == 10:
                        localctx = Mx_parserParser.PostfixDecrementExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 308
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 309
                        self.match(Mx_parserParser.T__14)
                        pass

                    elif la_ == 11:
                        localctx = Mx_parserParser.MemberFunctionCallContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 310
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 311
                        self.match(Mx_parserParser.T__17)
                        self.state = 312
                        self.match(Mx_parserParser.IDENTIFIER)

                        self.state = 313
                        self.match(Mx_parserParser.LPAREN)
                        self.state = 315
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321000103940) != 0):
                            self.state = 314
                            self.expressionLists()


                        self.state = 317
                        self.match(Mx_parserParser.RPAREN)
                        pass

                    elif la_ == 12:
                        localctx = Mx_parserParser.MemberMemberCallContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 318
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 319
                        self.match(Mx_parserParser.T__17)
                        self.state = 320
                        self.match(Mx_parserParser.IDENTIFIER)
                        pass

             
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Square_brackets1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Mx_parserParser.RULE_square_brackets1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSquare_brackets1" ):
                listener.enterSquare_brackets1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSquare_brackets1" ):
                listener.exitSquare_brackets1(self)




    def square_brackets1(self):

        localctx = Mx_parserParser.Square_brackets1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_square_brackets1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(Mx_parserParser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Square_brackets2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Mx_parserParser.RULE_square_brackets2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSquare_brackets2" ):
                listener.enterSquare_brackets2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSquare_brackets2" ):
                listener.exitSquare_brackets2(self)




    def square_brackets2(self):

        localctx = Mx_parserParser.Square_brackets2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_square_brackets2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(Mx_parserParser.T__22)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,i)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_expressionLists

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionLists" ):
                listener.enterExpressionLists(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionLists" ):
                listener.exitExpressionLists(self)




    def expressionLists(self):

        localctx = Mx_parserParser.ExpressionListsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expressionLists)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.expression(0)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 331
                self.match(Mx_parserParser.T__4)
                self.state = 332
                self.expression(0)
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Mx_parserParser.RULE_logicOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicOperator" ):
                listener.enterLogicOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicOperator" ):
                listener.exitLogicOperator(self)




    def logicOperator(self):

        localctx = Mx_parserParser.LogicOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_logicOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
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


    class RelationalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Mx_parserParser.RULE_relationalOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalOperator" ):
                listener.enterRelationalOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalOperator" ):
                listener.exitRelationalOperator(self)




    def relationalOperator(self):

        localctx = Mx_parserParser.RelationalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relationalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
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


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ParameterContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ParameterContext,i)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = Mx_parserParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.parameter()
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 343
                self.match(Mx_parserParser.T__4)
                self.state = 344
                self.parameter()
                self.state = 349
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
            return self.getTypedRuleContext(Mx_parserParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(Mx_parserParser.IDENTIFIER, 0)

        def arrayType(self):
            return self.getTypedRuleContext(Mx_parserParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = Mx_parserParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parameter)
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.type_()
                self.state = 351
                self.match(Mx_parserParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.arrayType()
                self.state = 354
                self.match(Mx_parserParser.IDENTIFIER)
                pass


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

        def IDENTIFIER(self):
            return self.getToken(Mx_parserParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return Mx_parserParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = Mx_parserParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2251829878456320) != 0)):
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


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(Mx_parserParser.TypeContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_arrayType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayType" ):
                listener.enterArrayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayType" ):
                listener.exitArrayType(self)




    def arrayType(self):

        localctx = Mx_parserParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.type_()
            self.state = 363 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 361
                self.match(Mx_parserParser.T__21)
                self.state = 362
                self.match(Mx_parserParser.T__22)
                self.state = 365 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Mx_parserParser.IDENTIFIER, 0)

        def arrayType(self):
            return self.getTypedRuleContext(Mx_parserParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_returnType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnType" ):
                listener.enterReturnType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnType" ):
                listener.exitReturnType(self)




    def returnType(self):

        localctx = Mx_parserParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_returnType)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.match(Mx_parserParser.T__31)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.match(Mx_parserParser.T__32)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 369
                self.match(Mx_parserParser.T__33)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 370
                self.match(Mx_parserParser.T__34)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 371
                self.match(Mx_parserParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 372
                self.arrayType()
                pass


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

        def INTEGER_CONSTANT(self):
            return self.getToken(Mx_parserParser.INTEGER_CONSTANT, 0)

        def string_constant(self):
            return self.getTypedRuleContext(Mx_parserParser.String_constantContext,0)


        def array_constant(self):
            return self.getTypedRuleContext(Mx_parserParser.Array_constantContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = Mx_parserParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_constant)
        try:
            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.match(Mx_parserParser.INTEGER_CONSTANT)
                pass
            elif token in [55, 56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.string_constant()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.match(Mx_parserParser.T__35)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 378
                self.match(Mx_parserParser.T__36)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 5)
                self.state = 379
                self.match(Mx_parserParser.T__37)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 6)
                self.state = 380
                self.array_constant()
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


    class Array_constantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,i)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_array_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_constant" ):
                listener.enterArray_constant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_constant" ):
                listener.exitArray_constant(self)




    def array_constant(self):

        localctx = Mx_parserParser.Array_constantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_array_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(Mx_parserParser.T__1)
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321000103940) != 0):
                self.state = 384
                self.expression(0)
                self.state = 389
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 385
                    self.match(Mx_parserParser.T__4)
                    self.state = 386
                    self.expression(0)
                    self.state = 391
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 394
            self.match(Mx_parserParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FstringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FSTRING_PART1(self):
            return self.getToken(Mx_parserParser.FSTRING_PART1, 0)

        def FSTRING_PART2(self):
            return self.getToken(Mx_parserParser.FSTRING_PART2, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.ExpressionContext,i)


        def FSTRING_MIDDLE_PART(self, i:int=None):
            if i is None:
                return self.getTokens(Mx_parserParser.FSTRING_MIDDLE_PART)
            else:
                return self.getToken(Mx_parserParser.FSTRING_MIDDLE_PART, i)

        def getRuleIndex(self):
            return Mx_parserParser.RULE_fstring

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFstring" ):
                listener.enterFstring(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFstring" ):
                listener.exitFstring(self)




    def fstring(self):

        localctx = Mx_parserParser.FstringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_fstring)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(Mx_parserParser.FSTRING_PART1)
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321000103940) != 0):
                self.state = 397
                self.expression(0)
                self.state = 398
                self.match(Mx_parserParser.FSTRING_MIDDLE_PART)
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 405
            self.match(Mx_parserParser.FSTRING_PART2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_constantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_CONTENT(self):
            return self.getToken(Mx_parserParser.STRING_CONTENT, 0)

        def fstring(self):
            return self.getTypedRuleContext(Mx_parserParser.FstringContext,0)


        def getRuleIndex(self):
            return Mx_parserParser.RULE_string_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_constant" ):
                listener.enterString_constant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_constant" ):
                listener.exitString_constant(self)




    def string_constant(self):

        localctx = Mx_parserParser.String_constantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_string_constant)
        try:
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(Mx_parserParser.STRING_CONTENT)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.fstring()
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 14)
         




