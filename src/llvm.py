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
class MyListener2(Mx_parserListener):
    varaible_cnt = 0
    init_cnt = 0
    global_str = ""
    class_member_enum = {}  # A.x -> 0
    function_definition_list = []  # [str]
    variable_map = {}  # name -> (type, value)
    # def enterEveryRule(self, ctx):
    #     rule_name = Mx_parserParser.ruleNames[ctx.getRuleIndex()]
    #     rule_text = ctx.getText()
    #     print(f"Entering rule: {rule_name}, Text: {rule_text}")

    # def exitEveryRule(self, ctx):
    #     rule_name = Mx_parserParser.ruleNames[ctx.getRuleIndex()]
    #     rule_text = ctx.getText()
    #     print(f"Existing rule: {rule_name}, Text: {rule_text}")

    def __init__(self) -> None:
        pass

    # def visitTerminal(self, node: TerminalNodeImpl):
    #     # 当访问到终端节点时调用此方法
    #     print(node.getText(), end="")

    def return_expression2ir(self, code, stream) -> str:  # stream[0] 为流
        if isinstance(code, Mx_parserParser.ExpressionListContext):
            # expressionList
            pass
        elif isinstance(code, Mx_parserParser.LogicExpressionContext):
            # logicExpression
            pass
        elif isinstance(code, Mx_parserParser.ConditionalExpressionContext):
            # conditionalExpression
            pass
        elif isinstance(code, Mx_parserParser.RelationalExpressionContext):
            # relationalExpression
            pass
        elif isinstance(code, Mx_parserParser.MuldivmodExpressionContext):
            # muldivmodExpression
            t1 = self.return_expression2ir(code.expression(0), stream)
            t2 = self.return_expression2ir(code.expression(1), stream)
            result = "%" + str(self.varaible_cnt)
            self.varaible_cnt += 1
            if code.MUL() != None:
                op = "mul"
            elif code.DIV() != None:
                op = "sdiv"
            else:
                op = "srem"
            stream[0] += result + " = " + op + " i32 " + t1 + " " + t2
            return result
        elif isinstance(code, Mx_parserParser.PlusminusExpressionContext):
            # plusminusExpression
            t1 = self.return_expression2ir(code.expression(0))
            t2 = self.return_expression2ir(code.expression(1))
            result = "%" + str(self.varaible_cnt)
            self.varaible_cnt += 1
            if code.PLUS() != None:
                op = "add"
            elif code.MINUS() != None:
                op = "sub"
            stream[0] += result + " = " + op + " i32 " + t1 + " " + t2
            return result
        elif isinstance(code, Mx_parserParser.ShiftExpressionContext):
            # shiftExpression
            t1 = self.return_expression2ir(code.expression(0))
            t2 = self.return_expression2ir(code.expression(1))
            result = "%" + str(self.varaible_cnt)
            self.varaible_cnt += 1
            if code.LSHIFT() != None:
                op = "shl"
            elif code.RSHIFT() != None:
                op = "ashr"
            print(result + " = " + op + " i32 " + t1 + " " + t2)
            return result
        elif isinstance(code, Mx_parserParser.AndxororExpressionContext):
            # andxororExpression
            t1 = self.return_expression2ir(code.expression(0))
            t2 = self.return_expression2ir(code.expression(1))
            result = "%" + str(self.varaible_cnt)
            self.varaible_cnt += 1
            if code.AND() != None:
                op = "and"
            elif code.XOR() != None:
                op = "xor"
            else:
                op = "or"
            stream += result + " = " + op + " i32 " + t1 + " " + t2
            return result
        elif isinstance(code, Mx_parserParser.PrefixIncrementExpressionContext):
            # prefixIncrementExpression
            result = "%" + str(self.varaible_cnt)
            self.varaible_cnt += 1
            t = self.return_expression2ir(code.expression())
            stream += result + " = add i32 " + t + " 1"
            return result
        elif isinstance(code, Mx_parserParser.PostfixIncrementExpressionContext):
            # postfixIncrementExpression
            t = self.return_expression2ir(code.expression())
            print(t + "+1" + " = add i32 " + t + " 1")
            return t + "+1"
        elif isinstance(code, Mx_parserParser.PrefixDecrementExpressionContext):
            # prefixDecrementExpression
            t = self.return_expression2ir(code.expression())
            print(t + " = sub i32 " + t + " 1")
            return t
        elif isinstance(code, Mx_parserParser.PostfixDecrementExpressionContext):
            # postfixDecrementExpression
            t = self.return_expression2ir(code.expression())
            print(t + "-1" + " = sub i32 " + t + " 1")
            return t + "-1"
        elif isinstance(code, Mx_parserParser.LogicalNotExpressionContext):
            # logicalNotExpression
            t = self.return_expression2ir(code.expression())
            print(t + "!" + " = xor i1 " + t + " 1")
            return t + "!"
        elif isinstance(code, Mx_parserParser.BitwiseNotExpressionContext):
            # bitwiseNotExpression
            t = self.return_expression2ir(code.expression())
            print(t + "~" + " = xor i32 " + t + " 1")
            return t + "~"
        elif isinstance(code, Mx_parserParser.UnaryMinusExpressionContext):
            # unaryMinusExpression
            t = self.return_expression2ir(code.expression())
            print(t + "-" + " = sub i32 0 " + t)
            return t + "-"
        elif isinstance(code, Mx_parserParser.FunctionCallContext):
            # functionCall
            pass
        elif isinstance(code, Mx_parserParser.MemberFunctionCallContext):
            # memberFunctionCall
            pass
        elif isinstance(code, Mx_parserParser.MemberMemberCallContext):
            # memberMemberCall
            pass
        elif isinstance(code, Mx_parserParser.ConstantExpressionContext):
            # constantExpression
            constant = code.constant()
            if constant.INTEGER_CONSTANT() != None:
                # if print:
                #     print(constant.getText(), end=" ")
                return constant.INTEGER_CONSTANT().getText()
            if constant.string_constant() != None:
                string_ = constant.string_constant().getText()
                string_ = string_.replace('\\"', "\\22")
                string_ = string_.replace("\\n", "\\0A")
                result = "%" + str(len(string_))  # 可能有问题
                if constant.string_constant().STRING_CONTENT() != None:
                    print(
                        result
                        + " = private constant ["
                        + str(len(string_) - 1)
                        + " x i8] c"
                        + string_[:-1]
                        + '\\00"'
                    )
                else:
                    fstring = constant.string_constant().fstring()
                    expressionlist = fstring.expression()
                    middle = fstring.FSTRING_MIDDLE_PART()
                    part1 = fstring.FSTRING_PART1().getText()[1:-1] + '\\00"'
                    part2 = fstring.FSTRING_PART2().getText()[1:-1] + '\\00"'
                    print(
                        "%"
                        + str(len(string_))
                        + "_PART1 = private constant ["
                        + str(len(part1))
                        + " x i8] c"
                        + part1
                    )
                    print(
                        "%"
                        + str(len(string_))
                        + "_PART2 = private constant ["
                        + str(len(part2))
                        + " x i8] c"
                        + part2
                    )
                    for i in range(len(expressionlist)):
                        expression = expressionlist[i]
                        if isinstance(
                            expression, Mx_parserParser.ConstantExpressionContext
                        ):
                            if expression.INTEGER_CONSTANT() != None:
                                print(
                                    result
                                    + "_"
                                    + str(i)
                                    + " = private constant ["
                                    + str(len(string_))
                                )

                    # 先放着，写好了字符串拼接和转换为字符串再来
                    # for i in range(len(expressionlist)):
                return result
            # if constant.array_constant() != None:
            #     expressionlist = constant.array_constant().expression()
            #     if len(expressionlist) == 0:
            #         return "null"
            #     type1 = self.return_expressiontype(expressionlist[0])
            #     for i in range(1, len(expressionlist)):
            #         type2 = self.return_expressiontype(expressionlist[i])

            #     return type1.split("[")[0] + "[" + str(int(type1[-2]) + 1) + "]"

            # 这个难说，看在哪里初始化
            if constant.getText() == "null":
                return "null"  # 这个应该没有
            if constant.getText() == "True":
                return 1
            return 0
        elif isinstance(code, Mx_parserParser.NewVariableExpressionContext):
            # newVariableExpression
            result = "%new" + code.type().getText()
            print(
                result
                + " = call "
                + self.type2ir(code.type().getText())
                + " @"
                + code.type().getText()
                + "_new()"  # 你需要手写int string, 这里认为默认构造没有参数的
            )
            return result
        elif isinstance(code, Mx_parserParser.NewArrayExpressionContext):
            # newArrayExpression
            pass
        elif isinstance(code, Mx_parserParser.VariableExpressionContext):
            # variableExpression
            identifier = code.IDENTIFIER().getText()
            name = identifier + str(len(self.variable_definition_map[identifier]))
            return name
        elif isinstance(code, Mx_parserParser.ArrayExpressionContext):
            # arrayExpression
            pass
        elif isinstance(code, Mx_parserParser.ParenthesesExpressionContext):
            # parenthesesExpression
            return self.return_expressiontype(code.expression())
        else:
            name = code.getText()
            # 如果没有匹配的规则，返回未知类型
            return "unknown"

    def type2ir(self, str) -> str:
        if str == "int":
            return "i32"
        elif str == "bool":
            return "i1"
        return "ptr"

    def enterProgram(self, ctx: Mx_parserParser.ProgramContext):
        class_definition_str = ""
        variable_definition_str = ""
        function_definition_str = ""
        for child in ctx.getChildren():
            if isinstance(child, Mx_parserParser.ClassDefinitionContext):
                class_definition_str += "%" + child.IDENTIFIER().getText() + " = type {"
                classmember = child.classMember()
                cnt = 0
                function_definition_str += (
                    "declare void @" + child.IDENTIFIER().getText() + "_new()\n"
                )
                for i in range(len(classmember)):
                    ii = classmember[i]
                    if ii.variableDeclaration() != None:
                        type = ii.variableDeclaration().type().getText()
                        name = ii.variableDeclaration().IDENTIFIER().getText()
                        class_definition_str += self.type2ir(type)
                        if i < len(classmember) - 1:
                            class_definition_str += ", "
                        self.class_member_enum[child.IDENTIFIER().getText() + name] = (
                            cnt
                        )
                        cnt += 1
                    elif ii.functionDefinition() != None:
                        type = ii.functionDefinition().returnType().getText()
                        name = ii.functionDefinition().IDENTIFIER().getText()
                        function_definition_str += (
                            "declare "
                            + self.type2ir(type)
                            + " @"
                            + child.IDENTIFIER().getText()
                            + name
                            + "( ptr"
                        )
                        parameterlist = self.parameterList_decode2name(
                            ii.functionDefinition().parameterList()
                        )
                        for i in parameterlist:
                            function_definition_str += ", " + self.type2ir(i[0])
                        function_definition_str += ")\n"

            elif isinstance(child, Mx_parserParser.FunctionDefinitionContext):
                type = child.returnType().getText()
                name = child.IDENTIFIER().getText()
                function_definition_str += (
                    "declare "
                    + self.type2ir(type)
                    + " @"
                    + child.IDENTIFIER().getText()
                    + name
                )
                parameterlist += self.parameterList_decode2type(child.parameterList())
                function_definition_str += "\n"
            elif isinstance(child, Mx_parserParser.VariableDeclarationContext):
                if child.type_() != None:
                    type = self.type2ir(child.type().getText())
                else:
                    type = "ptr"
                default = "0"
                if type == "ptr":
                    default = "null"
                for i in child.variableDeclarationparts():
                    name = i.IDENTIFIER().getText()
                    variable_definition_str += "@" + name + " = global " + type + " "
                    if i.expression() == None:
                        variable_definition_str += default
                    else:
                        init = 1
                        if isinstance(i.expression(), Mx_parserParser.constant()):
                            constant = Mx_parserParser.constant()
                            if constant.INTEGER_CONSTANT() != None:
                                init = 0
                                variable_definition_str += (
                                    constant.INTEGER_CONSTANT().getText()
                                )
                            elif constant.getText() == "true":
                                init = 0
                                variable_definition_str += "1"
                            elif constant.getText() == "false":
                                init = 0
                                variable_definition_str += "0"
                        if init:
                            variable_definition_str += default
                            init_func = (
                                "define void @init"
                                + str(self.init_cnt)
                                + " (){\n  entry:\n"
                            )

    def parameterList_decode2type(
        self, code: Mx_parserParser.ParameterListContext
    ) -> str:  # (i1, i32)
        parameterlist = code.parameter()
        if parameterlist == None:
            return "()"
        ans = "("
        for i in range(len(parameterlist)):
            parameter = parameterlist[i]
            if parameter.type() != None:
                ans += self.type2ir(parameter.type().getText())
            else:
                ans += "ptr"
            if i < len(parameterlist) - 1:
                ans += ", "
        ans += ")"
        return ans

    def parameterList_decode2name(
        self, code: Mx_parserParser.ParameterListContext
    ) -> list:  # [(type, name)]
        parameterlist = code.parameter()
        if parameterlist == None:
            return []
        ans = []
        for i in range(len(parameterlist)):
            parameter = parameterlist[i]
            if parameter.type() != None:
                ans.append(
                    (
                        self.type2ir(parameter.type().getText()),
                        parameter.IDENTIFIER().getText(),
                    )
                )
            else:
                ans.append(("ptr", parameter.IDENTIFIER().getText()))
        return ans

    def enterFunctionDefinition(self, ctx: Mx_parserParser.FunctionDefinitionContext):
        pass

    def exitFunctionDefinition(self, ctx: Mx_parserParser.FunctionDefinitionContext):
        pass

    def exitClassDefinition(self, ctx: Mx_parserParser.ClassDefinitionContext):
        pass

    def enterClassDefinition(self, ctx: Mx_parserParser.ClassDefinitionContext):
        pass

    def enterVariableDeclaration(self, ctx: Mx_parserParser.VariableDeclarationContext):
        pass

    def enterElsestatement(self, ctx: Mx_parserParser.ElsestatementContext):
        pass

    def exitElsestatement(self, ctx: Mx_parserParser.ElsestatementContext):
        pass

    # def enterClassDefinition(self, ctx):
    #     class_ = self.class_decode(ctx)
    #     self.usertype_map[class_.name] = class_
    #     if class_.name[:-3] in self.function_definition_map:
    #         print("Multiple Definitions")
    #         sys.exit(1)

    def enterType(self, ctx: Mx_parserParser.TypeContext):
        pass

    def enterExpressionStatement(self, ctx: Mx_parserParser.ExpressionStatementContext):
        pass

    def enterIfStatement(self, ctx: Mx_parserParser.IfStatementContext):
        pass

    def exitIfStatement(self, ctx: Mx_parserParser.IfStatementContext):
        pass

    def enterWhileStatement(self, ctx: Mx_parserParser.WhileStatementContext):
        pass

    def exitWhileStatement(self, ctx: Mx_parserParser.WhileStatementContext):
        pass

    def enterForControl(self, ctx: Mx_parserParser.ForControlContext):
        pass

    def enterForStatement(self, ctx: Mx_parserParser.ForStatementContext):
        pass

    def exitForStatement(self, ctx: Mx_parserParser.ForStatementContext):
        pass

    def enterReturnStatement(self, ctx: Mx_parserParser.ReturnStatementContext):
        pass

    def enterAssignmentStatement(self, ctx: Mx_parserParser.AssignmentStatementContext):
        pass


# with open("in.txt", "r") as f:
#     code = f.read()
def main(code):

    with open("./src/head.ll", "r") as f:
        print(f.read())

    # 创建输入流和语法分析器
    input_stream = InputStream(code)
    lexer = Mx_parserLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Mx_parserParser(token_stream)

    # 构建语法树
    tree = parser.program()

    # 创建监听器实例并遍历语法树
    listener = MyListener2()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == "__main__":
    code = sys.stdin.read()
    main(code)
