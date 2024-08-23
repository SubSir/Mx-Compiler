import sys


def function_decode(code: str) -> str:
    return_str = ""
    lines = code.splitlines()
    func = lines[0].strip().split()[2]
    name = func.split("(")[0][1:]
    parameter = func.split("(")[1].split(")")[0]
    var_cnt = 0
    var_map = {}
    if parameter != "":
        parameter = parameter.split(",")
        for i in parameter:
            var_map[i.split(" ")[1]] = var_cnt
            var_cnt += 4
    return_str += "\t.global " + name + "\n"
    return_str += name + ":\n"
    for i in range(1, len(lines)):
        t = lines[i].split()
        for j in t:
            if j.startswith("%var"):
                if j not in var_map:
                    var_map[j] = var_cnt
                    var_cnt += 4
    if var_cnt % 16 != 0:
        var_cnt += 16 - var_cnt % 16

    return_str += "\taddi sp, sp, -" + str(var_cnt) + "\n"
    for i in range(1, len(lines) - 1):
        line = lines[i]
        if line.startswith("\t"):
            pass
        elif "." in line:
            return_str += name + line + "\n"


def main(code: str):
    global_str = ""
    lines = code.splitlines()
    for line in lines:
        global_str += line + "\n"
        if line.startswith("}"):
            function_decode(global_str)
            global_str = ""


if __name__ == "__main__":
    code = sys.stdin.read()
    main(code)
