package algorithm;

public class DijkstraNode {
    private ListNode[] vexs;
    private int numOfVexs;

    DijkstraNode(ListNode[] vexs) {
        this.vexs = vexs;
        numOfVexs = vexs.length;
    }

    static class ListNode {
        int weight;
        int index;
        ListNode next = null;
        ListNode(int index, int val) {
            this.index = index;
            this.weight = val;
        }
    }

    private int[] execute(int v){
        if(v < 0 || v >= numOfVexs)
            throw new ArrayIndexOutOfBoundsException();

        int[] distance = new int[numOfVexs];
        boolean[] st = new boolean[numOfVexs];
        st[vexs[v].index] = true;
        ListNode p = vexs[v];
        while (p != null){
            distance[p.index] = p.weight;
            p = p.next;
        }

        for (int i = 0; i < numOfVexs; i++) {
            int min = Integer.MIN_VALUE;
            int index = -1;

            for (int j = 0; j < numOfVexs; j++) {
                if(!st[j] && distance[j] > min){
                    index = j;
                    min = distance[j];
                }
            }
            if(index != -1)
                st[index] = true;
            for (int j = 0; j < numOfVexs; j++) {
                if(!st[j]){
                    ListNode current = vexs[j];
                    while (current != null){
                        if(current.index == index){
                            distance[j] = Math.min(distance[j], distance[index] + current.weight);
                            break;
                        }
                        current = current.next;
                    }
                }
            }

        }
        return distance;

    }



}
