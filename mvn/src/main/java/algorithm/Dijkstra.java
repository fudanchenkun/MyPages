package algorithm;

public class Dijkstra {
    private int[][] edges;
    private int numOfVexs;


    Dijkstra(int[][] edges){
        this.edges = edges;
        this.numOfVexs = edges.length;
    }

    public int[] execute(int v) {
        if(v > numOfVexs || v < 0)
            throw new ArrayIndexOutOfBoundsException();
        boolean[] st = new boolean[numOfVexs];
        int[] distance = new int[numOfVexs];

        for (int i = 0; i < numOfVexs; i++) {
            for (int j = i + 1; j < numOfVexs; j++) {
                if(edges[i][j] == 0){
                    edges[i][j] = Integer.MAX_VALUE;
                    edges[j][i] = Integer.MAX_VALUE;
                 }
            }
        }

        for(int i = 0; i < numOfVexs; i++) {
            distance[i] = edges[v][i];
        }

        st[v] = true;
        for (int i = 0; i < numOfVexs; ++i) {
            int min = Integer.MIN_VALUE;
            int index = -1;
            // 找出没有归入到确定路径的节点的最短距离
            for (int j = 0; j < numOfVexs; ++j) {
                if(!st[j]){
                    if(distance[j] > min){
                        index = j;
                        min = distance[j];
                    }
                }
            }
            // 把最近的节点加入到确定集
            if(index != -1)
                st[index] = true;
            // 更新distance
            for (int j = 0; j < numOfVexs; j++) {
                if(!st[j]){
                    if(edges[index][j] != Integer.MAX_VALUE &&
                            (min + edges[index][j] < distance[j])){
                        distance[j] = min + edges[index][j];
                    }
                }
            }
        }
        return distance;
    }


}
