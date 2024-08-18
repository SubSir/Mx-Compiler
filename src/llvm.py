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
    variable_cnt = 0
    init_cnt = 0
    label_cnt = 0
    string_cnt = 1
    global_str = ""
    class_member_enum = {}  # A.x -> 0
    class_size_map = {}  # class_name -> size
    function_definition_list = []  # [str]
    variable_map = {}  # name -> (type, value) e.g. (int, 0)
    function_definition_map = {}  # name -> returnType
    loop_stack = []
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

    def return_expression2ir(
        self, code, stream
    ) -> str:  # stream[0] 为流, 返回variable_map的index
        result = "%" + str(self.variable_cnt)
        self.variable_cnt += 1
        # if isinstance(code, Mx_parserParser.ExpressionListContext):
        #     # expressionList
        #     type = self.variable_map[code.IDENTIFIER().getText()][0]
        #     t1 = self.variable_map[code.IDENTIFIER().getText()][1]
        #     t2 = self.return_expression2ir(code.expression(), stream)
        #     type2 = self.variable_map[t2][0]
        #     stream[0] += (
        #         "store "
        #         + self.type2ir(type2)
        #         + " "
        #         + self.variable_map[t2][1]
        #         + ", "
        #         + self.type2ir(type)
        #         + " "
        #         + result
        #         + "\n"
        #     )
        #     self.variable_map[code.IDENTIFIER().getText()] = (type, result)
        #     return code.IDENTIFIER().getText()
        if isinstance(code, Mx_parserParser.LogicExpressionContext):
            # logicExpression
            t1 = self.return_expression2ir(code.expression(0), stream)
            t2 = self.return_expression2ir(code.expression(1), stream)

            if code.logicOperator().getText() == "&&":
                stream[0] += (
                    result
                    + " = and i1 "
                    + self.variable_map[t1][1]
                    + ", "
                    + self.variable_map[t2][1]
                    + "\n"
                )
            else:
                stream[0] += (
                    result
                    + " = or i1 "
                    + self.variable_map[t1][1]
                    + ", "
                    + self.variable_map[t2][1]
                    + "\n"
                )
            self.variable_map[code.getText()] = ("bool", result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.ConditionalExpressionContext):
            # conditionalExpression
            t1 = self.return_expression2ir(code.expression(0), stream)
            t2 = self.return_expression2ir(code.expression(1), stream)
            t3 = self.return_expression2ir(code.expression(2), stream)

            stream[0] += (
                "br i1 "
                + self.variable_map[t1][1]
                + ", label %.label"
                + str(self.label_cnt)
                + ", label %.label"
                + str(self.label_cnt + 1)
                + "\n\n"
            )
            stream[0] += ".label" + str(self.label_cnt) + ": \n"
            stream[0] += "br label %.label" + str(self.label_cnt + 2) + "\n\n"
            stream[0] += ".label" + str(self.label_cnt + 1) + ": \n"
            stream[0] += "br label %.label" + str(self.label_cnt + 2) + "\n\n"
            stream[0] += ".label" + str(self.label_cnt + 2) + ": \n"
            type = self.variable_map[t2][0]
            stream[0] += (
                result
                + " = phi "
                + self.type2ir(type)
                + " [ "
                + self.variable_map[t2][1]
                + ", %.label"
                + str(self.label_cnt)
                + " ], [ "
                + self.variable_map[t3][1]
                + ", %.label"
                + str(self.label_cnt + 1)
                + " ]\n"
            )
            self.variable_map[code.getText()] = (type, result)
            self.label_cnt += 3
            return code.getText()
        elif isinstance(code, Mx_parserParser.RelationalExpressionContext):
            # relationalExpression
            t1 = self.return_expression2ir(code.expression(0), stream)
            t2 = self.return_expression2ir(code.expression(1), stream)

            if self.variable_map[t1][0] == "int":
                if code.relationalOperator().getText() == "<":
                    stream[0] += (
                        result
                        + " = icmp slt i32 "
                        + self.variable_map[t1][1]
                        + ", "
                        + self.variable_map[t2][1]
                        + "\n"
                    )
                elif code.relationalOperator().getText() == ">":
                    stream[0] += (
                        result
                        + " = icmp sgt i32 "
                        + self.variable_map[t1][1]
                        + ", "
                        + self.variable_map[t2][1]
                        + "\n"
                    )
                elif code.relationalOperator().getText() == "<=":
                    stream[0] += (
                        result
                        + " = icmp sle i32 "
                        + self.variable_map[t1][1]
                        + ", "
                        + self.variable_map[t2][1]
                        + "\n"
                    )
                elif code.relationalOperator().getText() == ">=":
                    stream[0] += (
                        result
                        + " = icmp sge i32 "
                        + self.variable_map[t1][1]
                        + ", "
                        + self.variable_map[t2][1]
                        + "\n"
                    )
                elif code.relationalOperator().getText() == "==":
                    stream[0] += (
                        result
                        + " = icmp eq i32 "
                        + self.variable_map[t1][1]
                        + ", "
                        + self.variable_map[t2][1]
                        + "\n"
                    )
                else:
                    stream[0] += (
                        result
                        + " = icmp ne i32 "
                        + self.variable_map[t1][1]
                        + ", "
                        + self.variable_map[t2][1]
                        + "\n"
                    )
            else:
                if code.relationalOperator().getText() == "<":
                    stream[0] += (
                        result
                        + " = call i1 @string.less(ptr "
                        + self.variable_map[t1][1]
                        + ", ptr "
                        + self.variable_map[t2][1]
                        + ")\n"
                    )
                elif code.relationalOperator().getText() == ">":
                    stream[0] += (
                        result
                        + " = call i1 @string.greater(ptr "
                        + self.variable_map[t1][1]
                        + ", ptr "
                        + self.variable_map[t2][1]
                        + ")\n"
                    )
                elif code.relationalOperator().getText() == "<=":
                    stream[0] += (
                        result
                        + " = call i1 @string.lessOrEqual(ptr "
                        + self.variable_map[t1][1]
                        + ", ptr "
                        + self.variable_map[t2][1]
                        + ")\n"
                    )
                elif code.relationalOperator().getText() == ">=":
                    stream[0] += (
                        result
                        + " = call i1 @string.greaterOrEqual(ptr "
                        + self.variable_map[t1][1]
                        + ", ptr "
                        + self.variable_map[t2][1]
                        + ")\n"
                    )
                elif code.relationalOperator().getText() == "==":
                    stream[0] += (
                        result
                        + " = call i1 @string.equal(ptr "
                        + self.variable_map[t1][1]
                        + ", ptr "
                        + self.variable_map[t2][1]
                        + ")\n"
                    )
                else:
                    stream[0] += (
                        result
                        + " = call i1 @string.notEqual(ptr "
                        + self.variable_map[t1][1]
                        + ", ptr "
                        + self.variable_map[t2][1]
                        + ")\n"
                    )
            self.variable_map[code.getText()] = ("bool", result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.MuldivmodExpressionContext):
            # muldivmodExpression
            t1 = self.return_expression2ir(code.expression(0), stream)
            t2 = self.return_expression2ir(code.expression(1), stream)

            if code.MUL() != None:
                op = "mul"
            elif code.DIV() != None:
                op = "sdiv"
            else:
                op = "srem"
            stream[0] += (
                result
                + " = "
                + op
                + " i32 "
                + self.variable_map[t1][1]
                + " "
                + self.variable_map[t2][1]
                + "\n"
            )
            self.varaible_map[code.getText()] = ("int", result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.PlusminusExpressionContext):
            # plusminusExpression
            t1 = self.return_expression2ir(code.expression(0), stream)
            t2 = self.return_expression2ir(code.expression(1), stream)
            if self.variable_map[t1][0] == "string":
                stream[0] += (
                    result
                    + " = call ptr @string.concat(ptr "
                    + self.variable_map[t1][1]
                    + ", ptr "
                    + self.variable_map[t2][1]
                    + ")\n"
                )
                self.variable_map[code.getText()] = ("string", result)
                return code.getText()
            if code.PLUS() != None:
                op = "add"
            elif code.MINUS() != None:
                op = "sub"
            stream[0] += (
                result
                + " = "
                + op
                + " i32 "
                + self.variable_map[t1][1]
                + " "
                + self.variable_map[t2][1]
                + "\n"
            )
            self.variable_map[code.getText()] = ("int", result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.ShiftExpressionContext):
            # shiftExpression
            t1 = self.return_expression2ir(code.expression(0), stream)
            t2 = self.return_expression2ir(code.expression(1), stream)

            if code.LSHIFT() != None:
                op = "shl"
            elif code.RSHIFT() != None:
                op = "ashr"
            stream[0] += (
                result
                + " = "
                + op
                + " i32 "
                + self.variable_map[t1][1]
                + " "
                + self.variable_map[t2][1]
                + "\n"
            )
            self.varaible_map[code.getText()] = ("int", result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.AndxororExpressionContext):
            # andxororExpression
            t1 = self.return_expression2ir(code.expression(0), stream)
            t2 = self.return_expression2ir(code.expression(1), stream)

            if code.AND() != None:
                op = "and"
            elif code.XOR() != None:
                op = "xor"
            else:
                op = "or"
            stream += (
                result
                + " = "
                + op
                + " i32 "
                + self.variable_map[t1][1]
                + " "
                + self.variable_map[t2][1]
                + "\n"
            )
            self.varaible_map[code.getText()] = ("int", result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.PrefixIncrementExpressionContext):
            # prefixIncrementExpression

            t = self.return_expression2ir(code.expression(), stream)
            stream += result + " = add i32 " + self.variable_map[t][1] + " 1\n"
            self.varaible_map[t] = ("int", result)
            return t
        elif isinstance(code, Mx_parserParser.PostfixIncrementExpressionContext):
            # postfixIncrementExpression

            t = self.return_expression2ir(code.expression(), stream)
            variable_map_t = self.variable_map[t][1]
            stream += result + " = add i32 " + variable_map_t + " 1\n"
            self.varaible_map[t] = ("int", result)
            result = "%" + str(self.variable_cnt)
            self.variable_cnt += 1
            stream += result + " = add i32 " + variable_map_t + " 0\n"
            self.varaible_map[t + "_tmp"] = ("int", result)
            return t + "tmp"
        elif isinstance(code, Mx_parserParser.PrefixDecrementExpressionContext):
            # prefixDecrementExpression

            t = self.return_expression2ir(code.expression(), stream)
            stream += result + " = sub i32 " + self.variable_map[t][1] + " 1\n"
            self.varaible_map[t] = ("int", result)
            return t
        elif isinstance(code, Mx_parserParser.PostfixDecrementExpressionContext):
            # postfixDecrementExpression

            t = self.return_expression2ir(code.expression(), stream)
            variable_map_t = self.variable_map[t][1]
            stream += result + " = sub i32 " + variable_map_t + " 1\n"
            self.varaible_map[t] = ("int", result)
            result = "%" + str(self.variable_cnt)
            self.variable_cnt += 1
            stream += result + " = add i32 " + variable_map_t + " 0\n"
            self.varaible_map[t + "_tmp"] = ("int", result)
            return t + "tmp"
        elif isinstance(code, Mx_parserParser.LogicalNotExpressionContext):
            # logicalNotExpression

            t = self.return_expression2ir(code.expression(), stream)
            stream[0] += result + " = xor i1 " + self.variable_map[t][1] + " 1\n"
            self.variable_map[code.getText()] = ("bool", result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.BitwiseNotExpressionContext):
            # bitwiseNotExpression

            t = self.return_expression2ir(code.expression(), stream)
            stream[0] += result + " = xor i32 " + self.variable_map[t][1] + " -1\n"
            self.variable_map[code.getText()] = ("int", result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.UnaryMinusExpressionContext):
            # unaryMinusExpression

            t = self.return_expression2ir(code.expression(), stream)
            stream[0] += result + " = sub i32 0 " + self.variable_map[t][1] + "\n"
            self.variable_map[code.getText()] = ("int", result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.FunctionCallContext):
            # functionCall
            text = code.IDENTIFIER().getText()
            if text == "print":
                t = self.return_expression2ir(
                    code.expressionLists().expression(0), stream
                )
                stream[0] += (
                    result
                    + " = call void @print("
                    + self.type2ir("string")
                    + " "
                    + self.variable_map[t][1]
                    + ")\n"
                )
                self.variable_map[code.getText()] = result
                return code.getText()
            elif text == "println":
                t = self.return_expression2ir(
                    code.expressionLists().expression(0), stream
                )
                stream[0] += (
                    "call void @println("
                    + self.type2ir("string")
                    + " "
                    + self.variable_map[t][1]
                    + ")\n"
                )
                self.variable_map[code.getText()] = result
                return code.getText()
            elif text == "printInt":
                t = self.return_expression2ir(
                    code.expressionLists().expression(0), stream
                )
                stream[0] += (
                    "call void @printInt("
                    + self.type2ir("int")
                    + " "
                    + self.variable_map[t][1]
                    + ")\n"
                )
                self.variable_map[code.getText()] = result
                return code.getText()
            elif text == "printlnInt":
                t = self.return_expression2ir(
                    code.expressionLists().expression(0), stream
                )
                stream[0] += (
                    "call void @printlnInt("
                    + self.type2ir("int")
                    + " "
                    + self.variable_map[t][1]
                    + ")\n"
                )
                self.variable_map[code.getText()] = result
                return code.getText()
            elif text == "getString":
                stream[0] += (
                    result + " = call " + self.type2ir("string") + " @getString()\n"
                )
                self.variable_map[code.getText()] = result
                return code.getText()
            elif text == "getInt":
                stream[0] += result + " = call " + self.type2ir("int") + " @getInt()\n"
                self.variable_map[code.getText()] = result
                return code.getText()
            elif text == "toString":
                t = self.return_expression2ir(
                    code.expressionLists().expression(0), stream
                )
                stream[0] += (
                    result
                    + " = call "
                    + self.type2ir("string")
                    + " @toString("
                    + self.type2ir("int")
                    + " "
                    + self.variable_map[t][1]
                    + ")\n"
                )
                self.variable_map[code.getText()] = result
                return code.getText()
            type = self.function_definition_map[text]
            expressionlist = "()"
            if code.expressionLists() != None:
                expressionlist = self.expressionLists_decode(
                    code.expressionLists(), stream
                )
            stream[0] += (
                result
                + " = call "
                + self.type2ir(type)
                + " @"
                + text
                + expressionlist
                + "\n"
            )
            self.variable_map[code.getText()] = result
            return code.getText()
        elif isinstance(code, Mx_parserParser.MemberFunctionCallContext):
            # memberFunctionCall

            t = self.return_expression2ir(code.expression(), stream)
            type = self.function_definition_map[code.IDENTIFIER().getText()]
            expressionlist = "(ptr " + self.variable_map[t][1] + ")"
            name = self.variable_map[t][0] + code.IDENTIFIER().getText()
            if code.expressionLists() != None:
                expressionlist = self.expressionLists_decode(
                    code.expressionLists(), stream
                )
                expressionlist = (
                    "(ptr " + self.variable_map[t][1] + ", " + expressionlist[1:]
                )
            stream[0] += (
                result
                + " = call "
                + self.type2ir(type)
                + " @"
                + name
                + expressionlist
                + "\n"
            )
            self.variable_map[code.getText()] = result
            return code.getText()
        elif isinstance(code, Mx_parserParser.MemberMemberCallContext):
            # memberMemberCall
            t = self.return_expression2ir(code.expression(), stream)
            index = self.variable_map[t][0] + "." + code.IDENTIFIER().getText()
            stream[0] += (
                result
                + " = getelementptr %"
                + self.variable_map[t][0]
                + ", ptr "
                + self.type2ir(self.variable_map[t][1])
                + ", i32 0, i32 "
                + str(self.class_member_enum[index])
                + "\n"
            )
            self.variable_map[code.getText()] = result
            return code.getText()
        elif isinstance(code, Mx_parserParser.ConstantExpressionContext):
            # constantExpression
            constant = code.constant()
            if constant.INTEGER_CONSTANT() != None:
                # if print:
                #     print(constant.getText(), end=" ")
                value = constant.INTEGER_CONSTANT().getText()
                self.variable_map[value] = ("int", value)
                return value
            if constant.string_constant() != None:
                if constant.string_constant().STRING_CONTENT() != None:
                    string_ = constant.string_constant().getText()
                    string_ = string_.replace('\\"', "\\22")
                    string_ = string_.replace("\\n", "\\0A")
                    self.global_str += (
                        "@string."
                        + str(self.string_cnt)
                        + " = global [ "
                        + str(len(string_) - 1)
                        + " x i8] c"
                        + string_[:-1]
                        + '\\00"\n'
                    )
                    self.variable_map[code.getText()] = (
                        "string",
                        "@string." + str(self.string_cnt),
                    )
                    self.string_cnt += 1
                    return code.getText()
                else:
                    pass  # fstring 没写
                    # fstring = constant.string_constant().fstring()
                    # expressionlist = fstring.expression()
                    # middle = fstring.FSTRING_MIDDLE_PART()
                    # part1 = fstring.FSTRING_PART1().getText()[1:-1] + '\\00"'
                    # part2 = fstring.FSTRING_PART2().getText()[1:-1] + '\\00"'
                    # print(
                    #     "%"
                    #     + str(len(string_))
                    #     + "_PART1 = private constant ["
                    #     + str(len(part1))
                    #     + " x i8] c"
                    #     + part1
                    # )
                    # print(
                    #     "%"
                    #     + str(len(string_))
                    #     + "_PART2 = private constant ["
                    #     + str(len(part2))
                    #     + " x i8] c"
                    #     + part2
                    # )
                    # for i in range(len(expressionlist)):
                    #     expression = expressionlist[i]
                    #     if isinstance(
                    #         expression, Mx_parserParser.ConstantExpressionContext
                    #     ):
                    #         if expression.INTEGER_CONSTANT() != None:
                    #             print(
                    #                 result
                    #                 + "_"
                    #                 + str(i)
                    #                 + " = private constant ["
                    #                 + str(len(string_))
                    #             )

                    # for i in range(len(expressionlist)):
            # if constant.array_constant() != None:
            #     expressionlist = constant.array_constant().expression()
            #     if len(expressionlist) == 0:
            #         return "null"
            #     type1 = self.return_expressiontype(expressionlist[0])
            #     for i in range(1, len(expressionlist)):
            #         type2 = self.return_expressiontype(expressionlist[i])

            #     return type1.split("[")[0] + "[" + str(int(type1[-2]) + 1) + "]"

            # 这个先不写
            if constant.getText() == "null":
                self.variable_map["null"] = ("null", "null")
                return "null"
            if constant.getText() == "True":
                self.variable_map["1"] = ("bool", "1")
                return "1"
            self.variable_map["0"] = ("bool", "0")
            return "0"
        elif isinstance(code, Mx_parserParser.NewVariableExpressionContext):
            # newVariableExpression
            stream[0] += (
                result
                + " = call ptr @malloc "
                + str(self.class_size_map[code.type_().getText()])
                + "\n"
            )  # 只有自定义类型
            self.variable_map[code.getText()] = (code.type_().getText(), result)
            stream[0] += (
                "call void @" + code.type_().getText() + "_new(ptr " + result + ")"
            )
            return code.getText()
        elif isinstance(code, Mx_parserParser.NewArrayExpressionContext):
            # newArrayExpression
            cnt = 0
            for i in code.getText():
                if i == "[":
                    cnt += 1
            expressionlist = code.expression()
            list = []
            for i in expressionlist:
                list.append(self.return_expression2ir(i, stream))
            stream[0] += (
                result + " = call ptr @__newIntArray( i32" + str(len(list)) + ")\n"
            )
            tmp = result
            for i in range(len(list)):
                result = str(self.variable_cnt)
                self.variable_cnt += 1
                stream[0] += (
                    result
                    + " = getelementptr i32, ptr "
                    + tmp
                    + ", i32 "
                    + str(len(list) - i - 1)
                    + "\n"
                )
                stream[0] += (
                    "store i32 "
                    + self.variable_map[list[i]][1]
                    + ", ptr "
                    + result
                    + "\n"
                )
            type_ = "class_" + code.type_() + str(cnt)
            stream[0] += (
                "call void @"
                + type_
                + "list_init(ptr "
                + tmp
                + ", i32 "
                + str(len(list))
                + ", ptr "
                + result
                + ")\n"
            )
            self.variable_map[code.getText()] = (type_, tmp)
            return code.getText()
        elif isinstance(code, Mx_parserParser.VariableExpressionContext):
            # variableExpression
            identifier = code.IDENTIFIER().getText()
            value = self.variable_map[identifier][1]
            if value[0] == "@":
                stream += (
                    result
                    + " = load "
                    + self.type2ir(self.variable_map[identifier][0])
                    + ", ptr "
                    + value
                    + "\n"
                )
                self.variable_map[result] = (self.variable_map[identifier][0], result)
                return result
            return value
        elif isinstance(code, Mx_parserParser.ArrayExpressionContext):
            # arrayExpression
            t1 = self.return_expression2ir(code.expression(0), stream)
            t2 = self.return_expression2ir(code.expression(1), stream)
            stream[0] += (
                result
                + " = getelementptr %"
                + self.variable_map[t1][0]
                + ", ptr "
                + self.type2ir(self.variable_map[t1][1])
                + ", i32 0, i32 1\n"
            )
            value = result
            result = "%" + str(self.variable_cnt)
            self.variable_cnt += 1
            stream[0] += (
                result
                + " = getelementptr "
                + self.type2ir(self.variable_map[identifier][0][:-2])
                + ", ptr "
                + value
                + ", "
                + self.type2ir(self.variable_map[t2][0])
                + " "
                + self.variable_map[t2][1]
                + "\n"
            )
            self.variable_map[code.getText()] = result
            return code.getText()
        elif isinstance(code, Mx_parserParser.ParenthesesExpressionContext):
            # parenthesesExpression
            return self.return_expression2ir(code.expression(), stream)
        else:
            name = code.getText()
            # 如果没有匹配的规则，返回未知类型
            return "unknown"

    def type2ir(self, str) -> str:
        if str == "int":
            return "i32"
        elif str == "bool":
            return "i1"
        elif str == "void":
            return "void"
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
                    "declare void @" + child.IDENTIFIER().getText() + "_new(ptr)\n"
                )
                self.function_definition_map[child.IDENTIFIER().getText() + "_new"] = (
                    "void"
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
                        self.function_definition_map[
                            child.IDENTIFIER().getText() + name
                        ] = self.type2ir(type)
                        parameterlist = self.parameterList_decode2name(
                            ii.functionDefinition().parameterList()
                        )
                        for i in parameterlist:
                            function_definition_str += ", " + self.type2ir(i[0])
                        function_definition_str += ")\n"
                self.class_size_map[child.IDENTIFIER().getText()] = cnt * 4

            elif isinstance(child, Mx_parserParser.FunctionDefinitionContext):
                type = child.returnType().getText()
                name = child.IDENTIFIER().getText()
                function_definition_str += (
                    "declare "
                    + self.type2ir(type)
                    + " @"
                    + child.IDENTIFIER().getText()
                )
                self.function_definition_map[child.IDENTIFIER().getText()] = (
                    self.type2ir(type)
                )
                function_definition_str += self.parameterList_decode2type(
                    child.parameterList()
                )
                function_definition_str += "\n"
            elif isinstance(child, Mx_parserParser.VariableDeclarationContext):
                if child.type_() != None:
                    type = self.type2ir(child.type_().getText())
                else:
                    type = "ptr"
                default = "0"
                if type == "ptr":
                    default = "null"
                    if child.type().getText() == "string":
                        default = "@.string.0"
                for i in child.variableDeclarationparts():
                    name = i.IDENTIFIER().getText()
                    variable_definition_str += "@" + name + " = global " + type + " "
                    self.variable_map[name] = (type, "@" + name)
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
                            elif constant.string_constant() != None:
                                init = 0
                                variable_definition_str += default
                        if init:
                            variable_definition_str += default
                            init_func = (
                                "define void @init"
                                + str(self.init_cnt)
                                + " (){\n  entry:\n"
                            )
                            exp = self.return_expression2ir(
                                i.expression(), [init_func]
                            )[1]
                            init_func += (
                                "    store "
                                + type
                                + " "
                                + exp
                                + ", ptr @"
                                + name
                                + "\n"
                            )
                            init_func += "    ret void\n}\n"
                            self.function_definition_list.append(init_func)
                            self.init_cnt += 1
                    variable_definition_str += "\n"
        self.global_str += class_definition_str
        self.global_str += function_definition_str
        self.global_str += variable_definition_str

    def expressionLists_decode(
        self, code: Mx_parserParser.ExpressionListsContext, stream
    ) -> str:  # (i1 %1, i32 %2)
        expressionlist = code.expression()
        ans = "("
        for i in range(len(expressionlist)):
            t = self.return_expression2ir(expressionlist[i], stream)
            ans += self.variable_map[t][0] + " " + self.variable_map[t][1]
            if i < len(expressionlist) - 1:
                ans += ", "
        ans += ")"
        return ans

    def parameterList_decode2type(
        self, code: Mx_parserParser.ParameterListContext
    ) -> str:  # (i1, i32)
        if code is None:
            return "()"
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
    ) -> list:  # [(type, name)] [(string, x)]
        if code is None:
            return []
        parameterlist = code.parameter()
        if parameterlist == None:
            return []
        ans = []
        for i in range(len(parameterlist)):
            parameter = parameterlist[i]
            if parameter.type() != None:
                ans.append(
                    (
                        parameter.type().getText(),
                        parameter.IDENTIFIER().getText(),
                    )
                )
            else:
                ans.append(
                    (
                        parameter.arrayType().getText(),
                        parameter.IDENTIFIER().getText(),
                    )
                )
        return ans

    def enterFunctionDefinition(self, ctx: Mx_parserParser.FunctionDefinitionContext):
        func_str = (
            "define "
            + self.type2ir(ctx.returnType().getText())
            + " @"
            + ctx.IDENTIFIER().getText()
        )
        parameterlist = self.parameterList_decode2name(ctx.parameterList())
        parameterstr = "("
        for i in range(len(parameterlist)):
            self.variable_map[parameterlist[i][1]] = (
                self.type2ir(parameterlist[i][0]),
                "%" + parameterlist[i][1],
            )
            parameterstr += parameterlist[i][0] + " %" + parameterlist[i][1]
            if i < len(parameterlist) - 1:
                parameterstr += ", "
        parameterstr += ")"
        func_str += parameterstr + " {\n"
        statement_list = ctx.functionBody().statement()
        for i in range(len(statement_list)):
            self.statement_decode2ir(statement_list[i], [func_str])
        func_str += "\n}\n"
        self.function_definition_list.append(func_str)

    def statement_decode2ir(self, code: Mx_parserParser.StatementContext, stream):
        if isinstance(code, Mx_parserParser.EmptyStatementContext):
            return
        elif isinstance(code, Mx_parserParser.ExpressionStatementContext):
            self.return_expression2ir(code.expression(), stream)
            return
        elif isinstance(code, Mx_parserParser.IfStatementContext):
            t = self.return_expression2ir(code.expression(), stream)
            stream[0] += (
                "br i1 "
                + t
                + ", label %.label"
                + str(self.label_cnt)
                + ", label %.label"
                + str(self.label_cnt + 1)
                + "\n"
            )
            stream[0] += ".label" + str(self.label_cnt) + ":\n"
            self.statement_decode2ir(code.statement(), stream)
            stream[0] += "br label %.label" + str(self.label_cnt + 2) + "\n"
            stream[0] += ".label" + str(self.label_cnt + 1) + ":\n"
            if code.elsestatement() is not None:
                self.statement_decode2ir(code.elsestatement().statement(), stream)
            stream[0] += "br label %.label" + str(self.label_cnt + 2) + "\n"
            stream[0] += ".label" + str(self.label_cnt + 2) + ":\n"
            self.label_cnt += 3
            return
        elif isinstance(code, Mx_parserParser.WhileStatementContext):
            stream[0] += "br label %.label" + str(self.label_cnt) + "\n"
            stream[0] += ".label" + str(self.label_cnt) + ":\n"
            t = self.return_expression2ir(code.expression(), stream)
            stream[0] += (
                "br i1 "
                + t
                + ", label %.label"
                + str(self.label_cnt + 1)
                + ", label %.label"
                + str(self.label_cnt + 2)
                + "\n"
            )
            stream[0] += ".label" + str(self.label_cnt + 1) + ":\n"
            self.loop_stack.append(self.label_cnt)
            self.statement_decode2ir(code.statement(), stream)
            self.loop_stack.pop()
            stream[0] += "br label %.label" + +str(self.label_cnt) + "\n"
            stream[0] += ".label" + str(self.label_cnt + 2) + ":\n"
            self.label_cnt += 3
            return
        elif isinstance(code, Mx_parserParser.ForStatementContext):
            if code.forControl().expression1() != None:
                self.statement_decode2ir(
                    code.forControl().expression1().expression(), stream
                )
            stream[0] += "br label %.label" + str(self.label_cnt + 3) + "\n"
            stream[0] += ".label" + str(self.label_cnt + 3) + ":\n"
            if code.forControl().expression2() != None:
                self.statement_decode2ir(
                    code.forControl().expression2().expression(), stream
                )
            stream[0] += (
                "br i1 1, label %.label"
                + str(self.label_cnt + 1)
                + ", label %.label"
                + str(self.label_cnt + 2)
                + "\n"
            )
            stream[0] += ".label" + str(self.label_cnt + 1) + ":\n"
            self.loop_stack.append(self.label_cnt)
            self.statement_decode2ir(code.statement(), stream)
            self.loop_stack.pop()
            stream[0] += "br label %.label" + str(self.label_cnt) + "\n"
            stream[0] += ".label" + str(self.label_cnt) + ":\n"
            if code.forControl().expression3() != None:
                self.statement_decode2ir(
                    code.forControl().expression3().expression(), stream
                )
            stream[0] += "br label %.label" + str(self.label_cnt) + "\n"
            stream[0] += ".label" + str(self.label_cnt + 2) + ":\n"
            self.label_cnt += 3
            return
        elif isinstance(code, Mx_parserParser.ReturnStatementContext):
            if code.expression() != None:
                t = self.return_expression2ir(code.expression(), stream)
                stream[0] += (
                    "ret "
                    + self.type2ir(self.variable_map[t][0])
                    + " "
                    + self.variable_map[t][1]
                    + "\n"
                )
            else:
                stream[0] += "ret void\n"
            return
        elif isinstance(code, Mx_parserParser.BlockContext):
            for i in range(len(code.statement())):
                self.statement_decode2ir(code.statement(i), stream)
        elif isinstance(code, Mx_parserParser.BreakStatementContext):
            stream[0] += "br label %.label" + str(self.loop_stack[-1] + 2) + "\n"
        elif isinstance(code, Mx_parserParser.ContinueStatementContext):
            stream[0] += "br label %.label" + str(self.loop_stack[-1]) + "\n"
        elif isinstance(code, Mx_parserParser.AssignmentStatementContext):
            code = code.assignment()
            t1 = self.return_expression2ir(code.expression(0), stream)
            t2 = self.return_expression2ir(code.expression(1), stream)
            if self.variable_map[t1][1][0] == "@":
                stream[0] += (
                    "store "
                    + self.type2ir(self.variable_map[t1][0])
                    + " "
                    + self.variable_map[t2][1]
                    + ", "
                    + "ptr "
                    + self.variable_map[t1][1]
                    + "\n"
                )
            else:
                self.variable_map[t1] = self.variable_map[t2]
        elif isinstance(code, Mx_parserParser.PrivatevariableDeclarationContext):
            variabledeclare = code.variableDeclaration()
            if variabledeclare.type_() != None:
                type_ = variabledeclare.type_()
                if type_ == "int" or type_ == "bool":
                    default = "0"
                elif type_ == "string":
                    default = "@.string.0"
                else:
                    default = "null"
                for i in variabledeclare.variableDeclarationparts():
                    if i.expression() != None:
                        t = self.return_expression2ir(i.expression(), stream)
                        self.variable_map[i.IDENTIFIER()] = self.variable_map[t]
                    else:
                        self.variable_map[i.IDENTIFIER()] = [type_, default]

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

    print(listener.global_str)
    for i in listener.function_definition_list:
        print(i)


if __name__ == "__main__":
    code = sys.stdin.read()
    main(code)
