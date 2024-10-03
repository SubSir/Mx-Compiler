#!/usr/bin/python3
import sys
import copy
from antlr4 import InputStream, CommonTokenStream
from parser.Mx_parserLexer import Mx_parserLexer
from parser.Mx_parserListener import Mx_parserListener
from parser.Mx_parserParser import Mx_parserParser
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Tree import ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener


# 定义一个监听器类来遍历和处理语法树
class MyListener4(Mx_parserListener):
    pass


def main(code):

    return_str = ""
    with open("./src/head.ll", "r") as f:
        return_str += f.read()

    return_str += "\n\n"

    # 创建输入流和语法分析器
    input_stream = InputStream(code)
    lexer = Mx_parserLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Mx_parserParser(token_stream)

    # 构建语法树
    tree = parser.program()

    # 创建监听器实例并遍历语法树
    listener = MyListener4()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return_str += listener.global_str
    for i in listener.function_definition_list:
        return_str += i

    lines = return_str.splitlines()
    stream_out = 1
    return_ans = ""

    for line in lines:
        if line.startswith("\t\t"):
            if stream_out == 1:
                return_ans += line + "\n"
            if "br" in line:
                stream_out = 0
        else:
            if ".label" in line or ".entry" in line:
                stream_out = 1
            return_ans += line + "\n"
    return return_ans


if __name__ == "__main__":
    code = sys.stdin.read()
    code2 = main(code)
    with open("llvm.ll", "w") as f:
        f.write(code2)
    print(code2)
