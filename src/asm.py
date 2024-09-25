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


class Interval:
    beg = -1
    end = -1

    def __init__(self, beg=-1, end=-1) -> None:
        self.beg = beg
        self.end = end


class RegUse:
    name = ""
    beg = -1
    end = -1
    reg = ""

    def __init__(self, name="", beg=-1, end=-1, reg=""):
        self.name = name
        self.beg = beg
        self.end = end
        self.reg = reg

    def __lt__(self, other):
        return self.beg < other.beg


class Mylistener3(llvmListener):
    return_str = ".text\n"
    enter_label = ""
    enter_function = ""
    data = ".data\n"
    variable_map = {}
    variable_cnt = 0
    label_map = {}
    tmp_branch_cnt = 0
    tmp_store = {}
    reg_map = {
        "s0": [],
        "s1": [],
        "s2": [],
        "s3": [],
        "s4": [],
        "s5": [],
        "s6": [],
        "s7": [],
        "s8": [],
        "s9": [],
        "s10": [],
        "s11": [],
    }

    def enterRet(self, ctx: llvmParser.RetContext):
        if ctx.value() != None:
            value = ctx.value()
            name = ctx.value().getText()
            if value.Privatevariable() != None:
                self.loadword(self.variable_map[name], "a0")
            elif value.Global_var() != None:
                self.return_str += "\tla a0, " + name[1:] + "\n"
            else:
                if name == "null":
                    name = "0"
                self.return_str += "\tli a0, " + name + "\n"
        self.return_str += "\tlw ra, 0(sp)\n"
        for i in self.tmp_store:
            self.loadword(self.tmp_store[i], i)
        if self.variable_cnt > 2047:
            self.return_str += "\tli t0, " + str(self.variable_cnt) + "\n"
            self.return_str += "\tadd sp, sp, t0\n"
        else:
            self.return_str += "\taddi sp, sp, " + str(self.variable_cnt) + "\n"
        self.return_str += "\tret\n"

    def loadword(self, index, name: str = "t0"):
        if isinstance(index, str):
            if name != index:
                self.return_str += "\tmv " + name + ", " + index + "\n"
            return
        if index > 2047 or index < -2048:
            self.return_str += "\tli t3, " + str(index) + "\n"
            self.return_str += "\tadd t3, sp, t3\n"
            self.return_str += "\tlw " + name + ", 0(t3)\n"
            return
        self.return_str += "\tlw " + name + ", " + str(index) + "(sp)\n"

    def saveword(self, index: int, name: str = "t0"):
        if isinstance(index, str):
            if name != index:
                self.return_str += "\tmv " + index + ", " + name + "\n"
            return
        if index > 2047 or index < -2048:
            self.return_str += "\tli t3, " + str(index) + "\n"
            self.return_str += "\tadd t3, sp, t3\n"
            self.return_str += "\tsw " + name + ", 0(t3)\n"
            return
        self.return_str += "\tsw " + name + ", " + str(index) + "(sp)\n"

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
                self.loadword(self.variable_map[name], "a" + str(i))
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
                    self.loadword(self.variable_map[name])
                else:
                    name = param.constant().getText()
                    if name == "null":
                        name = "0"
                    self.return_str += "\tli t0, " + name + "\n"
                self.saveword(i * 4)

    def enterCall(self, ctx: llvmParser.CallContext):
        i = 0
        if ctx.params() != None:
            self.params_decode(ctx.params())
            i = len(ctx.params().parameter())
        self.return_str += "\tcall " + ctx.Global_var().getText()[1:] + "\n"
        if i > 8:
            self.return_str += "\taddi sp, sp, " + str((i - 8) * 4) + "\n"
        if ctx.Privatevariable() != None:
            self.saveword(self.variable_map[ctx.Privatevariable().getText()], "a0")

    def enterBinary_op(self, ctx: llvmParser.Binary_opContext):
        value1 = ctx.value(0)
        value2 = ctx.value(1)
        if value1.Privatevariable() != None:
            self.loadword(self.variable_map[value1.Privatevariable().getText()], "t1")
        elif value1.Global_var() != None:
            self.return_str += "\tla t1, " + value1.Global_var().getText() + "\n"
        else:
            name = value1.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t1, " + name + "\n"
        if value2.Privatevariable() != None:
            self.loadword(self.variable_map[value2.Privatevariable().getText()], "t2")
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
        self.saveword(self.variable_map[ctx.Privatevariable().getText()])

    def enterBranch(self, ctx: llvmParser.BranchContext):
        if ctx.value() != None:
            value = ctx.value()
            if value.Privatevariable() != None:
                self.loadword(self.variable_map[value.Privatevariable().getText()])
            else:
                name = value.getText()
                if name == "null":
                    name = "0"
                self.return_str += "\tli t0, " + name + "\n"
            label1 = self.enter_label + ctx.Label(0).getText()
            label2 = self.enter_label + ctx.Label(1).getText()
            tmp_br = "tmp_br" + str(self.tmp_branch_cnt)
            self.return_str += "\tbnez t0, " + tmp_br + "\n"
            self.return_str += "\tj " + label2 + "\n"
            self.return_str += tmp_br + ":\n"
            self.return_str += "\tj " + label1 + "\n"
            self.tmp_branch_cnt += 1
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
            self.loadword(self.variable_map[var.Privatevariable().getText()], "t1")
            self.return_str += "\tlw t0, 0(t1)\n"
            self.saveword(self.variable_map[ctx.Privatevariable().getText()])
            return
        name = var.Global_var().getText()[1:]
        self.return_str += "\tlw t0, " + name + "\n"
        self.saveword(self.variable_map[ctx.Privatevariable().getText()])

    def enterGetelementptr(self, ctx: llvmParser.GetelementptrContext):
        value = ctx.value()
        if value.Privatevariable() != None:
            self.loadword(self.variable_map[value.Privatevariable().getText()], "t2")
        else:
            name = value.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t2, " + name + "\n"
        self.return_str += "\tslli t2, t2, 2\n"
        var = ctx.var()
        if var.Privatevariable() != None:
            self.loadword(self.variable_map[var.Privatevariable().getText()], "t1")
            self.return_str += "\tadd t0, t1, t2\n"
            self.saveword(self.variable_map[ctx.Privatevariable().getText()])
            return
        name = var.Global_var().getText()[1:]
        self.return_str += "\tlw t0, " + name + "\n"
        self.return_str += "\tadd t0, t0, t2\n"
        self.saveword(self.variable_map[ctx.Privatevariable().getText()])

    def enterStore(self, ctx: llvmParser.StoreContext):
        value = ctx.value()
        if value.Privatevariable() != None:
            self.loadword(self.variable_map[value.Privatevariable().getText()], "t1")
        elif value.Global_var() != None:
            self.return_str += "\tla t1, " + value.Global_var().getText()[1:] + "\n"
        else:
            name = value.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t1, " + name + "\n"
        var = ctx.var()
        if var.Privatevariable() != None:
            self.loadword(self.variable_map[var.Privatevariable().getText()])
            self.return_str += "\tsw t1, 0(t0)\n"
            return
        name = var.Global_var().getText()[1:]
        self.return_str += "\tlui t0, %hi(" + name + ")\n"
        self.return_str += "\tsw t1, %lo(" + name + ")(t0)\n"

    def enterCompare(self, ctx: llvmParser.CompareContext):
        value1 = ctx.value(0)
        if value1.Privatevariable() != None:
            self.loadword(self.variable_map[value1.Privatevariable().getText()], "t1")
        elif value1.Global_var() != None:
            self.return_str += "\tla t1, " + value1.Global_var().getText()[1:] + "\n"
        else:
            name = value1.getText()
            if name == "null":
                name = "0"
            self.return_str += "\tli t1, " + name + "\n"
        value2 = ctx.value(1)
        if value2.Privatevariable() != None:
            self.loadword(self.variable_map[value2.Privatevariable().getText()], "t2")
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
        self.saveword(self.variable_map[privatevariable.getText()])

    def enterPhi(self, ctx: llvmParser.PhiContext):
        for i in range(len(ctx.Label())):
            label1 = (
                self.enter_function
                + ctx.Label(i).getText()
                + self.enter_label[len(self.enter_function) :]
            )
            value1 = ctx.value(i)
            value1_str = ""
            if value1.Privatevariable() != None:
                index = self.variable_map[value1.Privatevariable().getText()]
                if isinstance(index, str):
                    value1_str += "\tmv t1, " + index + "\n"
                else:
                    if index > 2047 or index < -2048:
                        value1_str += "\tli t0, " + str(index) + "\n"
                        value1_str += "\tadd t0, sp, t0\n"
                        value1_str += "\tlw t1, 0(t0)\n"
                    else:
                        value1_str += "\tlw t1, " + str(index) + "(sp)\n"
            elif value1.Global_var() != None:
                value1_str += "\tla t1, " + value1.Global_var().getText()[1:] + "\n"
            else:
                name = value1.getText()
                if name == "null":
                    name = "0"
                value1_str += "\tli t1, " + name + "\n"
            index = self.variable_map[ctx.Privatevariable().getText()]
            str1 = value1_str
            if isinstance(index, str):
                str1 += "\tmv " + index + ", t1\n"
            else:
                if index > 2047 or index < -2048:
                    str1 += "\tli t0, " + str(index) + "\n"
                    str1 += "\tadd t0, sp, t0\n"
                    str1 += "\tsw t1, 0(t0)\n"
                else:
                    str1 += "\tsw t1, " + str(index) + "(sp)\n"
            if label1 not in self.label_map:
                self.label_map[label1] = str1
            else:
                self.label_map[label1] = str1 + self.label_map[label1]

    def enterBasic_block(self, ctx: llvmParser.Basic_blockContext):
        name = ctx.Label().getText()
        self.enter_label = self.enter_function + name
        self.return_str += self.enter_label + ":\n"

    def conflict_graph(
        self,
        ctx: llvmParser.Basic_blockContext,
        list: list,
        define_map: dict,
        block_index: dict,
    ):
        block_index.append((ctx.Label().getText(), len(list)))
        list.append(-1)
        for i in ctx.instruction():
            if i.call() != None:
                call = i.call()
                if call.params() != None:
                    for j in call.params().parameter():
                        if j.Privatevariable() != None:
                            list.append(j.Privatevariable().getText())
                if call.Privatevariable() != None:
                    list.append("")
                    define_map[call.Privatevariable().getText()] = len(list) - 1
            elif i.ret() != None:
                ret = i.ret()
                if ret.value() != None:
                    value = ret.value()
                    if value.Privatevariable() != None:
                        list.append(value.Privatevariable().getText())
            elif i.binary_op() != None:
                binary_op = i.binary_op()
                for j in binary_op.value():
                    if j.Privatevariable() != None:
                        list.append(j.Privatevariable().getText())
                list.append("")
                define_map[binary_op.Privatevariable().getText()] = len(list) - 1
            elif i.branch() != None:
                branch = i.branch()
                if branch.value() != None:
                    value = branch.value()
                    if value.Privatevariable() != None:
                        list.append(value.Privatevariable().getText())
            elif i.load() != None:
                load = i.load()
                var = load.var()
                if var.Privatevariable() != None:
                    list.append(var.Privatevariable().getText())
                list.append("")
                define_map[load.Privatevariable().getText()] = len(list) - 1
            elif i.store() != None:
                value = i.store().value()
                var = i.store().var()
                if var.Privatevariable() != None:
                    list.append(var.Privatevariable().getText())
                if value.Privatevariable() != None:
                    list.append(value.Privatevariable().getText())
            elif i.getelementptr() != None:
                value = i.getelementptr().value()
                var = i.getelementptr().var()
                if value.Privatevariable() != None:
                    list.append(value.Privatevariable().getText())
                if var.Privatevariable() != None:
                    list.append(var.Privatevariable().getText())
                list.append("")
                define_map[i.getelementptr().Privatevariable().getText()] = (
                    len(list) - 1
                )
            elif i.compare() != None:
                compare = i.compare()
                for j in compare.value():
                    if j.Privatevariable() != None:
                        list.append(j.Privatevariable().getText())
                list.append("")
                define_map[compare.Privatevariable().getText()] = len(list) - 1
            elif i.phi() != None:
                phi = i.phi()
                for j in phi.value():
                    if j.Privatevariable() != None:
                        list.append(j.Privatevariable().getText())
                list.append("")
                define_map[phi.Privatevariable().getText()] = len(list) - 1

    def _traverse_blocks(self, bm: dict, queue: list, from_: str, visited: list):
        visited.append(from_)
        for j in bm[from_][1]:
            if j not in visited:
                self._traverse_blocks(bm, queue, j, visited)
        queue.append(from_)

    def merge_intervals(self, intervals):
        intervals.sort(key=lambda x: x.beg)

        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.beg:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged

    def has_intersection(self, list1, list2):
        list1.sort(key=lambda x: x.beg)
        list2.sort(key=lambda x: x.beg)

        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            a, b = list1[i], list2[j]
            if a.end >= b.beg and a.beg <= b.end:
                return True
            if a.end < b.end:
                i += 1
            else:
                j += 1

        return False

    def reverse_graph(self, bm: dict):
        reversed_bm = {}
        for node, (_, out_neighbors) in bm.items():
            if node not in reversed_bm:
                reversed_bm[node] = ([], [])
            for neighbor in out_neighbors:
                if neighbor not in reversed_bm:
                    reversed_bm[neighbor] = ([], [])
                reversed_bm[neighbor][1].append(node)
        return reversed_bm

    def dfs(self, node: str, graph: dict, visited: set):
        visited.add(node)

        for neighbor in graph[node][1]:
            if neighbor not in visited:
                self.dfs(neighbor, graph, visited)

    def search_circle(self, bm: dict, reversed_bm: dict, from_: str):

        visited_original = set()
        self.dfs(from_, bm, visited_original)

        visited_reversed = set()
        self.dfs(from_, reversed_bm, visited_reversed)

        common_nodes = visited_original.intersection(visited_reversed)

        return common_nodes

    def block_register(
        self,
        name: str,
        block_name: str,
        block_index: list,
        circle: list,
        regusemap: dict,
        block_index_map: dict,
        final_end: int,
        be=-1,
        en=-1,
    ):
        list2 = []
        for i in circle:
            if block_name in i:
                list2 = circle[i]
                break
        beg = -1
        end = -1
        p = block_index_map[block_name]
        beg = block_index[p][1]
        if p == len(block_index) - 1:
            end = final_end
        else:
            end = block_index[p + 1][1]
        if len(list2) == 0:
            if be != -1:
                beg = be
            if en != -1:
                end = en
        reguse = Interval(beg=beg, end=end)
        if name not in regusemap:
            regusemap[name] = []
        if reguse in regusemap[name]:
            return
        regusemap[name].append(reguse)
        for t in list2:
            beg = t.beg
            end = t.end
            reguse = Interval(beg=beg, end=end)
            if reguse not in regusemap[name]:
                regusemap[name].append(reguse)

    def enterFunction(self, ctx: llvmParser.FunctionContext):
        list = []
        visited = []
        define_map = {}
        block_map = {}

        for i in ctx.basic_block():
            to_list = []
            for j in i.instruction():
                if j.branch() != None:
                    for k in j.branch().Label():
                        to_list.append(k.getText())
            block_map[i.Label().getText()] = [i, to_list]
        queue = []
        self._traverse_blocks(block_map, queue, ".entry", visited)
        queue = queue[::-1]
        circle = {}
        rbm = self.reverse_graph(block_map)
        block_index = []
        for i in queue:
            self.conflict_graph(block_map[i][0], list, define_map, block_index)
        block_index_map = {}
        for i in range(len(block_index)):
            block_index_map[block_index[i][0]] = i
        for i in block_map:
            flag = False
            for cir in circle:
                if i in cir:
                    flag = True
                    break
            if flag:
                continue
            cir = self.search_circle(block_map, rbm, i)
            if frozenset(cir) not in circle:
                relist = []
                for t in cir:
                    if t not in block_index_map:
                        continue
                    p = block_index_map[t]
                    beg = block_index[p][1]
                    if p == len(block_index) - 1:
                        end = len(list)
                    else:
                        end = block_index[p + 1][1]
                    reguse = Interval(beg=beg, end=end)
                    relist.append(reguse)
                self.merge_intervals(relist)
                circle[frozenset(cir)] = relist

        if ctx.params() != None:
            for i in ctx.params().parameter():
                if i.Privatevariable() != None:
                    define_map[i.Privatevariable().getText()] = -1
        reguselist = []
        regusemap = {}
        for i in range(len(list)):
            name = list[i]
            if name != "" and name != -1:
                define = define_map[name]
                define_block = ".entry"
                for k in range(len(block_index)):
                    if block_index[k][1] < define and (
                        k == len(block_index) - 1 or block_index[k + 1][1] > define
                    ):
                        define_block = block_index[k][0]
                        break
                use_block = ""
                for k in range(len(block_index)):
                    if block_index[k][1] < i and (
                        k == len(block_index) - 1 or block_index[k + 1][1] > i
                    ):
                        use_block = block_index[k][0]
                        break
                final_end = len(list)
                if define < i:
                    # reguselist.append(RegUse(name=name, beg=define, end=i))
                    if name not in regusemap:
                        regusemap[name] = []
                    regusemap[name].append(Interval(beg=define, end=i))
                    if define_block != use_block:
                        interval = [Interval(beg=define, end=i)]
                        for k in circle:
                            m = circle[k]
                            if self.has_intersection(interval, m):
                                for t in m:
                                    # reguselist.append(
                                    #     RegUse(name=name, beg=t.beg, end=t.end)
                                    # )
                                    regusemap[name].append(
                                        Interval(beg=t.beg, end=t.end)
                                    )
                else:
                    self.block_register(
                        name,
                        define_block,
                        block_index,
                        circle,
                        regusemap,
                        block_index_map,
                        final_end,
                    )
        for i in regusemap:
            use = self.merge_intervals(regusemap[i])
            for j in use:
                reguselist.append(RegUse(i, j.beg, j.end))
        reguselist.sort()
        reg_map = copy.deepcopy(self.reg_map)
        for i in reguselist:
            if i.reg == "":
                list1 = []
                for j in reguselist:
                    if j.name == i.name:
                        list1.append(j)
                for j in reg_map:
                    list2 = reg_map[j]
                    if self.has_intersection(list1, list2) == False:
                        reg_map[j] += list1
                        for k in list1:
                            k.reg = j
                        self.variable_map[i.name] = j
                        break

        self.variable_cnt = 4
        tmp_store = {}
        for i in reg_map:
            if len(reg_map[i]) != 0:
                tmp_store[i] = self.variable_cnt
                self.variable_cnt += 4
        self.tmp_store = tmp_store
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
        if self.variable_cnt > 2047:
            self.return_str += "\tli t0, -" + str(self.variable_cnt) + "\n"
            self.return_str += "\tadd sp, sp, t0\n"
        else:
            self.return_str += "\taddi sp, sp, -" + str(self.variable_cnt) + "\n"
        self.return_str += "\tsw ra, 0(sp)\n"
        for i in tmp_store:
            self.saveword(tmp_store[i], i)
        if ctx.params() is not None:
            params = ctx.params().parameter()
            for i in range(min(8, len(params))):
                if params[i].Privatevariable() is not None:
                    var_name = params[i].Privatevariable().getText()
                    self.saveword(self.variable_map[var_name], "a" + str(i))
                    # self.variable_map[var_name] = "a" + str(i)

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
    with open("asm.s", "w") as f:
        f.write(listener.return_str + listener.data)
    return_str = ""
    lines = listener.return_str.splitlines()
    i = 0
    replace_map = {}
    while i < len(lines):
        if (
            not lines[i].startswith("\t")
            and not lines[i].startswith("tmp")
            and not lines[i].endswith("entry:")
        ):
            if lines[i + 1].startswith("\tj"):
                label1 = lines[i][:-1]
                label2 = lines[i + 1][3:]
                replace_map[label1] = label2
                i += 2
                continue
        return_str += lines[i] + "\n"
        i += 1
    _return_str = ""
    while _return_str != return_str:
        _return_str = return_str
        for i in replace_map:
            return_str = return_str.replace(
                "j " + i + "\n", "j " + replace_map[i] + "\n"
            )
    with open("asm_optim.s", "w") as f:
        f.write(return_str + listener.data)
    return return_str + listener.data


if __name__ == "__main__":
    code = sys.stdin.read()
    code2 = main(code)
    with open("asm_optim.s", "w") as f:
        f.write(code2)
    print(code2)
