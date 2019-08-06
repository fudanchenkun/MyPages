package algorithm;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.PriorityQueue;


public class FindPath {
    ArrayList<ArrayList<Integer>> ans = new ArrayList<ArrayList<Integer>>();
    void findOne(TreeNode root, int target, ArrayList<Integer> path){
        if(target < 0)
            return;
        if(target == root.val && root.left == null && root.right == null){
            path.add(root.val);
            ans.add(path);
            return ;
        }
        path.add(root.val);
        ArrayList<Integer> newPath = new ArrayList<>();
        newPath.addAll(path);
        if(root.left != null)
            findOne(root.left, target - root.val, path);
        if(root.right != null)
            findOne(root.right, target-root.val, newPath);
        return;
    }

    public ArrayList<ArrayList<Integer>> findPath(TreeNode root,int target) {
        if(root==null)return ans;
        findOne(root, target, new ArrayList<Integer>());
        return ans;
    }

    public static void main(String[] args) {
        Integer[] seq = new Integer[]{1,2,3,4,9,3,10};
        TreeNode root = TreeNode.createTree(seq);
        System.out.println("Tree Built");
        FindPath findPath = new FindPath();
        ArrayList<ArrayList<Integer>> ans = findPath.findPath(root, 7);
        for (int i = 0; i < ans.size(); i++) {
            for (int j = 0; j < ans.get(i).size(); j++) {
                System.out.print(ans.get(i).get(j));
            }
            System.out.println();
        }
//        TreeNode.printTree(root);


       PriorityQueue<Integer> priorityQueue =  new PriorityQueue<>();
    }
}
