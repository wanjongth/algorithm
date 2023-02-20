package com.prac;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class DpMain {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(new DP11727().solution(Integer.parseInt(br.readLine())));
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
