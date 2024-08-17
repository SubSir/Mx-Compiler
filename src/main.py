#!/usr/bin/python3
import semantic
import llvm
import sys

code = sys.stdin.read()
code2 = semantic.main(code)
with open("semantic.txt", "w") as f:
    f.write(code2)
llvm.main(code2)
