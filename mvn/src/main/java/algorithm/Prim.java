package algorithm;

public class Prim {
    private int[][] edges;
    private int numOfVexs;

    Prim(int[][] edges){
        this.edges = edges;
        this.numOfVexs = edges.length;
    }

    public int execute(int v0){
        // 已经并入生成树的节点集合
        boolean[] st = new boolean[numOfVexs];
        // 当前生成树到对应节点的最小值
        int[] lowset = new int[numOfVexs];
        int sum = 0;

        st[0] = true;
        for (int i = 0; i < numOfVexs; i++)
            lowset[i] = edges[v0][i];

        for (int i = 0; i < numOfVexs; i++) {
            int min = Integer.MAX_VALUE;
            int index = -1;
            for (int j = 0; j < numOfVexs; j++) {
                if(!st[j] && lowset[j] < min){
                    min = lowset[j];
                    index = j;
                }
            }
            st[index] = true;
            sum += min;

            for (int j = 0; j < numOfVexs; j++) {
                if(!st[j] && edges[index][j]<lowset[j])
                    lowset[j] = edges[index][j];
            }
        }
        return sum;
    }


}
