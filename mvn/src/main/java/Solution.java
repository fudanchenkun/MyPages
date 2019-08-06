import java.util.PriorityQueue;
import java.util.Comparator;
public class Solution {
    private PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    private PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(15, new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            return o2 - o1;
        }
    });
    public void Insert(Integer num) {
        if(minHeap.size() == maxHeap.size()){
            maxHeap.add(num);
        }
        else{
            minHeap.add(num);
        }
        if(maxHeap.size() > 0 && minHeap.size() > 0 && maxHeap.peek() > minHeap.peek()){
            int tmp1 = maxHeap.poll();
            int tmp2 = minHeap.poll();
            maxHeap.add(tmp2);
            minHeap.add(tmp1);
        }
    }

    public Double GetMedian() {
        return (minHeap.size() == maxHeap.size()?Double.valueOf(minHeap.peek() + maxHeap.peek()) / 2:Double.valueOf(maxHeap.peek()));
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Integer[] nums = new Integer[]{5,2,3,4,1,6,7,0,8};
        for (int i = 0; i < nums.length; i++) {
            solution.Insert(i);
        }
        System.out.println(solution.GetMedian());
    }
}