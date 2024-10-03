#!/bin/bash

cd ravel
cd build
export PATH="/usr/local/opt/bin:$PATH"
cd ../../

# 获取第一个参数
arg=$1

# 获取第二个参数作为 mx 文件
mx_file=$2

# 根据参数执行相应的操作
case $arg in
    1)
        testcases/optim-new/scripts/test_asm.bash src/main.py testcases/optim-new/"$mx_file" builtin.s
        ;;
    2)
        testcases/optim-new/scripts/test_asm_all.bash src/main.py testcases/optim-new/ builtin.s
        ;;
    *)
        echo "Invalid argument: $arg"
        echo "Usage: $0 <arg> <mx_file>"
        exit 1
        ;;
esac