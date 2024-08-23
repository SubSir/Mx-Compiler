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
class MyListener2(Mx_parserListener):
    variable_cnt = 0
    enter_class = ""
    enter_function = ""
    init_cnt = 0
    label_cnt = 0
    string_cnt = 1
    global_str = ""
    label_str = ""
    class_member_enum = {}  # A.x -> 0
    class_size_map = {}  # class_name -> size
    function_definition_list = []  # [str]
    variable_map = {}  # name -> (type, value) e.g. (int, 0)
    write_map = {}  # name -> ptr
    function_definition_map = {}  # name -> returnType
    loop_stack = []
    branch_map = {}
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

    def copy(self, other: "MyListener2"):
        self.variable_cnt = other.variable_cnt
        self.enter_class = other.enter_class
        self.enter_function = other.enter_function
        self.init_cnt = other.init_cnt
        self.label_cnt = other.label_cnt
        self.string_cnt = other.string_cnt
        self.global_str = other.global_str
        self.label_str = other.label_str
        self.class_member_enum = copy.deepcopy(other.class_member_enum)
        self.class_size_map = copy.deepcopy(other.class_size_map)
        self.function_definition_list = copy.deepcopy(other.function_definition_list)
        self.variable_map = copy.deepcopy(other.variable_map)
        self.write_map = copy.deepcopy(other.write_map)
        self.function_definition_map = copy.deepcopy(other.function_definition_map)
        self.loop_stack = copy.deepcopy(other.loop_stack)
        self.branch_map = copy.deepcopy(other.branch_map)
        return

    # def visitTerminal(self, node: TerminalNodeImpl):
    #     # 当访问到终端节点时调用此方法
    #     print(node.getText(), end="")
    def isPrivate(self, code: str) -> bool:
        if code[:6] == "class_" and (code[-1]).isdigit():
            return True
        return False

    def transform_string(self, str: str):
        string_ = str[1:-1]
        _string = string_.replace("\\", "")
        len_ = len(_string)
        i = 0
        while i < len(string_):
            if string_[i : i + 2] == "\\\\":
                i += 1
                len_ += 1
            i += 1
        string_ = string_.replace('\\"', "\\22")
        string_ = string_.replace("\\n", "\\0A")
        return '"' + string_ + '\\00"', len_ + 1

    def array_constantdecode(self, code: Mx_parserParser.Array_constantContext, stream):
        result = "%var" + str(self.variable_cnt)
        self.variable_cnt += 1
        expressionlist = [
            self.return_expression2ir(i, stream) for i in code.expression()
        ]
        dim = 0
        for i in expressionlist:
            if self.isPrivate(self.variable_map[i][0]):
                dim = max(dim, int(self.variable_map[i][0]) + 1)
                type_ = self.variable_map[i][0][6:-1]
            else:
                dim = max(dim, 1)
                type_ = self.variable_map[i][0]
        type_ = self.arraytype_transform(type_ + dim * "[]")
        stream[0] += (
            result
            + " = call ptr @malloc(i32 "
            + str(self.class_size_map[type_])
            + ")\n\t\t"
        )
        stream[0] += (
            "call void @"
            + type_
            + "init(ptr "
            + result
            + ", i32 "
            + str(len(expressionlist))
            + ")\n\t\t"
        )
        self.variable_map[code.getText()] = (type_, result)
        self.write_map[code.getText()] = ""
        tmp_ = result
        if type_[-1] == "1":
                _type = self.arraytype_reform(type_)[:-2]
        else:
            _type = type_[:-1] + str(int(type_[-1]) - 1)
        for i in range(len(expressionlist)):
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            stream[0] += (
                result
                + " = getelementptr %"
                + type_
                + ", ptr "
                + tmp_
                + ", i32 0, i32 1\n\t\t"
            )
            _tmp = result
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            stream[0] += result + " = load ptr, ptr " + _tmp + "\n\t\t"
            value = result
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            # if self.isPrivate(self.enter_class):
            #     type_ = self.variable_map[t1][0][:-2]
            # else:
            stream[0] += (
                result
                + " = getelementptr "
                + self.type2ir(_type)
                + ", ptr "
                + value
                + ", i32 "
                + str(i)
                + "\n\t\t"
            )
            ptr = result
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            stream[0] += (
                "store "
                + self.type2ir(_type)
                + " "
                + self.variable_map[expressionlist[i]][1]
                + ", ptr "
                + ptr
                + "\n\t\t"
            )
        return code.getText()

    def return_expression2ir(
        self, code, stream
    ) -> str:  # stream[0] 为流, 返回variable_map的index
        result = "%var" + str(self.variable_cnt)
        self.variable_cnt += 1
        # stream[0] += "\n\t\t; expression: " + code.getText() + "\n\t\t\n\t\t"
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
        #         + "\n\t\t"
        #     )
        #     self.variable_map[code.IDENTIFIER().getText()] = (type, result)
        #     return code.IDENTIFIER().getText()
        if isinstance(code, Mx_parserParser.LogicANDExpressionContext):
            # logicExpression
            label_cnt = self.label_cnt
            self.label_cnt += 3
            t = self.return_expression2ir(code.expression(0), stream)
            stream[0] += (
                "br i1 "
                + self.variable_map[t][1]
                + ", label %.label"
                + str(label_cnt)
                + ", label %.label"
                + str(label_cnt + 1)
                + "\n\t"
            )
            tmp_map = self.variable_map.copy()
            stream[0] += "\n.label" + str(label_cnt) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt)
            t1 = self.return_expression2ir(code.expression(1), stream)
            type1 = self.variable_map[t1][0]
            name1 = self.variable_map[t1][1]
            stream[0] += "br label %.label" + str(label_cnt + 2) + "\n\t"
            tmp_label1 = self.label_str
            change_map = {}
            for i in tmp_map:
                if (i in self.write_map and self.write_map[i] == "") and tmp_map[i][
                    1
                ] != self.variable_map[i][1]:
                    change_map[i] = (self.variable_map[i][1], tmp_map[i][1])
            stream[0] += "\n.label" + str(label_cnt + 1) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 1)
            stream[0] += "br label %.label" + str(label_cnt + 2) + "\n\t"
            tmp_label2 = self.label_str
            stream[0] += "\n.label" + str(label_cnt + 2) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 2)
            for i in change_map:
                result = "%var" + str(self.variable_cnt)
                self.variable_cnt += 1
                stream[0] += (
                    result
                    + " = phi "
                    + self.type2ir(self.variable_map[i][0])
                    + "["
                    + change_map[i][0]
                    + ", %"
                    + tmp_label1
                    + "], ["
                    + change_map[i][1]
                    + ", %"
                    + tmp_label2
                    + "]\n\t\t"
                )
                self.variable_map[i] = (self.variable_map[i][0], result)
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            stream[0] += (
                result
                + " = phi "
                + self.type2ir(type1)
                + "["
                + name1
                + ", %"
                + tmp_label1
                + "], [0, %"
                + tmp_label2
                + "]\n\t\t"
            )
            self.variable_map[code.getText()] = (type1, result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.LogicORExpressionContext):
            # LogicExpression
            label_cnt = self.label_cnt
            self.label_cnt += 3
            t = self.return_expression2ir(code.expression(0), stream)
            stream[0] += (
                "br i1 "
                + self.variable_map[t][1]
                + ", label %.label"
                + str(label_cnt)
                + ", label %.label"
                + str(label_cnt + 1)
                + "\n\t"
            )
            tmp_map = self.variable_map.copy()
            stream[0] += "\n.label" + str(label_cnt) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt)
            type1 = "bool"
            name1 = "1"
            stream[0] += "br label %.label" + str(label_cnt + 2) + "\n\t"
            tmp_label1 = self.label_str
            change_map = {}
            stream[0] += "\n.label" + str(label_cnt + 1) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 1)
            t2 = self.return_expression2ir(code.expression(1), stream)
            name2 = self.variable_map[t2][1]
            for i in tmp_map:
                if (i in self.write_map and self.write_map[i] == "") and tmp_map[i][
                    1
                ] != self.variable_map[i][1]:
                    if i in change_map:
                        change_map[i] = (change_map[i][0], self.variable_map[i][1])
                    else:
                        change_map[i] = (tmp_map[i][1], self.variable_map[i][1])
            stream[0] += "br label %.label" + str(label_cnt + 2) + "\n\t"
            tmp_label2 = self.label_str
            stream[0] += "\n.label" + str(label_cnt + 2) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 2)
            for i in change_map:
                result = "%var" + str(self.variable_cnt)
                self.variable_cnt += 1
                stream[0] += (
                    result
                    + " = phi "
                    + self.type2ir(self.variable_map[i][0])
                    + "["
                    + change_map[i][0]
                    + ", %"
                    + tmp_label1
                    + "], ["
                    + change_map[i][1]
                    + ", %"
                    + tmp_label2
                    + "]\n\t\t"
                )
                self.variable_map[i] = (self.variable_map[i][0], result)
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            stream[0] += (
                result
                + " = phi "
                + self.type2ir(type1)
                + "["
                + name1
                + ", %"
                + tmp_label1
                + "], ["
                + name2
                + ", %"
                + tmp_label2
                + "]\n\t\t"
            )
            self.variable_map[code.getText()] = (type1, result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.ConditionalExpressionContext):
            # conditionalExpression
            label_cnt = self.label_cnt
            self.label_cnt += 3
            t = self.return_expression2ir(code.expression(0), stream)
            stream[0] += (
                "br i1 "
                + self.variable_map[t][1]
                + ", label %.label"
                + str(label_cnt)
                + ", label %.label"
                + str(label_cnt + 1)
                + "\n\t"
            )
            tmp_map = self.variable_map.copy()
            stream[0] += "\n.label" + str(label_cnt) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt)
            t1 = self.return_expression2ir(code.expression(1), stream)
            type1 = self.variable_map[t1][0]
            name1 = self.variable_map[t1][1]
            stream[0] += "br label %.label" + str(label_cnt + 2) + "\n\t"
            tmp_label1 = self.label_str
            change_map = {}
            for i in tmp_map:
                if (i in self.write_map and self.write_map[i] == "") and tmp_map[i][
                    1
                ] != self.variable_map[i][1]:
                    change_map[i] = (self.variable_map[i][1], tmp_map[i][1])
            stream[0] += "\n.label" + str(label_cnt + 1) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 1)
            self.variable_map = tmp_map.copy()
            t2 = self.return_expression2ir(code.expression(2), stream)
            name2 = self.variable_map[t2][1]
            for i in tmp_map:
                if (i in self.write_map and self.write_map[i] == "") and tmp_map[i][
                    1
                ] != self.variable_map[i][1]:
                    if i in change_map:
                        change_map[i] = (change_map[i][0], self.variable_map[i][1])
                    else:
                        change_map[i] = (tmp_map[i][1], self.variable_map[i][1])
            stream[0] += "br label %.label" + str(label_cnt + 2) + "\n\t"
            tmp_label2 = self.label_str
            stream[0] += "\n.label" + str(label_cnt + 2) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 2)
            for i in change_map:
                result = "%var" + str(self.variable_cnt)
                self.variable_cnt += 1
                stream[0] += (
                    result
                    + " = phi "
                    + self.type2ir(self.variable_map[i][0])
                    + "["
                    + change_map[i][0]
                    + ", %"
                    + tmp_label1
                    + "], ["
                    + change_map[i][1]
                    + ", %"
                    + tmp_label2
                    + "]\n\t\t"
                )
                self.variable_map[i] = (self.variable_map[i][0], result)
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            if type1 != "void":
                stream[0] += (
                    result
                    + " = phi "
                    + self.type2ir(type1)
                    + "["
                    + name1
                    + ", %"
                    + tmp_label1
                    + "], ["
                    + name2
                    + ", %"
                    + tmp_label2
                    + "]\n\t\t"
                )
            self.variable_map[code.getText()] = (type1, result)
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
                        + "\n\t\t"
                    )
                elif code.relationalOperator().getText() == ">":
                    stream[0] += (
                        result
                        + " = icmp sgt i32 "
                        + self.variable_map[t1][1]
                        + ", "
                        + self.variable_map[t2][1]
                        + "\n\t\t"
                    )
                elif code.relationalOperator().getText() == "<=":
                    stream[0] += (
                        result
                        + " = icmp sle i32 "
                        + self.variable_map[t1][1]
                        + ", "
                        + self.variable_map[t2][1]
                        + "\n\t\t"
                    )
                elif code.relationalOperator().getText() == ">=":
                    stream[0] += (
                        result
                        + " = icmp sge i32 "
                        + self.variable_map[t1][1]
                        + ", "
                        + self.variable_map[t2][1]
                        + "\n\t\t"
                    )
                elif code.relationalOperator().getText() == "==":
                    stream[0] += (
                        result
                        + " = icmp eq i32 "
                        + self.variable_map[t1][1]
                        + ", "
                        + self.variable_map[t2][1]
                        + "\n\t\t"
                    )
                else:
                    stream[0] += (
                        result
                        + " = icmp ne i32 "
                        + self.variable_map[t1][1]
                        + ", "
                        + self.variable_map[t2][1]
                        + "\n\t\t"
                    )
            else:
                if code.relationalOperator().getText() == "<":
                    stream[0] += (
                        result
                        + " = call i1 @string.less(ptr "
                        + self.variable_map[t1][1]
                        + ", ptr "
                        + self.variable_map[t2][1]
                        + ")\n\t\t"
                    )
                elif code.relationalOperator().getText() == ">":
                    stream[0] += (
                        result
                        + " = call i1 @string.greater(ptr "
                        + self.variable_map[t1][1]
                        + ", ptr "
                        + self.variable_map[t2][1]
                        + ")\n\t\t"
                    )
                elif code.relationalOperator().getText() == "<=":
                    stream[0] += (
                        result
                        + " = call i1 @string.lessOrEqual(ptr "
                        + self.variable_map[t1][1]
                        + ", ptr "
                        + self.variable_map[t2][1]
                        + ")\n\t\t"
                    )
                elif code.relationalOperator().getText() == ">=":
                    stream[0] += (
                        result
                        + " = call i1 @string.greaterOrEqual(ptr "
                        + self.variable_map[t1][1]
                        + ", ptr "
                        + self.variable_map[t2][1]
                        + ")\n\t\t"
                    )
                elif code.relationalOperator().getText() == "==":
                    if (
                        self.variable_map[t1][1] == "null"
                        or self.variable_map[t2][1] == "null"
                    ):
                        stream[0] += (
                            result
                            + " = icmp eq ptr "
                            + self.variable_map[t1][1]
                            + ", "
                            + self.variable_map[t2][1]
                            + "\n\t\t"
                        )
                    else:
                        stream[0] += (
                            result
                            + " = call i1 @string.equal(ptr "
                            + self.variable_map[t1][1]
                            + ", ptr "
                            + self.variable_map[t2][1]
                            + ")\n\t\t"
                        )
                else:
                    if (
                        self.variable_map[t1][1] == "null"
                        or self.variable_map[t2][1] == "null"
                    ):
                        stream[0] += (
                            result
                            + " = icmp ne ptr "
                            + self.variable_map[t1][1]
                            + ", "
                            + self.variable_map[t2][1]
                            + "\n\t\t"
                        )
                    else:
                        stream[0] += (
                            result
                            + " = call i1 @string.notEqual(ptr "
                            + self.variable_map[t1][1]
                            + ", ptr "
                            + self.variable_map[t2][1]
                            + ")\n\t\t"
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
                + ", "
                + self.variable_map[t2][1]
                + "\n\t\t"
            )
            self.variable_map[code.getText()] = ("int", result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.PlusminusExpressionContext):
            # plusminusExpression
            t1 = self.return_expression2ir(code.expression(0), stream)
            t2 = self.return_expression2ir(code.expression(1), stream)
            if self.variable_map[t1][0] == "string":
                stream[0] += (
                    result
                    + " = call ptr @string.add(ptr "
                    + self.variable_map[t1][1]
                    + ", ptr "
                    + self.variable_map[t2][1]
                    + ")\n\t\t"
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
                + ", "
                + self.variable_map[t2][1]
                + "\n\t\t"
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
                + ", "
                + self.variable_map[t2][1]
                + "\n\t\t"
            )
            self.variable_map[code.getText()] = ("int", result)
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
            stream[0] += (
                result
                + " = "
                + op
                + " i32 "
                + self.variable_map[t1][1]
                + ", "
                + self.variable_map[t2][1]
                + "\n\t\t"
            )
            self.variable_map[code.getText()] = ("int", result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.PrefixIncrementExpressionContext):
            # prefixIncrementExpression
            t = self.return_expression2ir(code.expression(), stream)
            stream[0] += result + " = add i32 " + self.variable_map[t][1] + ", 1\n\t\t"
            if self.write_map[code.expression().getText()] != "":
                stream[0] += (
                    "store "
                    + self.type2ir(self.variable_map[code.expression().getText()][0])
                    + " "
                    + result
                    + ", "
                    + "ptr "
                    + self.write_map[code.expression().getText()]
                    + "\n\t\t"
                )
            self.variable_map[t] = ("int", result)
            return t
        elif isinstance(code, Mx_parserParser.PostfixIncrementExpressionContext):
            # postfixIncrementExpression
            t = self.return_expression2ir(code.expression(), stream)
            variable_map_t = self.variable_map[t][1]
            stream[0] += result + " = add i32 " + variable_map_t + ", 1\n\t\t"
            if self.write_map[code.expression().getText()] != "":
                stream[0] += (
                    "store "
                    + self.type2ir(self.variable_map[code.expression().getText()][0])
                    + " "
                    + result
                    + ", "
                    + "ptr "
                    + self.write_map[code.expression().getText()]
                    + "\n\t\t"
                )
            self.variable_map[t] = ("int", result)
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            stream[0] += result + " = add i32 " + variable_map_t + ", 0\n\t\t"
            self.variable_map[t + "_tmp"] = ("int", result)
            return t + "_tmp"
        elif isinstance(code, Mx_parserParser.PrefixDecrementExpressionContext):
            # prefixDecrementExpression
            t = self.return_expression2ir(code.expression(), stream)
            stream[0] += result + " = sub i32 " + self.variable_map[t][1] + ", 1\n\t\t"
            if self.write_map[code.expression().getText()] != "":
                stream[0] += (
                    "store "
                    + self.type2ir(self.variable_map[code.expression().getText()][0])
                    + " "
                    + result
                    + ", "
                    + "ptr "
                    + self.write_map[code.expression().getText()]
                    + "\n\t\t"
                )
            self.variable_map[t] = ("int", result)
            return t
        elif isinstance(code, Mx_parserParser.PostfixDecrementExpressionContext):
            # postfixDecrementExpression
            t = self.return_expression2ir(code.expression(), stream)
            variable_map_t = self.variable_map[t][1]
            stream[0] += result + " = sub i32 " + variable_map_t + ", 1\n\t\t"
            if self.write_map[code.expression().getText()] != "":
                stream[0] += (
                    "store "
                    + self.type2ir(self.variable_map[code.expression().getText()][0])
                    + " "
                    + result
                    + ", "
                    + "ptr "
                    + self.write_map[code.expression().getText()]
                    + "\n\t\t"
                )
            self.variable_map[t] = ("int", result)
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            stream[0] += result + " = add i32 " + variable_map_t + ", 0\n\t\t"
            self.variable_map[t + "_tmp"] = ("int", result)
            return t + "_tmp"
        elif isinstance(code, Mx_parserParser.LogicalNotExpressionContext):
            # logicalNotExpression
            t = self.return_expression2ir(code.expression(), stream)
            stream[0] += result + " = xor i1 " + self.variable_map[t][1] + ", 1\n\t\t"
            self.variable_map[code.getText()] = ("bool", result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.BitwiseNotExpressionContext):
            # bitwiseNotExpression
            t = self.return_expression2ir(code.expression(), stream)
            stream[0] += result + " = xor i32 " + self.variable_map[t][1] + ", -1\n\t\t"
            self.variable_map[code.getText()] = ("int", result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.UnaryMinusExpressionContext):
            # unaryMinusExpression
            t = self.return_expression2ir(code.expression(), stream)
            stream[0] += result + " = sub i32 0, " + self.variable_map[t][1] + "\n\t\t"
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
                    "call void @print("
                    + self.type2ir("string")
                    + " "
                    + self.variable_map[t][1]
                    + ")\n\t\t"
                )
                self.variable_map[code.getText()] = ("void", result)
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
                    + ")\n\t\t"
                )
                self.variable_map[code.getText()] = ("void", result)
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
                    + ")\n\t\t"
                )
                self.variable_map[code.getText()] = ("void", result)
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
                    + ")\n\t\t"
                )
                self.variable_map[code.getText()] = ("void", result)
                return code.getText()
            elif text == "getString":
                stream[0] += (
                    result + " = call " + self.type2ir("string") + " @getString()\n\t\t"
                )
                self.variable_map[code.getText()] = ("string", result)
                return code.getText()
            elif text == "getInt":
                stream[0] += (
                    result + " = call " + self.type2ir("int") + " @getInt()\n\t\t"
                )
                self.variable_map[code.getText()] = ("int", result)
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
                    + ")\n\t\t"
                )
                self.variable_map[code.getText()] = ("string", result)
                return code.getText()
            ptr = 0
            if self.enter_class != "":
                tmp = self.enter_class + text
                if tmp in self.function_definition_map:
                    text = tmp
                    ptr = 1
            type = self.function_definition_map[text]
            expressionlist = "()"
            if code.expressionLists() != None:
                expressionlist = self.expressionLists_decode(
                    code.expressionLists(), stream
                )
                if ptr == 1:
                    expressionlist = "(ptr %this, " + expressionlist[1:]
            elif ptr == 1:
                expressionlist = "(ptr %this)"
            if type != "void":
                stream[0] += (
                    result
                    + " = call "
                    + self.type2ir(type)
                    + " @"
                    + text
                    + expressionlist
                    + "\n\t\t"
                )
            else:
                stream[0] += (
                    "call "
                    + self.type2ir(type)
                    + " @"
                    + text
                    + expressionlist
                    + "\n\t\t"
                )
            self.variable_map[code.getText()] = (type, result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.MemberFunctionCallContext):
            # memberFunctionCall

            t = self.return_expression2ir(code.expression(), stream)
            if self.variable_map[t][0] == "string":
                func = code.IDENTIFIER().getText()
                if func == "length":
                    stream[0] += (
                        result
                        + " = call "
                        + self.type2ir("int")
                        + " @string.length("
                        + self.type2ir("string")
                        + " "
                        + self.variable_map[t][1]
                        + ")\n\t\t"
                    )
                    self.variable_map[code.getText()] = ("int", result)
                    return code.getText()
                elif func == "substring":
                    expressionlist = self.expressionLists_decode(
                        code.expressionLists(), stream
                    )
                    stream[0] += (
                        result
                        + " = call "
                        + self.type2ir("string")
                        + " @string.substring("
                        + self.type2ir("string")
                        + " "
                        + self.variable_map[t][1]
                        + ","
                        + expressionlist[1:-1]
                        + ")\n\t\t"
                    )
                    self.variable_map[code.getText()] = ("string", result)
                    return code.getText()
                elif func == "parseInt":
                    stream[0] += (
                        result
                        + " = call "
                        + self.type2ir("int")
                        + " @string.parseInt("
                        + self.type2ir("string")
                        + " "
                        + self.variable_map[t][1]
                        + ")\n\t\t"
                    )
                    self.variable_map[code.getText()] = ("int", result)
                    return code.getText()
                elif func == "ord":
                    expressionlist = self.expressionLists_decode(
                        code.expressionLists(), stream
                    )
                    stream[0] += (
                        result
                        + " = call "
                        + self.type2ir("int")
                        + " @string.ord("
                        + self.type2ir("string")
                        + " "
                        + self.variable_map[t][1]
                        + ","
                        + expressionlist[1:-1]
                        + ")\n\t\t"
                    )
                    self.variable_map[code.getText()] = ("int", result)
                    return code.getText()
            name = self.variable_map[t][0] + code.IDENTIFIER().getText()
            type = self.function_definition_map[name]
            expressionlist = "(ptr " + self.variable_map[t][1] + ")"
            if code.expressionLists() != None:
                expressionlist = self.expressionLists_decode(
                    code.expressionLists(), stream
                )
                expressionlist = (
                    "(ptr " + self.variable_map[t][1] + ", " + expressionlist[1:]
                )
            if type != "void":
                stream[0] += (
                    result
                    + " = call "
                    + self.type2ir(type)
                    + " @"
                    + name
                    + expressionlist
                    + "\n\t\t"
                )
            else:
                stream[0] += (
                    "call "
                    + self.type2ir(type)
                    + " @"
                    + name
                    + expressionlist
                    + "\n\t\t"
                )
            self.variable_map[code.getText()] = (type, result)
            return code.getText()
        elif isinstance(code, Mx_parserParser.MemberMemberCallContext):
            # memberMemberCall
            t = self.return_expression2ir(code.expression(), stream)
            index = self.variable_map[t][0] + code.IDENTIFIER().getText()
            stream[0] += (
                result
                + " = getelementptr %"
                + self.variable_map[t][0]
                + ", ptr "
                + self.variable_map[t][1]
                + ", i32 0, i32 "
                + str(self.class_member_enum[index][0])
                + "\n\t\t"
            )
            ptr = result
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            stream[0] += (
                result
                + " = load "
                + self.type2ir(self.class_member_enum[index][1])
                + ", ptr "
                + ptr
                + "\n\t\t"
            )
            self.variable_map[code.getText()] = (
                self.class_member_enum[index][1],
                result,
            )
            self.write_map[code.getText()] = ptr
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
                    _string, len_ = self.transform_string(string_)
                    self.global_str += (
                        "@string."
                        + str(self.string_cnt)
                        + " = global [ "
                        + str(len_)
                        + " x i8] c"
                        + _string
                        + "\n"
                    )
                    self.variable_map[code.getText()] = (
                        "string",
                        "@string." + str(self.string_cnt),
                    )
                    self.string_cnt += 1
                    return code.getText()
                else:
                    pass  # fstring 被转换了
            if constant.array_constant() != None:
                array_ = constant.array_constant()
                return self.array_constantdecode(array_, stream)

            if constant.getText() == "null":
                self.variable_map["null"] = ("null", "null")
                return "null"
            if constant.getText() == "true":
                self.variable_map["1"] = ("bool", "1")
                return "1"
            self.variable_map["0"] = ("bool", "0")
            return "0"
        elif isinstance(code, Mx_parserParser.NewVariableExpressionContext):
            # newVariableExpression
            stream[0] += (
                result
                + " = call ptr @malloc(i32 "
                + str(self.class_size_map[code.type_().getText()])
                + ")\n\t\t"
            )  # 只有自定义类型
            self.variable_map[code.getText()] = (code.type_().getText(), result)
            stream[0] += (
                "call void @"
                + code.type_().getText()
                + "_new(ptr "
                + result
                + ")\n\t\t"
            )
            return code.getText()
        elif isinstance(code, Mx_parserParser.NewArrayExpressionContext):
            # newArrayExpression
            cnt = 0
            for i in code.getText():
                if i == "[":
                    cnt += 1
            if (
                cnt == 1
                and code.type_().getText() == "int"
                or code.type_().getText() == "bool"
            ):
                if code.type_().getText() == "int":
                    _type = "Int"
                else:
                    _type = "Bool"
            else:
                _type = "Ptr"
            _type = _type[0].upper() + _type[1:]
            if self.isPrivate(self.enter_class):
                t = self.return_expression2ir(code.expression(0), stream)
                stream[0] += (
                    result
                    + " = call ptr@__new"
                    + _type
                    + "Array(i32 "
                    + self.variable_map[t][1]
                    + ")\n\t\t"
                )
                self.variable_map[code.getText()] = (
                    code.type_().getText() + cnt * "[]",
                    result,
                )
                self.write_map[code.getText()] = ""
                return code.getText()
            if code.array_constant() != None:
                return self.array_constantdecode(code.array_constant(), stream)
            expressionlist = code.expression()
            list = []
            type_ = "class_" + code.type_().getText() + str(cnt)
            stream[0] += (
                result
                + " = call ptr @malloc(i32 "
                + str(self.class_size_map[type_])
                + ")\n\t\t"
            )
            src = result
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            for i in expressionlist:
                list.append(self.return_expression2ir(i, stream))
            stream[0] += (
                result + " = call ptr @__newIntArray( i32 " + str(len(list)) + ")\n\t\t"
            )
            tmp = result
            for i in range(len(list)):
                result = "%var" + str(self.variable_cnt)
                self.variable_cnt += 1
                stream[0] += (
                    result
                    + " = getelementptr i32, ptr "
                    + tmp
                    + ", i32 "
                    + str(len(list) - i - 1)
                    + "\n\t\t"
                )
                stream[0] += (
                    "store i32 "
                    + self.variable_map[list[i]][1]
                    + ", ptr "
                    + result
                    + "\n\t\t"
                )
            stream[0] += (
                "call void @"
                + type_
                + "list_init(ptr "
                + src
                + ", i32 "
                + str(len(list))
                + ", ptr "
                + tmp
                + ")\n\t\t"
            )
            self.variable_map[code.getText()] = (type_, src)
            return code.getText()
        elif isinstance(code, Mx_parserParser.VariableExpressionContext):
            # variableExpression
            identifier = code.IDENTIFIER().getText()
            if self.enter_class != "":
                index = self.enter_class + identifier
                if index in self.class_member_enum:
                    t = "this"
                    stream[0] += (
                        result
                        + " = getelementptr %"
                        + self.variable_map[t][0]
                        + ", ptr "
                        + self.variable_map[t][1]
                        + ", i32 0, i32 "
                        + str(self.class_member_enum[index][0])
                        + "\n\t\t"
                    )
                    ptr = result
                    result = "%var" + str(self.variable_cnt)
                    self.variable_cnt += 1
                    stream[0] += (
                        result
                        + " = load "
                        + self.type2ir(self.class_member_enum[index][1])
                        + ", ptr "
                        + ptr
                        + "\n\t\t"
                    )
                    self.variable_map[code.getText()] = (
                        self.class_member_enum[index][1],
                        result,
                    )
                    self.write_map[code.getText()] = ptr
                    return code.getText()
            value = self.variable_map[identifier][1]
            if self.write_map[identifier] != "":
                stream[0] += (
                    result
                    + " = load "
                    + self.type2ir(self.variable_map[identifier][0])
                    + ", ptr "
                    + self.write_map[identifier]
                    + "\n\t\t"
                )
                self.variable_map[identifier] = (
                    self.variable_map[identifier][0],
                    result,
                )
                return identifier
            return identifier
        elif isinstance(code, Mx_parserParser.ArrayExpressionContext):
            # arrayExpression
            t1 = self.return_expression2ir(code.expression(0), stream)
            t2 = self.return_expression2ir(code.expression(1), stream)
            if self.isPrivate(self.enter_class):
                type_ = self.variable_map[t1][0][:-2]
                stream[0] += (
                    result
                    + " = getelementptr "
                    + self.type2ir(type_)
                    + ", ptr "
                    + self.variable_map[t1][1]
                    + ", "
                    + self.type2ir(self.variable_map[t2][0])
                    + " "
                    + self.variable_map[t2][1]
                    + "\n\t\t"
                )
                ptr = result
                result = "%var" + str(self.variable_cnt)
                self.variable_cnt += 1
                stream[0] += (
                    result
                    + " = load "
                    + self.type2ir(type_)
                    + ", ptr "
                    + ptr
                    + "\n\t\t"
                )
                self.variable_map[code.getText()] = (type_, result)
                self.write_map[code.getText()] = ptr
                return code.getText()
            stream[0] += (
                result
                + " = getelementptr %"
                + self.variable_map[t1][0]
                + ", ptr "
                + self.variable_map[t1][1]
                + ", i32 0, i32 1\n\t\t"
            )
            _tmp = result
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            stream[0] += result + " = load ptr, ptr " + _tmp + "\n\t\t"
            value = result
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            # if self.isPrivate(self.enter_class):
            #     type_ = self.variable_map[t1][0][:-2]
            # else:
            if self.variable_map[t1][0][-1] == "1":
                type_ = self.arraytype_reform(self.variable_map[t1][0])[:-2]
            else:
                type_ = self.variable_map[t1][0][:-1] + str(
                    int(self.variable_map[t1][0][-1]) - 1
                )
            stream[0] += (
                result
                + " = getelementptr "
                + self.type2ir(type_)
                + ", ptr "
                + value
                + ", "
                + self.type2ir(self.variable_map[t2][0])
                + " "
                + self.variable_map[t2][1]
                + "\n\t\t"
            )
            ptr = result
            result = "%var" + str(self.variable_cnt)
            self.variable_cnt += 1
            stream[0] += (
                result + " = load " + self.type2ir(type_) + ", ptr " + ptr + "\n\t\t"
            )
            self.variable_map[code.getText()] = (type_, result)
            self.write_map[code.getText()] = ptr
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

    def enterConstruction(self, ctx: Mx_parserParser.ConstructionContext):
        func_str = (
            "define void @"
            + ctx.IDENTIFIER().getText()
            + "_new(ptr %this){\nentry:\n\t\t"
        )
        self.label_str = "entry"
        statement_list = ctx.functionBody().statement()
        stream = [func_str]
        for i in range(len(statement_list)):
            self.statement_decode2ir(statement_list[i], stream)
        stream[0] += "ret void\n}\n"
        self.function_definition_list.append(stream[0])

    def enterProgram(self, ctx: Mx_parserParser.ProgramContext):
        class_definition_str = ""
        variable_definition_str = ""
        function_definition_str = ""
        for child in ctx.getChildren():
            if isinstance(child, Mx_parserParser.ClassDefinitionContext):
                class_definition_str += "%" + child.IDENTIFIER().getText() + " = type {"
                classmember = child.classMember()
                cnt = 0
                var_list = []
                construct = 0
                # function_definition_str += (
                #     "declare void @" + child.IDENTIFIER().getText() + "_new(ptr)\n\t\t"
                # )
                self.function_definition_map[child.IDENTIFIER().getText() + "_new"] = (
                    "void"
                )
                for i in range(len(classmember)):
                    ii = classmember[i]
                    if ii.variableDeclaration() != None:
                        declare = ii.variableDeclaration()
                        if declare.type_() != None:
                            type = declare.type_().getText()
                        else:
                            type = declare.arrayType().getText()
                        if not self.isPrivate(child.IDENTIFIER().getText()):
                            type = self.arraytype_transform(type)
                        for parts in declare.variableDeclarationparts():
                            name = parts.IDENTIFIER().getText()
                            var_list.append(self.type2ir(type))

                            self.class_member_enum[
                                child.IDENTIFIER().getText() + name
                            ] = (cnt, type)
                            cnt += 1
                    elif ii.functionDefinition() != None:
                        type = ii.functionDefinition().returnType().getText()
                        type = self.arraytype_transform(type)
                        name = ii.functionDefinition().IDENTIFIER().getText()
                        # function_definition_str += (
                        #     "declare "
                        #     + self.type2ir(type)
                        #     + " @"
                        #     + child.IDENTIFIER().getText()
                        #     + name
                        #     + "( ptr"
                        # )
                        self.function_definition_map[
                            child.IDENTIFIER().getText() + name
                        ] = type
                        # parameterlist = self.parameterList_decode2name(
                        #     ii.functionDefinition().parameterList()
                        # )
                        # for i in parameterlist:
                        #     function_definition_str += ", " + self.type2ir(i[0])
                        # function_definition_str += ")\n\t\t"
                    else:
                        construct = 1
                if construct == 0:
                    function_definition_str += (
                        "define void @"
                        + child.IDENTIFIER().getText()
                        + "_new(ptr){\n\t\tret void \n}\n"
                    )
                self.class_size_map[child.IDENTIFIER().getText()] = cnt * 4
                for i in range(len(var_list)):
                    class_definition_str += var_list[i]
                    if i != len(var_list) - 1:
                        class_definition_str += ", "
                class_definition_str += "}\n"

            elif isinstance(child, Mx_parserParser.FunctionDefinitionContext):
                type = child.returnType().getText()
                type = self.arraytype_transform(type)
                name = child.IDENTIFIER().getText()
                # function_definition_str += (
                #     "declare "
                #     + self.type2ir(type)
                #     + " @"
                #     + child.IDENTIFIER().getText()
                # )
                self.function_definition_map[child.IDENTIFIER().getText()] = type
                # function_definition_str += self.parameterList_decode2type(
                #     child.parameterList()
                # )
                function_definition_str += "\n\t\t"
            elif isinstance(child, Mx_parserParser.VariableDeclarationContext):
                if child.type_() != None:
                    type = self.type2ir(child.type_().getText())
                    type_ = child.type_().getText()
                else:
                    type = "ptr"
                    type_ = child.arrayType().getText()
                type_ = self.arraytype_transform(type_)
                default = "0"
                if type == "ptr":
                    default = "null"
                    if child.type_() != None and child.type_().getText() == "string":
                        default = "@.string.0"
                for i in child.variableDeclarationparts():
                    name = i.IDENTIFIER().getText()
                    variable_definition_str += "@" + name + " = global " + type + " "
                    self.variable_map[name] = (type_, "@" + name)
                    self.write_map[name] = "@" + name
                    if i.expression() == None:
                        variable_definition_str += default
                    else:
                        init = 1
                        if isinstance(
                            i.expression(), Mx_parserParser.ConstantExpressionContext
                        ):
                            constant = i.expression().constant()
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
                                + " (){\nentry:\n\t\t"
                            )
                            self.label_str = "entry"
                            stream = [init_func]
                            exp = self.variable_map[
                                self.return_expression2ir(i.expression(), stream)
                            ][1]
                            stream[0] += (
                                "    store "
                                + type
                                + " "
                                + exp
                                + ", ptr @"
                                + name
                                + "\n\t\t"
                            )
                            stream[0] += "    ret void\n\n}\n\n"
                            self.function_definition_list.append(stream[0])
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
            ans += self.type2ir(self.variable_map[t][0]) + " " + self.variable_map[t][1]
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
            if parameter.type_() != None:
                ans.append(
                    (
                        parameter.type_().getText(),
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
        type_ = ctx.returnType().getText()
        self.enter_function = self.enter_class + ctx.IDENTIFIER().getText()
        func_str = (
            "define "
            + self.type2ir(type_)
            + " @"
            + self.enter_class
            + ctx.IDENTIFIER().getText()
        )
        parameterlist = self.parameterList_decode2name(ctx.parameterList())
        parameterstr = "("
        if self.enter_class != "":
            parameterstr += "ptr %this"
        for i in range(len(parameterlist)):
            type = parameterlist[i][0]
            if not self.isPrivate(self.enter_class):
                type = self.arraytype_transform(type)
            self.variable_map[parameterlist[i][1]] = (
                type,
                "%" + parameterlist[i][1],
            )
            self.write_map[parameterlist[i][1]] = ""
            parameterstr += (
                ", " + self.type2ir(parameterlist[i][0]) + " %" + parameterlist[i][1]
            )
        parameterstr += ")"
        if self.enter_class == "" and parameterstr != "()":
            parameterstr = parameterstr[:1] + parameterstr[2:]
        func_str += parameterstr + " {\nentry:\n\t\t"
        self.label_str = "entry"
        if ctx.IDENTIFIER().getText() == "main":
            for i in range(self.init_cnt):
                func_str += "call void @init" + str(i) + "()\n\t\t"
        statement_list = ctx.functionBody().statement()
        stream = [func_str]
        for i in range(len(statement_list)):
            self.statement_decode2ir(statement_list[i], stream)
        default = self.return_default(type_)
        stream[0] += "ret " + self.type2ir(type_) + " " + default
        stream[0] += "\n}\n"
        self.function_definition_list.append(stream[0])

    def return_default(self, code: str) -> str:
        if code == "void":
            return ""
        if code == "bool" or code == "int":
            return "0"
        if code == "string":
            return "@.string.0"
        return "null"

    def branch_map_record(self, label: int):
        if label in self.branch_map:
            self.branch_map[label].append((self.label_str, self.variable_map.copy()))
        else:
            self.branch_map[label] = [(self.label_str, self.variable_map.copy())]

    def branch_map_decode(self, label: int, stream):
        if label in self.branch_map and len(self.branch_map[label]) > 1:
            m = self.branch_map[label]
            i0 = m[0]
            for i in range(1, len(m)):
                for j in i0[1]:
                    if (j in self.write_map and self.write_map[j] == "") and i0[1][j][
                        1
                    ] != m[i][1][j][1]:
                        result = "%var" + str(self.variable_cnt)
                        self.variable_cnt += 1
                        stream[0] += (
                            result
                            + " = phi "
                            + self.type2ir(i0[1][j][0])
                            + " ["
                            + i0[1][j][1]
                            + ", %"
                            + i0[0]
                            + "], ["
                            + m[i][1][j][1]
                            + ", %"
                            + m[i][0]
                            + "]\n\t\t"
                        )
                        self.variable_map[j] = (self.variable_map[j][0], result)

        if label in self.branch_map and len(self.branch_map[label]) == 1:
            self.variable_map = self.branch_map[label][0][1]

    def statement_decode2ir(self, code: Mx_parserParser.StatementContext, stream):
        stream[0] += "\n; statement: " + code.getText() + "\n\n\t\t"
        if isinstance(code, Mx_parserParser.EmptyStatementContext):
            return
        elif isinstance(code, Mx_parserParser.ExpressionStatementContext):
            self.return_expression2ir(code.expression(), stream)
            return
        elif isinstance(code, Mx_parserParser.IfStatementContext):
            label_cnt = self.label_cnt
            self.label_cnt += 3
            t = self.return_expression2ir(code.expression(), stream)
            stream[0] += (
                "br i1 "
                + self.variable_map[t][1]
                + ", label %.label"
                + str(label_cnt)
                + ", label %.label"
                + str(label_cnt + 1)
                + "\n\t"
            )
            tmp_map = self.variable_map.copy()
            stream[0] += "\n.label" + str(label_cnt) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt)
            self.statement_decode2ir(code.statement(), stream)
            stream[0] += "br label %.label" + str(label_cnt + 2) + "\n\t"
            tmp_label1 = self.label_str
            change_map = {}
            for i in tmp_map:
                if (i in self.write_map and self.write_map[i] == "") and tmp_map[i][
                    1
                ] != self.variable_map[i][1]:
                    change_map[i] = (self.variable_map[i][1], tmp_map[i][1])
            stream[0] += "\n.label" + str(label_cnt + 1) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 1)
            if code.elsestatement() is not None:
                self.variable_map = tmp_map.copy()
                self.statement_decode2ir(code.elsestatement().statement(), stream)
                for i in tmp_map:
                    if (i in self.write_map and self.write_map[i] == "") and tmp_map[i][
                        1
                    ] != self.variable_map[i][1]:
                        if i in change_map:
                            change_map[i] = (change_map[i][0], self.variable_map[i][1])
                        else:
                            change_map[i] = (tmp_map[i][1], self.variable_map[i][1])
            stream[0] += "br label %.label" + str(label_cnt + 2) + "\n\t"
            tmp_label2 = self.label_str
            stream[0] += "\n.label" + str(label_cnt + 2) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 2)
            for i in change_map:
                result = "%var" + str(self.variable_cnt)
                self.variable_cnt += 1
                stream[0] += (
                    result
                    + " = phi "
                    + self.type2ir(self.variable_map[i][0])
                    + "["
                    + change_map[i][0]
                    + ", %"
                    + tmp_label1
                    + "], ["
                    + change_map[i][1]
                    + ", %"
                    + tmp_label2
                    + "]\n\t\t"
                )
                self.variable_map[i] = (self.variable_map[i][0], result)
            return
        elif isinstance(code, Mx_parserParser.WhileStatementContext):
            label_cnt = self.label_cnt
            self.label_cnt += 4
            stream[0] += "br label %.label" + str(label_cnt + 3) + "\n\t"
            tmp_label1 = self.label_str
            tmp_me = copy.deepcopy(self)
            tmp_me.copy(self)
            tmp_stream = [""]
            tmp_stream[0] += "\n.label" + str(label_cnt + 1) + ":\n\t\t"
            tmp_me.label_str = ".label" + str(label_cnt + 1)
            tmp_me.loop_stack.append(label_cnt)
            tmp_me.statement_decode2ir(code.statement(), tmp_stream)
            tmp_me.loop_stack.pop()
            tmp_me.branch_map_record(label_cnt)
            tmp_stream[0] += "br label %.label" + str(label_cnt) + "\n\t"
            tmp_stream[0] += "\n.label" + str(label_cnt) + ":\n\t\t"
            tmp_me.label_str = ".label" + str(label_cnt)
            tmp_me.branch_map_decode(label_cnt, tmp_stream)
            tmp_label2 = tmp_me.label_str
            tmp_stream[0] += "br label %.label" + str(label_cnt + 3) + "\n\t"
            # self.label_str = ".label" + str(label_cnt + 3)
            tmp_cnt = tmp_me.variable_cnt
            tmp_var_map = self.variable_map.copy()
            for i in self.variable_map:
                if (
                    i in self.write_map and self.write_map[i] == ""
                ) and tmp_me.variable_map[i][1] != self.variable_map[i][1]:
                    result = "%var" + str(tmp_cnt)
                    tmp_cnt += 1
                    self.variable_map[i] = (self.variable_map[i][0], result)
            stream[0] += "\n.label" + str(label_cnt + 1) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 1)
            self.loop_stack.append(label_cnt)
            self.statement_decode2ir(code.statement(), stream)
            self.loop_stack.pop()
            self.branch_map_record(label_cnt)
            stream[0] += "br label %.label" + str(label_cnt) + "\n\t"
            stream[0] += "\n.label" + str(label_cnt) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt)
            self.branch_map_decode(label_cnt, stream)
            stream[0] += "br label %.label" + str(label_cnt + 3) + "\n\t"
            stream[0] += "\n.label" + str(label_cnt + 3) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 3)
            topo_list = []
            for i in tmp_var_map:
                if (i in self.write_map and self.write_map[i] == "") and tmp_var_map[i][
                    1
                ] != self.variable_map[i][1]:
                    result = "%var" + str(self.variable_cnt)
                    self.variable_cnt += 1
                    topo_list.append(
                        (
                            self.variable_map[i][1],
                            result,
                            (
                                result
                                + " = phi "
                                + self.type2ir(self.variable_map[i][0])
                                + "["
                                + tmp_var_map[i][1]
                                + ", %"
                                + tmp_label1
                                + "], ["
                                + self.variable_map[i][1]
                                + ", %"
                                + tmp_label2
                                + "]\n\t\t"
                            ),
                        )
                    )
                    self.variable_map[i] = (self.variable_map[i][0], result)
            while topo_list:
                for i in topo_list:
                    flag = 0
                    for j in topo_list:
                        if i[0] == j[1]:
                            flag = 1
                            break
                    if flag == 0:
                        stream[0] += i[2]
                        topo_list.remove(i)
            t2 = self.return_expression2ir(code.expression(), stream)
            self.branch_map_record(label_cnt + 2)
            stream[0] += (
                "br i1 "
                + self.variable_map[t2][1]
                + ", label %.label"
                + str(label_cnt + 1)
                + ", label %.label"
                + str(label_cnt + 2)
                + "\n\t\t"
            )
            stream[0] += "\n.label" + str(label_cnt + 2) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 2)
            self.branch_map_decode(label_cnt + 2, stream)
            # print(tmp_stream[0])
            return
        elif isinstance(code, Mx_parserParser.ForStatementContext):
            label_cnt = self.label_cnt
            self.label_cnt += 4
            if code.forControl().expression1() != None:
                if code.forControl().expression1().expression() != None:
                    self.return_expression2ir(
                        code.forControl().expression1().expression(), stream
                    )
                elif code.forControl().expression1().assignment() != None:
                    assignment = code.forControl().expression1().assignment()
                    self.assignment_decode2ir(assignment, stream)
                else:
                    variabledeclare = (
                        code.forControl().expression1().variableDeclaration()
                    )
                    self.variabledeclaration_decode2ir(variabledeclare, stream)

            stream[0] += "br label %.label" + str(label_cnt + 3) + "\n\t"
            tmp_label1 = self.label_str
            tmp_me = copy.deepcopy(self)
            tmp_me.copy(self)
            tmp_stream = [""]
            tmp_stream[0] += "\n.label" + str(label_cnt + 1) + ":\n\t\t"
            tmp_me.label_str = ".label" + str(label_cnt + 1)
            tmp_me.loop_stack.append(label_cnt)
            tmp_me.statement_decode2ir(code.statement(), tmp_stream)
            tmp_me.loop_stack.pop()
            tmp_me.branch_map_record(label_cnt)
            tmp_stream[0] += "br label %.label" + str(label_cnt) + "\n\t"
            tmp_stream[0] += "\n.label" + str(label_cnt) + ":\n\t\t"
            tmp_me.label_str = ".label" + str(label_cnt)
            tmp_me.branch_map_decode(label_cnt, tmp_stream)
            if code.forControl().expression3() != None:
                if code.forControl().expression3().expression() != None:
                    tmp_me.return_expression2ir(
                        code.forControl().expression3().expression(), tmp_stream
                    )
                else:
                    assignment = code.forControl().expression3().assignment()
                    tmp_me.assignment_decode2ir(assignment, tmp_stream)
            tmp_label2 = tmp_me.label_str
            tmp_stream[0] += "br label %.label" + str(label_cnt + 3) + "\n\t"
            # self.label_str = ".label" + str(label_cnt + 3)
            tmp_cnt = tmp_me.variable_cnt
            tmp_var_map = self.variable_map.copy()
            for i in self.variable_map:
                if (
                    i in self.write_map and self.write_map[i] == ""
                ) and tmp_me.variable_map[i][1] != self.variable_map[i][1]:
                    result = "%var" + str(tmp_cnt)
                    tmp_cnt += 1
                    self.variable_map[i] = (self.variable_map[i][0], result)
            stream[0] += "\n.label" + str(label_cnt + 1) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 1)
            self.loop_stack.append(label_cnt)
            self.statement_decode2ir(code.statement(), stream)
            self.loop_stack.pop()
            self.branch_map_record(label_cnt)
            stream[0] += "br label %.label" + str(label_cnt) + "\n\t"
            stream[0] += "\n.label" + str(label_cnt) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt)
            self.branch_map_decode(label_cnt, stream)
            if code.forControl().expression3() != None:
                if code.forControl().expression3().expression() != None:
                    self.return_expression2ir(
                        code.forControl().expression3().expression(), stream
                    )
                else:
                    assignment = code.forControl().expression3().assignment()
                    self.assignment_decode2ir(assignment, stream)
            stream[0] += "br label %.label" + str(label_cnt + 3) + "\n\t"
            stream[0] += "\n.label" + str(label_cnt + 3) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 3)
            topo_list = []
            for i in tmp_var_map:
                if (i in self.write_map and self.write_map[i] == "") and tmp_var_map[i][
                    1
                ] != self.variable_map[i][1]:
                    result = "%var" + str(self.variable_cnt)
                    self.variable_cnt += 1
                    topo_list.append(
                        (
                            self.variable_map[i][1],
                            result,
                            (
                                result
                                + " = phi "
                                + self.type2ir(self.variable_map[i][0])
                                + "["
                                + tmp_var_map[i][1]
                                + ", %"
                                + tmp_label1
                                + "], ["
                                + self.variable_map[i][1]
                                + ", %"
                                + tmp_label2
                                + "]\n\t\t"
                            ),
                        )
                    )
                    self.variable_map[i] = (self.variable_map[i][0], result)
            while topo_list:
                for i in topo_list:
                    flag = 0
                    for j in topo_list:
                        if i[0] == j[1]:
                            flag = 1
                            break
                    if flag == 0:
                        stream[0] += i[2]
                        topo_list.remove(i)
            if code.forControl().expression2() != None:
                t2 = self.return_expression2ir(
                    code.forControl().expression2().expression(), stream
                )
                self.branch_map_record(label_cnt + 2)
                stream[0] += (
                    "br i1 "
                    + self.variable_map[t2][1]
                    + ", label %.label"
                    + str(label_cnt + 1)
                    + ", label %.label"
                    + str(label_cnt + 2)
                    + "\n\t\t"
                )
            else:
                stream[0] += "br label %.label" + str(label_cnt + 1) + "\n\t\t"
            stream[0] += "\n.label" + str(label_cnt + 2) + ":\n\t\t"
            self.label_str = ".label" + str(label_cnt + 2)
            self.branch_map_decode(label_cnt + 2, stream)
            # print(tmp_stream[0])
            return
        elif isinstance(code, Mx_parserParser.ReturnStatementContext):
            if code.expression() != None:
                t = self.return_expression2ir(code.expression(), stream)
                stream[0] += (
                    "ret "
                    + self.type2ir(self.variable_map[t][0])
                    + " "
                    + self.variable_map[t][1]
                    + "\n\t\t"
                )
            else:
                stream[0] += "ret void\n\t\t"
            return
        elif isinstance(code, Mx_parserParser.BlockContext):
            for i in range(len(code.statement())):
                self.statement_decode2ir(code.statement(i), stream)
        elif isinstance(code, Mx_parserParser.BreakStatementContext):
            self.branch_map_record(self.loop_stack[-1] + 2)
            stream[0] += "br label %.label" + str(self.loop_stack[-1] + 2) + "\n\t\t"
        elif isinstance(code, Mx_parserParser.ContinueStatementContext):
            self.branch_map_record(self.loop_stack[-1])
            stream[0] += "br label %.label" + str(self.loop_stack[-1]) + "\n\t\t"
        elif isinstance(code, Mx_parserParser.AssignmentStatementContext):
            code = code.assignment()
            self.assignment_decode2ir(code, stream)
        elif isinstance(code, Mx_parserParser.PrivatevariableDeclarationContext):
            variabledeclare = code.variableDeclaration()
            self.variabledeclaration_decode2ir(variabledeclare, stream)

    def variabledeclaration_decode2ir(self, variabledeclare, stream):
        if variabledeclare.type_() != None:
            type_ = variabledeclare.type_().getText()
        else:
            type_ = variabledeclare.arrayType().getText()
        type_ = self.arraytype_transform(type_)
        default = self.return_default(type_)
        for i in variabledeclare.variableDeclarationparts():
            name = i.IDENTIFIER().getText()
            if name == "d1":
                print("")
            self.write_map[name] = ""
            if i.expression() != None:
                t = self.return_expression2ir(i.expression(), stream)
                self.variable_map[name] = self.variable_map[t]
            else:
                self.variable_map[name] = [type_, default]

    def arraytype_transform(self, code: str) -> str:
        if code[-1] != "]":
            return code
        cnt = 0
        for i in code:
            if i == "[":
                cnt += 1
        return "class_" + code[: -2 * cnt] + str(cnt)

    def arraytype_reform(self, code: str) -> str:
        cnt = int(code[-1])
        return code[6:-1] + "[]" * cnt

    def assignment_decode2ir(self, code: Mx_parserParser.AssignmentContext, stream):
        t1 = self.return_expression2ir(code.expression(0), stream)
        t2 = self.return_expression2ir(code.expression(1), stream)
        name = code.expression(0).getText()
        if self.write_map[code.expression(0).getText()] != "":
            stream[0] += (
                "store "
                + self.type2ir(self.variable_map[t2][0])
                + " "
                + self.variable_map[t2][1]
                + ", "
                + "ptr "
                + self.write_map[code.expression(0).getText()]
                + "\n\t\t"
            )
        else:
            self.variable_map[t1] = self.variable_map[t2]

    def exitFunctionDefinition(self, ctx: Mx_parserParser.FunctionDefinitionContext):
        self.enter_function = ""

    def exitClassDefinition(self, ctx: Mx_parserParser.ClassDefinitionContext):
        self.enter_class = ""

    def enterClassDefinition(self, ctx: Mx_parserParser.ClassDefinitionContext):
        self.enter_class = ctx.IDENTIFIER().getText()
        self.variable_map["this"] = (self.enter_class, "%this")
        self.write_map["this"] = ""


# with open("in.txt", "r") as f:
#     code = f.read()
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
    listener = MyListener2()
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
            if ".label" in line or "entry" in line:
                stream_out = 1
            return_ans += line + "\n"
    return return_ans


if __name__ == "__main__":
    code = sys.stdin.read()
    code2 = main(code)
    with open("llvm.ll", "w") as f:
        f.write(code2)
    print(code2)
