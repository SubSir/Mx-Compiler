from antlr4 import InputStream, CommonTokenStream
from parser.Mx_parserLexer import Mx_parserLexer
from parser.Mx_parserListener import Mx_parserListener
from parser.Mx_parserParser import Mx_parserParser
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Tree import ParseTreeWalker


class arrayclass:
    type = ""
    dimansion = 0

    def __init__(self, type, dimansion):
        self.type = type
        self.dimansion = dimansion


class functionclass:
    returnType = ""
    name = ""
    parameterList = []
    priority = -1
    # body = []     语法检查尚不考虑

    def __init__(self, returnType, parameterList, priority):
        self.returnType = returnType
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

    def to_string(self) -> str:
        return self.type + self.value


class classclass:
    # name = ""     作为字典键
    class_member_list = []
    class_function_list = []

    def __init__(self, class_member_list, class_function_list):
        self.class_member_list = class_member_list
        self.class_function_list = class_function_list


# 定义一个监听器类来遍历和处理语法树
class MyListener(Mx_parserListener):
    function_definition_map = {}  # name -> functionclass
    function_definition_stack = []  # list[functionclass]
    usertype_map = {}
    int_main_check = False
    variable_definition_map = {}  # name -> parameterclass
    variable_definition_stack = []  # list[parameterclass]
    priority = 0

    # def enterEveryRule(self, ctx):
    #     rule_name = Mx_parserParser.ruleNames[ctx.getRuleIndex()]
    #     rule_text = ctx.getText()
    #     print(f"Entering rule: {rule_name}, Text: {rule_text}")

    # def exitEveryRule(self, ctx):
    #     rule_name = Mx_parserParser.ruleNames[ctx.getRuleIndex()]
    #     rule_text = ctx.getText()
    #     print(f"Existing rule: {rule_name}, Text: {rule_text}")

    # def visitTerminal(self, node: TerminalNodeImpl):
    #     # 当访问到终端节点时调用此方法
    #     print(node.getText())
    def return_expressiontype(self, code) -> str:
        if code.getRuleIndex() == parser.RULE_expressionList:
            # expressionList
            if self.return_expressiontype(
                code.expression()
            ) != self.return_expressiontype(
                self.variable_definition_map[code.IDENTIFIER().getText()]
            ):
                print("error: type mismatch")
            return self.return_expressiontype(code.expression())
        elif code.getRuleIndex() == parser.RULE_logicExpression:
            # logicExpression
            if self.return_expressiontype(
                code.expression(0)
            ) != self.return_expressiontype(code.expression(1)):
                print("error: type mismatch")
            return "bool"
        elif code.getRuleIndex() == parser.RULE_conditionalExpression:
            # conditionalExpression
            if self.return_expressiontype(code.expression(0)) != "bool":
                print("error: type mismatch")
            type1 = self.return_expressiontype(code.expression(1))
            type2 = self.return_expressiontype(code.expression(2))
            if type1 != type2:
                print("error: type mismatch")
            return type1
        elif code.getRuleIndex() == parser.RULE_relationalExpression:
            # relationalExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2:
                print("error: type mismatch")
            if (
                type1 == "bool"
                and code.relationOperator().getText() != "=="
                and code.relationOperator().getText() != "!="
            ):
                print("error: bool type cannot be compared")
            return "bool"
        elif code.getRuleIndex() == parser.RULE_arithmeticExpression:
            # arithmeticExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2:
                print("error: type mismatch")
            return type1
        elif code.getRuleIndex() == parser.RULE_muldivmodExpression:
            # muldivmodExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2:
                print("error: type mismatch")
            if type1 != "int":
                print("error: type cannot be used in arithmetic expression")
            return type1
        elif code.getRuleIndex() == parser.RULE_arithmeticExpression:
            # plusminusExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2:
                print("error: type mismatch")
            if type1 != "int" and type1 != "string":
                print("error: type cannot be used in arithmetic expression")
            return type1
        elif code.getRuleIndex() == parser.RULE_shiftExpression:
            # shiftExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2:
                print("error: type mismatch")
            if type1 != "int":
                print("error: type cannot be used in arithmetic expression")
            return type1
        elif code.getRuleIndex() == parser.RULE_andxororExpression:
            # andxororExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2:
                print("error: type mismatch")
            if type1 != "bool" and type1 != "int":
                print("error: type cannot be used in arithmetic expression")
            return type1
        elif code.getRuleIndex() == parser.RULE_prefixIncrementExpression:
            # prefixIncrementExpression
            return self.return_expressiontype(code.expression())
        elif code.getRuleIndex() == parser.RULE_postfixIncrementExpression:
            # postfixIncrementExpression
            return self.return_expressiontype(code.expression())
        elif code.getRuleIndex() == parser.RULE_prefixDecrementExpression:
            # prefixDecrementExpression
            return self.return_expressiontype(code.expression())
        elif code.getRuleIndex() == parser.RULE_postfixDecrementExpression:
            # postfixDecrementExpression
            return self.return_expressiontype(code.expression())
        elif code.getRuleIndex() == parser.RULE_logicalNotExpression:
            # logicalNotExpression
            return self.return_expressiontype(code.expression())
        elif code.getRuleIndex() == parser.RULE_bitwiseNotExpression:
            # bitwiseNotExpression
            return self.return_expressiontype(code.expression())
        elif code.getRuleIndex() == parser.RULE_unaryMinusExpression:
            # unaryMinusExpression
            return self.return_expressiontype(code.expression())
        elif code.getRuleIndex() == parser.RULE_functionCall:
            # functionCall
            if code.IDENTIFIER().getText() in self.function_definition_map:
                func = self.function_definition_map[code.IDENTIFIER().getText()]
                for i in range(len(func.parameter_list)):
                    if (
                        self.return_expressiontype(code.expressionList().expression(i))
                        != func.parameter_list[i].type
                    ):
                        print("error: type mismatch")
                return func.return_Type
            else:
                print("error: undefined function")
        elif code.getRuleIndex() == parser.RULE_memberFunctionCall:
            # memberFunctionCall
            if code.IDENTIFIER().getText() in self.function_definition_map:
                func = self.function_definition_map[code.IDENTIFIER().getText()]
                for i in range(len(func.parameter_list)):
                    if (
                        self.return_expressiontype(code.expressionList().expression(i))
                        != func.parameter_list[i].type
                    ):
                        print("error: type mismatch")
                return func.return_Type
            else:
                print("error: undefined function")
        elif code.getRuleIndex() == parser.RULE_constantExpression:
            # constantExpression
            constant = code.constant()
            if constant.INTEGER_CONSTANT() != None:
                return "int"
            if constant.string_constant() != None:
                return "string"
            if constant.getText() == "null":
                return "null"
            return "bool"
        elif code.getRuleIndex() == parser.RULE_newVariableExpression:
            # newVariableExpression
            return code.type().getText()
        elif code.getRuleIndex() == parser.RULE_newArrayExpression:
            # newArrayExpression
            return "newArrayExpression"
        elif code.getRuleIndex() == parser.RULE_variableExpression:
            # variableExpression
            return "variableExpression"
        elif code.getRuleIndex() == parser.RULE_arrayExpression:
            # arrayExpression
            return "arrayExpression"
        elif code.getRuleIndex() == parser.RULE_parenthesesExpression:
            # parenthesesExpression
            return "parenthesesExpression"
        else:
            # 如果没有匹配的规则，返回未知类型
            return "unknown"

    def array_decode(self, code) -> arrayclass:
        return arrayclass(code.type().getText(), (len(code) - 1) / 2)

    def parameter_decode(self, code) -> parameterclass:
        if code.type() != None:
            return parameterclass(
                arrayclass(
                    code.type().getText(),
                    0,
                ),
                code.IDENTIFIER().getText(),
                None,
                self.priority,
            )
        else:
            return parameterclass(
                self.array_decode(code),
                code.IDENTIFIER().getText(),
                None,
                self.priority,
            )

    def parameterList_decode(self, code) -> list[parameterclass]:
        parameters = code.parameter()
        return_list = []
        for param in parameters:
            return_list.append(self.parameter_decode(param))

    def variableDeclaration_decode(self, code) -> list[parameterclass]:
        return_list = []
        variableDeclarationparts = code.variableDeclarationparts()
        arrayclass_ = None
        if code.type() != None:
            arrayclass_ = arrayclass(
                code.type().getText(),
                0,
            )
        else:
            arrayclass_ = self.array_decode(code)
        for variableDeclarationpart in variableDeclarationparts:

            if variableDeclarationpart.expression() != None:
                return_list.append(
                    parameterclass(
                        arrayclass_,
                        variableDeclarationpart.IDENTIFIER().getText(),
                        None,
                        self.priority,
                    )
                )

    def classMember_decode(self, code):
        if code.variableDeclaration() != None:
            return self.variableDeclaration_decode(code.variableDeclaration())
        else:
            return self.classMember_decode(code.classMember())

    def class_decode(self, code) -> classclass:
        class_member_list = code.classMember()
        class_function_list = code.functionDefinition()
        return classclass(class_member_list, class_function_list)

    def enterFunctionDefinition(self, ctx):
        self.priority += 1
        returnType = ctx.returnType().getText()
        name = ctx.IDENTIFIER().getText()
        parameterList = ctx.parameterList()
        parameter_list = []
        num_parameters = 0
        if parameterList is not None:
            parameter_list = self.parameterList_decode(parameterList)

        if ctx.returnType().getText() != "void":
            self.function_definition_stack.append(returnType)

        if name == "main" and returnType == "int" and num_parameters == 0:
            if self.int_main_check:
                print("Error: Multiple definitions of main function")
            self.int_main_check = True
        func = functionclass(returnType, parameter_list, self.priority)
        self.function_definition_map[name] = func
        self.function_definition_stack.append(func)
        self.variable_definition_stack += parameter_list
        for param in parameter_list:
            self.variable_definition_map[param.name] = param

    def exitFunctionDefinition(self, ctx):
        self.priority -= 1
        for i in range(len(self.variable_definition_stack) - 1, -1, -1):
            if self.variable_definition_stack[i].priority - 1 >= self.priority:
                break
            self.variable_definition_map.pop(self.variable_definition_stack[i].name)
            self.variable_definition_stack.pop()

        for i in range(len(self.variable_definition_stack) - 1, -1, -1):
            if self.variable_definition_stack[i].priority == self.priority:
                break
            self.variable_definition_map.pop(self.variable_definition_stack[i].name)
            self.variable_definition_stack.pop()

    def enterType(self, ctx):
        if (
            ctx.IDENTIFIER() != None
            and ctx.IDENTIFIER().getText() not in self.usertype_map.keys()
        ):
            print("Error: Undefined type")

    def enterClassDefinition(self, ctx):
        self.usertype_map[ctx.IDENTIFIER().getText()] = ctx.getText()


with open("in.txt", "r") as f:
    code = f.read()

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
