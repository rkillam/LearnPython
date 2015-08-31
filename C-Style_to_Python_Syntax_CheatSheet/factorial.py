import factorial_calculator


factCalc = factorial_calculator.FactorialCalculator()

for i in range(1, 11):
    fact = factCalc.calc(i)

    if fact > 100:
        print("Large Answer: {}".format(fact))
    else:
        print("Small Answer: {}".format(fact))
