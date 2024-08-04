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
    # name = ""     作为字典键
    parameterList = []
    # body = []     语法检查尚不考虑

    def __init__(self, returnType, parameterList):
        self.returnType = returnType
        self.parameterList = parameterList


class parameterclass:
    type = ""
    name = ""
    value = ""

    def __init__(self, type, name, value):
        self.type = type
        self.name = name
        self.value = value


class classclass:
    # name = ""     作为字典键
    class_member_list = []
    class_function_list = []

    def __init__(self, class_member_list, class_function_list):
        self.class_member_list = class_member_list
        self.class_function_list = class_function_list


def array_decode(code) -> arrayclass:
    return arrayclass(code.type().getText(), (len(code) - 1) / 2)


def parameter_decode(code) -> parameterclass:
    if code.type() != None:
        return parameterclass(
            arrayclass(
                code.type().getText(),
                0,
            ),
            code.IDENTIFIER().getText(),
            None,
        )
    else:
        return parameterclass(
            array_decode(code),
            code.IDENTIFIER().getText(),
            None,
        )


def parameterList_decode(code) -> list[parameterclass]:
    parameters = code.parameter()
    return_list = []
    for param in parameters:
        return_list.append(parameter_decode(param))


def variableDeclaration_decode(code) -> list[parameterclass]:
    return_list = []
    if code.type() != None:
        return_list.append(
            parameterclass(
                arrayclass(
                    code.type().getText(),
                    0,
                ),
                code.IDENTIFIER().getText(),
                None,
            )
        )
    else:
        return parameterclass(
            array_decode(code),
            code.IDENTIFIER().getText(),
            None,
        )


def class_decode(code) -> classclass:
    class_member_list = code.classMember()
    class_function_list = code.functionDefinition()
    return classclass(class_member_list, class_function_list)


# 定义一个监听器类来遍历和处理语法树
class MyListener(Mx_parserListener):
    function_definition_map = {}
    function_definition_stack = []  # list[functionclass]
    usertype_map = {}
    int_main_check = False

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

    def enterFunctionDefinition(self, ctx):
        returnType = ctx.returnType().getText()
        name = ctx.IDENTIFIER().getText()
        parameterList = ctx.parameterList()
        parameter_list = []
        num_parameters = 0
        if parameterList is not None:
            parameter_list = parameterList_decode(parameterList)

        if ctx.returnType().getText() != "void":
            self.function_definition_stack.append(returnType)

        if name == "main" and returnType == "int" and num_parameters == 0:
            if self.int_main_check:
                print("Error: Multiple definitions of main function")
            self.int_main_check = True
        self.function_definition_map[name] = functionclass(returnType, parameter_list)
        self.function_definition_stack.append(functionclass(returnType, parameter_list))

    def exitFunctionDefinition(self, ctx):
        self.function_definition_stack.pop()

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
