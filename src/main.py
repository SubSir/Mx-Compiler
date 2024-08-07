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

    def __init__(self, type, name, value, priority):
        self.type = type
        self.name = name
        self.value = value
        self.priority = priority


class classclass:
    name = ""
    class_member_map = {}  # name -> parameterclass
    class_function_map = {}  # name -> functionclass

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
    function_definition_map = {}  # name -> list[functionclass]
    function_definition_stack = []  # list[functionclass]
    usertype_map = {}  # name -> classclass
    int_main_check = False
    variable_definition_map = {}  # name -> list[parameterclass]
    variable_definition_stack = []  # list[parameterclass]
    priority = 0
    loop = 0
    enterclass = ""

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

    def return_expressiontype(self, code, print=False) -> str:
        if isinstance(code, Mx_parserParser.ExpressionListContext):
            # expressionList
            type1 = self.return_expressiontype(code.expression())
            name = code.IDENTIFIER().getText()
            if name == "this":
                print("error: cannot assign to this")
                sys.exit(1)
            if name in self.variable_definition_map:
                type2 = self.variable_definition_map[name][-1].type
            else:
                print("error: undeclared variable")
                sys.exit(1)

            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            return self.return_expressiontype(code.expression())
        elif isinstance(code, Mx_parserParser.LogicExpressionContext):
            # logicExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != "bool[0]" or type2 != "bool[0]":
                print("error: type mismatch")
                sys.exit(1)
            return "bool[0]"
        elif isinstance(code, Mx_parserParser.ConditionalExpressionContext):
            # conditionalExpression
            if self.return_expressiontype(code.expression(0)) != "bool[0]":
                print("error: type mismatch")
                sys.exit(1)
            type1 = self.return_expressiontype(code.expression(1))
            type2 = self.return_expressiontype(code.expression(2))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            return type1
        elif isinstance(code, Mx_parserParser.RelationalExpressionContext):
            # relationalExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            if (
                type1 == "bool[0]"
                and code.relationalOperator().getText() != "=="
                and code.relationalOperator().getText() != "!="
            ):
                print("error: bool type cannot be compared")
                sys.exit(1)
            return "bool[0]"
        elif isinstance(code, Mx_parserParser.MuldivmodExpressionContext):
            # muldivmodExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            if type1 != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type1
        elif isinstance(code, Mx_parserParser.PlusminusExpressionContext):
            # plusminusExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            if type1 != "int[0]" and type1 != "string[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type1
        elif isinstance(code, Mx_parserParser.ShiftExpressionContext):
            # shiftExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            if type1 != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type1
        elif isinstance(code, Mx_parserParser.AndxororExpressionContext):
            # andxororExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            if type1 != "bool[0]" and type1 != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type1
        elif isinstance(code, Mx_parserParser.PrefixIncrementExpressionContext):
            # prefixIncrementExpression
            type = self.return_expressiontype(code.expression())
            if type != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type
        elif isinstance(code, Mx_parserParser.PostfixIncrementExpressionContext):
            # postfixIncrementExpression
            type = self.return_expressiontype(code.expression())
            if type != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type
        elif isinstance(code, Mx_parserParser.PrefixDecrementExpressionContext):
            # prefixDecrementExpression
            type = self.return_expressiontype(code.expression())
            if type != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type
        elif isinstance(code, Mx_parserParser.PostfixDecrementExpressionContext):
            # postfixDecrementExpression
            type = self.return_expressiontype(code.expression())
            if type != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type
        elif isinstance(code, Mx_parserParser.LogicalNotExpressionContext):
            # logicalNotExpression
            return self.return_expressiontype(code.expression())
        elif isinstance(code, Mx_parserParser.BitwiseNotExpressionContext):
            # bitwiseNotExpression
            return self.return_expressiontype(code.expression())
        elif isinstance(code, Mx_parserParser.UnaryMinusExpressionContext):
            # unaryMinusExpression
            return self.return_expressiontype(code.expression())
        elif isinstance(code, Mx_parserParser.FunctionCallContext):
            # functionCall
            name = code.IDENTIFIER().getText()
            if name in self.function_definition_map:
                func = self.function_definition_map[name][-1]
                len1 = 0
                if code.expressionLists() is not None:
                    len1 = len(code.expressionLists().expression())
                if len1 != len(func.parameterList):
                    print("error: wrong number of arguments")
                    sys.exit(1)
                for i in range(len(func.parameterList)):
                    if code.expressionLists() == None:
                        print("error: type mismatch")
                        sys.exit(1)
                    type1 = self.return_expressiontype(
                        code.expressionLists().expression(i)
                    )
                    type2 = func.parameterList[i].type
                    if type1 != type2 and type1 != "null" and type2 != "null":
                        print("error: type mismatch")
                        sys.exit(1)
                return func.returnType
            else:
                print("error: undefined function")
                sys.exit(1)
        elif isinstance(code, Mx_parserParser.MemberFunctionCallContext):
            # memberFunctionCall
            type = self.return_expressiontype(code.expression())
            name = code.IDENTIFIER().getText()
            if type in self.usertype_map:
                type_ = self.usertype_map[type]
                if name in type_.class_function_map:
                    func = type_.class_function_map[name]
                    len1 = 0
                    if code.expressionLists() is not None:
                        len1 = len(code.expressionLists().expression())
                    if len1 != len(func.parameterList):
                        print("error: wrong number of arguments")
                        sys.exit(1)
                    for i in range(len(func.parameterList)):
                        if code.expressionLists() == None:
                            print("error: type mismatch")
                            sys.exit(1)
                        type1 = self.return_expressiontype(
                            code.expressionLists().expression(i)
                        )
                        type2 = func.parameterList[i].type
                        if type1 != type2 and type1 != "null" and type2 != "null":
                            print("error: type mismatch")
                            sys.exit(1)
                    return func.returnType
                else:
                    print("error: undefined function")
                    sys.exit(1)
            elif name == "size" and type[-1] == "]":  # 写的很糟糕
                return "int[0]"
            elif type == "string[0]":
                if name == "length":
                    return "int[0]"
                elif name == "substring":
                    return "string[0]"
                elif name == "parseInt":
                    return "int[0]"
                elif name == "ord":
                    return "int[0]"
            else:
                print("error: undefined function")
                sys.exit(1)
        elif isinstance(code, Mx_parserParser.MemberMemberCallContext):
            # memberMemberCall
            type = self.return_expressiontype(code.expression())
            name = code.IDENTIFIER().getText()
            if type in self.usertype_map:
                type_ = self.usertype_map[type]
                if name in type_.class_member_map:
                    mem = type_.class_member_map[name]
                    return mem.type
                else:
                    print("error: undefined function")
                    sys.exit(1)
            elif name == "size" and type[-1] == "]":  # 写的很糟糕
                return "int[0]"
            elif type == "string[0]":
                if name == "length":
                    return "int[0]"
                elif name == "substring":
                    return "string[0]"
                elif name == "parseInt":
                    return "int[0]"
                elif name == "ord":
                    return "int[0]"
            else:
                print("error: undefined function")
                sys.exit(1)
        elif isinstance(code, Mx_parserParser.ConstantExpressionContext):
            # constantExpression
            constant = code.constant()
            if constant.INTEGER_CONSTANT() != None:
                if print:
                    print(constant.getText(), end=" ")
                return "int[0]"
            if constant.string_constant() != None:
                return "string[0]"
            if constant.array_constant() != None:
                expressionlist = constant.array_constant().expression()
                if len(expressionlist) == 0:
                    return "null"
                type1 = self.return_expressiontype(expressionlist[0])
                for i in range(1, len(expressionlist)):
                    type2 = self.return_expressiontype(expressionlist[i])
                    if type2 != "null" and type1[:-3] != type2[:-3]:
                        print("error: type mismatch")
                        sys.exit(1)
                return type1.split("[")[0] + "[" + str(int(type1[-2]) + 1) + "]"
            if constant.getText() == "null":
                return "null"
            return "bool[0]"
        elif isinstance(code, Mx_parserParser.NewVariableExpressionContext):
            # newVariableExpression
            return code.type_().getText() + "[0]"
        elif isinstance(code, Mx_parserParser.NewArrayExpressionContext):
            # newArrayExpression
            expression = code.expression()
            for i in range(len(expression)):
                type_ = self.return_expressiontype(expression[i])
                if type_ != "int[0]":
                    print("error: type mismatch")
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
                        print("error: type mismatch")
                        sys.exit(1)
                type2 = type1.split("[")[0] + "[" + str(int(type1[-2]) + 1) + "]"
                if type2 != type:
                    print("error: type mismatch")
                    sys.exit(1)

            return type
        elif isinstance(code, Mx_parserParser.VariableExpressionContext):
            # variableExpression
            identifier = code.IDENTIFIER().getText()
            if identifier in self.variable_definition_map:
                type = self.variable_definition_map[identifier][-1].type
            else:
                print("error: undeclared variable")
                sys.exit(1)
            return type
        elif isinstance(code, Mx_parserParser.ArrayExpressionContext):
            # arrayExpression
            expression = code.expression()
            if isinstance(
                code.expression(0), Mx_parserParser.NewArrayExpressionContext
            ) or isinstance(
                code.expression(0), Mx_parserParser.NewVariableExpressionContext
            ):
                print(
                    "error: The shape of multidimensional array must be specified from left to right"
                )
                sys.exit(1)
            for i in range(1, len(expression)):
                type_ = self.return_expressiontype(expression[i])
                if type_ != "int[0]":
                    print("error: type mismatch")
                    sys.exit(1)
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

    def return_const_or_not(self, code) -> bool:
        if isinstance(code, Mx_parserParser.ConstantExpressionContext):
            return True
        elif isinstance(code, Mx_parserParser.NewVariableExpressionContext):
            return False
        elif isinstance(code, Mx_parserParser.NewArrayExpressionContext):
            return False
        elif isinstance(code, Mx_parserParser.VariableExpressionContext):
            return False
        elif isinstance(code, Mx_parserParser.ArrayExpressionContext):
            return False
        elif isinstance(code, Mx_parserParser.ParenthesesExpressionContext):
            return self.return_const_or_not(code.expression())
        elif isinstance(code, Mx_parserParser.MemberMemberCallContext):
            return False  # 写的很糟糕
        elif isinstance(code, Mx_parserParser.MemberFunctionCallContext):
            return True
        elif isinstance(code, Mx_parserParser.ConditionalExpressionContext):
            isconst1 = self.return_const_or_not(code.expression(1))
            isconst2 = self.return_const_or_not(code.expression(2))
            return isconst1 or isconst2
        elif isinstance(code, Mx_parserParser.PrefixIncrementExpressionContext):
            if self.return_const_or_not(code.expression()) == True:
                print("error: The operand of ++ or -- must be a variable")
                sys.exit(1)
            return False
        elif isinstance(code, Mx_parserParser.PrefixDecrementExpressionContext):
            if self.return_const_or_not(code.expression()) == True:
                print("error: The operand of ++ or -- must be a variable")
                sys.exit(1)
            return False
        elif isinstance(code, Mx_parserParser.PostfixIncrementExpressionContext):
            if self.return_const_or_not(code.expression()) == True:
                print("error: The operand of ++ or -- must be a variable")
                sys.exit(1)
            return True
        elif isinstance(code, Mx_parserParser.PostfixDecrementExpressionContext):
            if self.return_const_or_not(code.expression()) == True:
                print("error: The operand of ++ or -- must be a variable")
                sys.exit(1)
            return True
        elif isinstance(code, Mx_parserParser.UnaryMinusExpressionContext):
            return True
        elif isinstance(code, Mx_parserParser.LogicalNotExpressionContext):
            return True
        elif isinstance(code, Mx_parserParser.BitwiseNotExpressionContext):
            return True
        elif isinstance(code, Mx_parserParser.FunctionCallContext):
            return True
        elif isinstance(code, Mx_parserParser.MemberFunctionCallContext):
            return True
        elif isinstance(code, Mx_parserParser.MemberMemberCallContext):
            return False
        elif isinstance(code, Mx_parserParser.MuldivmodExpressionContext):
            return True
        elif isinstance(code, Mx_parserParser.PlusminusExpressionContext):
            return True
        elif isinstance(code, Mx_parserParser.ShiftExpressionContext):
            return True
        elif isinstance(code, Mx_parserParser.RelationalExpressionContext):
            return True
        elif isinstance(code, Mx_parserParser.AndxororExpressionContext):
            return True
        elif isinstance(code, Mx_parserParser.LogicExpressionContext):
            return True
        elif isinstance(code, Mx_parserParser.ExpressionListContext):
            return True

    def return_expression2ir(self, code, print=False) -> str:
        if isinstance(code, Mx_parserParser.ExpressionListContext):
            # expressionList
            type1 = self.return_expressiontype(code.expression())
            name = code.IDENTIFIER().getText()
            if name == "this":
                print("error: cannot assign to this")
                sys.exit(1)
            if name in self.variable_definition_map:
                type2 = self.variable_definition_map[name][-1].type
            else:
                print("error: undeclared variable")
                sys.exit(1)

            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            return self.return_expressiontype(code.expression())
        elif isinstance(code, Mx_parserParser.LogicExpressionContext):
            # logicExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != "bool[0]" or type2 != "bool[0]":
                print("error: type mismatch")
                sys.exit(1)
            return "bool[0]"
        elif isinstance(code, Mx_parserParser.ConditionalExpressionContext):
            # conditionalExpression
            if self.return_expressiontype(code.expression(0)) != "bool[0]":
                print("error: type mismatch")
                sys.exit(1)
            type1 = self.return_expressiontype(code.expression(1))
            type2 = self.return_expressiontype(code.expression(2))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            return type1
        elif isinstance(code, Mx_parserParser.RelationalExpressionContext):
            # relationalExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            if (
                type1 == "bool[0]"
                and code.relationalOperator().getText() != "=="
                and code.relationalOperator().getText() != "!="
            ):
                print("error: bool type cannot be compared")
                sys.exit(1)
            return "bool[0]"
        elif isinstance(code, Mx_parserParser.MuldivmodExpressionContext):
            # muldivmodExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            if type1 != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type1
        elif isinstance(code, Mx_parserParser.PlusminusExpressionContext):
            # plusminusExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            if type1 != "int[0]" and type1 != "string[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type1
        elif isinstance(code, Mx_parserParser.ShiftExpressionContext):
            # shiftExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            if type1 != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type1
        elif isinstance(code, Mx_parserParser.AndxororExpressionContext):
            # andxororExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
                sys.exit(1)
            if type1 != "bool[0]" and type1 != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type1
        elif isinstance(code, Mx_parserParser.PrefixIncrementExpressionContext):
            # prefixIncrementExpression
            type = self.return_expressiontype(code.expression())
            if type != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type
        elif isinstance(code, Mx_parserParser.PostfixIncrementExpressionContext):
            # postfixIncrementExpression
            type = self.return_expressiontype(code.expression())
            if type != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type
        elif isinstance(code, Mx_parserParser.PrefixDecrementExpressionContext):
            # prefixDecrementExpression
            type = self.return_expressiontype(code.expression())
            if type != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type
        elif isinstance(code, Mx_parserParser.PostfixDecrementExpressionContext):
            # postfixDecrementExpression
            type = self.return_expressiontype(code.expression())
            if type != "int[0]":
                print("error: type cannot be used in arithmetic expression")
                sys.exit(1)
            return type
        elif isinstance(code, Mx_parserParser.LogicalNotExpressionContext):
            # logicalNotExpression
            return self.return_expressiontype(code.expression())
        elif isinstance(code, Mx_parserParser.BitwiseNotExpressionContext):
            # bitwiseNotExpression
            return self.return_expressiontype(code.expression())
        elif isinstance(code, Mx_parserParser.UnaryMinusExpressionContext):
            # unaryMinusExpression
            return self.return_expressiontype(code.expression())
        elif isinstance(code, Mx_parserParser.FunctionCallContext):
            # functionCall
            name = code.IDENTIFIER().getText()
            if name in self.function_definition_map:
                func = self.function_definition_map[name][-1]
                len1 = 0
                if code.expressionLists() is not None:
                    len1 = len(code.expressionLists().expression())
                if len1 != len(func.parameterList):
                    print("error: wrong number of arguments")
                    sys.exit(1)
                for i in range(len(func.parameterList)):
                    if code.expressionLists() == None:
                        print("error: type mismatch")
                        sys.exit(1)
                    type1 = self.return_expressiontype(
                        code.expressionLists().expression(i)
                    )
                    type2 = func.parameterList[i].type
                    if type1 != type2 and type1 != "null" and type2 != "null":
                        print("error: type mismatch")
                        sys.exit(1)
                return func.returnType
            else:
                print("error: undefined function")
                sys.exit(1)
        elif isinstance(code, Mx_parserParser.MemberFunctionCallContext):
            # memberFunctionCall
            type = self.return_expressiontype(code.expression())
            name = code.IDENTIFIER().getText()
            if type in self.usertype_map:
                type_ = self.usertype_map[type]
                if name in type_.class_function_map:
                    func = type_.class_function_map[name]
                    len1 = 0
                    if code.expressionLists() is not None:
                        len1 = len(code.expressionLists().expression())
                    if len1 != len(func.parameterList):
                        print("error: wrong number of arguments")
                        sys.exit(1)
                    for i in range(len(func.parameterList)):
                        if code.expressionLists() == None:
                            print("error: type mismatch")
                            sys.exit(1)
                        type1 = self.return_expressiontype(
                            code.expressionLists().expression(i)
                        )
                        type2 = func.parameterList[i].type
                        if type1 != type2 and type1 != "null" and type2 != "null":
                            print("error: type mismatch")
                            sys.exit(1)
                    return func.returnType
                else:
                    print("error: undefined function")
                    sys.exit(1)
            elif name == "size" and type[-1] == "]":  # 写的很糟糕
                return "int[0]"
            elif type == "string[0]":
                if name == "length":
                    return "int[0]"
                elif name == "substring":
                    return "string[0]"
                elif name == "parseInt":
                    return "int[0]"
                elif name == "ord":
                    return "int[0]"
            else:
                print("error: undefined function")
                sys.exit(1)
        elif isinstance(code, Mx_parserParser.MemberMemberCallContext):
            # memberMemberCall
            type = self.return_expressiontype(code.expression())
            name = code.IDENTIFIER().getText()
            if type in self.usertype_map:
                type_ = self.usertype_map[type]
                if name in type_.class_member_map:
                    mem = type_.class_member_map[name]
                    return mem.type
                else:
                    print("error: undefined function")
                    sys.exit(1)
            elif name == "size" and type[-1] == "]":  # 写的很糟糕
                return "int[0]"
            elif type == "string[0]":
                if name == "length":
                    return "int[0]"
                elif name == "substring":
                    return "string[0]"
                elif name == "parseInt":
                    return "int[0]"
                elif name == "ord":
                    return "int[0]"
            else:
                print("error: undefined function")
                sys.exit(1)
        elif isinstance(code, Mx_parserParser.ConstantExpressionContext):
            # constantExpression
            constant = code.constant()
            if constant.INTEGER_CONSTANT() != None:
                if print:
                    print(constant.getText(), end=" ")
                return "int[0]"
            if constant.string_constant() != None:
                return "string[0]"
            if constant.array_constant() != None:
                expressionlist = constant.array_constant().expression()
                if len(expressionlist) == 0:
                    return "null"
                type1 = self.return_expressiontype(expressionlist[0])
                for i in range(1, len(expressionlist)):
                    type2 = self.return_expressiontype(expressionlist[i])
                    if type2 != "null" and type1[:-3] != type2[:-3]:
                        print("error: type mismatch")
                        sys.exit(1)
                return type1.split("[")[0] + "[" + str(int(type1[-2]) + 1) + "]"
            if constant.getText() == "null":
                return "null"
            return "bool[0]"
        elif isinstance(code, Mx_parserParser.NewVariableExpressionContext):
            # newVariableExpression
            return code.type_().getText() + "[0]"
        elif isinstance(code, Mx_parserParser.NewArrayExpressionContext):
            # newArrayExpression
            expression = code.expression()
            for i in range(len(expression)):
                type_ = self.return_expressiontype(expression[i])
                if type_ != "int[0]":
                    print("error: type mismatch")
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
                        print("error: type mismatch")
                        sys.exit(1)
                type2 = type1.split("[")[0] + "[" + str(int(type1[-2]) + 1) + "]"
                if type2 != type:
                    print("error: type mismatch")
                    sys.exit(1)

            return type
        elif isinstance(code, Mx_parserParser.VariableExpressionContext):
            # variableExpression
            identifier = code.IDENTIFIER().getText()
            name = identifier + str(len(self.variable_definition_map[identifier]))
            return name
        elif isinstance(code, Mx_parserParser.ArrayExpressionContext):
            # arrayExpression
            expression = code.expression()
            if isinstance(
                code.expression(0), Mx_parserParser.NewArrayExpressionContext
            ) or isinstance(
                code.expression(0), Mx_parserParser.NewVariableExpressionContext
            ):
                print(
                    "error: The shape of multidimensional array must be specified from left to right"
                )
                sys.exit(1)
            for i in range(1, len(expression)):
                type_ = self.return_expressiontype(expression[i])
                if type_ != "int[0]":
                    print("error: type mismatch")
                    sys.exit(1)
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

    def array_decode(self, code) -> arrayclass:
        return arrayclass(code.type_().getText(), (code.getChildCount() - 1) // 2)

    def parameter_decode(self, code) -> parameterclass:
        text = code.getText()
        if code.type_() != None:
            return parameterclass(
                arrayclass(
                    code.type_().getText(),
                    0,
                ).to_string(),
                code.IDENTIFIER().getText(),
                None,
                self.priority,
            )
        else:
            return parameterclass(
                self.array_decode(code.arrayType()).to_string(),
                code.IDENTIFIER().getText(),
                None,
                self.priority,
            )

    def parameterList_decode(self, code) -> list[parameterclass]:
        if code == None:
            return []
        parameters = code.parameter()
        if parameters == None:
            return []
        return_list = []
        for param in parameters:
            return_list.append(self.parameter_decode(param))
        return return_list

    def variableDeclaration_decode(self, code) -> list[parameterclass]:
        return_list = []
        variableDeclarationparts = code.variableDeclarationparts()
        arrayclass_ = None
        if code.type_() != None:
            arrayclass_ = arrayclass(
                code.type_().getText(),
                0,
            )
        else:
            arrayclass_ = self.array_decode(code.arrayType())

        type_ = arrayclass_.to_string()
        for variableDeclarationpart in variableDeclarationparts:

            if variableDeclarationpart.expression() != None:
                type2 = self.return_expressiontype(variableDeclarationpart.expression())
                if type2 != type_ and type2 != "null":
                    print("error: type mismatch")
                    sys.exit(1)

                if type2 == "null":
                    if type_ == "int[0]" or type_ == "bool[0]" or type_ == "string[0]":
                        print(
                            "error: null cannot be assigned to primitive type variable"
                        )
                        sys.exit(1)
            name = variableDeclarationpart.IDENTIFIER().getText()
            if name == "this":
                print("error: this is a reserved word")
                sys.exit(1)

            return_list.append(
                parameterclass(
                    type_,
                    name,
                    None,
                    self.priority,
                )
            )
        return return_list

    def functionDefinition_decode(self, code) -> functionclass:
        type = self.type_to_string(code.returnType().getText())
        name = code.IDENTIFIER().getText()
        parameter_list = self.parameterList_decode(code.parameterList())
        return functionclass(type, name, parameter_list, self.priority)

    def class_decode(self, code) -> classclass:
        name = code.IDENTIFIER().getText() + "[0]"
        members = code.classMember()
        class_ = classclass(name)
        for member in members:
            if member.variableDeclaration() != None:
                member_list = self.variableDeclaration_decode(
                    member.variableDeclaration()
                )
                for i in member_list:
                    if i.name in class_.class_member_map:
                        print("error: redeclaration")
                        sys.exit(1)
                    class_.class_member_map[i.name] = i
            elif member.functionDefinition() != None:
                self.priority += 1
                function = self.functionDefinition_decode(member.functionDefinition())
                if function.name in class_.class_function_map:
                    print("error: redeclaration")
                    sys.exit(1)
                class_.class_function_map[function.name] = function
                self.priority -= 1
            else:
                self.priority += 1
                if "construction" in class_.class_function_map:
                    print("error: redeclaration")
                    sys.exit(1)
                if (
                    member.construction().IDENTIFIER().getText()
                    != code.IDENTIFIER().getText()
                ):
                    print(
                        "error: The name of class constructor must be the same as the class name."
                    )
                    sys.exit(1)
                class_.class_function_map["construction"] = functionclass(
                    "void[0]",
                    "construction",
                    self.parameterList_decode(member.construction().parameterList()),
                    self.priority,
                )
                self.priority -= 1
        if "construction" not in class_.class_function_map:
            class_.class_function_map["construction"] = functionclass(
                "void[0]",
                "construction",
                [],
                self.priority,
            )
        return class_

    def enterConstruction(self, ctx: Mx_parserParser.ConstructionContext):
        self.function_definition_stack.append(
            functionclass(
                "void[0]",
                "construction",
                self.parameterList_decode(ctx.parameterList()),
                self.priority,
            )
        )

    def exitConstruction(self, ctx: Mx_parserParser.ConstructionContext):
        self.function_definition_stack.pop()

    def type_to_string(self, text: str):
        if text[-1] == "]" and text[-2].isdigit():
            return text
        if len(text) > 2 and text[-2] == "[":
            cut = ""
            cnt = 0
            for i in range(len(text)):
                if text[i] == "[":
                    cnt += 1
                    if cut == "":
                        cut = text[:i]
            return cut + "[" + str(cnt) + "]"
        return text + "[0]"

    def enterProgram(self, ctx: Mx_parserParser.ProgramContext):
        self.priority += 1
        for child in ctx.getChildren():
            if isinstance(child, Mx_parserParser.ClassDefinitionContext):
                class_ = self.class_decode(child)
                if class_.name in self.usertype_map:
                    print("error: redeclaration")
                    sys.exit(1)
                self.usertype_map[class_.name] = class_
                # self.variable_definition_map["this"] = [
                #     parameterclass(class_.name, "this", None, self.priority)
                # ]
                if class_.name[:-3] in self.function_definition_map:
                    print("Error: redeclaration")
                    sys.exit(1)
            elif isinstance(child, Mx_parserParser.FunctionDefinitionContext):
                returnType = self.type_to_string(child.returnType().getText())
                name = child.IDENTIFIER().getText()
                parameterList = child.parameterList()
                parameter_list = []
                num_parameters = 0
                if parameterList is not None:
                    num_parameters = len(parameterList.parameter())
                    parameter_list = self.parameterList_decode(parameterList)

                if (
                    name == "main"
                    and returnType == "int[0]"
                    and num_parameters == 0
                    and self.priority == 1
                ):
                    if self.int_main_check:
                        print("Error: Multiple definitions of main function")
                        sys.exit(1)
                    self.int_main_check = True
                func = functionclass(returnType, name, parameter_list, self.priority)
                if (
                    name in self.function_definition_map
                    and self.enterclass == ""
                    and self.priority == self.function_definition_map[name][-1].piority
                ):
                    print("Error: redeclaration")
                    sys.exit(1)
                if not (
                    name in self.function_definition_map
                    and self.priority == self.function_definition_map[name][-1].priority
                ):
                    if name not in self.function_definition_map:
                        self.function_definition_map[name] = []
                    self.function_definition_map[name] += [func]
                    # self.function_definition_stack.append(func)
                # self.variable_definition_stack += parameter_list
                # for param in parameter_list:
                #     if param.name not in self.variable_definition_map:
                #         self.variable_definition_map[param.name] = [param]
                #     else:
                #         self.variable_definition_map[param.name] += [param]
                if self.type_to_string(name) in self.usertype_map:
                    print("Error: redeclaration")
                    sys.exit(1)
        self.priority -= 1

    def enterFunctionDefinition(self, ctx: Mx_parserParser.FunctionDefinitionContext):
        self.priority += 1
        returnType = self.type_to_string(ctx.returnType().getText())
        name = ctx.IDENTIFIER().getText()
        if name == "this":
            print("error: this is a reserved word.")
            sys.exit(1)

        parameterList = ctx.parameterList()
        parameter_list = []
        num_parameters = 0
        if parameterList is not None:
            num_parameters = len(parameterList.parameter())
            parameter_list = self.parameterList_decode(parameterList)

        # if (
        #     name == "main"
        #     and returnType == "int[0]"
        #     and num_parameters == 0
        #     and self.priority == 1
        # ):
        #     if self.int_main_check:
        #         print("Error: Multiple definitions of main function")
        #         sys.exit(1)
        #     self.int_main_check = True
        func = functionclass(returnType, name, parameter_list, self.priority)
        if (
            name in self.function_definition_map
            and self.enterclass == ""
            and self.priority == self.function_definition_map[name][-1].priority
            and self.priority != 1
        ):
            print("Error: redeclaration")
            sys.exit(1)
        if not (
            name in self.function_definition_map
            and self.priority == self.function_definition_map[name][-1].priority
        ):
            if name not in self.function_definition_map:
                self.function_definition_map[name] = []
            self.function_definition_map[name] += [func]
        if self.priority == 1 or self.enterclass != "":
            self.function_definition_stack.append(func)
        self.variable_definition_stack += parameter_list
        for param in parameter_list:
            if param.name not in self.variable_definition_map:
                self.variable_definition_map[param.name] = [param]
            else:
                self.variable_definition_map[param.name] += [param]
        if self.type_to_string(name) in self.usertype_map and self.priority != 1:
            print("Error: redeclaration")
            sys.exit(1)

    def exitFunctionDefinition(self, ctx: Mx_parserParser.FunctionDefinitionContext):
        self.priority -= 1
        if (
            self.function_definition_stack[-1].returned == False
            and self.function_definition_stack[-1].returnType != "void[0]"
            and not (
                self.function_definition_stack[-1].returnType == "int[0]"
                and self.function_definition_stack[-1].name == "main"
            )
        ):
            print(
                "Error: Function "
                + self.function_definition_stack[-1].name
                + " does not return a value"
            )
            sys.exit(1)
        for i in range(len(self.variable_definition_stack) - 1, -1, -1):
            if self.variable_definition_stack[i].priority <= self.priority:
                break
            if (
                len(
                    self.variable_definition_map[self.variable_definition_stack[i].name]
                )
                == 1
            ):
                self.variable_definition_map.pop(self.variable_definition_stack[i].name)
            else:
                self.variable_definition_map[
                    self.variable_definition_stack[i].name
                ].pop()
            self.variable_definition_stack.pop()
            i -= 1

        for i in range(len(self.function_definition_stack) - 1, -1, -1):
            if self.function_definition_stack[i].priority - 1 <= self.priority:
                break
            if len(
                self.function_definition_map[self.function_definition_stack[i].name]
                == 1
            ):
                self.function_definition_map.pop(self.function_definition_stack[i].name)
            else:
                self.function_definition_map[
                    self.function_definition_stack[i].name
                ].pop()
            self.function_definition_stack.pop()
            i -= 1

    def exitClassDefinition(self, ctx: Mx_parserParser.ClassDefinitionContext):
        self.priority -= 1
        self.enterclass = ""
        self.function_definition_map.pop("construction")
        self.variable_definition_map.pop("this")
        for i in range(len(self.variable_definition_stack) - 1, -1, -1):
            if self.variable_definition_stack[i].priority <= self.priority:
                break
            if (
                len(
                    self.variable_definition_map[self.variable_definition_stack[i].name]
                )
                == 1
            ):
                self.variable_definition_map.pop(self.variable_definition_stack[i].name)
            else:
                self.variable_definition_map[
                    self.variable_definition_stack[i].name
                ].pop()
            self.variable_definition_stack.pop()
            i -= 1

        for i in range(len(self.function_definition_stack) - 1, -1, -1):
            if self.function_definition_stack[i].priority - 1 <= self.priority:
                break
            if (
                len(
                    self.function_definition_map[self.function_definition_stack[i].name]
                )
                == 1
            ):
                self.function_definition_map.pop(self.function_definition_stack[i].name)
            else:
                self.function_definition_map[
                    self.function_definition_stack[i].name
                ].pop()
            self.function_definition_stack.pop()
            i -= 1

    def enterClassDefinition(self, ctx: Mx_parserParser.ClassDefinitionContext):
        self.priority += 1
        self.enterclass = ctx.IDENTIFIER().getText() + "[0]"
        class_ = self.usertype_map[ctx.IDENTIFIER().getText() + "[0]"]
        self.variable_definition_map["this"] = [
            parameterclass(class_.name, "this", None, self.priority)
        ]
        for i in class_.class_member_map.values():
            if (
                i.name in self.variable_definition_map
                and self.priority == self.variable_definition_map[i.name][-1].priority
            ):
                print("Error: redeclaration")
                sys.exit(1)
            if i.name not in self.variable_definition_map:
                self.variable_definition_map[i.name] = [i]
            else:
                self.variable_definition_map[i.name] += [i]
            self.variable_definition_stack.append(i)

        for i in class_.class_function_map.values():
            if (
                i.name in self.function_definition_map
                and i.priority == self.function_definition_map[i.name][-1].priority
            ):
                print("Error: redeclaration")
                sys.exit(1)
            if i.name not in self.function_definition_map:
                self.function_definition_map[i.name] = [i]
            else:
                self.function_definition_map[i.name] += [i]

    def enterVariableDeclaration(self, ctx: Mx_parserParser.VariableDeclarationContext):
        list = self.variableDeclaration_decode(ctx)
        for i in list:
            if (
                i.name in self.variable_definition_map
                and self.enterclass == ""
                and self.variable_definition_map[i.name][-1].priority == i.priority
            ):
                print("Error: redeclaration")
                sys.exit(1)
            if not (
                i.name in self.variable_definition_map
                and self.variable_definition_map[i.name][-1].priority == i.priority
            ):
                if i.name not in self.variable_definition_map:
                    self.variable_definition_map[i.name] = [i]
                else:
                    self.variable_definition_map[i.name] += [i]
                self.variable_definition_stack.append(i)

    def enterElsestatement(self, ctx: Mx_parserParser.ElsestatementContext):
        self.priority -= 1
        for i in range(len(self.variable_definition_stack) - 1, -1, -1):
            if self.variable_definition_stack[i].priority <= self.priority:
                break
            if (
                len(
                    self.variable_definition_map[self.variable_definition_stack[i].name]
                )
                == 1
            ):
                self.variable_definition_map.pop(self.variable_definition_stack[i].name)
            else:
                self.variable_definition_map[
                    self.variable_definition_stack[i].name
                ].pop()
            self.variable_definition_stack.pop()
            i -= 1
        self.priority += 1

    def exitElsestatement(self, ctx: Mx_parserParser.ElsestatementContext):
        self.priority -= 1
        for i in range(len(self.variable_definition_stack) - 1, -1, -1):
            if self.variable_definition_stack[i].priority <= self.priority:
                break
            if (
                len(
                    self.variable_definition_map[self.variable_definition_stack[i].name]
                )
                == 1
            ):
                self.variable_definition_map.pop(self.variable_definition_stack[i].name)
            else:
                self.variable_definition_map[
                    self.variable_definition_stack[i].name
                ].pop()
            self.variable_definition_stack.pop()
            i -= 1
        self.priority += 1

    # def enterClassDefinition(self, ctx):
    #     class_ = self.class_decode(ctx)
    #     self.usertype_map[class_.name] = class_
    #     if class_.name[:-3] in self.function_definition_map:
    #         print("Error: redeclaration")
    #         sys.exit(1)

    def enterType(self, ctx: Mx_parserParser.TypeContext):
        if (
            ctx.IDENTIFIER() != None
            and self.type_to_string(ctx.IDENTIFIER().getText())
            not in self.usertype_map.keys()
        ):
            print("Error: Undefined type")
            sys.exit(1)

    def enterExpressionStatement(self, ctx: Mx_parserParser.ExpressionStatementContext):
        self.return_expressiontype(ctx.expression())
        self.return_const_or_not(ctx.expression())

    def enterIfStatement(self, ctx: Mx_parserParser.IfStatementContext):
        self.priority += 1
        if self.return_expressiontype(ctx.expression()) != "bool[0]":
            print("Error: if statement condition is not bool")
            sys.exit(1)

    def exitIfStatement(self, ctx: Mx_parserParser.IfStatementContext):
        self.priority -= 1
        for i in range(len(self.variable_definition_stack) - 1, -1, -1):
            if self.variable_definition_stack[i].priority <= self.priority:
                break
            if (
                len(
                    self.variable_definition_map[self.variable_definition_stack[i].name]
                )
                == 1
            ):
                self.variable_definition_map.pop(self.variable_definition_stack[i].name)
            else:
                self.variable_definition_map[
                    self.variable_definition_stack[i].name
                ].pop()
            self.variable_definition_stack.pop()
            i -= 1

    def enterWhileStatement(self, ctx: Mx_parserParser.WhileStatementContext):
        self.loop += 1
        self.priority += 1
        if self.return_expressiontype(ctx.expression()) != "bool[0]":
            print("Error: if statement condition is not bool")
            sys.exit(1)

    def exitWhileStatement(self, ctx: Mx_parserParser.WhileStatementContext):
        self.loop -= 1
        self.priority -= 1
        for i in range(len(self.variable_definition_stack) - 1, -1, -1):
            if self.variable_definition_stack[i].priority <= self.priority:
                break
            if (
                len(
                    self.variable_definition_map[self.variable_definition_stack[i].name]
                )
                == 1
            ):
                self.variable_definition_map.pop(self.variable_definition_stack[i].name)
            else:
                self.variable_definition_map[
                    self.variable_definition_stack[i].name
                ].pop()
            self.variable_definition_stack.pop()
            i -= 1

    def enterForControl(self, ctx: Mx_parserParser.ForControlContext):
        expression = ctx.expression2()
        if expression != None:
            type = self.return_expressiontype(expression.expression())
            if type != "bool[0]":
                print("Error: for statement condition is not bool")
                sys.exit(1)

    def enterForStatement(self, ctx: Mx_parserParser.ForStatementContext):
        self.loop += 1
        self.priority += 1

    def exitForStatement(self, ctx: Mx_parserParser.ForStatementContext):
        self.loop -= 1
        self.priority -= 1
        for i in range(len(self.variable_definition_stack) - 1, -1, -1):
            if self.variable_definition_stack[i].priority <= self.priority:
                break
            if (
                len(
                    self.variable_definition_map[self.variable_definition_stack[i].name]
                )
                == 1
            ):
                self.variable_definition_map.pop(self.variable_definition_stack[i].name)
            else:
                self.variable_definition_map[
                    self.variable_definition_stack[i].name
                ].pop()
            self.variable_definition_stack.pop()
            i -= 1

    def enterReturnStatement(self, ctx: Mx_parserParser.ReturnStatementContext):
        returntype = self.function_definition_stack[-1].returnType
        expression = ctx.expression()
        if expression != None:
            type1 = self.return_expressiontype(expression)
            if type1 != returntype and not (
                type1 == "null"
                and returntype != "int[0]"
                and returntype != "bool[0]"
                and returntype != "string[0]"
            ):
                print(
                    "Error: return statement type does not match function return type"
                )
                sys.exit(1)
            self.function_definition_stack[-1].returned = True
        else:
            if returntype != "void[0]":
                print(
                    "Error: return statement type does not match function return type"
                )
                sys.exit(1)

    def enterAssignmentStatement(self, ctx: Mx_parserParser.AssignmentStatementContext):
        if self.return_const_or_not(ctx.expression(0)):
            print("Error: assignment statement type does not match variable type")
            sys.exit(1)
        if isinstance(ctx.expression(0), Mx_parserParser.VariableExpressionContext):
            if ctx.exception(0).IDENTIFIER().getText() == "this":
                print("Error: this cannot be assigned")
                sys.exit(1)
        type1 = self.return_expressiontype(ctx.expression(0))
        type2 = self.return_expressiontype(ctx.expression(1))
        if type1 != type2 and type2 != "null":
            print("Error: assignment statement type does not match variable type")
            sys.exit(1)
        if type2 == "null":
            if type1 == "int[0]" or type1 == "bool[0]" or type1 == "string[0]":
                print("Error: null cannot be assigned to primitive type variable")
                sys.exit(1)

    def enterBlock(self, ctx):
        self.priority += 1

    def exitBlock(self, ctx):
        self.priority -= 1
        for i in range(len(self.variable_definition_stack) - 1, -1, -1):
            if self.variable_definition_stack[i].priority <= self.priority:
                break
            if (
                len(
                    self.variable_definition_map[self.variable_definition_stack[i].name]
                )
                == 1
            ):
                self.variable_definition_map.pop(self.variable_definition_stack[i].name)
            else:
                self.variable_definition_map[
                    self.variable_definition_stack[i].name
                ].pop()
            self.variable_definition_stack.pop()
            i -= 1

        for i in range(len(self.function_definition_stack) - 1, -1, -1):
            if self.function_definition_stack[i].priority - 1 <= self.priority:
                break
            if len(
                self.function_definition_map[self.function_definition_stack[i].name]
                == 1
            ):
                self.function_definition_map.pop(self.function_definition_stack[i].name)
            else:
                self.function_definition_map[
                    self.function_definition_stack[i].name
                ].pop()
            self.function_definition_stack.pop()
            i -= 1

    def enterBreakStatement(self, ctx):
        if self.loop == 0:
            print("Error: break statement outside of loop")
            sys.exit(1)

    def enterContinueStatement(self, ctx):
        if self.loop == 0:
            print("Error: continue statement outside of loop")
            sys.exit(1)


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Syntax error at line {line}:{column}. {msg}")
        sys.exit(1)


# with open("in.txt", "r") as f:
#     code = f.read()

code = sys.stdin.read()

# 创建输入流和语法分析器
input_stream = InputStream(code)
lexer = Mx_parserLexer(input_stream)
lexer.removeErrorListeners()
lexer.addErrorListener(MyErrorListener())
token_stream = CommonTokenStream(lexer)
parser = Mx_parserParser(token_stream)
parser.removeErrorListeners()
parser.addErrorListener(MyErrorListener())

# 构建语法树
tree = parser.program()

# 创建监听器实例并遍历语法树
listener = MyListener()
walker = ParseTreeWalker()
walker.walk(listener, tree)
if listener.int_main_check == False:
    print("Error: No main function")
    sys.exit(1)
sys.exit(0)
