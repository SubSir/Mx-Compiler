#!/usr/bin/python3
import sys
from antlr4 import InputStream, CommonTokenStream
import antlr4
from llvmparser.llvmListener import llvmListener
from llvmparser.llvmLexer import llvmLexer
from llvmparser.llvmParser import llvmParser
from antlr4.tree.Tree import ParseTreeWalker


class Mylistener3(llvmListener):

    variable_map = {}
    return_ans = ""

    def __init__(self) -> None:
        self.variable_map = {}
        self.return_ans = ""

    def _traverse_nodes(self, node):
        if hasattr(node, "Privatevariable") and node.Privatevariable() is not None:
            var_name = node.Privatevariable().getText()
            if var_name not in self.variable_map:
                self.variable_map[var_name] = 1
            else:
                self.variable_map[var_name] += 1
        for child in node.getChildren():
            if isinstance(child, antlr4.ParserRuleContext):
                self._traverse_nodes(child)

    def enterModule(self, ctx: llvmParser.ModuleContext):
        self._traverse_nodes(ctx)


class Mylistener2_5(llvmListener):
    imm_map = {}

    def __init__(self) -> None:
        self.imm_map = {}

    def enterBinary_op(self, ctx: llvmParser.Binary_opContext):
        value1 = ctx.value(0)
        value2 = ctx.value(1)
        op = ctx.bin_op().getText()
        var = ctx.Privatevariable().getText()
        t1 = ""
        t2 = ""
        if value1.constant() != None:
            t1 = int(value1.constant().getText())
        elif value1.getText() in self.imm_map:
            t1 = self.imm_map[value1.getText()]
        if value2.constant() != None:
            t2 = int(value2.constant().getText())
        elif value2.getText() in self.imm_map:
            t2 = self.imm_map[value2.getText()]
        if not isinstance(t1, str) and not isinstance(t2, str):
            if op == "add":
                self.imm_map[var] = t1 + t2
            elif op == "sub":
                self.imm_map[var] = t1 - t2
            elif op == "mul":
                self.imm_map[var] = t1 * t2
            elif op == "sdiv":
                if t2 == 0:
                    return
                self.imm_map[var] = t1 // t2
            elif op == "srem":
                if t2 == 0:
                    return
                self.imm_map[var] = t1 % t2
            elif op == "shl":
                self.imm_map[var] = t1 << t2
            elif op == "ashr":
                self.imm_map[var] = t1 >> t2
            elif op == "and":
                self.imm_map[var] = t1 & t2
            elif op == "or":
                self.imm_map[var] = t1 | t2
            elif op == "xor":
                self.imm_map[var] = t1 ^ t2
            return
        if value1.getText() == "0":
            if op == "add" or op == "or":
                self.imm_map[var] = value2.getText()
            elif (
                op == "mul"
                or op == "sdiv"
                or op == "srem"
                or op == "shl"
                or op == "ashr"
                or op == "and"
            ):
                self.imm_map[var] = 0
        if value2.getText() == "0":
            if op == "add" or op == "or" or op == "sub" or op == "shl" or op == "ashr":
                self.imm_map[var] = value1.getText()
            elif op == "mul" or op == "and":
                self.imm_map[var] = 0

    def enterCompare(self, ctx: llvmParser.CompareContext):
        value1 = ctx.value(0)
        value2 = ctx.value(1)
        op = ctx.cond().getText()
        var = ctx.Privatevariable().getText()
        t1 = ""
        t2 = ""
        if value1.constant() != None and value1.constant().getText().isdigit():
            t1 = int(value1.constant().getText())
        elif value1.getText() in self.imm_map:
            t1 = self.imm_map[value1.getText()]
        if value2.constant() != None and value2.constant().getText().isdigit():
            t2 = int(value2.constant().getText())
        elif value2.getText() in self.imm_map:
            t2 = self.imm_map[value2.getText()]
        if not isinstance(t1, str) and not isinstance(t2, str):
            if op == "eq":
                self.imm_map[var] = int(t1 == t2)
            elif op == "ne":
                self.imm_map[var] = int(t1 != t2)
            elif op == "slt":
                self.imm_map[var] = int(t1 < t2)
            elif op == "sgt":
                self.imm_map[var] = int(t1 > t2)
            elif op == "sle":
                self.imm_map[var] = int(t1 <= t2)
            elif op == "sge":
                self.imm_map[var] = int(t1 >= t2)


class Mylistener3_5(llvmListener):
    inline_func = {}
    call_str = {}
    label = ""
    enter_func = ""
    queue_set = set()

    def enterModule(self, ctx: llvmParser.ModuleContext):
        for i in ctx.getChildren():
            if isinstance(i, llvmParser.FunctionContext):
                cnt = 0
                for j in i.basic_block():
                    cnt += len(j.instruction())
                if cnt > 100:
                    continue
                use = set()
                labels = []
                for j in i.basic_block():
                    var_use, label_use = self.traverse_block(j)
                    use = use | var_use
                    labels.append(label_use)
                params = []
                if i.params() != None:
                    for k in i.params().parameter():
                        params.append(k.Privatevariable().getText())
                self.inline_func[i.Global_var().getText()] = [use, params, labels]

    def enterCall(self, ctx: llvmParser.CallContext):
        if (
            ctx.Global_var().getText() in self.inline_func
            and ctx.Global_var().getText() != self.enter_func
        ):
            if ctx.Privatevariable() != None:
                str_ = (
                    ctx.Privatevariable().getText()
                    + " = call "
                    + ctx.type_().getText()
                    + " "
                    + ctx.Global_var().getText()
                    + "("
                )
                param = []
                if ctx.params() != None:
                    cnt = 0
                    for i in ctx.params().parameter():
                        str_ += i.type_().getText() + " "
                        if i.Privatevariable() != None:
                            str_ += i.Privatevariable().getText()
                            param.append(i.Privatevariable().getText())
                        elif i.Global_var() != None:
                            str_ += i.Global_var().getText()
                            param.append(i.Global_var().getText())
                        elif i.constant() != None:
                            str_ += i.constant().getText()
                            param.append(i.constant().getText())
                        if cnt < len(ctx.params().parameter()) - 1:
                            str_ += ", "
                        cnt += 1
                str_ += ")"
                self.call_str[str_] = [
                    ctx.Privatevariable().getText(),
                    ctx.Global_var().getText(),
                    param,
                    self.label,
                ]
            else:
                str_ = (
                    "call "
                    + ctx.type_().getText()
                    + " "
                    + ctx.Global_var().getText()
                    + "("
                )
                param = []
                if ctx.params() != None:
                    cnt = 0
                    for i in ctx.params().parameter():
                        str_ += i.type_().getText() + " "
                        if i.Privatevariable() != None:
                            str_ += i.Privatevariable().getText()
                            param.append(i.Privatevariable().getText())
                        elif i.Global_var() != None:
                            str_ += i.Global_var().getText()
                            param.append(i.Global_var().getText())
                        elif i.constant() != None:
                            str_ += i.constant().getText()
                            param.append(i.constant().getText())
                        if cnt < len(ctx.params().parameter()) - 1:
                            str_ += ", "
                        cnt += 1
                str_ += ")"
                self.call_str[str_] = [
                    None,
                    ctx.Global_var().getText(),
                    param,
                    self.label,
                ]
            self.queue_set.add(str_)

    def enterFunction(self, ctx: llvmParser.FunctionContext):
        self.enter_func = ctx.Global_var().getText()

    def enterBasic_block(self, ctx: llvmParser.Basic_blockContext):
        self.label = ctx.Label().getText()

    def traverse_block(
        self,
        ctx: llvmParser.Basic_blockContext,
    ):
        use_set = set()
        for i in ctx.instruction():
            if i.call() != None:
                call = i.call()
                if call.params() != None:
                    for j in call.params().parameter():
                        if j.Privatevariable() != None:
                            use_set.add(j.Privatevariable().getText())
            elif i.ret() != None:
                ret = i.ret()
                if ret.value() != None:
                    value = ret.value()
                    if value.Privatevariable() != None:
                        use_set.add(value.Privatevariable().getText())
            elif i.binary_op() != None:
                binary_op = i.binary_op()
                for j in binary_op.value():
                    if j.Privatevariable() != None:
                        use_set.add(j.Privatevariable().getText())
            elif i.branch() != None:
                branch = i.branch()
                if branch.value() != None:
                    value = branch.value()
                    if value.Privatevariable() != None:
                        use_set.add(value.Privatevariable().getText())
            elif i.load() != None:
                load = i.load()
                var = load.var()
                if var.Privatevariable() != None:
                    use_set.add(var.Privatevariable().getText())
            elif i.store() != None:
                value = i.store().value()
                var = i.store().var()
                if var.Privatevariable() != None:
                    use_set.add(var.Privatevariable().getText())
                if value.Privatevariable() != None:
                    use_set.add(value.Privatevariable().getText())
            elif i.getelementptr() != None:
                value = i.getelementptr().value()
                var = i.getelementptr().var()
                if value.Privatevariable() != None:
                    use_set.add(value.Privatevariable().getText())
                if var.Privatevariable() != None:
                    use_set.add(var.Privatevariable().getText())
            elif i.compare() != None:
                compare = i.compare()
                for j in compare.value():
                    if j.Privatevariable() != None:
                        use_set.add(j.Privatevariable().getText())
            elif i.phi() != None:
                phi = i.phi()
                for j in phi.value():
                    if j.Privatevariable() != None:
                        use_set.add(j.Privatevariable().getText())
        return use_set, ctx.Label().getText()


def variable_replace(origin_var: str, new_var: str, stream: str):
    stream[0] = stream[0].replace(origin_var + " ", new_var + " ")
    stream[0] = stream[0].replace(origin_var + ",", new_var + ",")
    stream[0] = stream[0].replace(origin_var + "\n", new_var + "\n")
    stream[0] = stream[0].replace(origin_var + ")", new_var + ")")


def main(code: str) -> str:
    while True:
        input_stream = InputStream(code)
        lexer = llvmLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = llvmParser(token_stream)

        tree = parser.module()
        walker = ParseTreeWalker()
        listener = Mylistener2_5()
        walker.walk(listener, tree)
        imm_map = listener.imm_map
        del_list = []
        for i in imm_map:
            del_list.append("\t\t" + i + " = ")
        return_ans = ""
        lines = code.splitlines()
        for line in lines:
            flag = 1
            for delete in del_list:
                if line.startswith(delete):
                    flag = 0
                    break
            if flag == 1:
                return_ans += line + "\n"

        def replace(key, imap, stream):
            if imap[key] in imap:
                replace(imap[key], imap, stream)
                imap[key] = imap[imap[key]]
            stream[0] = stream[0].replace(key + " ", str(imm_map[key]) + " ")
            stream[0] = stream[0].replace(key + ",", str(imm_map[key]) + ",")
            stream[0] = stream[0].replace(key + "\n", str(imm_map[key]) + "\n")
            stream[0] = stream[0].replace(key + ")", str(imm_map[key]) + ")")

        stream = [return_ans]
        for i in imm_map:
            replace(i, imm_map, stream)
        code = stream[0]
        if imm_map == {}:
            break

    while True:
        input_stream = InputStream(code)
        lexer = llvmLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = llvmParser(token_stream)

        tree = parser.module()
        walker = ParseTreeWalker()
        listener = Mylistener3()
        walker.walk(listener, tree)
        var_map = listener.variable_map
        del_list = []
        for i in var_map:
            if var_map[i] == 1:
                del_list.append("\t\t" + i + " = ")
        return_ans = ""
        lines = code.splitlines()
        for line in lines:
            flag = 1
            for delete in del_list:
                if line.startswith(delete):
                    if "call" in line:
                        line = "\t\t" + line.split("= ")[1]
                    else:
                        flag = 0
                    break
            if flag == 1:
                return_ans += line + "\n"
        if code == return_ans:
            break
        code = return_ans

    with open("llvm.ll", "w") as f:
        f.write(code)

    input_stream = InputStream(code)
    lexer = llvmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = llvmParser(token_stream)

    tree = parser.module()
    walker = ParseTreeWalker()
    listener = Mylistener3_5()
    walker.walk(listener, tree)
    inline_cnt = 0
    lines = code.splitlines()
    func_str = ""
    func_name = ""
    func_map = {}
    ret = ""
    label = ""
    ret_label2 = ""
    for i in range(len(lines)):
        line = lines[i]
        if line.startswith("define"):
            if func_name != "":
                func_map[func_name].append(func_str)
                func_map[func_name].append(ret)
                func_map[func_name].append(ret_label2)
            ret = ""
            func_str = line + "\n"
            func_name = line.split()[2]
            if func_name[-1] == "(":
                func_name = func_name[:-1]
            elif func_name[-2] == "(":
                func_name = func_name[:-2]
        elif line.startswith("\t\tret void"):
            func_map[func_name] = [func_str]
            func_str = ""
            ret_label2 = label
        elif line.startswith("\t\tret"):
            ret = line.split()[2]
            func_map[func_name] = [func_str]
            func_str = ""
            ret_label2 = label
        elif line.startswith(".label"):
            func_str += line + "\n"
            label = line
        elif i == len(lines) - 1:
            func_str += line + "\n"
            func_map[func_name].append(func_str)
            func_map[func_name].append(ret)
            func_map[func_name].append(ret_label2)
        else:
            func_str += line + "\n"
    var_replace_map = {}
    # label_replace_map = {}
    for i in listener.queue_set:
        stream = [i]
        for j in var_replace_map:
            variable_replace(j, var_replace_map[j], stream)
        code_split = code.split(stream[0])
        return_ans = ""
        for j in range(len(code_split) - 1):
            inline_index = "_" + str(inline_cnt)
            ret_label = ".label" + str(inline_cnt) + "_"
            inline_cnt += 1
            func = func_map[listener.call_str[i][1]]
            entry = func[0]
            first = -1
            entry_str = ""
            for k in range(len(entry)):
                if entry[k : k + 6] == ".entry":
                    first = k
                if first != -1 and entry[k] == ":":
                    entry_str = entry[first:k]
                    entry = entry[k + 4 :]
                    break
            end = -1
            beg = -1
            for k in range(len(code_split[j]) - 1, -1, -1):
                if code_split[j][k] == ":":
                    end = k
                if end != -1 and code_split[j][k] == ".":
                    beg = k
                    break
            origin_label = code_split[j][beg:end]
            add_str = entry + "\n\t\tbr label %" + ret_label + "\n" + func[1][:-3]
            func2 = listener.inline_func[listener.call_str[i][1]]
            var_set = func2[0] - set(func2[1])
            add_str = add_str.replace(entry_str + "]", origin_label + "]")
            for k in func2[2]:
                # if k == ".entry":
                #     continue
                add_str = add_str.replace(k + "]", k + inline_index + "]")
                add_str = add_str.replace(k + ":", k + inline_index + ":")
                add_str = add_str.replace(k + "\n", k + inline_index + "\n")
                add_str = add_str.replace(k + ",", k + inline_index + ",")
            for k in range(len(code_split)):
                code_split[k] = code_split[k].replace(
                    origin_label + "]", ret_label + "]"
                )
            stream = [add_str]
            for k in var_set:
                variable_replace(k, k + inline_index, stream)
            for k in range(len(listener.call_str[i][2])):
                variable_replace(func2[1][k], listener.call_str[i][2][k], stream)
            if listener.call_str[i][0] != None:
                var_replace_map[listener.call_str[i][0]] = func[2] + inline_index
            return_ans += code_split[j] + stream[0] + "\n" + ret_label + ":\n"
            if j == len(code_split) - 2:
                return_ans += code_split[j + 1]
        code = return_ans
        stream = [code]
        for j in var_replace_map:
            variable_replace(j, var_replace_map[j], stream)
        # for j in label_replace_map:
        #     stream[0].replace(j + "]", label_replace_map[j] + "]")
        code = stream[0]

    return code


if __name__ == "__main__":
    code = sys.stdin.read()
    code2 = main(code)
    with open("llvm.s", "w") as f:
        f.write(code2)
    print(code2)
