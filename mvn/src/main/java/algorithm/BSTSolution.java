package algorithm;

public class BSTSolution {
    static int index = 0;

    static class TreeNode{
        private TreeNode left;
        private TreeNode right;
        private int val;

        TreeNode(int val){
            this.val = val;
        }
    }

    TreeNode insertNode(TreeNode root, int val){
        TreeNode current = root;
        TreeNode newNode = new TreeNode(val);
        TreeNode parent;
        if(root == null){
            root = newNode;
            return root;
        }
        while (true){
            parent = current;
            if(val < current.val){
                current = current.left;
                if(current == null){
                    parent.left = newNode;
                    return root;
                }
            }
            else if(val > current.val){
                current = current.right;
                if(current == null){
                    parent.right = newNode;
                    return root;
                }
            }
            else
                return root;

        }

    }

    boolean afterCheck(TreeNode root, int[] seq){
        if(root.left != null)
            if(!afterCheck(root.left, seq))
                return false;
        if(root.right != null)
            if(!afterCheck(root.right, seq))
                return false;
        boolean ans = (seq[index] == root.val);
        System.out.println(String.format("%s, %s, %s",root.val, index, seq[index]));
        index++;
        return ans;
    }

    void scanTree(TreeNode root, int[] seq, int i){
        if(root.left != null)
            scanTree(root.left, seq, i);
        if(root.right != null)
            scanTree(root.right, seq, i);
        System.out.println(String.format("%s, %s, %s",root.val, index, seq[index]));
        index++;
        return;
    }

    public boolean VerifySquenceOfBST(int [] sequence) {
        if(sequence.length == 0)return true;
        TreeNode root = null;
        for(int i=0;i<sequence.length;i++)
        {
            root = insertNode(root, sequence[i]);
        }
        scanTree(root, sequence, 0);
        index = 0;
        return afterCheck(root, sequence);
    }

    public static void main(String[] args) {
//        Collections
        int[] seq = new int[]{4,6,7,5};
        BSTSolution bstSolution = new BSTSolution();
        System.out.println(bstSolution.VerifySquenceOfBST(seq));
    }
}