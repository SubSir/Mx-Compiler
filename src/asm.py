#!/usr/bin/python3
import sys
import copy
from antlr4 import InputStream, CommonTokenStream
import antlr4
from llvmparser.llvmListener import llvmListener
from llvmparser.llvmLexer import llvmLexer
from llvmparser.llvmParser import llvmParser
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Tree import ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener


class Mylistener3(llvmListener):
    return_str = ".text\n"
    enter_label = ""
    enter_function = ""
    data = ".data\n"
    variable_map = {}
    variable_cnt = 0
    label_map = {}

    def enterRet(self, ctx: llvmParser.RetContext):
        if ctx.value() != None:
            value = ctx.value()
            name = ctx.value().getText()
            if value.Privatevariable() != None:
                self.return_str += "\tlw a0, " + str(self.variable_map[name]) + "(sp)\n"
            elif value.Global_var() != None:
                self.return_str += "\tla a0, " + name[1:] + "\n"
            else:
                if name == "null":
                    name = "0"
                self.return_str += "\tli a0, " + name + "\n"
        self.return_str += "\tlw ra, 0(sp)\n"
        self.return_str += "\taddi sp, sp, " + str(self.variable_cnt) + "\n"
        self.return_str += "\tret\n"

    def params_decode(self, code: llvmParser.ParamsContext):
        params = code.parameter()
        for i in range(min(len(params), 8)):
            param = params[i]
            if param.Global_var() != None:
                name = param.Global_var().getText()[1:]
                if name[0] == ".":
                    self.return_str += "\tla a" + str(i) + ", " + name + "\n"
                else:
                    self.return_str += "\tlw a" + str(i) + ", " + name + "\n"
            elif param.Privatevariable() != None:
                name = param.Privatevariable().getText()
                self.return_str += (
                    "\tlw a" + str(i) + ", " + str(self.variable_map[name]) + "(sp)\n"
                )
            else:
                name = param.constant().getText()
                if name == "null":
                    name = "0"
                self.return_str += "\tli a" + str(i) + ", " + name + "\n"
        if len(params) > 8:
            self.return_str += "\taddi sp, sp, -" + str((len(params) - 8) * 4) + "\n"
            for i in range(len(params) - 8):
                param = params[i + 8]
                if param.Global_var() != None:
                    name = param.Global_var().getText()[1:]
                    if name[0] == ".":
                        self.return_str += "\tla t0, " + name + "\n"
                    else:
                        self.return_str += "\tlw t0, " + name + "\n"
                elif param.Privatevariable() != None:
                    name = param.Privatevariable().getText()
                    self.return_str += (
                        "\tlw t0, " + str(self.variable_map[name]) + "(sp)\n"
                    )
                else:
                    name = param.constant().getText()
                    if name == "null":
                        name = "0"
                    self.return_str += "\tli t0, " + name + "\n"
                self.return_str += "\tsw t0, " + str(i * 4) + "(sp)\n"

    def enterCall(self, ctx: llvmParser.CallContext):
        i = 0
        if ctx.params() != None:
            self.params_decode(ctx.params())
            i = len(ctx.params().parameter())
        self.return_str += "\tcall " + ctx.Global_var().getText()[1:] + "\n"
        if i > 8:
            self.return_str += "\taddi sp, sp, " + str((i - 8) * 4) + "\n"
        if ctx.Privatevariable() != None:
            self.return_str += (
                "\tsw a0, "
                + str(self.variable_map[ctx.Privatevariable().getText()])
                + "(sp)\n"
            )

    def enterBinary_op(self, ctx: llvmParser.Binary_opContext):
        value1 = ctx.value(0)
        value2 = ctx.value(1)
        if value1.Privatevariable() != None:
            self.return_str += (
                "\tlw t1, "
                + str(self.variable_map[value1.Privatevariable().getText()])
                + "(sp)\n"
            )
        elif value1.Global_var() != None:
            self.return_str += "\tla t1, " + value1.Global_var().getText() + "\n"
        else:
            name = value1.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t1, " + name + "\n"
        if value2.Privatevariable() != None:
            self.return_str += (
                "\tlw t2, "
                + str(self.variable_map[value2.Privatevariable().getText()])
                + "(sp)\n"
            )
        elif value2.Global_var() != None:
            self.return_str += "\tla t2, " + value2.Global_var().getText() + "\n"
        else:
            name = value2.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t2, " + name + "\n"
        op = ctx.bin_op().getText()
        if op == "add":
            self.return_str += "\tadd t0, t1, t2\n"
        elif op == "sub":
            self.return_str += "\tsub t0, t1, t2\n"
        elif op == "mul":
            self.return_str += "\tmul t0, t1, t2\n"
        elif op == "sdiv":
            self.return_str += "\tdiv t0, t1, t2\n"
        elif op == "srem":
            self.return_str += "\trem t0, t1, t2\n"
        elif op == "shl":
            self.return_str += "\tsll t0, t1, t2\n"
        elif op == "ashr":
            self.return_str += "\tsra t0, t1, t2\n"
        elif op == "and":
            self.return_str += "\tand t0, t1, t2\n"
        elif op == "or":
            self.return_str += "\tor t0, t1, t2\n"
        elif op == "xor":
            self.return_str += "\txor t0, t1, t2\n"
        else:
            sys.exit(1)
        self.return_str += (
            "\tsw t0, "
            + str(self.variable_map[ctx.Privatevariable().getText()])
            + "(sp)\n"
        )

    def enterBranch(self, ctx: llvmParser.BranchContext):
        if ctx.value() != None:
            value = ctx.value()
            if value.Privatevariable() != None:
                self.return_str += (
                    "\tlw t0, "
                    + str(self.variable_map[value.Privatevariable().getText()])
                    + "(sp)\n"
                )
            else:
                name = value.getText()
                if name == "null":
                    name = "0"
                self.return_str += "\tli t0, " + name + "\n"
            label1 = self.enter_label + ctx.Label(0).getText()
            label2 = self.enter_label + ctx.Label(1).getText()
            self.return_str += "\tbnez t0, " + label1 + "\n"
            self.return_str += "\tj " + label2 + "\n"
            if label1 not in self.label_map:
                self.label_map[label1] = (
                    "\tj " + self.enter_function + ctx.Label(0).getText() + "\n"
                )
            else:
                self.label_map[label1] += (
                    "\tj " + self.enter_function + ctx.Label(0).getText() + "\n"
                )
            if label2 not in self.label_map:
                self.label_map[label2] = (
                    "\tj " + self.enter_function + ctx.Label(1).getText() + "\n"
                )
            else:
                self.label_map[label2] += (
                    "\tj " + self.enter_function + ctx.Label(1).getText() + "\n"
                )
            return
        label = self.enter_label + ctx.Label(0).getText()
        self.return_str += "\tj " + label + "\n"
        if label not in self.label_map:
            self.label_map[label] = (
                "\tj " + self.enter_function + ctx.Label(0).getText() + "\n"
            )
        else:
            self.label_map[label] += (
                "\tj " + self.enter_function + ctx.Label(0).getText() + "\n"
            )

    def enterLoad(self, ctx: llvmParser.LoadContext):
        var = ctx.var()
        if var.Privatevariable() != None:
            self.return_str += (
                "\tlw t1, "
                + str(self.variable_map[var.Privatevariable().getText()])
                + "(sp)\n"
            )
            self.return_str += "\tlw t0, 0(t1)\n"
            self.return_str += (
                "\tsw t0,"
                + str(self.variable_map[ctx.Privatevariable().getText()])
                + "(sp)\n"
            )
            return
        name = var.Global_var().getText()[1:]
        self.return_str += "\tlw t0, " + name + "\n"
        self.return_str += (
            "\tsw t0,"
            + str(self.variable_map[ctx.Privatevariable().getText()])
            + "(sp)\n"
        )

    def enterGetelementptr(self, ctx: llvmParser.GetelementptrContext):
        value = ctx.value()
        if value.Privatevariable() != None:
            self.return_str += (
                "\tlw t2, "
                + str(self.variable_map[value.Privatevariable().getText()])
                + "(sp)\n"
            )
        else:
            name = value.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t2, " + name + "\n"
        self.return_str += "\tslli t2, t2, 2\n"
        var = ctx.var()
        if var.Privatevariable() != None:
            self.return_str += (
                "\tlw t1, "
                + str(self.variable_map[var.Privatevariable().getText()])
                + "(sp)\n"
            )
            self.return_str += "\tadd t0, t1, t2\n"
            self.return_str += (
                "\tsw t0,"
                + str(self.variable_map[ctx.Privatevariable().getText()])
                + "(sp)\n"
            )
            return
        name = var.Global_var().getText()[1:]
        self.return_str += "\tlw t0, " + name + "\n"
        self.return_str += "\tadd t0, t0, t2\n"
        self.return_str += (
            "\tsw t0,"
            + str(self.variable_map[ctx.Privatevariable().getText()])
            + "(sp)\n"
        )

    def enterStore(self, ctx: llvmParser.StoreContext):
        value = ctx.value()
        if value.Privatevariable() != None:
            self.return_str += (
                "\tlw t1, "
                + str(self.variable_map[value.Privatevariable().getText()])
                + "(sp)\n"
            )
        elif value.Global_var() != None:
            self.return_str += "\tla t1, " + value.Global_var().getText()[1:] + "\n"
        else:
            name = value.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t1, " + name + "\n"
        var = ctx.var()
        if var.Privatevariable() != None:
            self.return_str += (
                "\tlw t0, "
                + str(self.variable_map[var.Privatevariable().getText()])
                + "(sp)\n"
            )
            self.return_str += "\tsw t1, 0(t0)\n"
            return
        name = var.Global_var().getText()[1:]
        self.return_str += "\tsw t1, " + name + ", t2\n"

    def enterCompare(self, ctx: llvmParser.CompareContext):
        value1 = ctx.value(0)
        if value1.Privatevariable() != None:
            self.return_str += (
                "\tlw t1, "
                + str(self.variable_map[value1.Privatevariable().getText()])
                + "(sp)\n"
            )
        elif value1.Global_var() != None:
            self.return_str += "\tla t1, " + value1.Global_var().getText()[1:] + "\n"
        else:
            name = value1.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t1, " + name + "\n"
        value2 = ctx.value(1)
        if value2.Privatevariable() != None:
            self.return_str += (
                "\tlw t2, "
                + str(self.variable_map[value2.Privatevariable().getText()])
                + "(sp)\n"
            )
        elif value2.Global_var() != None:
            self.return_str += "\tla t2, " + value2.Global_var().getText()[1:] + "\n"
        else:
            name = value2.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t2, " + name + "\n"
        op = ctx.cond().getText()
        if op == "eq":
            self.return_str += "\txor t1, t1, t2\n"
            self.return_str += "\tseqz t0, t1\n"
        elif op == "ne":
            self.return_str += "\txor t1, t1, t2\n"
            self.return_str += "\tsnez t0, t1\n"
        elif op == "slt":
            self.return_str += "\tslt t0, t1, t2\n"
        elif op == "sgt":
            self.return_str += "\tslt t0, t2, t1\n"
        elif op == "sle":
            self.return_str += "\tslt t0, t2, t1\n"
            self.return_str += "\txori t0, t0, 1\n"
        elif op == "sge":
            self.return_str += "\tslt t0, t1, t2\n"
            self.return_str += "\txori t0, t0, 1\n"
        else:
            sys.exit(1)
        privatevariable = ctx.Privatevariable()
        self.return_str += (
            "\tsw t0, " + str(self.variable_map[privatevariable.getText()]) + "(sp)\n"
        )

    def enterPhi(self, ctx: llvmParser.PhiContext):
        label1 = (
            self.enter_function
            + ctx.Label(0).getText()
            + self.enter_label[len(self.enter_function) :]
        )
        label2 = (
            self.enter_function
            + ctx.Label(1).getText()
            + self.enter_label[len(self.enter_function) :]
        )
        value1 = ctx.value(0)
        value2 = ctx.value(1)
        value1_str = ""
        value2_str = ""
        if value1.Privatevariable() != None:
            value1_str += (
                "\tlw t1, "
                + str(self.variable_map[value1.Privatevariable().getText()])
                + "(sp)\n"
            )
        elif value1.Global_var() != None:
            value1_str += "\tla t1, " + value1.Global_var().getText()[1:] + "\n"
        else:
            name = value1.getText()
            if name == "null":
                name = "0"
            value1_str += "\tli t1, " + name + "\n"
        if value2.Privatevariable() != None:
            value2_str += (
                "\tlw t2, "
                + str(self.variable_map[value2.Privatevariable().getText()])
                + "(sp)\n"
            )
        elif value2.Global_var() != None:
            value2_str += "\tla t2, " + value2.Global_var().getText()[1:] + "\n"
        else:
            name = value2.getText()
            if name == "null":
                name = "0"
            value2_str += "\tli t2, " + name + "\n"
        if label1 not in self.label_map:
            self.label_map[label1] = (
                value1_str
                + "\tsw t1, "
                + str(self.variable_map[ctx.Privatevariable().getText()])
                + "(sp)\n"
            )
        else:
            self.label_map[label1] = (
                value1_str
                + "\tsw t1, "
                + str(self.variable_map[ctx.Privatevariable().getText()])
                + "(sp)\n"
                + self.label_map[label1]
            )
        if label2 not in self.label_map:
            self.label_map[label2] = (
                value2_str
                + "\tsw t2, "
                + str(self.variable_map[ctx.Privatevariable().getText()])
                + "(sp)\n"
            )
        else:
            self.label_map[label2] = (
                value2_str
                + "\tsw t2, "
                + str(self.variable_map[ctx.Privatevariable().getText()])
                + "(sp)\n"
                + self.label_map[label2]
            )

    def enterBasic_block(self, ctx: llvmParser.Basic_blockContext):
        name = ctx.Label().getText()
        self.enter_label = self.enter_function + name
        self.return_str += self.enter_label + ":\n"

    def enterFunction(self, ctx: llvmParser.FunctionContext):
        self.variable_cnt = 4
        self.enter_function = ctx.Global_var().getText()[1:]
        extra_param_list = []
        if ctx.params() is not None:
            if len(ctx.params().parameter()) > 8:
                params = ctx.params().parameter()[8:]
                for i in params:
                    if i.Privatevariable() is not None:
                        self.variable_map[i.Privatevariable().getText()] = -1
                        extra_param_list.append(i.Privatevariable().getText())
        self._traverse_nodes(ctx)
        self.variable_cnt += 16 - (self.variable_cnt % 16)
        for i in range(len(extra_param_list)):
            self.variable_map[extra_param_list[i]] = self.variable_cnt + i * 4
        self.return_str += (
            ".globl " + self.enter_function + "\n" + self.enter_function + ":\n"
        )
        self.return_str += "\taddi sp, sp, -" + str(self.variable_cnt) + "\n"
        self.return_str += "\tsw ra, 0(sp)\n"

        if ctx.params() is not None:
            params = ctx.params().parameter()
            for i in range(min(8, len(params))):
                if params[i].Privatevariable() is not None:
                    var_name = params[i].Privatevariable().getText()
                    self.return_str += (
                        "\tsw a"
                        + str(i)
                        + ", "
                        + str(self.variable_map[var_name])
                        + "(sp)\n"
                    )

    def _traverse_nodes(self, node):
        if hasattr(node, "Privatevariable") and node.Privatevariable() is not None:
            var_name = node.Privatevariable().getText()
            if var_name not in self.variable_map:
                self.variable_map[var_name] = self.variable_cnt
                self.variable_cnt += 4
        else:
            for child in node.getChildren():
                if isinstance(child, antlr4.ParserRuleContext):
                    self._traverse_nodes(child)

    def exitFunction(self, ctx: llvmParser.FunctionContext):
        self.variable_map = {}
        self.variable_cnt = 0
        for i in self.label_map:
            self.return_str += i + ":\n" + self.label_map[i]

        self.label_map = {}

    def enterGlobalvariable(self, ctx: llvmParser.GlobalvariableContext):
        self.data += ".align 4\n"
        self.data += ctx.Global_var().getText()[1:] + ":\n"
        if ctx.string_constant() != None:
            val = ctx.string_constant().getText()[1:]
            self.data += "\t.word " + val + "\n"
            return
        val = ctx.constant().getText()
        if val == "null":
            val = "0"
        self.data += "\t.word " + val + "\n"

    def enterString_declare(self, ctx: llvmParser.String_declareContext):
        self.data += ctx.Global_var().getText()[1:] + ":\n"
        str = ctx.StringLiteral().getText()[1:-1]
        str = str.replace("\\22", '\\"')
        str = str.replace("\\0A", "\\n")
        str = str.replace("\\00", "")
        self.data += '\t.asciz "' + str + '"\n'


def main(code: str) -> str:
    input_stream = InputStream(code)
    lexer = llvmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = llvmParser(token_stream)

    tree = parser.module()
    walker = ParseTreeWalker()
    listener = Mylistener3()
    walker.walk(listener, tree)
    listener.return_str = listener.return_str.replace("newBoolArray", "newIntArray")
    return listener.return_str + listener.data


if __name__ == "__main__":
    code = sys.stdin.read()
    code2 = main(code)
    with open("asm.s", "w") as f:
        f.write(code2)
    print(code2)
