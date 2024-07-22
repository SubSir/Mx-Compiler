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
classDefinition: 'class' IDENTIFIER '{' classMember* '}';

// 全局变量声明
globalVariableDeclaration: variableDeclaration;

// 变量声明
variableDeclaration:
	type IDENTIFIER (',' IDENTIFIER)* ';'
	| type IDENTIFIER '=' expression ';';

// 类成员
classMember:
	type IDENTIFIER (',' IDENTIFIER)* ';'
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
	| IDENTIFIER '[' expression ']' '=' expression ';'		# arrayAssignment
	| IDENTIFIER '=' expression ';'							# assignment
	| '{' statement* '}'									# block
	| 'break' ';'											# breakStatement
	| 'continue' ';'										# continueStatement;

// for循环控制结构
forControl: (expression? ';' expression? ';' expression?);

// 表达式
expression:
	assignmentExpression (',' assignmentExpression)*		# expressionList
	| expression logicOperator expression					# logicExpression
	| expression '?' expression ':' expression				# conditionalExpression
	| expression relationalOperator expression				# relationalExpression
	| expression arithmeticOperator expression				# arithmeticExpression
	| '++' expression										# prefixIncrementExpression
	| expression '++'										# postfixIncrementExpression
	| '--' expression										# postfixDecrementExpression
	| expression '--'										# postfixDecrementExpression
	| '!' expression										# logicalNotExpression
	| '~' expression										# bitwiseNotExpression
	| '-' expression										# unaryMinusExpression
	| IDENTIFIER '(' (expression (',' expression)*)? ')'	# functionCall
	| IDENTIFIER '.' IDENTIFIER '(' (
		expression (',' expression)*
	)? ')'										# memberFunctionCall
	| expression '[' expression ']'				# arrayAccess
	| constant									# constantExpression
	| 'new' arrayType '[' INTEGER_CONSTANT ']'	# newArrayExpression
	| IDENTIFIER								# variableExpression
	| '(' expression ')'						# parenthesesExpression;

// 赋值表达式
assignmentExpression: IDENTIFIER assignmentOperator expression;

// 逻辑运算符
logicOperator: '&&' | '||';

// 赋值运算符
assignmentOperator:
	'='
	| '+='
	| '-='
	| '*='
	| '/='
	| '%='
	| '<<='
	| '>>='
	| '&='
	| '^='
	| '|=';

// 算术运算符
arithmeticOperator:
	'+'
	| '-'
	| '*'
	| '/'
	| '%'
	| '<<'
	| '>>'
	| '&'
	| '^'
	| '|';

// 关系运算符
relationalOperator: '<' | '>' | '<=' | '>=' | '==' | '!=';

// 函数参数列表
parameterList: parameter (',' parameter)*;

// 函数参数
parameter: type IDENTIFIER;

// 类型定义
type:
	'int'
	| 'bool'
	| 'string'
	| 'void'
	| 'string'
	| IDENTIFIER
	| type '[]'; // 类型或用户定义类型

// 基本类型数组
arrayType: type ('[' ']')?;

// 返回类型
returnType: 'int' | 'bool' | 'string' | 'void';

// 常量
constant:
	INTEGER_CONSTANT
	| STRING_CONSTANT
	| 'true'
	| 'false'
	| 'null';

// 标识符
IDENTIFIER: [a-zA-Z] [a-zA-Z0-9_]*;

// 整数常量
INTEGER_CONSTANT: [0-9]+;

// 用于解析字符串常量
STRING_CONSTANT: '"' (ESC | ~[\r\n"])* '"';
ESC: '\\' (['"\\nrt]);

// 注释
LINE_COMMENT: '//' ~[\r\n]* -> skip;

BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// 空白符
WS: [ \t\r\n]+ -> skip;