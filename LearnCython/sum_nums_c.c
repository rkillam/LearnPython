#include <stdio.h>
#include <stdlib.h>

unsigned long long sum_nums(long n) {
    unsigned long long s = 0;
    long i;
    for(i = 1; i <= n; ++i) {
        s += i;
    }

    return s;
}

int main(int argc, char* argv[]) {
    char* end;
    long n = strtol(argv[1], &end, 10);

    printf("%llu\n", sum_nums(n));

    return 0;
}
