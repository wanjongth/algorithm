package com.prac;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class GraphMain {
    public static void main(String[] args) throws IOException {
        new P10451().input();
    }
}


class P10451 {
    /**
     순열 사이클 다국어
     시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
     1 초	256 MB	17549	11052	7944	62.739%
     문제


     1부터 N까지 정수 N개로 이루어진 순열을 나타내는 방법은 여러 가지가 있다. 예 를 들어,
     8개의 수로 이루어진 순열 (3, 2, 7, 8, 1, 4, 5, 6)을 배열을 이용해 표현하면
     ... 와 같다. 또는, Figure 1과 같이 방향 그래프로 나타낼 수도 있다.

     순열을 배열을 이용해
     (i ~ n)
     (Xi~Xn)
     로 나타냈다면,
     i에서 Xi로 간선을 이어 그래프로 만들 수 있다.

     Figure 1에 나와있는 것 처럼, 순열 그래프 (3, 2, 7, 8, 1, 4, 5, 6) 에는 총 3개의 사이클이 있다. 이러한 사이클을 "순열 사이클" 이라고 한다.

     N개의 정수로 이루어진 순열이 주어졌을 때,
     순열 사이클의 개수를 구하는 프로그램을 작성하시오.

     입력
     첫째 줄에 테스트 케이스의 개수 T가 주어진다.
     각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.

     출력
     각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.

     예제 입력 1
     2
     8
     3 2 7 8 1 4 5 6
     10
     2 1 3 4 5 6 7 9 10 8
     예제 출력 1
     3
     7
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());

        for (int i = 0; i < tc; i++) {
            int n = Integer.parseInt(br.readLine());
            int[] p = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

            Graph graph = new Graph(n+1);

            for (int j = 1; j <= n; j++) {
                graph.addEdge(j, p[j-1]);
            }

            int cnt = 0;
            for (int j = 1; j <= n; j++) {
                if(!graph.getVisited()[j]){
                    cnt++;
                    graph.BFS(j);
                }
            }

            System.out.println(cnt);
        }
    }
}

class P1707 {
    /**
     이분 그래프
     시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
     2 초	256 MB	80657	21479	13028	23.738%
     문제
     그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
     그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

     그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

     입력
     입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다.
     각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다.
     각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데,
     각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다.

     출력
     K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

     제한
     2 ≤ K ≤ 5
     1 ≤ V ≤ 20,000
     1 ≤ E ≤ 200,000
     예제 입력 1
     2
     3 2
     1 3
     2 3
     4 4
     1 2
     2 3
     3 4
     4 2
     예제 출력 1
     YES
     NO


     ## 참고
     이분 그래프란 인접한 정점끼리 서로 다른 색으로 칠하여 모든 정점을 두 그룹으로 나누고, 서로 다른 그룹의 정점을 간선으로 연결한 그래프를 말한다.
     "모든 인접한 정점이 서로 다른 색으로 칠해지면 이분 그래프"이고, 그렇지 않으면 이분 그래프가 아니다.
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int k = Integer.parseInt(br.readLine());

        for (int i = 0; i < k; i++) {
            int[] firstLine = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int v = firstLine[0]; // 정점 개수
            int e = firstLine[1]; // 간선 개수
            BinGraph graph = new BinGraph(v + 1);

            for (int j = 0; j < e; j++) {
                int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                graph.addEdge(arr[0], arr[1]);
                graph.addEdge(arr[1], arr[0]);
            }

            graph.isBinGraphWithBFS(v);
        }
    }
}


class BinGraph {
    private int V; // 정점의 개수
    private ArrayList<Integer> adj[]; // 그래프

    private int visited[];

    public BinGraph(int v) {
        V = v;
        adj = new ArrayList[v];
        visited = new int[v];

//        System.out.println(Arrays.toString(visited));

        for (int i = 0; i < v; ++i) {
            adj[i] = new ArrayList<>();
        }

    }

    void addEdge(int v, int w) {
        adj[v].add(w);
    }

    void isBinGraphWithBFS(int v) {
        Queue<Integer> queue = new LinkedList<>();

        for (int j = 0; j <= v ; j++) {

            if (visited[j] == 0) {
                visited[j] = 1;
                queue.add(j);
            }

            while (!queue.isEmpty()) {
                Integer now = queue.poll();

                //            System.out.println("now = " + now);
                for (int i = 0; i < adj[now].size(); i++) {
                    //                System.out.println("node = " + node);
                    //                System.out.println("Arrays.toString(visited) = " + Arrays.toString(visited));

                    // 방문한적 없다면 큐에 추가
                    if(visited[adj[now].get(i)] == 0) {
                        queue.add(adj[now].get(i));
                    }

                    // 현재 노드랑 연결된 부분이 같으면 NO 리턴
                    if(visited[adj[now].get(i)] == visited[now]){
                        System.out.println("NO");
                        return;
                    }

                    // 기준 노드가 1, 연결된 노드가 방문한적 없다면 2
                    if(visited[now] == 1 && visited[adj[now].get(i)] == 0) {
                        visited[adj[now].get(i)] = 2;
                    } else if(visited[now] == 2 && visited[adj[now].get(i)] == 0) { // 기준 노드가 2, 연결된 노드가 방문한적 없다면 1
                        visited[adj[now].get(i)] = 1;
                    }
                }
            }
        }

        System.out.println("YES");
    }

    @Override
    public String toString() {
        return "BinGraph{" +
                "V=" + V +
                ", adj=" + Arrays.toString(adj) +
                ", visited=" + Arrays.toString(visited) +
                '}';
    }
}

class P11724 {
    /**
     연결 요소의 개수
     문제
     방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

     입력
     첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
     둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
     (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

     출력
     첫째 줄에 연결 요소의 개수를 출력한다.

     예제 입력 1
     6 5
     1 2
     2 5
     5 1
     3 4
     4 6
     예제 출력 1
     2
     예제 입력 2
     6 8
     1 2
     2 5
     5 1
     3 4
     4 6
     5 4
     2 4
     2 3
     예제 출력 2
     1
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] firstLine = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = firstLine[0];// 정점 개수
        int m = firstLine[1];// 간선 개수

        Graph graph = new Graph(n + 1);
        for (int i = 0; i < m; i++) {
            int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            graph.addEdge(arr[0], arr[1]);
            graph.addEdge(arr[1], arr[0]);// 무방향 그래프이므로 반대로도
        }

        int cnt = 0;
        for (int i = 1; i <= n; i++) {
            if (!graph.getVisited()[i]) {
                graph.DFS(i);
                cnt ++;
            }
        }

        System.out.println(cnt);
    }
}


class P1260 {
    /**
     * DFS와 BFS
     * 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
     * 2 초	128 MB	233973	88695	52640	36.740%
     * 문제
     * 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
     * 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
     * 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
     *
     * <p>
     * 입력
     * 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
     * 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
     * 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
     *
     * <p>
     * 출력
     * 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
     * V부터 방문된 점을 순서대로 출력하면 된다.
     * <p>
     * 예제 입력 1
     4 5 1
     1 2
     1 3
     1 4
     2 4
     3 4
     * 예제 출력 1
     * 1 2 4 3
     * 1 2 3 4
     * 예제 입력 2
     * 5 5 3
     * 5 4
     * 5 2
     * 1 2
     * 3 4
     * 3 1
     * 예제 출력 2
     * 3 1 2 5 4
     * 3 1 4 2 5
     * 예제 입력 3
     * 1000 1 1000
     * 999 1000
     * 예제 출력 3
     * 1000 999
     * 1000 999
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = arr[0];
        int m = arr[1];
        int v = arr[2];

        Graph graph = new Graph(n + 1);

        for (int i = 0; i < m; i++) {
            arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            graph.addEdge(arr[0], arr[1]);
            graph.addEdge(arr[1], arr[0]);
        }

        graph.graphSort();
        graph.DFS(v);
        graph.BFS(v);

        System.out.println(graph.getDFSreturn());
        System.out.println(graph.getBFSreturn());
    }
}


class Graph {
    private int V; // 정점의 개수
    private LinkedList<Integer> adj[]; // 그래프

    private boolean visited[];

    private StringBuilder DFSreturn = new StringBuilder();
    private StringBuilder BFSreturn = new StringBuilder();

    public boolean[] getVisited() {
        return visited;
    }

    public StringBuilder getDFSreturn() {
        return DFSreturn;
    }

    public StringBuilder getBFSreturn() {
        return BFSreturn;
    }

    public Graph(int v) {
        V = v;
        adj = new LinkedList[v];
        visited = new boolean[v];

        for (int i = 0; i < v; ++i) {
            adj[i] = new LinkedList<>();
        }

    }

    void addEdge(int v, int w) {
        adj[v].add(w);
    }

    void graphSort() {
        for (LinkedList<Integer> node : adj) {
            Collections.sort(node);
        }
    }

    /* DFS
     * v : 시작 노드
     *  */
    void DFS(int v) {
        // v를 시작 노드로 DFSUtil 재귀 호출
        DFSUtil(v, visited);
    }

    void DFSUtil(int v, boolean visited[]) {
        // 현재 노드를 방문한 것으로 표시하고 값을 출력
        visited[v] = true;

        DFSreturn.append(v + " ");

        for (Integer node : adj[v]) {
            // 방문하지 않았으면 그 노드를 시작노드로 재귀호출
            if (!visited[node]) {
                DFSUtil(node, visited);
            }
        }
    }

    void BFS(int v) {
        Queue<Integer> queue = new LinkedList<>();

        // 시작노드 방문처리, queue에 삽입, 출력
        visited[v] = true;
        queue.add(v);

        while (!queue.isEmpty()) {
            Integer a = queue.poll();

            BFSreturn.append(a + " ");

            for (Integer node : adj[a]) {
                if (!visited[node]) {
                    visited[node] = true;
                    queue.add(node);
                }
            }
        }
    }

    @Override
    public String toString() {
        return "Graph{" +
                "V=" + V +
                ", adj=" + Arrays.toString(adj) +
                '}';
    }
}
