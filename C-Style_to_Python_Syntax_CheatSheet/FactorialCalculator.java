public class FactorialCalculator {
    public int calc(int n) {
        int result = 1;
        while(n > 0) {
            result *= n;
            n--;
        }

        return result;
    }
}

