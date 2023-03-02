package com.prac;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class DpMain {
    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        System.out.println(new DP9465().solution());
        new DP9465().input();
    }
}

class DP9465 {
    /**
     스티커

     상근이의 여동생 상냥이는 문방구에서 스티커 2n개를 구매했다. 스티커는 그림 (a)와 같이 2행 n열로 배치되어 있다.
     상냥이는 스티커를 이용해 책상을 꾸미려고 한다.

     상냥이가 구매한 스티커의 품질은 매우 좋지 않다. 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다.
     즉, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.



     모든 스티커를 붙일 수 없게된 상냥이는 각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내려고 한다.
     먼저, 그림 (b)와 같이 각 스티커에 점수를 매겼다. 상냥이가 뗄 수 있는 스티커의 점수의 최댓값을 구하는 프로그램을 작성하시오. 즉, 2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합을 구해야 한다.

     위의 그림의 경우에 점수가 50, 50, 100, 60인 스티커를 고르면, 점수는 260이 되고 이 것이 최대 점수이다.
     가장 높은 점수를 가지는 두 스티커 (100과 70)은 변을 공유하기 때문에, 동시에 뗄 수 없다.

     입력
     첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 n (1 ≤ n ≤ 100,000)이 주어진다.
     다음 두 줄에는 n개의 정수가 주어지며, 각 정수는 그 위치에 해당하는 스티커의 점수이다. 연속하는 두 정수 사이에는 빈 칸이 하나 있다.
     점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

     출력
     각 테스트 케이스 마다, 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값을 출력한다.
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int[] arr0 = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int[] arr1 = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

            int solution = solution(n, arr0, arr1);
            System.out.println(solution);
        }
    }

    private int solution(int n, int[] arr0, int[] arr1) {

        int[][] dp = new int[2][n + 1];

        dp[0][1] = arr0[0];
        dp[1][1] = arr1[0];

        if (n > 1){
            dp[0][2] = arr1[0] + arr0[1];
            dp[1][2] = arr0[0] + arr1[1];
        }

        for (int i = 3; i <= n; i++) {
            dp[0][i] = Math.max(dp[1][i - 2], dp[1][i - 1]) + arr0[i-1];
            dp[1][i] = Math.max(dp[0][i - 2], dp[0][i - 1]) + arr1[i-1];
        }

        return Math.max(dp[0][n], dp[1][n]);
    }
}

class DP2193 {
    /**
     이친수

     문제
     0과 1로만 이루어진 수를 이진수라 한다. 이러한 이진수 중 특별한 성질을 갖는 것들이 있는데,
     이들을 이친수(pinary number)라 한다. 이친수는 다음의 성질을 만족한다.

     이친수는 0으로 시작하지 않는다.
     이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
     예를 들면 1, 10, 100, 101, 1000, 1001 등이 이친수가 된다. 하지만 0010101이나 101101은 각각 1, 2번 규칙에 위배되므로 이친수가 아니다.

     N(1 ≤ N ≤ 90)이 주어졌을 때, N자리 이친수의 개수를 구하는 프로그램을 작성하시오.

     입력
     첫째 줄에 N이 주어진다.

     출력
     첫째 줄에 N자리 이친수의 개수를 출력한다.
     */

    public long solution(int n) {
        // 범위가 90까지 이므로, 충분히 큰 정수를 담을 수 있게 long arr로 선언해야 한다.
        long[] dp = new long[n + 2];

        dp[1] = 1;
        dp[2] = 1;

        for (int i = 3; i < n + 2; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }

//        System.out.println("Arrays.toString(dp) = " + Arrays.toString(dp));
        return dp[n];
    }
}

class DP11057 {
    /**
     오르막 수
     시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
     1 초	256 MB	45707	22328	17257	47.633%
     문제
     오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.

     예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.

     수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.

     입력
     첫째 줄에 N (1 ≤ N ≤ 1,000)이 주어진다.

     출력
     첫째 줄에 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지를 출력한다.
     */

    public long solution(int n) {
        if (n == 1) {
            return 10;
        }

        int mod = 10007;

        long answer = 0;

        long[][] dp = new long[n + 1][11];

        for (int i = 0; i < 11; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i < n+1; i++) {
            for (int j = 1; j < 11; j++) {
                dp[i][j] = (dp[i -1][j] + dp[i][j-1]) % mod;
            }
        }

        for (int i = 0; i < 11; i++) {
            answer += dp[n][i];
        }

        return answer % mod;
    }
}

class DP10844 {
    /**
     문제
     45656이란 수를 보자.

     이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

     N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

     입력
     첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

     출력
     첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

     */

    public long solution(int n) {
        long answer = 0;
        long mod = 1000000000;

        long[][] dp = new long[n + 1][10];

        for (int i = 1; i < 10; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i < n+1; i++) {
            for (int j = 0; j < 10; j++) {
                if (j == 0) {
                    dp[i][j] = (dp[i-1][j+1]) % mod;
                } else if (j == 9){
                    dp[i][j] = (dp[i-1][j-1]) % mod;
                } else {
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod;
                }
            }
        }

        for (int i = 0; i < 10; i++) {
            answer += dp[n][i];
//            System.out.println("dp[n][i] = " + dp[n][i]);
        }


        return answer%mod;
    }
}

class DP9095 {
    /**
     문제
     정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

     1+1+1+1
     1+1+2
     1+2+1
     2+1+1
     2+2
     1+3
     3+1
     정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

     입력
     첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

     출력
     각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

     예제 입력 1
     3
     4
     7
     10
     예제 출력 1
     7
     44
     274
     */

    public int solution(int n) {
        int dp[] = new int[11];

        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;


        for (int i = 4; i <= n ; i++) {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        }
        return dp[n];
    }
}

class DP11727 {
    /**
     * 문제
     * 2×n 크기의 직사각형을 1×2, 2×1, 2*2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
     *
     *
     * 입력
     * 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
     *
     * 출력
     * 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
     */


    public int solution(int n) {
        int dp[] = new int[1001];

        dp[1] = 1;
        dp[2] = 3;

        for (int i = 3; i <= n ; i++) {
            dp[i] = (dp[i - 1] % 10007 + 2 * (dp[i - 2] % 10007))%10007;
        }

        return dp[n] % 10007;
    }
}

class DP11726 {
    /**
     * 문제
     * 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
     *
     *
     * 입력
     * 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
     *
     * 출력
     * 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
     */

    public int solution(int n) {

        int dp[] = new int[1001];

        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= n ; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
        }

        return dp[n]%10007;
    }
}

class DP1463 {
    /**
     * 문제
     * 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
     *
     * X가 3으로 나누어 떨어지면, 3으로 나눈다.
     * X가 2로 나누어 떨어지면, 2로 나눈다.
     * 1을 뺀다.
     * 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
     *
     * 입력
     * 첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.
     *
     * 출력
     * 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
     *
     * 예제 입력 1
     * 2
     * 예제 출력 1
     * 1
     * 예제 입력 2
     * 10
     * 예제 출력 2
     * 3
     * 힌트
     * 10의 경우에 10 → 9 → 3 → 1 로 3번 만에 만들 수 있다.
     * 5 -> 4 -> 2 -> 1
     */

    /**
     * DP 문제를 풀 땐 3가지 단계를 생각한다.
     * 1. 테이블 정의
     * 2. 점화식 찾기
     * 3. 초기값 정하기
     *
     * 문제에 적용해보자.
     *
     * 1. 테이블 정의
     *
     * D[i] = 정수가 i를 1로 만들때 연산을 하는 횟수의 최솟값
     *
     * 2. 점화식 찾기
     *
     * D[12] = ?
     * 3으로 나누거나 (D[12] = D[4] + 1) = (D[k] = D[k/3] + 1)
     * 2로 나누거나 (D[12] = D[6] + 1) = (D[k] = D[k/2] + 1)
     * 1을 빼거나 (D[12]=D[11]+1) = (D[k] = D[k-1] + 1)
     * -> D[12] = min(D[4] + 1, D[6] + 1, D[11] + 1)
     * -> D[k] = min(D[k/3] + 1, D[k/2] + 1, D[k-1] + 1)
     *
     * 즉,
     * -> D[i] = min(3으로 나눌 때, 2로 나눌 때, 1을 뺄 때)
     *
     * 3. 초기값 정의하기
     *
     * D[0] = D[1] = 0
     */

    public int solution(int X) {

        int dp[] = new int[X + 1];

        dp[0] = dp[1] = 0;

        for (int i = 2; i <= X; i++) {
            dp[i] = dp[i - 1] + 1;
            if(i % 2 == 0) dp[i] = Math.min(dp[i], dp[i / 2] + 1);
            if(i % 3 == 0) dp[i] = Math.min(dp[i], dp[i / 3] + 1);
        }

        return dp[X];
    }


    /*    *//**
     * 왜 틀렸는지 모르겠음..
     *//*
    public int solution(int X) {
        int answer = 1;

        if (X == 1) {
            return 0;
        }

        HashSet<Integer> nodeSet = new HashSet<>();
        int curNode ;

        curNode = X - 1;
        if (curNode == 1) {
            return 1;
        } else {
            nodeSet.add(curNode);
        }
        if (X % 2 == 0){
            curNode = X / 2;
            if (curNode == 1) {
                return 1;
            } else {
                nodeSet.add(curNode);
            }
        } else if (X % 3 == 0) {
            curNode = X / 3;
            if (curNode == 1) {
                return 1;
            } else {
                nodeSet.add(curNode);
            }
        }
        System.out.println("nodeSet = " + nodeSet);

        mainLoop:
        while (true) {
            HashSet<Integer> newNodeSet = new HashSet<>();
            answer ++;
            for (int parentNode : nodeSet) {
//                System.out.println("parentNode = " + parentNode);

                curNode  = parentNode - 1;
                if (curNode == 1) {
                    break mainLoop;
                } else {
                    newNodeSet.add(curNode);
                }

                if (parentNode % 2 == 0){
                    curNode  = parentNode / 2;
                    if (curNode == 1) {
                        break mainLoop;
                    } else {
                        newNodeSet.add(curNode);
                    }
                } else if (parentNode % 3 == 0) {
                    curNode = parentNode / 3;
                    if (curNode == 1) {
                        break mainLoop;
                    } else {
                        newNodeSet.add(curNode);
                    }
                }
            }

            System.out.println("newNodeSet = " + newNodeSet);
            // 최신화
            nodeSet = newNodeSet;
        }
        return answer;
    }*/
}
