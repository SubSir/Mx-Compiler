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
        4,1,61,425,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,3,1,71,8,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,80,8,2,10,2,
        12,2,83,9,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,92,8,3,10,3,12,3,95,
        9,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,103,8,3,10,3,12,3,106,9,3,1,3,1,
        3,3,3,110,8,3,1,4,1,4,1,4,3,4,115,8,4,1,5,1,5,1,5,3,5,120,8,5,1,
        6,1,6,1,6,3,6,125,8,6,1,6,1,6,1,6,1,7,1,7,5,7,132,8,7,10,7,12,7,
        135,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        150,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        3,8,166,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,177,8,8,10,8,
        12,8,180,9,8,1,8,1,8,1,8,1,8,1,8,3,8,187,8,8,1,9,3,9,190,8,9,1,9,
        1,9,3,9,194,8,9,1,9,1,9,3,9,198,8,9,1,10,1,10,1,11,1,11,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,3,13,220,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,
        230,8,13,10,13,12,13,233,9,13,1,13,1,13,3,13,237,8,13,1,13,1,13,
        1,13,1,13,1,13,5,13,244,8,13,10,13,12,13,247,9,13,1,13,1,13,3,13,
        251,8,13,1,13,1,13,1,13,1,13,3,13,257,8,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,3,13,267,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,300,
        8,13,10,13,12,13,303,9,13,1,13,1,13,3,13,307,8,13,1,13,1,13,1,13,
        1,13,1,13,5,13,314,8,13,10,13,12,13,317,9,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,3,13,328,8,13,1,13,1,13,1,13,1,13,5,13,
        334,8,13,10,13,12,13,337,9,13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,
        5,16,346,8,16,10,16,12,16,349,9,16,1,17,1,17,1,18,1,18,1,19,1,19,
        1,19,5,19,358,8,19,10,19,12,19,361,9,19,1,20,1,20,1,20,1,20,1,20,
        1,20,3,20,369,8,20,1,21,1,21,1,22,1,22,1,22,4,22,376,8,22,11,22,
        12,22,377,1,23,1,23,1,23,1,23,1,23,1,23,3,23,386,8,23,1,24,1,24,
        1,24,1,24,1,24,1,24,3,24,394,8,24,1,25,1,25,1,25,1,25,5,25,400,8,
        25,10,25,12,25,403,9,25,3,25,405,8,25,1,25,1,25,1,26,1,26,1,26,3,
        26,412,8,26,5,26,414,8,26,10,26,12,26,417,9,26,1,26,1,26,1,27,1,
        27,3,27,423,8,27,1,27,0,1,26,28,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,0,7,1,0,41,43,1,0,39,
        40,1,0,44,45,1,0,46,48,1,0,24,25,1,0,26,31,2,0,32,34,51,51,477,0,
        61,1,0,0,0,2,66,1,0,0,0,4,75,1,0,0,0,6,109,1,0,0,0,8,111,1,0,0,0,
        10,119,1,0,0,0,12,121,1,0,0,0,14,129,1,0,0,0,16,186,1,0,0,0,18,189,
        1,0,0,0,20,199,1,0,0,0,22,201,1,0,0,0,24,203,1,0,0,0,26,266,1,0,
        0,0,28,338,1,0,0,0,30,340,1,0,0,0,32,342,1,0,0,0,34,350,1,0,0,0,
        36,352,1,0,0,0,38,354,1,0,0,0,40,368,1,0,0,0,42,370,1,0,0,0,44,372,
        1,0,0,0,46,385,1,0,0,0,48,393,1,0,0,0,50,395,1,0,0,0,52,408,1,0,
        0,0,54,422,1,0,0,0,56,60,3,2,1,0,57,60,3,4,2,0,58,60,3,6,3,0,59,
        56,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,
        0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,0,0,1,65,1,1,
        0,0,0,66,67,3,46,23,0,67,68,5,51,0,0,68,70,5,49,0,0,69,71,3,38,19,
        0,70,69,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,5,50,0,0,73,74,
        3,14,7,0,74,3,1,0,0,0,75,76,5,1,0,0,76,77,5,51,0,0,77,81,5,2,0,0,
        78,80,3,10,5,0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,
        0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,3,0,0,85,86,5,4,0,0,86,
        5,1,0,0,0,87,88,3,42,21,0,88,93,3,8,4,0,89,90,5,5,0,0,90,92,3,8,
        4,0,91,89,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,
        1,0,0,0,95,93,1,0,0,0,96,97,5,4,0,0,97,110,1,0,0,0,98,99,3,44,22,
        0,99,104,3,8,4,0,100,101,5,5,0,0,101,103,3,8,4,0,102,100,1,0,0,0,
        103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,
        106,104,1,0,0,0,107,108,5,4,0,0,108,110,1,0,0,0,109,87,1,0,0,0,109,
        98,1,0,0,0,110,7,1,0,0,0,111,114,5,51,0,0,112,113,5,6,0,0,113,115,
        3,26,13,0,114,112,1,0,0,0,114,115,1,0,0,0,115,9,1,0,0,0,116,120,
        3,6,3,0,117,120,3,12,6,0,118,120,3,2,1,0,119,116,1,0,0,0,119,117,
        1,0,0,0,119,118,1,0,0,0,120,11,1,0,0,0,121,122,5,51,0,0,122,124,
        5,49,0,0,123,125,3,38,19,0,124,123,1,0,0,0,124,125,1,0,0,0,125,126,
        1,0,0,0,126,127,5,50,0,0,127,128,3,14,7,0,128,13,1,0,0,0,129,133,
        5,2,0,0,130,132,3,16,8,0,131,130,1,0,0,0,132,135,1,0,0,0,133,131,
        1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,133,1,0,0,0,136,137,
        5,3,0,0,137,15,1,0,0,0,138,187,5,4,0,0,139,140,3,26,13,0,140,141,
        5,4,0,0,141,187,1,0,0,0,142,143,5,7,0,0,143,144,5,49,0,0,144,145,
        3,26,13,0,145,146,5,50,0,0,146,149,3,16,8,0,147,148,5,8,0,0,148,
        150,3,16,8,0,149,147,1,0,0,0,149,150,1,0,0,0,150,187,1,0,0,0,151,
        152,5,9,0,0,152,153,5,49,0,0,153,154,3,26,13,0,154,155,5,50,0,0,
        155,156,3,16,8,0,156,187,1,0,0,0,157,158,5,10,0,0,158,159,5,49,0,
        0,159,160,3,18,9,0,160,161,5,50,0,0,161,162,3,16,8,0,162,187,1,0,
        0,0,163,165,5,11,0,0,164,166,3,26,13,0,165,164,1,0,0,0,165,166,1,
        0,0,0,166,167,1,0,0,0,167,187,5,4,0,0,168,187,3,6,3,0,169,170,3,
        26,13,0,170,171,5,6,0,0,171,172,3,26,13,0,172,173,5,4,0,0,173,187,
        1,0,0,0,174,178,5,2,0,0,175,177,3,16,8,0,176,175,1,0,0,0,177,180,
        1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,181,1,0,0,0,180,178,
        1,0,0,0,181,187,5,3,0,0,182,183,5,12,0,0,183,187,5,4,0,0,184,185,
        5,13,0,0,185,187,5,4,0,0,186,138,1,0,0,0,186,139,1,0,0,0,186,142,
        1,0,0,0,186,151,1,0,0,0,186,157,1,0,0,0,186,163,1,0,0,0,186,168,
        1,0,0,0,186,169,1,0,0,0,186,174,1,0,0,0,186,182,1,0,0,0,186,184,
        1,0,0,0,187,17,1,0,0,0,188,190,3,20,10,0,189,188,1,0,0,0,189,190,
        1,0,0,0,190,191,1,0,0,0,191,193,5,4,0,0,192,194,3,22,11,0,193,192,
        1,0,0,0,193,194,1,0,0,0,194,195,1,0,0,0,195,197,5,4,0,0,196,198,
        3,24,12,0,197,196,1,0,0,0,197,198,1,0,0,0,198,19,1,0,0,0,199,200,
        3,26,13,0,200,21,1,0,0,0,201,202,3,26,13,0,202,23,1,0,0,0,203,204,
        3,26,13,0,204,25,1,0,0,0,205,206,6,13,-1,0,206,207,5,16,0,0,207,
        267,3,26,13,20,208,209,5,17,0,0,209,267,3,26,13,19,210,211,5,18,
        0,0,211,267,3,26,13,18,212,213,5,19,0,0,213,267,3,26,13,17,214,215,
        5,40,0,0,215,267,3,26,13,16,216,217,5,51,0,0,217,219,5,49,0,0,218,
        220,3,32,16,0,219,218,1,0,0,0,219,220,1,0,0,0,220,221,1,0,0,0,221,
        267,5,50,0,0,222,267,3,48,24,0,223,224,5,21,0,0,224,231,3,42,21,
        0,225,226,3,28,14,0,226,227,3,26,13,0,227,228,3,30,15,0,228,230,
        1,0,0,0,229,225,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,
        1,0,0,0,232,234,1,0,0,0,233,231,1,0,0,0,234,236,3,28,14,0,235,237,
        3,26,13,0,236,235,1,0,0,0,236,237,1,0,0,0,237,238,1,0,0,0,238,239,
        3,30,15,0,239,245,1,0,0,0,240,241,3,28,14,0,241,242,3,30,15,0,242,
        244,1,0,0,0,243,240,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,
        246,1,0,0,0,246,250,1,0,0,0,247,245,1,0,0,0,248,249,5,49,0,0,249,
        251,5,50,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,267,1,0,0,0,252,
        253,5,21,0,0,253,256,3,42,21,0,254,255,5,49,0,0,255,257,5,50,0,0,
        256,254,1,0,0,0,256,257,1,0,0,0,257,267,1,0,0,0,258,267,5,51,0,0,
        259,260,5,49,0,0,260,261,3,26,13,0,261,262,5,50,0,0,262,267,1,0,
        0,0,263,264,5,51,0,0,264,265,5,6,0,0,265,267,3,26,13,1,266,205,1,
        0,0,0,266,208,1,0,0,0,266,210,1,0,0,0,266,212,1,0,0,0,266,214,1,
        0,0,0,266,216,1,0,0,0,266,222,1,0,0,0,266,223,1,0,0,0,266,252,1,
        0,0,0,266,258,1,0,0,0,266,259,1,0,0,0,266,263,1,0,0,0,267,335,1,
        0,0,0,268,269,10,23,0,0,269,270,5,14,0,0,270,271,3,26,13,0,271,272,
        5,15,0,0,272,273,3,26,13,24,273,334,1,0,0,0,274,275,10,8,0,0,275,
        276,7,0,0,0,276,334,3,26,13,9,277,278,10,7,0,0,278,279,7,1,0,0,279,
        334,3,26,13,8,280,281,10,6,0,0,281,282,7,2,0,0,282,334,3,26,13,7,
        283,284,10,5,0,0,284,285,7,3,0,0,285,334,3,26,13,6,286,287,10,3,
        0,0,287,288,3,36,18,0,288,289,3,26,13,4,289,334,1,0,0,0,290,291,
        10,2,0,0,291,292,3,34,17,0,292,293,3,26,13,3,293,334,1,0,0,0,294,
        301,10,24,0,0,295,296,3,28,14,0,296,297,3,26,13,0,297,298,3,30,15,
        0,298,300,1,0,0,0,299,295,1,0,0,0,300,303,1,0,0,0,301,299,1,0,0,
        0,301,302,1,0,0,0,302,304,1,0,0,0,303,301,1,0,0,0,304,306,3,28,14,
        0,305,307,3,26,13,0,306,305,1,0,0,0,306,307,1,0,0,0,307,308,1,0,
        0,0,308,309,3,30,15,0,309,315,1,0,0,0,310,311,3,28,14,0,311,312,
        3,30,15,0,312,314,1,0,0,0,313,310,1,0,0,0,314,317,1,0,0,0,315,313,
        1,0,0,0,315,316,1,0,0,0,316,334,1,0,0,0,317,315,1,0,0,0,318,319,
        10,22,0,0,319,334,5,16,0,0,320,321,10,21,0,0,321,334,5,17,0,0,322,
        323,10,14,0,0,323,324,5,20,0,0,324,325,5,51,0,0,325,327,5,49,0,0,
        326,328,3,32,16,0,327,326,1,0,0,0,327,328,1,0,0,0,328,329,1,0,0,
        0,329,334,5,50,0,0,330,331,10,13,0,0,331,332,5,20,0,0,332,334,5,
        51,0,0,333,268,1,0,0,0,333,274,1,0,0,0,333,277,1,0,0,0,333,280,1,
        0,0,0,333,283,1,0,0,0,333,286,1,0,0,0,333,290,1,0,0,0,333,294,1,
        0,0,0,333,318,1,0,0,0,333,320,1,0,0,0,333,322,1,0,0,0,333,330,1,
        0,0,0,334,337,1,0,0,0,335,333,1,0,0,0,335,336,1,0,0,0,336,27,1,0,
        0,0,337,335,1,0,0,0,338,339,5,22,0,0,339,29,1,0,0,0,340,341,5,23,
        0,0,341,31,1,0,0,0,342,347,3,26,13,0,343,344,5,5,0,0,344,346,3,26,
        13,0,345,343,1,0,0,0,346,349,1,0,0,0,347,345,1,0,0,0,347,348,1,0,
        0,0,348,33,1,0,0,0,349,347,1,0,0,0,350,351,7,4,0,0,351,35,1,0,0,
        0,352,353,7,5,0,0,353,37,1,0,0,0,354,359,3,40,20,0,355,356,5,5,0,
        0,356,358,3,40,20,0,357,355,1,0,0,0,358,361,1,0,0,0,359,357,1,0,
        0,0,359,360,1,0,0,0,360,39,1,0,0,0,361,359,1,0,0,0,362,363,3,42,
        21,0,363,364,5,51,0,0,364,369,1,0,0,0,365,366,3,44,22,0,366,367,
        5,51,0,0,367,369,1,0,0,0,368,362,1,0,0,0,368,365,1,0,0,0,369,41,
        1,0,0,0,370,371,7,6,0,0,371,43,1,0,0,0,372,375,3,42,21,0,373,374,
        5,22,0,0,374,376,5,23,0,0,375,373,1,0,0,0,376,377,1,0,0,0,377,375,
        1,0,0,0,377,378,1,0,0,0,378,45,1,0,0,0,379,386,5,32,0,0,380,386,
        5,33,0,0,381,386,5,34,0,0,382,386,5,35,0,0,383,386,5,51,0,0,384,
        386,3,44,22,0,385,379,1,0,0,0,385,380,1,0,0,0,385,381,1,0,0,0,385,
        382,1,0,0,0,385,383,1,0,0,0,385,384,1,0,0,0,386,47,1,0,0,0,387,394,
        5,52,0,0,388,394,3,54,27,0,389,394,5,36,0,0,390,394,5,37,0,0,391,
        394,5,38,0,0,392,394,3,50,25,0,393,387,1,0,0,0,393,388,1,0,0,0,393,
        389,1,0,0,0,393,390,1,0,0,0,393,391,1,0,0,0,393,392,1,0,0,0,394,
        49,1,0,0,0,395,404,5,2,0,0,396,401,3,26,13,0,397,398,5,5,0,0,398,
        400,3,26,13,0,399,397,1,0,0,0,400,403,1,0,0,0,401,399,1,0,0,0,401,
        402,1,0,0,0,402,405,1,0,0,0,403,401,1,0,0,0,404,396,1,0,0,0,404,
        405,1,0,0,0,405,406,1,0,0,0,406,407,5,3,0,0,407,51,1,0,0,0,408,415,
        5,55,0,0,409,411,3,26,13,0,410,412,5,60,0,0,411,410,1,0,0,0,411,
        412,1,0,0,0,412,414,1,0,0,0,413,409,1,0,0,0,414,417,1,0,0,0,415,
        413,1,0,0,0,415,416,1,0,0,0,416,418,1,0,0,0,417,415,1,0,0,0,418,
        419,5,57,0,0,419,53,1,0,0,0,420,423,5,56,0,0,421,423,3,52,26,0,422,
        420,1,0,0,0,422,421,1,0,0,0,423,55,1,0,0,0,42,59,61,70,81,93,104,
        109,114,119,124,133,149,165,178,186,189,193,197,219,231,236,245,
        250,256,266,301,306,315,327,333,335,347,359,368,377,385,393,401,
        404,411,415,422
    ]

class Mx_parserParser ( Parser ):

    grammarFileName = "Mx_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'{'", "'}'", "';'", "','", 
                     "'='", "'if'", "'else'", "'while'", "'for'", "'return'", 
                     "'break'", "'continue'", "'?'", "':'", "'++'", "'--'", 
                     "'!'", "'~'", "'.'", "'new'", "'['", "']'", "'&&'", 
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
    RULE_forControl = 9
    RULE_expression1 = 10
    RULE_expression2 = 11
    RULE_expression3 = 12
    RULE_expression = 13
    RULE_square_brackets1 = 14
    RULE_square_brackets2 = 15
    RULE_expressionLists = 16
    RULE_logicOperator = 17
    RULE_relationalOperator = 18
    RULE_parameterList = 19
    RULE_parameter = 20
    RULE_type = 21
    RULE_arrayType = 22
    RULE_returnType = 23
    RULE_constant = 24
    RULE_array_constant = 25
    RULE_fstring = 26
    RULE_string_constant = 27

    ruleNames =  [ "program", "functionDefinition", "classDefinition", "variableDeclaration", 
                   "variableDeclarationparts", "classMember", "construction", 
                   "functionBody", "statement", "forControl", "expression1", 
                   "expression2", "expression3", "expression", "square_brackets1", 
                   "square_brackets2", "expressionLists", "logicOperator", 
                   "relationalOperator", "parameterList", "parameter", "type", 
                   "arrayType", "returnType", "constant", "array_constant", 
                   "fstring", "string_constant" ]

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
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251864238194690) != 0):
                self.state = 59
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 56
                    self.functionDefinition()
                    pass

                elif la_ == 2:
                    self.state = 57
                    self.classDefinition()
                    pass

                elif la_ == 3:
                    self.state = 58
                    self.variableDeclaration()
                    pass


                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
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
            self.state = 66
            self.returnType()
            self.state = 67
            self.match(Mx_parserParser.IDENTIFIER)
            self.state = 68
            self.match(Mx_parserParser.LPAREN)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251829878456320) != 0):
                self.state = 69
                self.parameterList()


            self.state = 72
            self.match(Mx_parserParser.RPAREN)
            self.state = 73
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
            self.state = 75
            self.match(Mx_parserParser.T__0)
            self.state = 76
            self.match(Mx_parserParser.IDENTIFIER)
            self.state = 77
            self.match(Mx_parserParser.T__1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251864238194688) != 0):
                self.state = 78
                self.classMember()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(Mx_parserParser.T__2)
            self.state = 85
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
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.type_()
                self.state = 88
                self.variableDeclarationparts()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 89
                    self.match(Mx_parserParser.T__4)
                    self.state = 90
                    self.variableDeclarationparts()
                    self.state = 95
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 96
                self.match(Mx_parserParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.arrayType()
                self.state = 99
                self.variableDeclarationparts()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 100
                    self.match(Mx_parserParser.T__4)
                    self.state = 101
                    self.variableDeclarationparts()
                    self.state = 106
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 107
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
            self.state = 111
            self.match(Mx_parserParser.IDENTIFIER)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 112
                self.match(Mx_parserParser.T__5)
                self.state = 113
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
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.construction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
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
            self.state = 121
            self.match(Mx_parserParser.IDENTIFIER)
            self.state = 122
            self.match(Mx_parserParser.LPAREN)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251829878456320) != 0):
                self.state = 123
                self.parameterList()


            self.state = 126
            self.match(Mx_parserParser.RPAREN)
            self.state = 127
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
            self.state = 129
            self.match(Mx_parserParser.T__1)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406351067201172) != 0):
                self.state = 130
                self.statement()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
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
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Mx_parserParser.StatementContext)
            else:
                return self.getTypedRuleContext(Mx_parserParser.StatementContext,i)


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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = Mx_parserParser.EmptyStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(Mx_parserParser.T__3)
                pass

            elif la_ == 2:
                localctx = Mx_parserParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.expression(0)
                self.state = 140
                self.match(Mx_parserParser.T__3)
                pass

            elif la_ == 3:
                localctx = Mx_parserParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.match(Mx_parserParser.T__6)
                self.state = 143
                self.match(Mx_parserParser.LPAREN)
                self.state = 144
                self.expression(0)
                self.state = 145
                self.match(Mx_parserParser.RPAREN)
                self.state = 146
                self.statement()
                self.state = 149
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 147
                    self.match(Mx_parserParser.T__7)
                    self.state = 148
                    self.statement()


                pass

            elif la_ == 4:
                localctx = Mx_parserParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.match(Mx_parserParser.T__8)
                self.state = 152
                self.match(Mx_parserParser.LPAREN)
                self.state = 153
                self.expression(0)
                self.state = 154
                self.match(Mx_parserParser.RPAREN)
                self.state = 155
                self.statement()
                pass

            elif la_ == 5:
                localctx = Mx_parserParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 157
                self.match(Mx_parserParser.T__9)
                self.state = 158
                self.match(Mx_parserParser.LPAREN)
                self.state = 159
                self.forControl()
                self.state = 160
                self.match(Mx_parserParser.RPAREN)
                self.state = 161
                self.statement()
                pass

            elif la_ == 6:
                localctx = Mx_parserParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 163
                self.match(Mx_parserParser.T__10)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321002414084) != 0):
                    self.state = 164
                    self.expression(0)


                self.state = 167
                self.match(Mx_parserParser.T__3)
                pass

            elif la_ == 7:
                localctx = Mx_parserParser.PrivatevariableDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 168
                self.variableDeclaration()
                pass

            elif la_ == 8:
                localctx = Mx_parserParser.AssignmentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 169
                self.expression(0)
                self.state = 170
                self.match(Mx_parserParser.T__5)
                self.state = 171
                self.expression(0)
                self.state = 172
                self.match(Mx_parserParser.T__3)
                pass

            elif la_ == 9:
                localctx = Mx_parserParser.BlockContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 174
                self.match(Mx_parserParser.T__1)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406351067201172) != 0):
                    self.state = 175
                    self.statement()
                    self.state = 180
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 181
                self.match(Mx_parserParser.T__2)
                pass

            elif la_ == 10:
                localctx = Mx_parserParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 182
                self.match(Mx_parserParser.T__11)
                self.state = 183
                self.match(Mx_parserParser.T__3)
                pass

            elif la_ == 11:
                localctx = Mx_parserParser.ContinueStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 184
                self.match(Mx_parserParser.T__12)
                self.state = 185
                self.match(Mx_parserParser.T__3)
                pass


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
        self.enterRule(localctx, 18, self.RULE_forControl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321002414084) != 0):
                self.state = 188
                self.expression1()


            self.state = 191
            self.match(Mx_parserParser.T__3)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321002414084) != 0):
                self.state = 192
                self.expression2()


            self.state = 195
            self.match(Mx_parserParser.T__3)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321002414084) != 0):
                self.state = 196
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
        self.enterRule(localctx, 20, self.RULE_expression1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
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
        self.enterRule(localctx, 22, self.RULE_expression2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
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
        self.enterRule(localctx, 24, self.RULE_expression3)
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

        def LPAREN(self):
            return self.getToken(Mx_parserParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(Mx_parserParser.RPAREN, 0)

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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                localctx = Mx_parserParser.PrefixIncrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 206
                self.match(Mx_parserParser.T__15)
                self.state = 207
                self.expression(20)
                pass

            elif la_ == 2:
                localctx = Mx_parserParser.PrefixDecrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 208
                self.match(Mx_parserParser.T__16)
                self.state = 209
                self.expression(19)
                pass

            elif la_ == 3:
                localctx = Mx_parserParser.LogicalNotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 210
                self.match(Mx_parserParser.T__17)
                self.state = 211
                self.expression(18)
                pass

            elif la_ == 4:
                localctx = Mx_parserParser.BitwiseNotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 212
                self.match(Mx_parserParser.T__18)
                self.state = 213
                self.expression(17)
                pass

            elif la_ == 5:
                localctx = Mx_parserParser.UnaryMinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 214
                self.match(Mx_parserParser.MINUS)
                self.state = 215
                self.expression(16)
                pass

            elif la_ == 6:
                localctx = Mx_parserParser.FunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 216
                self.match(Mx_parserParser.IDENTIFIER)
                self.state = 217
                self.match(Mx_parserParser.LPAREN)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321002414084) != 0):
                    self.state = 218
                    self.expressionLists()


                self.state = 221
                self.match(Mx_parserParser.RPAREN)
                pass

            elif la_ == 7:
                localctx = Mx_parserParser.ConstantExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 222
                self.constant()
                pass

            elif la_ == 8:
                localctx = Mx_parserParser.NewArrayExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 223
                self.match(Mx_parserParser.T__20)
                self.state = 224
                self.type_()
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 225
                        self.square_brackets1()
                        self.state = 226
                        self.expression(0)
                        self.state = 227
                        self.square_brackets2() 
                    self.state = 233
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 234
                self.square_brackets1()
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321002414084) != 0):
                    self.state = 235
                    self.expression(0)


                self.state = 238
                self.square_brackets2()
                self.state = 245
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 240
                        self.square_brackets1()
                        self.state = 241
                        self.square_brackets2() 
                    self.state = 247
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                self.state = 250
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 248
                    self.match(Mx_parserParser.LPAREN)
                    self.state = 249
                    self.match(Mx_parserParser.RPAREN)


                pass

            elif la_ == 9:
                localctx = Mx_parserParser.NewVariableExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 252
                self.match(Mx_parserParser.T__20)
                self.state = 253
                self.type_()
                self.state = 256
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 254
                    self.match(Mx_parserParser.LPAREN)
                    self.state = 255
                    self.match(Mx_parserParser.RPAREN)


                pass

            elif la_ == 10:
                localctx = Mx_parserParser.VariableExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 258
                self.match(Mx_parserParser.IDENTIFIER)
                pass

            elif la_ == 11:
                localctx = Mx_parserParser.ParenthesesExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 259
                self.match(Mx_parserParser.LPAREN)
                self.state = 260
                self.expression(0)
                self.state = 261
                self.match(Mx_parserParser.RPAREN)
                pass

            elif la_ == 12:
                localctx = Mx_parserParser.ExpressionListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 263
                self.match(Mx_parserParser.IDENTIFIER)
                self.state = 264
                self.match(Mx_parserParser.T__5)
                self.state = 265
                self.expression(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 333
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = Mx_parserParser.ConditionalExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 268
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 269
                        self.match(Mx_parserParser.T__13)
                        self.state = 270
                        self.expression(0)
                        self.state = 271
                        self.match(Mx_parserParser.T__14)
                        self.state = 272
                        self.expression(24)
                        pass

                    elif la_ == 2:
                        localctx = Mx_parserParser.MuldivmodExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 274
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 275
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15393162788864) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 276
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = Mx_parserParser.PlusminusExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 277
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 278
                        _la = self._input.LA(1)
                        if not(_la==39 or _la==40):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 279
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = Mx_parserParser.ShiftExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 280
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 281
                        _la = self._input.LA(1)
                        if not(_la==44 or _la==45):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 282
                        self.expression(7)
                        pass

                    elif la_ == 5:
                        localctx = Mx_parserParser.AndxororExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 283
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 284
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 492581209243648) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 285
                        self.expression(6)
                        pass

                    elif la_ == 6:
                        localctx = Mx_parserParser.RelationalExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 286
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 287
                        self.relationalOperator()
                        self.state = 288
                        self.expression(4)
                        pass

                    elif la_ == 7:
                        localctx = Mx_parserParser.LogicExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 290
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 291
                        self.logicOperator()
                        self.state = 292
                        self.expression(3)
                        pass

                    elif la_ == 8:
                        localctx = Mx_parserParser.ArrayExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 294
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 301
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 295
                                self.square_brackets1()
                                self.state = 296
                                self.expression(0)
                                self.state = 297
                                self.square_brackets2() 
                            self.state = 303
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                        self.state = 304
                        self.square_brackets1()
                        self.state = 306
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321002414084) != 0):
                            self.state = 305
                            self.expression(0)


                        self.state = 308
                        self.square_brackets2()
                        self.state = 315
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 310
                                self.square_brackets1()
                                self.state = 311
                                self.square_brackets2() 
                            self.state = 317
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                        pass

                    elif la_ == 9:
                        localctx = Mx_parserParser.PostfixIncrementExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 318
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 319
                        self.match(Mx_parserParser.T__15)
                        pass

                    elif la_ == 10:
                        localctx = Mx_parserParser.PostfixDecrementExpressionContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 320
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 321
                        self.match(Mx_parserParser.T__16)
                        pass

                    elif la_ == 11:
                        localctx = Mx_parserParser.MemberFunctionCallContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 322
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 323
                        self.match(Mx_parserParser.T__19)
                        self.state = 324
                        self.match(Mx_parserParser.IDENTIFIER)

                        self.state = 325
                        self.match(Mx_parserParser.LPAREN)
                        self.state = 327
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321002414084) != 0):
                            self.state = 326
                            self.expressionLists()


                        self.state = 329
                        self.match(Mx_parserParser.RPAREN)
                        pass

                    elif la_ == 12:
                        localctx = Mx_parserParser.MemberMemberCallContext(self, Mx_parserParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 330
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 331
                        self.match(Mx_parserParser.T__19)
                        self.state = 332
                        self.match(Mx_parserParser.IDENTIFIER)
                        pass

             
                self.state = 337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_square_brackets1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
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
        self.enterRule(localctx, 30, self.RULE_square_brackets2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
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
        self.enterRule(localctx, 32, self.RULE_expressionLists)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.expression(0)
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 343
                self.match(Mx_parserParser.T__4)
                self.state = 344
                self.expression(0)
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
        self.enterRule(localctx, 34, self.RULE_logicOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
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
        self.enterRule(localctx, 36, self.RULE_relationalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
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
        self.enterRule(localctx, 38, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.parameter()
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 355
                self.match(Mx_parserParser.T__4)
                self.state = 356
                self.parameter()
                self.state = 361
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
        self.enterRule(localctx, 40, self.RULE_parameter)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.type_()
                self.state = 363
                self.match(Mx_parserParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.arrayType()
                self.state = 366
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
        self.enterRule(localctx, 42, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
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
        self.enterRule(localctx, 44, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.type_()
            self.state = 375 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 373
                self.match(Mx_parserParser.T__21)
                self.state = 374
                self.match(Mx_parserParser.T__22)
                self.state = 377 
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
        self.enterRule(localctx, 46, self.RULE_returnType)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(Mx_parserParser.T__31)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.match(Mx_parserParser.T__32)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 381
                self.match(Mx_parserParser.T__33)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 382
                self.match(Mx_parserParser.T__34)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 383
                self.match(Mx_parserParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 384
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
        self.enterRule(localctx, 48, self.RULE_constant)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(Mx_parserParser.INTEGER_CONSTANT)
                pass
            elif token in [55, 56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.string_constant()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 389
                self.match(Mx_parserParser.T__35)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 390
                self.match(Mx_parserParser.T__36)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 5)
                self.state = 391
                self.match(Mx_parserParser.T__37)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 6)
                self.state = 392
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
        self.enterRule(localctx, 50, self.RULE_array_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(Mx_parserParser.T__1)
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321002414084) != 0):
                self.state = 396
                self.expression(0)
                self.state = 401
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 397
                    self.match(Mx_parserParser.T__4)
                    self.state = 398
                    self.expression(0)
                    self.state = 403
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 406
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
        self.enterRule(localctx, 52, self.RULE_fstring)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(Mx_parserParser.FSTRING_PART1)
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 115406321002414084) != 0):
                self.state = 409
                self.expression(0)
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==60:
                    self.state = 410
                    self.match(Mx_parserParser.FSTRING_MIDDLE_PART)


                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 418
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
        self.enterRule(localctx, 54, self.RULE_string_constant)
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.match(Mx_parserParser.STRING_CONTENT)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
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
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 13)
         




