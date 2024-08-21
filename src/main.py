#!/usr/bin/python3
import semantic
import llvm
import sys

code = sys.stdin.read()
code2 = semantic.main(code)
with open("semantic.txt", "w") as f:
    f.write(code2)
code3 = llvm.main(code2)
with open("llvm.ll", "w") as f:
    f.write(code3)
print(code3)
