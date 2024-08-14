import semantic
import llvm
import sys

code = sys.stdin.read()
code2 = semantic.main(code)
print(code2)
