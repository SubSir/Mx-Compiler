#!/usr/bin/python3
import sys
from antlr4 import InputStream, CommonTokenStream
import antlr4
from llvmparser.llvmListener import llvmListener
from llvmparser.llvmLexer import llvmLexer
from llvmparser.llvmParser import llvmParser
from antlr4.tree.Tree import ParseTreeWalker


class Mylistener3(llvmListener):

    variable_map = {}
    return_ans = ""

    def _traverse_nodes(self, node):
        if hasattr(node, "Privatevariable") and node.Privatevariable() is not None:
            var_name = node.Privatevariable().getText()
            if var_name not in self.variable_map:
                self.variable_map[var_name] = 1
            else:
                self.variable_map[var_name] += 1
        for child in node.getChildren():
            if isinstance(child, antlr4.ParserRuleContext):
                self._traverse_nodes(child)

    def enterModule(self, ctx: llvmParser.ModuleContext):
        self._traverse_nodes(ctx)


def main(code: str) -> str:
    input_stream = InputStream(code)
    lexer = llvmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = llvmParser(token_stream)

    tree = parser.module()
    walker = ParseTreeWalker()
    listener = Mylistener3()
    walker.walk(listener, tree)
    var_map = listener.variable_map
    del_list = []
    for i in var_map:
        if var_map[i] == 1:
            del_list.append("\t\t" + i + " = ")
    return_ans = ""
    lines = code.splitlines()
    for line in lines:
        flag = 1
        for delete in del_list:
            if line.startswith(delete):
                flag = 0
                break
        if flag == 1:
            return_ans += line + "\n"
    return return_ans


if __name__ == "__main__":
    code = sys.stdin.read()
    code2 = main(code)
    with open("llvm.s", "w") as f:
        f.write(code2)
    print(code2)
