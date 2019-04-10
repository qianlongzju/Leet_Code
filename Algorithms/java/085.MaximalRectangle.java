public class Solution {
    public int maximalRectangle(char[][] matrix) {
        int m = matrix.length;
        if (m == 0)
            return 0;
        int n = matrix[0].length;
        int[][] heights = new int[m][n];
        for (int i=0; i < m; ++i) {
            for (int j=0; j < n; ++j) {
                if (matrix[i][j] == '0')
                    continue;
                if (i == 0)
                    heights[i][j] = 1;
                else 
                    heights[i][j] = heights[i-1][j] + 1;
            }
        }
        int maxArea = 0;
        for (int i=0; i < m; i++) {
            int area = largestRectangleArea(heights[i]);
            if (area > maxArea) 
                maxArea = area;
        }
        return maxArea;
    }
    private int largestRectangleArea(int[] height) {
        if (height.length < 1) {
            return 0;
        }
        Stack<Integer> heights = new Stack<>();
        Stack<Integer> indexes = new Stack<>();
        heights.push(height[0]);
        indexes.push(0);
        int largestArea = height[0];
        int i = 1;
        while (i < height.length) {
            if (height[i] >= heights.peek()) {
                heights.push(height[i]);
                indexes.push(i);
            } else {
                int h=0, j=0;
                while (!heights.empty() && height[i] < heights.peek()) {
                    h = heights.peek();
                    j = indexes.peek();
                    int area = h * (i - j);
                    if (area > largestArea) {
                        largestArea = area;
                    }
                    heights.pop();
                    indexes.pop();
                }
                heights.push(height[i]);
                indexes.push(j);
            }
            i++;
        }
        while (!heights.empty()) {
            if (heights.peek() * (i - indexes.peek()) > largestArea) {
                largestArea = heights.peek() * (i - indexes.peek());
            }
            heights.pop();
            indexes.pop();
        }
        return largestArea;
    }
}
