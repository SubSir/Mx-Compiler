// 定义语言的名称和版本
grammar Mx_parser;
// 程序入口点
program: (
		functionDefinition
		| classDefinition
		| globalVariableDeclaration
	)* EOF;

// 函数定义
functionDefinition:
	returnType IDENTIFIER '(' parameterList? ')' functionBody;

// 类定义
classDefinition: 'class' IDENTIFIER '{' classMember* '}' ';';

// 全局变量声明
globalVariableDeclaration: variableDeclaration;

// 变量声明
variableDeclaration:
	type variableDeclarationparts (',' variableDeclarationparts)* ';'
	| arrayType variableDeclarationparts (
		',' variableDeclarationparts
	)* ';';

variableDeclarationparts: IDENTIFIER ('=' expression)?;

// 类成员
classMember:
	variableDeclaration
	| IDENTIFIER '(' parameterList? ')' functionBody
	| functionDefinition;

// 函数体
functionBody: '{' (statement)* '}';

// 语句
statement:
	';'														# emptyStatement
	| expression ';'										# expressionStatement
	| 'if' '(' expression ')' statement ('else' statement)?	# ifStatement
	| 'while' '(' expression ')' statement					# whileStatement
	| 'for' '(' forControl ')' statement					# forStatement
	| 'return' expression? ';'								# returnStatement
	| variableDeclaration									# privatevariableDeclaration
	| expression '=' expression ';'							# assignmentStatement
	| '{' statement* '}'									# block
	| 'break' ';'											# breakStatement
	| 'continue' ';'										# continueStatement;

// for循环控制结构
forControl: (expression? ';' expression? ';' expression?);

// 表达式
expression:
	IDENTIFIER '=' expression								# expressionList
	| expression logicOperator expression					# logicExpression
	| expression '?' expression ':' expression				# conditionalExpression
	| expression relationalOperator expression				# relationalExpression
	| expression (MUL | DIV | MOD) expression				# muldivmodExpression
	| expression (PLUS | MINUS) expression					# plusminusExpression
	| expression (LSHIFT | RSHIFT) expression				# shiftExpression
	| expression (AND | XOR | OR) expression				# andxororExpression
	| '++' expression										# prefixIncrementExpression
	| expression '++'										# postfixIncrementExpression
	| '--' expression										# prefixDecrementExpression
	| expression '--'										# postfixDecrementExpression
	| '!' expression										# logicalNotExpression
	| '~' expression										# bitwiseNotExpression
	| '-' expression										# unaryMinusExpression
	| IDENTIFIER '(' (expression (',' expression)*)? ')'	# functionCall
	| expression '.' IDENTIFIER (
		'(' ( expression (',' expression)*)? ')'
	)?															# memberFunctionCall
	| constant													# constantExpression
	| 'new' type												# newVariableExpression
	| 'new' type ('[' expression ']')* ('[' expression? ']')+	# newArrayExpression
	| IDENTIFIER												# variableExpression
	| expression ('[' expression ']')* ('[' expression? ']')+	# arrayExpression
	| '(' expression ')'										# parenthesesExpression;

// 逻辑运算符
logicOperator: '&&' | '||';

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
returnType: 'int' | 'bool' | 'string' | 'void' | IDENTIFIER;

// 常量
constant:
	INTEGER_CONSTANT
	| string_constant
	| 'true'
	| 'false'
	| 'null';

// 标识符
IDENTIFIER: [a-zA-Z] [a-zA-Z0-9_]*;

// 整数常量
INTEGER_CONSTANT: [0-9]+;

// 注释
LINE_COMMENT: '//' ~[\r\n]* -> skip;

BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// 空白符
WS: [ \t\r\n]+ -> skip;

// F-string的规则
fstring:
	'f"' (
		(text = STRING_CONTENT)? format_expression (
			text = STRING_CONTENT
		)?
	)* '"';

// 格式化表达式的规则
format_expression: '$' expression '$';

STRING_CONTENT: '"' ( ESC | ~[\r\n"])* '"';

ESC: '\\' (['"\\nrt]);

// 用于解析字符串常量
string_constant: STRING_CONTENT | format_expression;