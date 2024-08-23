import sys


def main(code: str):
    global_str = ""
    lines = code.splitlines()
    for line in lines:
        if line.startswith("define "):
          

if __name__ == "__main__":
    code = sys.stdin.read()
    main(code)
