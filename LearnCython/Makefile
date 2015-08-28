N := 1000000000

sum_nums_cypy: sum_nums_cypy.pyx
	cython --embed -a $<
	gcc -I/usr/include/python3.4m/ $(basename $<).c -o $@ -lpython3.4m

sum_nums_c: sum_nums_c.c
	gcc $< -o $@

test: test.sh sum_nums_cypy sum_nums_c
	./$< $(N)
