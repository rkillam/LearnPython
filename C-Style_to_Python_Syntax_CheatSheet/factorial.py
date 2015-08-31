class FactorialCalculator(object):
    def calc(self, n):
        result = 1
        while n > 0:
            result *= n
            n -= 1

        return result


factCalc = FactorialCalculator()

for i in range(1, 11):
    fact = factCalc.calc(i)

    if fact > 100:
        print("Large Answer: {}".format(fact))
    else:
        print("Small Answer: {}".format(fact))
