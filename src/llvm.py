#!/usr/bin/python3
import sys
from antlr4 import InputStream, CommonTokenStream
from parser.Mx_parserLexer import Mx_parserLexer
from parser.Mx_parserListener import Mx_parserListener
from parser.Mx_parserParser import Mx_parserParser
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Tree import ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener


class arrayclass:
    type = ""
    dimansion = 0

    def __init__(self, type, dimansion):
        self.type = type
        self.dimansion = dimansion

    def to_string(self) -> str:
        return self.type + "[" + str(int(self.dimansion)) + "]"


class functionclass:
    returnType = ""
    name = ""
    parameterList = []
    priority = -1
    returned = 0
    # body = []     语法检查尚不考虑

    def __init__(self, returnType, name, parameterList, priority):
        self.returnType = returnType
        self.name = name
        self.parameterList = parameterList
        self.priority = priority


class parameterclass:
    type = ""
    name = ""
    value = ""
    priority = -1
    size = []

    def __init__(self, type, name, value, priority, size=None):
        self.type = type
        self.name = name
        self.value = value
        self.priority = priority
        if size == None:
            self.size = []
        else:
            self.size = size


class classclass:
    name = ""
    class_member_map = {}  # name -> parameterclass
    class_function_map = {}  # name -> functionclass
    class_member_index_map = {}  # name -> index

    def __init__(self, name, class_member_map_=None, class_function_map_=None):
        self.name = name
        if class_member_map_ is None:
            self.class_member_map = {}
        else:
            self.class_member_map = class_member_map_
        if class_function_map_ is None:
            self.class_function_map = {}
        else:
            self.class_function_map = class_function_map_


# 定义一个监听器类来遍历和处理语法树
class MyListener(Mx_parserListener):
    # def enterEveryRule(self, ctx):
    #     rule_name = Mx_parserParser.ruleNames[ctx.getRuleIndex()]
    #     rule_text = ctx.getText()
    #     print(f"Entering rule: {rule_name}, Text: {rule_text}")

    # def exitEveryRule(self, ctx):
    #     rule_name = Mx_parserParser.ruleNames[ctx.getRuleIndex()]
    #     rule_text = ctx.getText()
    #     print(f"Existing rule: {rule_name}, Text: {rule_text}")

    def __init__(self) -> None:
        print_ = functionclass(
            "void[0]",
            "print",
            [parameterclass("string[0]", "__str", "", 0)],
            0,
        )
        println = functionclass(
            "void[0]",
            "println",
            [parameterclass("string[0]", "__str", "", 0)],
            0,
        )
        printInt = functionclass(
            "void[0]",
            "printInt",
            [parameterclass("int[0]", "__int", "", 0)],
            0,
        )
        printlnInt = functionclass(
            "void[0]",
            "printlnInt",
            [parameterclass("int[0]", "__int", "", 0)],
            0,
        )
        getstring = functionclass(
            "string[0]",
            "getString",
            [],
            0,
        )
        getint = functionclass(
            "int[0]",
            "getInt",
            [],
            0,
        )
        tostring = functionclass(
            "string[0]",
            "toString",
            [parameterclass("int[0]", "__int", "", 0)],
            0,
        )
        self.function_definition_stack.append(print_)
        self.function_definition_stack.append(println)
        self.function_definition_stack.append(printlnInt)
        self.function_definition_stack.append(printInt)
        self.function_definition_stack.append(getstring)
        self.function_definition_stack.append(getint)
        self.function_definition_stack.append(tostring)
        for i in self.function_definition_stack:
            self.function_definition_map[i.name] = [i]

    # def visitTerminal(self, node: TerminalNodeImpl):
    #     # 当访问到终端节点时调用此方法
    #     print(node.getText(), end="")

    def return_expression2ir(self, code, print=False) -> str:
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
            t1 = self.return_expression2ir(code.expression(0))
            t2 = self.return_expression2ir(code.expression(1))
            result = "%" + t1 + "_" + t2
            if code.MUL() != None:
                op = "mul"
            elif code.DIV() != None:
                op = "sdiv"
            else:
                op = "srem"
            print(result + " = " + op + " i32 " + t1 + " " + t2)
            return result
        elif isinstance(code, Mx_parserParser.PlusminusExpressionContext):
            # plusminusExpression
            t1 = self.return_expression2ir(code.expression(0))
            t2 = self.return_expression2ir(code.expression(1))
            result = "%" + t1 + "_" + t2
            if code.PLUS() != None:
                op = "add"
            elif code.MINUS() != None:
                op = "sub"
            print(result + " = " + op + " i32 " + t1 + " " + t2)
            return result
        elif isinstance(code, Mx_parserParser.ShiftExpressionContext):
            # shiftExpression
            t1 = self.return_expression2ir(code.expression(0))
            t2 = self.return_expression2ir(code.expression(1))
            result = "%" + t1 + "_" + t2
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
            result = "%" + t1 + "_" + t2
            if code.AND() != None:
                op = "and"
            elif code.XOR() != None:
                op = "xor"
            else:
                op = "or"
            print(result + " = " + op + " i32 " + t1 + " " + t2)
            return result
        elif isinstance(code, Mx_parserParser.PrefixIncrementExpressionContext):
            # prefixIncrementExpression
            t = self.return_expression2ir(code.expression())
            print(t + " = add i32 " + t + " 1")
            return t
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
            name = code.IDENTIFIER().getText()
            func = self.function_definition_map[name][-1]
            func2ir = self.type2ir(func.returnType()) + " @" + name + "("
            result = "%" + name
            for i in range(len(func.parameterList)):
                type2 = func.parameterList[i].type
                func2ir += (
                    self.type2ir(type2)
                    + " "
                    + self.return_expression2ir(code.expressionList().expression(i))
                )
            func2ir += ")"
            print(result + " = call " + func2ir)
            return result
        elif isinstance(code, Mx_parserParser.MemberFunctionCallContext):
            # memberFunctionCall
            type = self.return_expressiontype(code.expression())
            name = code.IDENTIFIER().getText()
            type_ = self.usertype_map[type]
            if name in type_.class_function_map:
                func = type_.class_function_map[name]
            elif name == "size" and type[-1] == "]":  # 写的很糟糕
                index = int(type[-2]) - 1
                return self.variable_definition_map[code.expression().getText()].size[
                    index
                ]
            elif type == "string[0]":
                if name == "length":
                    func = functionclass("int[0]", name, [], 0)
                elif name == "substring":
                    func = functionclass(
                        "string[0]",
                        name,
                        [
                            parameterclass("int[0]", "a", 0, 0),
                            parameterclass("int[0]", "b", 0, 0),
                        ],
                        0,
                    )
                elif name == "parseInt":
                    func = functionclass("int[0]", name, [], 0)
                elif name == "ord":
                    func = functionclass(
                        "string[0]", name, [parameterclass("int[0]", "a", 0, 0)], 0
                    )
            func2ir = (
                self.type2ir(func.returnType())
                + " @"
                + type
                + "_"
                + name
                + "("
                + "%"
                + self.type2ir(type)
                + " "
                + self.return_expression2ir(code.expression())
            )  # void 有问题
            result = "%" + type + "_" + name
            for i in range(len(func.parameterList)):
                type2 = func.parameterList[i].type
                func2ir += (
                    self.type2ir(type2)
                    + " "
                    + self.return_expression2ir(code.expressionList().expression(i))
                )
            func2ir += ")"
            print(result + " = call " + func2ir)
            return result
        elif isinstance(code, Mx_parserParser.MemberMemberCallContext):
            # memberMemberCall
            type = self.return_expressiontype(code.expression())
            name = code.IDENTIFIER().getText()
            type_ = self.usertype_map[type]
            mem = type_.class_member_map[name]
            index = type_.class_member_index_map[name]
            caller = self.return_expression2ir(code.expression())
            result = caller + "_" + name
            print(
                result
                + " = getelementptr "
                + self.type2ir(type_)
                + ", ptr "
                + caller
                + ", i32 0, i32 "
                + str(index)
            )
            return result
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
            expression = code.expression()
            for i in range(len(expression)):
                type_ = self.return_expressiontype(expression[i])
                if type_ != "int[0]":
                    print("Type Mismatch")
                    sys.exit(1)

            dimansion = len(code.square_brackets1())
            type = arrayclass(code.type_().getText(), dimansion).to_string()
            if code.array_constant() != None:
                expressionlist = code.array_constant().expression()
                if len(expressionlist) == 0:
                    return type
                type1 = self.return_expressiontype(expressionlist[0])
                for i in range(1, len(expressionlist)):
                    type2 = self.return_expressiontype(expressionlist[i])
                    if type2 != "null" and type1[:-3] != type2[:-3]:
                        print("Type Mismatch")
                        sys.exit(1)
                type2 = type1.split("[")[0] + "[" + str(int(type1[-2]) + 1) + "]"
                if type2 != type:
                    print("Type Mismatch")
                    sys.exit(1)
                    # 没写
            return type
        elif isinstance(code, Mx_parserParser.VariableExpressionContext):
            # variableExpression
            identifier = code.IDENTIFIER().getText()
            name = identifier + str(len(self.variable_definition_map[identifier]))
            return name
        elif isinstance(code, Mx_parserParser.ArrayExpressionContext):
            # arrayExpression
            expression = code.expression()
            for i in range(1, len(expression)):
                pass

            dimansion = len(code.square_brackets1())
            type = self.return_expressiontype(code.expression(0))
            dimansion2 = int(type.split("[")[1].split("]")[0])
            return type.split("[")[0] + "[" + str(dimansion2 - dimansion) + "]"
        elif isinstance(code, Mx_parserParser.ParenthesesExpressionContext):
            # parenthesesExpression
            return self.return_expressiontype(code.expression())
        else:
            name = code.getText()
            # 如果没有匹配的规则，返回未知类型
            return "unknown"

    def type2ir(self, str) -> str:
        if str == "int[0]":
            return "i32"
        elif str == "bool[0]":
            return "i1"
        elif str == "string[0]":
            return "i8*"

    def enterProgram(self, ctx: Mx_parserParser.ProgramContext):
        for child in ctx.getChildren():
            if isinstance(child, Mx_parserParser.ClassDefinitionContext):
                pass
            elif isinstance(child, Mx_parserParser.FunctionDefinitionContext):
                pass

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

    # 创建输入流和语法分析器
    input_stream = InputStream(code)
    lexer = Mx_parserLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Mx_parserParser(token_stream)

    # 构建语法树
    tree = parser.program()

    # 创建监听器实例并遍历语法树
    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == "__main__":
    code = sys.stdin.read()
    main(code)
