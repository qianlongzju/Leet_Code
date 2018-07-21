public class Solution {
    public String fractionToDecimal(int numerator2, int denominator2) {
            String result = "";
            long numerator = numerator2;
            long denominator = denominator2;
            if (numerator * denominator < 0)
                result = "-";
            numerator = Math.abs(numerator);
            denominator = Math.abs(denominator);
            if (numerator % denominator == 0)
                return result + (numerator / denominator);
            result += (numerator / denominator) + ".";
            numerator %= denominator;
            ArrayList<Long> reminders = new ArrayList<Long>();
            ArrayList<Long> numerators = new ArrayList<Long>();
            numerators.add(numerator);
            numerator *= 10;
            while (numerator != 0) {
                reminders.add(numerator / denominator);
                numerator %= denominator;
                int left = numerators.indexOf(numerator);
                if (left != -1) {
                    for (int t=0; t < left; t++)
                        result += reminders.get(t);
                    result += "(";
                    for (; left < reminders.size(); left++)
                        result += reminders.get(left);
                    result += ")";
                    return result;
                }
                numerators.add(numerator);
                numerator *= 10;
            }
            for (long i:reminders) {
                result += i;
            }
            return result;
    }
}
