#!/usr/bin/python3
import semantic
import llvm
import sys
import asm

code = sys.stdin.read()
code2 = semantic.main(code)
# with open("semantic.txt", "w") as f:
#     f.write(code2)
try:
    code3 = llvm.main(code2)
    with open("llvm.ll", "w") as f:
        f.write(code3)
    code4 = asm.main(code3)
    with open("test.s", "w") as f:
        f.write(code4)
    with open("builtin.s", "r") as f:
        print(f.read())
    print(code4)
except:
    pass
