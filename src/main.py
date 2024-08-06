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
    class_member_list = []  # list[parameterclass]
    class_function_list = []  # list[functionclass]

    def __init__(self, name, class_member_list=[], class_function_list=[]):
        self.name = name
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
    loop = 0

    # def enterEveryRule(self, ctx):
    #     rule_name = Mx_parserParser.ruleNames[ctx.getRuleIndex()]
    #     rule_text = ctx.getText()
    #     print(f"Entering rule: {rule_name}, Text: {rule_text}")

    # def exitEveryRule(self, ctx):
    #     rule_name = Mx_parserParser.ruleNames[ctx.getRuleIndex()]
    #     rule_text = ctx.getText()
    #     print(f"Existing rule: {rule_name}, Text: {rule_text}")

    def visitTerminal(self, node: TerminalNodeImpl):
        # 当访问到终端节点时调用此方法
        print(node.getText(), end="")

    def return_expressiontype(self, code) -> str:
        if isinstance(code, Mx_parserParser.ExpressionListContext):
            # expressionList
            type1 = self.return_expressiontype(code.expression())
            type2 = self.return_expressiontype(
                self.variable_definition_map[code.IDENTIFIER().getText()]
            )
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
            return self.return_expressiontype(code.expression())
        elif isinstance(code, Mx_parserParser.LogicExpressionContext):
            # logicExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
            return "bool[0]"
        elif isinstance(code, Mx_parserParser.ConditionalExpressionContext):
            # conditionalExpression
            if self.return_expressiontype(code.expression(0)) != "bool[0]":
                print("error: type mismatch")
            type1 = self.return_expressiontype(code.expression(1))
            type2 = self.return_expressiontype(code.expression(2))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
            return type1
        elif isinstance(code, Mx_parserParser.RelationalExpressionContext):
            # relationalExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
            if (
                type1 == "bool[0]"
                and code.relationOperator().getText() != "=="
                and code.relationOperator().getText() != "!="
            ):
                print("error: bool type cannot be compared")
            return "bool[0]"
        elif isinstance(code, Mx_parserParser.MuldivmodExpressionContext):
            # muldivmodExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
            if type1 != "int[0]":
                print("error: type cannot be used in arithmetic expression")
            return type1
        elif isinstance(code, Mx_parserParser.PlusminusExpressionContext):
            # plusminusExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
            if type1 != "int[0]" and type1 != "string[0]":
                print("error: type cannot be used in arithmetic expression")
            return type1
        elif isinstance(code, Mx_parserParser.ShiftExpressionContext):
            # shiftExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
            if type1 != "int[0]":
                print("error: type cannot be used in arithmetic expression")
            return type1
        elif isinstance(code, Mx_parserParser.AndxororExpressionContext):
            # andxororExpression
            type1 = self.return_expressiontype(code.expression(0))
            type2 = self.return_expressiontype(code.expression(1))
            if type1 != type2 and type1 != "null" and type2 != "null":
                print("error: type mismatch")
            if type1 != "bool[0]" and type1 != "int[0]":
                print("error: type cannot be used in arithmetic expression")
            return type1
        elif isinstance(code, Mx_parserParser.PrefixIncrementExpressionContext):
            # prefixIncrementExpression
            return self.return_expressiontype(code.expression())
        elif isinstance(code, Mx_parserParser.PostfixIncrementExpressionContext):
            # postfixIncrementExpression
            return self.return_expressiontype(code.expression())
        elif isinstance(code, Mx_parserParser.PrefixIncrementExpressionContext):
            # prefixDecrementExpression
            return self.return_expressiontype(code.expression())
        elif isinstance(code, Mx_parserParser.PostfixDecrementExpressionContext):
            # postfixDecrementExpression
            return self.return_expressiontype(code.expression())
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
            if code.IDENTIFIER().getText() in self.function_definition_map:
                func = self.function_definition_map[code.IDENTIFIER().getText()]
                for i in range(len(func.parameter_list)):
                    type1 = self.return_expressiontype(
                        code.expressionList().expression(i)
                    )
                    type2 = self.return_expressiontype(func.parameter_list[i])
                    if type1 != type2 and type1 != "null" and type2 != "null":
                        print("error: type mismatch")
                return func.return_Type
            else:
                print("error: undefined function")
        elif isinstance(code, Mx_parserParser.MemberFunctionCallContext):
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
        elif isinstance(code, Mx_parserParser.ConstantExpressionContext):
            # constantExpression
            constant = code.constant()
            if constant.INTEGER_CONSTANT() != None:
                return "int[0]"
            if constant.string_constant() != None:
                return "string[0]"
            if constant.getText() == "null":
                return "null"
            return "bool[0]"
        elif isinstance(code, Mx_parserParser.NewVariableExpressionContext):
            # newVariableExpression
            return code.type_().getText() + "[0]"
        elif isinstance(code, Mx_parserParser.NewArrayExpressionContext):
            # newArrayExpression
            dimansion = len(code.square_brackets1())
            return arrayclass(code.type_().getText(), dimansion).to_string()
        elif isinstance(code, Mx_parserParser.VariableExpressionContext):
            # variableExpression
            identifier = code.IDENTIFIER().getText()
            if identifier not in self.variable_definition_map:
                print("error: undefined variable")
            return self.variable_definition_map[identifier].type
        elif isinstance(code, Mx_parserParser.ArrayExpressionContext):
            # arrayExpression
            dimansion = len(code.square_brackets1())
            type = self.return_expressiontype(code.expression(0))
            dimansion2 = int(type.split("[")[1].split("]")[0])
            return type.split("[")[0] + "[" + str(dimansion - dimansion2) + "]"
        elif isinstance(code, Mx_parserParser.ParenthesesExpressionContext):
            # parenthesesExpression
            return self.return_expressiontype(code.expression())
        else:
            # 如果没有匹配的规则，返回未知类型
            return "unknown"

    def array_decode(self, code) -> arrayclass:
        return arrayclass(code.type_().getText(), (code.getChildCount() - 1) // 2)

    def parameter_decode(self, code) -> parameterclass:
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
                self.array_decode(code).to_string(),
                code.IDENTIFIER().getText(),
                None,
                self.priority,
            )

    def parameterList_decode(self, code) -> list[parameterclass]:
        parameters = code.parameter()
        if parameters == None:
            return []
        return_list = []
        for param in parameters:
            return_list.append(self.parameter_decode(param))

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
                if type2 != type_:
                    print("error: type mismatch")

            return_list.append(
                parameterclass(
                    type_,
                    variableDeclarationpart.IDENTIFIER().getText(),
                    None,
                    self.priority,
                )
            )
        return return_list

    def functionDefinition_decode(self, code) -> functionclass:
        type = code.returnType().getText()
        name = code.IDENTIFIER().getText()
        parameter_list = self.parameterList_decode(code.parameterList())
        return functionclass(type, name, parameter_list, self.priority)

    def class_decode(self, code) -> classclass:
        name = code.IDENTIFIER().getText()
        members = code.classMember()
        class_ = classclass(name)
        for member in members:
            if member.variableDeclaration() != None:
                class_.class_member_list += self.variableDeclaration_decode(
                    member.variableDeclaration()
                )
            elif member.functionDefinition() != None:
                class_.class_function_list += self.functionDefinition_decode(
                    member.functionDefinition()
                )
            else:
                class_.class_function_list.append(
                    functionclass(
                        None,
                        "construction",
                        self.parameterList_decode(member.parameterList()),
                        self.priority,
                    )
                )
        return class_

    def type_to_string(self, text: str):
        if text[-1] == "]" and text[-2].isdigit():
            return text
        if text[-2] == "[":
            cnt = 0
            for i in text:
                if i == "[":
                    cnt += 1
            return text + "[" + str(cnt) + "]"
        return text + "[0]"

    def enterFunctionDefinition(self, ctx):
        self.priority += 1
        returnType = self.type_to_string(ctx.returnType().getText())
        name = ctx.IDENTIFIER().getText()
        parameterList = ctx.parameterList()
        parameter_list = []
        num_parameters = 0
        if parameterList is not None:
            num_parameters = len(parameterList.parameter())
            parameter_list = self.parameterList_decode(parameterList)

        if ctx.returnType().getText() != "void":
            self.function_definition_stack.append(returnType)

        if name == "main" and returnType == "int" and num_parameters == 0:
            if self.int_main_check:
                print("Error: Multiple definitions of main function")
            self.int_main_check = True
        func = functionclass(returnType, name, parameter_list, self.priority)
        self.function_definition_map[name] = func
        self.function_definition_stack.append(func)
        self.variable_definition_stack += parameter_list
        for param in parameter_list:
            self.variable_definition_map[param.name] = param

    def exitFunctionDefinition(self, ctx):
        self.priority -= 1
        if (
            self.function_definition_stack[-1].returned == False
            and self.function_definition_stack[-1].returnType != "void"
            and not (
                self.function_definition_stack[-1].returnType == "int"
                and self.function_definition_stack[-1].name != "main"
            )
        ):
            print(
                "Error: Function "
                + self.function_definition_stack[-1].name
                + " does not return a value"
            )
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

    def enterVariableDeclaration(self, ctx):
        list = self.variableDeclaration_decode(ctx)
        self.variable_definition_stack += list
        for i in list:
            self.variable_definition_map[i.name] = i

    def enterClassDefinition(self, ctx):
        class_ = self.class_decode(ctx)
        self.usertype_map[class_.name] = class_

    def enterType(self, ctx):
        if (
            ctx.IDENTIFIER() != None
            and ctx.IDENTIFIER().getText() not in self.usertype_map.keys()
        ):
            print("Error: Undefined type")

    def enterExpressionStatement(self, ctx):
        self.return_expressiontype(ctx.expression())

    def enterIfStatement(self, ctx):
        if self.return_expressiontype(ctx.expression()) != "bool[0]":
            print("Error: if statement condition is not bool")

    def enterWhileStatement(self, ctx):
        self.loop += 1
        if self.return_expressiontype(ctx.expression()) != "bool[0]":
            print("Error: if statement condition is not bool")

    def exitWhileStatement(self, ctx):
        self.loop -= 1

    def enterForControl(self, ctx):
        expression = ctx.expression(1)
        if expression != None:
            if self.return_expressiontype(expression) != "bool[0]":
                print("Error: for statement condition is not bool")

    def enterForStatement(self, ctx):
        self.loop += 1

    def exitForStatement(self, ctx):
        self.loop -= 1

    def enterReturnStatement(self, ctx):
        returntype = self.function_definition_stack[-1].returnType
        expression = ctx.expression()
        if expression != None:
            if self.return_expressiontype(expression) != returntype:
                print(
                    "Error: return statement type does not match function return type"
                )
            self.function_definition_stack[-1].returned = True
        else:
            if returntype != "void":
                print(
                    "Error: return statement type does not match function return type"
                )

    def enterAssignmentStatement(self, ctx):
        if self.return_expressiontype(ctx.expression(0)) != self.return_expressiontype(
            ctx.expression(1)
        ):
            print("Error: assignment statement type does not match variable type")

    def enterBlock(self, ctx):
        self.priority += 1

    def exitBlock(self, ctx):
        self.priority -= 1

    def enterBreakStatement(self, ctx):
        if self.loop == 0:
            print("Error: break statement outside of loop")

    def enterContinueStatement(self, ctx):
        if self.loop == 0:
            print("Error: continue statement outside of loop")


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
