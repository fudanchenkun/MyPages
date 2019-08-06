package algorithm;

import com.sun.source.tree.Tree;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class TreeNode {
    TreeNode left;
    TreeNode right;
    Integer val;

    TreeNode(Integer val){
        this.val = val;
    }

    public static TreeNode createTree(Integer[] seq){
//        Integer[] treeSeq = new Integer[seq.length + 1];
//        treeSeq[0] = -1;
//        System.arraycopy(seq, 0, treeSeq, 1, seq.length);
        if(seq.length == 0)return null;
        TreeNode[] queue = new TreeNode[seq.length + 1];

        for (int j = 1; j < queue.length; j++)
            queue[j] = new TreeNode(seq[j-1]);
        int i = 1;
        while (2 * i < queue.length){
            TreeNode node = queue[i];
            if(2*i < queue.length)
                node.left = queue[2*i];
            if(2*i+1 < queue.length)
                node.right = queue[2*i+1];
            i++;
        }
        return queue[1];
    }

    public static void BFSPrint(TreeNode root){
        List<TreeNode> queue = new ArrayList<>();
        queue.add(root);
        while (!queue.isEmpty()){
            TreeNode node = queue.get(0);
            System.out.println(node.val);
            if(node.left != null)
                queue.add(node.left);
            if(node.right != null)
                queue.add(node.right);
            queue.remove(0);
        }
    }


    public static void prePrint(TreeNode root){
        Stack<TreeNode> stack = new Stack<>();
        if(root == null)return;
        TreeNode node = root;
        while (!stack.isEmpty() || node != null){
            while (node != null){
                System.out.print(String.format("%s ", node.val));
                stack.push(node);
                node = node.left;
            }
            if(!stack.isEmpty()){
                node = stack.pop();
                node = node.right;
            }
        }
    }

    public static void inPrint(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        if (root == null) return;
        TreeNode node = root;
        while (!stack.isEmpty() || node != null) {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
            if (!stack.isEmpty()) {
                node = stack.pop();
                System.out.print(String.format("%s ", node.val));
                node = node.right;
            }
        }
    }

    public static void afterPrint(TreeNode root){
        // 要重寫
        Stack<TreeNode> stack = new Stack<>();
        TreeNode node = root;
        while (!stack.isEmpty() || node != null){
            while (node != null){
                stack.push(node);
                node = node.left;
            }

            if(!stack.isEmpty()){
                node = stack.pop();
                node = node.right;
                System.out.print(String.format("%s ", node.val));
            }
        }


    }

    public static void main(String[] args) {
        Integer[] seq = new Integer[]{1,2,3,4,5,6};
        TreeNode root = createTree(seq);
        System.out.println("Tree Built");
        BFSPrint(root);
        prePrint(root);
        System.out.println();
        inPrint(root);
        System.out.println();
        afterPrint(root);
    }

}
