#!/usr/bin/python3
import semantic
import llvm
import sys
import asm
import llvm_optim

code = sys.stdin.read()
code2 = semantic.main(code)
with open("semantic.txt", "w") as f:
    f.write(code2)
try:
    code3 = llvm.main(code2)
    with open("llvm.ll", "w") as f:
        f.write(code3)
    len_code = len(code3)
    while True:
        code3 = llvm_optim.main(code3)
        with open("llvm_optim.ll", "w") as f:
            f.write(code3)
        if len(code3) == len_code:
            break
        else:
            len_code = len(code3)
    code4 = asm.main(code3)
    with open("test.s", "w") as f:
        f.write(code4)
    with open("src/builtin.s", "r") as f:
        print(f.read())
    print(code4)
except:
    pass
