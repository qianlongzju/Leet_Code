public class Solution {
    public int largestRectangleArea(int[] height) {
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
