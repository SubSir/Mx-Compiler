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


class Mylistener2_5(llvmListener):
    imm_map = {}

    def __init__(self) -> None:
        self.imm_map = {}

    def enterBinary_op(self, ctx: llvmParser.Binary_opContext):
        value1 = ctx.value(0)
        value2 = ctx.value(1)
        op = ctx.bin_op().getText()
        var = ctx.Privatevariable().getText()
        if value1.constant() != None and value2.constant() != None:
            if op == "add":
                self.imm_map[var] = int(value1.constant().getText()) + int(
                    value2.constant().getText()
                )
            elif op == "sub":
                self.imm_map[var] = int(value1.constant().getText()) - int(
                    value2.constant().getText()
                )
            elif op == "mul":
                self.imm_map[var] = int(value1.constant().getText()) * int(
                    value2.constant().getText()
                )
            elif op == "sdiv":
                if value2.constant().getText() == "0":
                    return
                self.imm_map[var] = int(value1.constant().getText()) / int(
                    value2.constant().getText()
                )
            elif op == "srem":
                if value2.constant().getText() == "0":
                    return
                self.imm_map[var] = int(value1.constant().getText()) % int(
                    value2.constant().getText()
                )
            elif op == "shl":
                self.imm_map[var] = int(value1.constant().getText()) << int(
                    value2.constant().getText()
                )
            elif op == "ashr":
                self.imm_map[var] = int(value1.constant().getText()) >> int(
                    value2.constant().getText()
                )
            elif op == "and":
                self.imm_map[var] = int(value1.constant().getText()) & int(
                    value2.constant().getText()
                )
            elif op == "or":
                self.imm_map[var] = int(value1.constant().getText()) | int(
                    value2.constant().getText()
                )
            elif op == "xor":
                self.imm_map[var] = int(value1.constant().getText()) ^ int(
                    value2.constant().getText()
                )
            return
        if value1.getText() == "0":
            if op == "add" or op == "or":
                self.imm_map[var] = value2.getText()
            elif (
                op == "mul"
                or op == "sdiv"
                or op == "srem"
                or op == "shl"
                or op == "ashr"
                or op == "and"
            ):
                self.imm_map[var] = 0
        if value2.getText() == "0":
            if op == "add" or op == "or" or op == "sub" or op == "shl" or op == "ashr":
                self.imm_map[var] = value1.getText()
            elif op == "mul" or op == "and":
                self.imm_map[var] = 0


def main(code: str) -> str:
    while True:
        input_stream = InputStream(code)
        lexer = llvmLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = llvmParser(token_stream)

        tree = parser.module()
        walker = ParseTreeWalker()
        listener = Mylistener2_5()
        walker.walk(listener, tree)
        imm_map = listener.imm_map
        del_list = []
        for i in imm_map:
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

        def replace(key, imap, stream):
            if imap[key] in imap:
                replace(imap[key], imap, stream)
                imap[key] = imap[imap[key]]
            stream[0] = stream[0].replace(key + " ", str(imm_map[key]) + " ")
            stream[0] = stream[0].replace(key + ",", str(imm_map[key]) + ",")
            stream[0] = stream[0].replace(key + "\n", str(imm_map[key]) + "\n")
            stream[0] = stream[0].replace(key + ")", str(imm_map[key]) + ")")

        stream = [return_ans]
        for i in imm_map:
            replace(i, imm_map, stream)
        code = stream[0]
        if imm_map == {}:
            break

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
                if "call" in line:
                    line = "\t\t" + line.split("= ")[1]
                else:
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
