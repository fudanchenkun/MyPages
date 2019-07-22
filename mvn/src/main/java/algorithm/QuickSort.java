package algorithm;

import java.util.Arrays;
import java.util.List;

public class QuickSort {

    static <E extends Comparable> void sort(E[] nums, int start, int end) {
        if(end - start <= 1)
            return;
        int i = start;
        int j = end;
        E flag = nums[start];
        while (i < j){

            while (i < j && nums[i].compareTo(flag) <= 0){
                i++;
            }
            if(i < j){
                nums[j] = nums[i];
                j--;
            }
            while (i < j && nums[j].compareTo(flag) > 0){
                j--;
            }
            if(i < j){
                nums[i] = nums[j];
                i++;
            }
        }
        nums[i] = flag;
        sort(nums, start, i - 1);
        sort(nums, i+1, end);
    }

    static <E> void swap(E a, E b){
        E tmp = a;
        a = b;
        b = tmp;
    }

    public static void main(String[] args) {
        Integer[] s = new Integer[]{5,3,8,1,9,4};
        for (int i = 0; i < s.length; i++) {
            System.out.print(s[i].toString() + " ");
        }
        System.out.println();
        QuickSort.sort(s, 0, s.length - 1);
        for (int i = 0; i < s.length; i++) {
            System.out.print(s[i].toString() + " ");
        }
    }
}
