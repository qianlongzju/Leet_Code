#!/usr/bin/env python
import os
import sys
import time

cmd = "leetcode submit {}"


def rename():
    for f in os.listdir("."):
        if f.endswith('.py') or f.endswith('.cpp') or f.endswith('.java'):
            t = f.replace("_", '.', 1)
            if f != t:
                os.system("git mv {} {}".format(f, t))


def remove_main_cpp():
    for f in os.listdir("."):
        if not f.endswith('.cpp'):
            continue
        with open(f) as t:
            code = t.readlines()
        for i in range(len(code)):
            if 'main' not in code[i]:
                continue
            with open(f, 'w') as t:
                t.write("".join(code[:i]))


def main(path):
    passed_file_name = "pass.txt"
    if os.path.exists(passed_file_name):
        with open(passed_file_name) as t:
            passed = t.read().split("\n")
    else:
        passed = []
    for f in sorted(os.listdir(path)):
        if f in passed:
            continue
        if not unicode(f, 'utf-8').split(".")[0].isnumeric():
            continue
        if f.endswith("py") or f.endswith("cpp") or f.endswith("java"):
            p = os.path.join(path, f)
            print(f)
            print(cmd.format(p))
            os.system(cmd.format(p))
            time.sleep(20)

if __name__ == '__main__':
    main(sys.argv[1])
