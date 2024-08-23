// 定义语言的名称和版本
grammar Mx_parser;
// 程序入口点
program: (
		functionDefinition
		| classDefinition
		| variableDeclaration ';'
	)* EOF;

// 函数定义
functionDefinition:
	returnType IDENTIFIER '(' parameterList? ')' functionBody;

// 类定义
classDefinition: 'class' IDENTIFIER '{' classMember* '}' ';';

// 变量声明
variableDeclaration:
	type variableDeclarationparts (',' variableDeclarationparts)*
	| arrayType variableDeclarationparts (
		',' variableDeclarationparts
	)*;

variableDeclarationparts: IDENTIFIER ('=' expression)?;

// 类成员
classMember:
	variableDeclaration ';'
	| construction
	| functionDefinition;

construction: IDENTIFIER '(' ')' functionBody;
// 函数体
functionBody: '{' (statement)* '}';

// 语句
statement:
	';'														# emptyStatement
	| expression ';'										# expressionStatement
	| 'if' '(' expression ')' statement (elsestatement)?	# ifStatement
	| 'while' '(' expression ')' statement					# whileStatement
	| 'for' '(' forControl ')' statement					# forStatement
	| 'return' expression? ';'								# returnStatement
	| variableDeclaration ';'								# privatevariableDeclaration
	| assignment ';'										# assignmentStatement
	| '{' statement* '}'									# block
	| 'break' ';'											# breakStatement
	| 'continue' ';'										# continueStatement;

elsestatement: 'else' statement;

assignment: expression '=' expression;

// for循环控制结构
forControl: (expression1? ';' expression2? ';' expression3?);

expression1: expression | assignment | variableDeclaration;
expression2: expression;
expression3: expression | assignment;

// 表达式
expression:
	expression (square_brackets1 expression square_brackets2)	# arrayExpression
	| expression '++'											# postfixIncrementExpression
	| expression '--'											# postfixDecrementExpression
	| '++' expression											# prefixIncrementExpression
	| '--' expression											# prefixDecrementExpression
	| '!' expression											# logicalNotExpression
	| '~' expression											# bitwiseNotExpression
	| '-' expression											# unaryMinusExpression
	| IDENTIFIER '(' expressionLists? ')'						# functionCall
	| expression '.' IDENTIFIER ('(' expressionLists? ')')		# memberFunctionCall
	| expression '.' IDENTIFIER									# memberMemberCall
	| constant													# constantExpression
	| 'new' type (square_brackets1 expression? square_brackets2)(square_brackets1 expression square_brackets2)* (
		square_brackets1 square_brackets2
	)* (array_constant)?										# newArrayExpression
	| 'new' type ('(' ')')?										# newVariableExpression
	| IDENTIFIER												# variableExpression
	| expression (MUL | DIV | MOD) expression					# muldivmodExpression
	| expression (PLUS | MINUS) expression						# plusminusExpression
	| expression (LSHIFT | RSHIFT) expression					# shiftExpression
	| expression (AND | XOR | OR) expression					# andxororExpression
	| '(' expression ')'										# parenthesesExpression
	| expression relationalOperator expression					# relationalExpression
	| expression '&&' expression								# logicANDExpression
	| expression '||' expression								# logicORExpression
	| <assoc = right> expression '?' expression ':' expression	# conditionalExpression;

square_brackets1: '[';
square_brackets2: ']';
expressionLists: expression (',' expression)*;

// 运算符
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
LSHIFT: '<<';
RSHIFT: '>>';
AND: '&';
XOR: '^';
OR: '|';
LPAREN: '(';
RPAREN: ')';

// 关系运算符
relationalOperator: '<' | '>' | '<=' | '>=' | '==' | '!=';

// 函数参数列表
parameterList: parameter (',' parameter)*;

// 函数参数
parameter: type IDENTIFIER | arrayType IDENTIFIER;

// 类型定义
type: 'int' | 'bool' | 'string' | IDENTIFIER;

// 基本类型数组
arrayType: type ('[' ']')+;

// 返回类型
returnType:
	'int'
	| 'bool'
	| 'string'
	| 'void'
	| IDENTIFIER
	| arrayType;

// 常量
constant:
	INTEGER_CONSTANT
	| string_constant
	| 'true'
	| 'false'
	| 'null'
	| array_constant;

array_constant: '{' (expression (',' expression)*)? '}';

// 标识符
IDENTIFIER: [a-zA-Z] [a-zA-Z0-9_]*;

// 整数常量
INTEGER_CONSTANT: [0-9]+;

// 注释
LINE_COMMENT: '//' ~[\r\n]* -> skip;

BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// F-string的规则
fstring:
	FSTRING_PART1 expression (FSTRING_MIDDLE_PART expression)* FSTRING_PART2;

FSTRING_PART1: 'f"' ( ESC2 | ~[\r\n"$])* '$';

STRING_CONTENT: '"' ( ESC | ~[\r\n"])* '"';

FSTRING_PART2: '$' ( ESC2 | ~[\r\n"$])* '"';

ESC: '\\' (['"\\nrt]);
ESC2: '\\' (['"\\nrt]) | '$$';

FSTRING_MIDDLE_PART: '$' ( ESC2 | ~[\r\n"$])* '$';

// 用于解析字符串常量
string_constant: STRING_CONTENT | fstring;

// 空白符
WS: [ \t\r\n]+ -> skip;