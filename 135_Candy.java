import java.util.*;
public class Solution {
    public int candy(int[] ratings) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if (ratings.length == 1) {
            return 1;
        }
        int[] result = new int[ratings.length];
        int[] leftToRight = new int[ratings.length];
        int[] rightToLeft = new int[ratings.length];
        // 1:bigger  -1:smaller 0:equal
        leftToRight[0] = 0;
        for (int i=1; i < ratings.length; i++) {
            if (ratings[i] > ratings[i-1]) {
                leftToRight[i] = 1;
            } else if (ratings[i] < ratings[i-1]) {
                leftToRight[i] = -1;
            } else {
                leftToRight[i] = 0;
            }
        }
        rightToLeft[ratings.length-1] = 0;
        for (int i=ratings.length-2; i >= 0; i--) {
            if (ratings[i] > ratings[i+1]) {
                rightToLeft[i] = 1;
            } else if (ratings[i] < ratings[i+1]) {
                rightToLeft[i] = -1;
            } else {
                rightToLeft[i] = 0;
            }
        }
        for (int i=0; i < ratings.length; i++) {
            if (leftToRight[i] <= 0 && rightToLeft[i] <= 0) {
                result[i] = 1;
            }
        }
        for (int i=0; i < ratings.length; i++) {
            if (result[i] == 1) {
                i++;
                while (i < ratings.length && ratings[i] > ratings[i-1]) {
                    result[i] = result[i-1] + 1;
                    i++;
                }
                i--;
            }
        }
        for (int i=ratings.length-1; i >= 0; i--) {
            if (result[i] == 1) {
                i--;
                while (i >=0 && ratings[i] > ratings[i+1]) {
                    result[i] = result[i+1] + 1;
                    i--;
                }
                if (i >= 0 && i+2 < ratings.length && ratings[i] < ratings[i+1]) {
                    result[i+1] = (result[i]>result[i+2]?result[i]:result[i+2]) + 1;
                }
                i++;
            }
        }
        int sum = 0; 
        for (int i=0; i < result.length; i++) {
            sum += result[i];
        }
        return sum;
    }
}
