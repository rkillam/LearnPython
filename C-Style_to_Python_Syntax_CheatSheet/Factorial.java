public class Factorial {
    public static void main(String[] args) {
        FactorialCalculator factCalc = new FactorialCalculator();

        for(int i = 1; i <= 10; ++i) {
            int fact = factCalc.calc(i);

            if(fact > 100) {
                System.out.println("Large Answer: " + fact);
            }
            else {
                System.out.println("Small Answer: " + fact);
            }
        }
    }
}
