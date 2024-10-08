#!/usr/bin/python3
import sys
from antlr4 import InputStream, CommonTokenStream
from parser.Mx_parserLexer import Mx_parserLexer
from parser.Mx_parserListener import Mx_parserListener
from parser.Mx_parserParser import Mx_parserParser
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Tree import ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener


# 定义一个监听器类来遍历和处理语法树
class MyListener1_5(Mx_parserListener):
    enter_function = ""
    assign_var = ""
    ans = ""
    tmp_cnt = 0
    init = 0
    add_end = ""

    # def enterEveryRule(self, ctx):
    #     rule_name = Mx_parserParser.ruleNames[ctx.getRuleIndex()]
    #     rule_text = ctx.getText()
    #     print(f"Entering rule: {rule_name}, Text: {rule_text}")

    # def exitEveryRule(self, ctx):
    #     rule_name = Mx_parserParser.ruleNames[ctx.getRuleIndex()]
    #     rule_text = ctx.getText()
    #     print(f"Existing rule: {rule_name}, Text: {rule_text}")

    def visitTerminal(self, node: TerminalNodeImpl):
        # 获取终端节点的文本
        text = node.getText()
        self.ans += text + " "
        if text == ";":
            self.ans += "\n"

    def enterFunctionDefinition(self, ctx: Mx_parserParser.FunctionDefinitionContext):
        self.enter_function = ctx.IDENTIFIER().getText()

    def exitFunctionDefinition(self, ctx: Mx_parserParser.FunctionDefinitionContext):
        self.enter_function = ""

    def exitNewArrayExpression(self, ctx: Mx_parserParser.NewArrayExpressionContext):
        var = self.assign_var
        list = [i.expression() for i in ctx.newpart()]
        exp = [i.getText() for i in list if i is not None]
        end_square = "\n}" * (len(exp) - 1)
        type_ = ctx.type_().getText()
        if self.enter_function == "":
            self.add_end += "void i1n2i3t_" + var + "(){\n\t\t"
            while len(exp) > 1:
                tmp_var = "t" + str(self.tmp_cnt) + "p"
                self.tmp_cnt += 1
                self.add_end += (
                    "for(int "
                    + tmp_var
                    + "=0;"
                    + tmp_var
                    + " < "
                    + exp[0]
                    + ";++"
                    + tmp_var
                    + "){\n\t\t"
                    + var
                    + "["
                    + tmp_var
                    + "] = new "
                    + type_
                    + " ["
                    + exp[1]
                    + "]"
                    + "[]" * (len(exp) - 2)
                    + ";\n\t\t"
                )
                exp.pop(0)
                var = var + "[" + tmp_var + "]"
            self.add_end += end_square + "\n}\n"
            return

        self.ans += ";\n"
        while len(exp) > 1:
            tmp_var = "t" + str(self.tmp_cnt) + "p"
            self.tmp_cnt += 1
            self.ans += (
                "for(int "
                + tmp_var
                + "=0;"
                + tmp_var
                + " < "
                + exp[0]
                + ";++"
                + tmp_var
                + "){\n\t\t"
                + var
                + "["
                + tmp_var
                + "] = new "
                + type_
                + " ["
                + exp[1]
                + "]"
                + "[]" * (len(exp) - 2)
                + ";\n\t\t"
            )
            exp.pop(0)
            var = var + "[" + tmp_var + "]"
        self.ans += end_square + "\n\t\t"

    def enterAssignment(self, ctx: Mx_parserParser.AssignmentContext):
        self.assign_var = ctx.expression(0).getText()

    def enterVariableDeclarationparts(
        self, ctx: Mx_parserParser.VariableDeclarationpartsContext
    ):
        self.assign_var = ctx.IDENTIFIER().getText()


def main(code: str) -> str:
    # 创建输入流和语法分析器
    input_stream = InputStream(code)
    lexer = Mx_parserLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Mx_parserParser(token_stream)

    # 构建语法树
    tree = parser.program()

    # 创建监听器实例并遍历语法树
    listener = MyListener1_5()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.ans[:-6] + listener.add_end


# with open("in.txt", "r") as f:
#     code = f.read()

if __name__ == "__main__":
    code = sys.stdin.read()
    main(code)
