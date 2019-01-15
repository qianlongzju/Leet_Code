class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (k == 0) {
            return new int[0];
        }
        int[] result = new int[nums.length-k+1];
        LinkedList<Integer> q = new LinkedList<>();
        for (int i=0; i < nums.length; i++) {
            if (q.size() != 0 && q.peekFirst() == i-k) {
                q.pollFirst();
            }
            while (q.size() != 0 && nums[q.peekLast()] < nums[i]) {
                q.pollLast();
            }
            q.addLast(i);
            if (i>=k-1) {
              result[i-(k-1)] = nums[q.peekFirst()];
            }
        }
        return result;
    }
}
