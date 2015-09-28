BASH := /bin/bash

CYTHON_COMPILER := /usr/local/bin/cython
CYTHON_FLAGS := --embed -a

GCC := /usr/bin/gcc
INCLUDES := /usr/include/python2.7
LIBRARIES := python2.7

CFLAGS := $(addprefix -I,$(INCLUDES))
LDFLAGS := $(addprefix -l,$(LIBRARIES))

N := 100000000

sum_nums_cypy: sum_nums_cypy.pyx
	$(CYTHON_COMPILER) $(CYTHON_FLAGS) $<
	$(GCC) $(CFLAGS) $(basename $<).c -o $@ $(LDFLAGS)

sum_nums_c: sum_nums_c.c
	$(GCC) $< -o $@

sum_nums_py: sum_nums_py.py
	$(CYTHON_COMPILER) $(CYTHON_FLAGS) $<
	$(GCC) $(CFLAGS) $(basename $<).c -o $@ $(LDFLAGS)

test: test.sh sum_nums_cypy sum_nums_c sum_nums_py
	$(BASH) $< $(N)
