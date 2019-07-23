package algorithm;

public class Floyd {
    private int[][] edges;
    private int numOfVexs;
    Floyd(int[][] edges){
        this.edges = edges;
        this.numOfVexs = edges.length;
    }

    public int[][] execute() {
        int[][] path = new int[numOfVexs][];
        int[][] ans = new int[numOfVexs][];
        for (int i = 0; i < numOfVexs; i++) {
            for (int j = 0; j <numOfVexs; j++) {
                ans[i][j] = edges[i][j];
//                path[i][j] = -1;
            }
        }
        for (int k = 0; k < numOfVexs; k++) {
            for (int i = 0; i < numOfVexs; i++) {
                for (int j = 0; j < numOfVexs; j++) {
                    if(ans[i][k] != Integer.MAX_VALUE && ans[k][j] != Integer.MAX_VALUE){
                        if(ans[i][j] < ans[i][k] + ans[k][j]){
                            ans[i][j] = ans[i][k] + ans[k][j];
                            path[i][j] = k;
                        }

                    }

                }

            }
        }

        return ans;
    }

}
