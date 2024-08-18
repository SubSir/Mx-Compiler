# Generated from Mx_parser.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .Mx_parserParser import Mx_parserParser
else:
    from Mx_parserParser import Mx_parserParser


# This class defines a complete listener for a parse tree produced by Mx_parserParser.
class Mx_parserListener(ParseTreeListener):

    # Enter a parse tree produced by Mx_parserParser#program.
    def enterProgram(self, ctx: Mx_parserParser.ProgramContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#program.
    def exitProgram(self, ctx: Mx_parserParser.ProgramContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#functionDefinition.
    def enterFunctionDefinition(self, ctx: Mx_parserParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#functionDefinition.
    def exitFunctionDefinition(self, ctx: Mx_parserParser.FunctionDefinitionContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#classDefinition.
    def enterClassDefinition(self, ctx: Mx_parserParser.ClassDefinitionContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#classDefinition.
    def exitClassDefinition(self, ctx: Mx_parserParser.ClassDefinitionContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx: Mx_parserParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx: Mx_parserParser.VariableDeclarationContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#variableDeclarationparts.
    def enterVariableDeclarationparts(
        self, ctx: Mx_parserParser.VariableDeclarationpartsContext
    ):
        pass

    # Exit a parse tree produced by Mx_parserParser#variableDeclarationparts.
    def exitVariableDeclarationparts(
        self, ctx: Mx_parserParser.VariableDeclarationpartsContext
    ):
        pass

    # Enter a parse tree produced by Mx_parserParser#classMember.
    def enterClassMember(self, ctx: Mx_parserParser.ClassMemberContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#classMember.
    def exitClassMember(self, ctx: Mx_parserParser.ClassMemberContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#construction.
    def enterConstruction(self, ctx: Mx_parserParser.ConstructionContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#construction.
    def exitConstruction(self, ctx: Mx_parserParser.ConstructionContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#functionBody.
    def enterFunctionBody(self, ctx: Mx_parserParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#functionBody.
    def exitFunctionBody(self, ctx: Mx_parserParser.FunctionBodyContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#emptyStatement.
    def enterEmptyStatement(self, ctx: Mx_parserParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#emptyStatement.
    def exitEmptyStatement(self, ctx: Mx_parserParser.EmptyStatementContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#expressionStatement.
    def enterExpressionStatement(self, ctx: Mx_parserParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#expressionStatement.
    def exitExpressionStatement(self, ctx: Mx_parserParser.ExpressionStatementContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#ifStatement.
    def enterIfStatement(self, ctx: Mx_parserParser.IfStatementContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#ifStatement.
    def exitIfStatement(self, ctx: Mx_parserParser.IfStatementContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#whileStatement.
    def enterWhileStatement(self, ctx: Mx_parserParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#whileStatement.
    def exitWhileStatement(self, ctx: Mx_parserParser.WhileStatementContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#forStatement.
    def enterForStatement(self, ctx: Mx_parserParser.ForStatementContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#forStatement.
    def exitForStatement(self, ctx: Mx_parserParser.ForStatementContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#returnStatement.
    def enterReturnStatement(self, ctx: Mx_parserParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#returnStatement.
    def exitReturnStatement(self, ctx: Mx_parserParser.ReturnStatementContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#privatevariableDeclaration.
    def enterPrivatevariableDeclaration(
        self, ctx: Mx_parserParser.PrivatevariableDeclarationContext
    ):
        pass

    # Exit a parse tree produced by Mx_parserParser#privatevariableDeclaration.
    def exitPrivatevariableDeclaration(
        self, ctx: Mx_parserParser.PrivatevariableDeclarationContext
    ):
        pass

    # Enter a parse tree produced by Mx_parserParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx: Mx_parserParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx: Mx_parserParser.AssignmentStatementContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#block.
    def enterBlock(self, ctx: Mx_parserParser.BlockContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#block.
    def exitBlock(self, ctx: Mx_parserParser.BlockContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#breakStatement.
    def enterBreakStatement(self, ctx: Mx_parserParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#breakStatement.
    def exitBreakStatement(self, ctx: Mx_parserParser.BreakStatementContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#continueStatement.
    def enterContinueStatement(self, ctx: Mx_parserParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#continueStatement.
    def exitContinueStatement(self, ctx: Mx_parserParser.ContinueStatementContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#elsestatement.
    def enterElsestatement(self, ctx: Mx_parserParser.ElsestatementContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#elsestatement.
    def exitElsestatement(self, ctx: Mx_parserParser.ElsestatementContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#assignment.
    def enterAssignment(self, ctx: Mx_parserParser.AssignmentContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#assignment.
    def exitAssignment(self, ctx: Mx_parserParser.AssignmentContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#forControl.
    def enterForControl(self, ctx: Mx_parserParser.ForControlContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#forControl.
    def exitForControl(self, ctx: Mx_parserParser.ForControlContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#expression1.
    def enterExpression1(self, ctx: Mx_parserParser.Expression1Context):
        pass

    # Exit a parse tree produced by Mx_parserParser#expression1.
    def exitExpression1(self, ctx: Mx_parserParser.Expression1Context):
        pass

    # Enter a parse tree produced by Mx_parserParser#expression2.
    def enterExpression2(self, ctx: Mx_parserParser.Expression2Context):
        pass

    # Exit a parse tree produced by Mx_parserParser#expression2.
    def exitExpression2(self, ctx: Mx_parserParser.Expression2Context):
        pass

    # Enter a parse tree produced by Mx_parserParser#expression3.
    def enterExpression3(self, ctx: Mx_parserParser.Expression3Context):
        pass

    # Exit a parse tree produced by Mx_parserParser#expression3.
    def exitExpression3(self, ctx: Mx_parserParser.Expression3Context):
        pass

    # Enter a parse tree produced by Mx_parserParser#logicalNotExpression.
    def enterLogicalNotExpression(
        self, ctx: Mx_parserParser.LogicalNotExpressionContext
    ):
        pass

    # Exit a parse tree produced by Mx_parserParser#logicalNotExpression.
    def exitLogicalNotExpression(
        self, ctx: Mx_parserParser.LogicalNotExpressionContext
    ):
        pass

    # Enter a parse tree produced by Mx_parserParser#postfixIncrementExpression.
    def enterPostfixIncrementExpression(
        self, ctx: Mx_parserParser.PostfixIncrementExpressionContext
    ):
        pass

    # Exit a parse tree produced by Mx_parserParser#postfixIncrementExpression.
    def exitPostfixIncrementExpression(
        self, ctx: Mx_parserParser.PostfixIncrementExpressionContext
    ):
        pass

    # Enter a parse tree produced by Mx_parserParser#constantExpression.
    def enterConstantExpression(self, ctx: Mx_parserParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#constantExpression.
    def exitConstantExpression(self, ctx: Mx_parserParser.ConstantExpressionContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#muldivmodExpression.
    def enterMuldivmodExpression(self, ctx: Mx_parserParser.MuldivmodExpressionContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#muldivmodExpression.
    def exitMuldivmodExpression(self, ctx: Mx_parserParser.MuldivmodExpressionContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#plusminusExpression.
    def enterPlusminusExpression(self, ctx: Mx_parserParser.PlusminusExpressionContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#plusminusExpression.
    def exitPlusminusExpression(self, ctx: Mx_parserParser.PlusminusExpressionContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#shiftExpression.
    def enterShiftExpression(self, ctx: Mx_parserParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#shiftExpression.
    def exitShiftExpression(self, ctx: Mx_parserParser.ShiftExpressionContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#arrayExpression.
    def enterArrayExpression(self, ctx: Mx_parserParser.ArrayExpressionContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#arrayExpression.
    def exitArrayExpression(self, ctx: Mx_parserParser.ArrayExpressionContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#relationalExpression.
    def enterRelationalExpression(
        self, ctx: Mx_parserParser.RelationalExpressionContext
    ):
        pass

    # Exit a parse tree produced by Mx_parserParser#relationalExpression.
    def exitRelationalExpression(
        self, ctx: Mx_parserParser.RelationalExpressionContext
    ):
        pass

    # Enter a parse tree produced by Mx_parserParser#conditionalExpression.
    def enterConditionalExpression(
        self, ctx: Mx_parserParser.ConditionalExpressionContext
    ):
        pass

    # Exit a parse tree produced by Mx_parserParser#conditionalExpression.
    def exitConditionalExpression(
        self, ctx: Mx_parserParser.ConditionalExpressionContext
    ):
        pass

    # Enter a parse tree produced by Mx_parserParser#postfixDecrementExpression.
    def enterPostfixDecrementExpression(
        self, ctx: Mx_parserParser.PostfixDecrementExpressionContext
    ):
        pass

    # Exit a parse tree produced by Mx_parserParser#postfixDecrementExpression.
    def exitPostfixDecrementExpression(
        self, ctx: Mx_parserParser.PostfixDecrementExpressionContext
    ):
        pass

    # Enter a parse tree produced by Mx_parserParser#prefixDecrementExpression.
    def enterPrefixDecrementExpression(
        self, ctx: Mx_parserParser.PrefixDecrementExpressionContext
    ):
        pass

    # Exit a parse tree produced by Mx_parserParser#prefixDecrementExpression.
    def exitPrefixDecrementExpression(
        self, ctx: Mx_parserParser.PrefixDecrementExpressionContext
    ):
        pass

    # Enter a parse tree produced by Mx_parserParser#variableExpression.
    def enterVariableExpression(self, ctx: Mx_parserParser.VariableExpressionContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#variableExpression.
    def exitVariableExpression(self, ctx: Mx_parserParser.VariableExpressionContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#prefixIncrementExpression.
    def enterPrefixIncrementExpression(
        self, ctx: Mx_parserParser.PrefixIncrementExpressionContext
    ):
        pass

    # Exit a parse tree produced by Mx_parserParser#prefixIncrementExpression.
    def exitPrefixIncrementExpression(
        self, ctx: Mx_parserParser.PrefixIncrementExpressionContext
    ):
        pass

    # Enter a parse tree produced by Mx_parserParser#newVariableExpression.
    def enterNewVariableExpression(
        self, ctx: Mx_parserParser.NewVariableExpressionContext
    ):
        pass

    # Exit a parse tree produced by Mx_parserParser#newVariableExpression.
    def exitNewVariableExpression(
        self, ctx: Mx_parserParser.NewVariableExpressionContext
    ):
        pass

    # Enter a parse tree produced by Mx_parserParser#unaryMinusExpression.
    def enterUnaryMinusExpression(
        self, ctx: Mx_parserParser.UnaryMinusExpressionContext
    ):
        pass

    # Exit a parse tree produced by Mx_parserParser#unaryMinusExpression.
    def exitUnaryMinusExpression(
        self, ctx: Mx_parserParser.UnaryMinusExpressionContext
    ):
        pass

    # Enter a parse tree produced by Mx_parserParser#parenthesesExpression.
    def enterParenthesesExpression(
        self, ctx: Mx_parserParser.ParenthesesExpressionContext
    ):
        pass

    # Exit a parse tree produced by Mx_parserParser#parenthesesExpression.
    def exitParenthesesExpression(
        self, ctx: Mx_parserParser.ParenthesesExpressionContext
    ):
        pass

    # Enter a parse tree produced by Mx_parserParser#memberFunctionCall.
    def enterMemberFunctionCall(self, ctx: Mx_parserParser.MemberFunctionCallContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#memberFunctionCall.
    def exitMemberFunctionCall(self, ctx: Mx_parserParser.MemberFunctionCallContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#bitwiseNotExpression.
    def enterBitwiseNotExpression(
        self, ctx: Mx_parserParser.BitwiseNotExpressionContext
    ):
        pass

    # Exit a parse tree produced by Mx_parserParser#bitwiseNotExpression.
    def exitBitwiseNotExpression(
        self, ctx: Mx_parserParser.BitwiseNotExpressionContext
    ):
        pass

    # Enter a parse tree produced by Mx_parserParser#functionCall.
    def enterFunctionCall(self, ctx: Mx_parserParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#functionCall.
    def exitFunctionCall(self, ctx: Mx_parserParser.FunctionCallContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#andxororExpression.
    def enterAndxororExpression(self, ctx: Mx_parserParser.AndxororExpressionContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#andxororExpression.
    def exitAndxororExpression(self, ctx: Mx_parserParser.AndxororExpressionContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#logicExpression.
    def enterLogicExpression(self, ctx: Mx_parserParser.LogicExpressionContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#logicExpression.
    def exitLogicExpression(self, ctx: Mx_parserParser.LogicExpressionContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#memberMemberCall.
    def enterMemberMemberCall(self, ctx: Mx_parserParser.MemberMemberCallContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#memberMemberCall.
    def exitMemberMemberCall(self, ctx: Mx_parserParser.MemberMemberCallContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#newArrayExpression.
    def enterNewArrayExpression(self, ctx: Mx_parserParser.NewArrayExpressionContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#newArrayExpression.
    def exitNewArrayExpression(self, ctx: Mx_parserParser.NewArrayExpressionContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#square_brackets1.
    def enterSquare_brackets1(self, ctx: Mx_parserParser.Square_brackets1Context):
        pass

    # Exit a parse tree produced by Mx_parserParser#square_brackets1.
    def exitSquare_brackets1(self, ctx: Mx_parserParser.Square_brackets1Context):
        pass

    # Enter a parse tree produced by Mx_parserParser#square_brackets2.
    def enterSquare_brackets2(self, ctx: Mx_parserParser.Square_brackets2Context):
        pass

    # Exit a parse tree produced by Mx_parserParser#square_brackets2.
    def exitSquare_brackets2(self, ctx: Mx_parserParser.Square_brackets2Context):
        pass

    # Enter a parse tree produced by Mx_parserParser#expressionLists.
    def enterExpressionLists(self, ctx: Mx_parserParser.ExpressionListsContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#expressionLists.
    def exitExpressionLists(self, ctx: Mx_parserParser.ExpressionListsContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#logicOperator.
    def enterLogicOperator(self, ctx: Mx_parserParser.LogicOperatorContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#logicOperator.
    def exitLogicOperator(self, ctx: Mx_parserParser.LogicOperatorContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#relationalOperator.
    def enterRelationalOperator(self, ctx: Mx_parserParser.RelationalOperatorContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#relationalOperator.
    def exitRelationalOperator(self, ctx: Mx_parserParser.RelationalOperatorContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#parameterList.
    def enterParameterList(self, ctx: Mx_parserParser.ParameterListContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#parameterList.
    def exitParameterList(self, ctx: Mx_parserParser.ParameterListContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#parameter.
    def enterParameter(self, ctx: Mx_parserParser.ParameterContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#parameter.
    def exitParameter(self, ctx: Mx_parserParser.ParameterContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#type.
    def enterType(self, ctx: Mx_parserParser.TypeContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#type.
    def exitType(self, ctx: Mx_parserParser.TypeContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#arrayType.
    def enterArrayType(self, ctx: Mx_parserParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#arrayType.
    def exitArrayType(self, ctx: Mx_parserParser.ArrayTypeContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#returnType.
    def enterReturnType(self, ctx: Mx_parserParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#returnType.
    def exitReturnType(self, ctx: Mx_parserParser.ReturnTypeContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#constant.
    def enterConstant(self, ctx: Mx_parserParser.ConstantContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#constant.
    def exitConstant(self, ctx: Mx_parserParser.ConstantContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#array_constant.
    def enterArray_constant(self, ctx: Mx_parserParser.Array_constantContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#array_constant.
    def exitArray_constant(self, ctx: Mx_parserParser.Array_constantContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#fstring.
    def enterFstring(self, ctx: Mx_parserParser.FstringContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#fstring.
    def exitFstring(self, ctx: Mx_parserParser.FstringContext):
        pass

    # Enter a parse tree produced by Mx_parserParser#string_constant.
    def enterString_constant(self, ctx: Mx_parserParser.String_constantContext):
        pass

    # Exit a parse tree produced by Mx_parserParser#string_constant.
    def exitString_constant(self, ctx: Mx_parserParser.String_constantContext):
        pass


del Mx_parserParser
