package com.prac;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

public class GraphMain {
    public static void main(String[] args) throws IOException {
        new P11724().input();
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
