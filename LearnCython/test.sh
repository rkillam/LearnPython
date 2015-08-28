#!/bin/bash

N=$1

python -c 'print("sum_nums_c {:,}".format('${N}'))'
time ./sum_nums_c ${N}
echo ""

python -c 'print("sum_nums_cypy {:,}".format('${N}'))'
time ./sum_nums_cypy ${N}
echo ""

python -c 'print("sum_nums_py.py {:,}".format('${N}'))'
time ./sum_nums_py.py ${N}
