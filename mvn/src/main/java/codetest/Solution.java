package codetest;

// 1. 构造一个空的头结点，就不必考虑头结点重复需要删除的情况
// 2.

public class Solution {
    public static ListNode deleteDuplication(ListNode head)
    {
        ListNode p = new ListNode(0);
        p.next = head;
        head = p;
        ListNode left;
        ListNode right;

        while(p.next != null){
            left = p.next;
            right = left;
            while(right.next != null && right.next.val == right.val){
                right = right.next;
            }
            if (left == right)
                p = p.next;
            else
                p.next = right.next;
        }
        return head.next;
    }

    public static void main(String[] args) {
        Integer[] input = {1, 1,2, 3, 3,3, 4, 4, 5};
        ListNode phead = new ListNode(input[0]);
        ListNode p = phead;
        for (int i = 1; i < input.length; i++) {
            ListNode tmp = new ListNode(input[i]);
            p.next = tmp;
            p = p.next;
        }

        ListNode ans = Solution.deleteDuplication(phead);
        System.out.println("ans --------------");
        while (ans != null){
            System.out.println(ans.val);
            ans = ans.next;
        }

    }

}
