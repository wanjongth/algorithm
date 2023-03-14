package com.prac;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class DpMain {
    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        System.out.println(new DP9465().solution());
        new DP11052().input();
    }
}
class DP11052 {
    /**
     카드 구매하기
     문제
     요즘 민규네 동네에서는 스타트링크에서 만든 PS카드를 모으는 것이 유행이다.

     PS카드는 PS(Problem Solving)분야에서 유명한 사람들의 아이디와 얼굴이 적혀있는 카드이다.
     각각의 카드에는 등급을 나타내는 색이 칠해져 있고, 다음과 같이 8가지가 있다.

     전설카드
     레드카드
     오렌지카드
     퍼플카드
     블루카드
     청록카드
     그린카드
     그레이카드
     카드는 카드팩의 형태로만 구매할 수 있고, 카드팩의 종류는 카드 1개가 포함된 카드팩,
     카드 2개가 포함된 카드팩, ... 카드 N개가 포함된 카드팩과 같이 총 N가지가 존재한다.

     민규는 카드의 개수가 적은 팩이더라도 가격이 비싸면 높은 등급의 카드가 많이 들어있을 것이라는 미신을 믿고 있다.
     따라서, 민규는 돈을 최대한 많이 지불해서 카드 N개 구매하려고 한다. 카드가 i개 포함된 카드팩의 가격은 Pi원이다.

     예를 들어, 카드팩이 총 4가지 종류가 있고, P1 = 1, P2 = 5, P3 = 6, P4 = 7인 경우에
     민규가 카드 4개를 갖기 위해 지불해야 하는 금액의 최댓값은 10원이다. 2개 들어있는 카드팩을 2번 사면 된다.

     P1 = 5, P2 = 2, P3 = 8, P4 = 10인 경우에는 카드가 1개 들어있는 카드팩을 4번 사면 20원이고, 이 경우가 민규가 지불해야 하는 금액의 최댓값이다.

     마지막으로, P1 = 3, P2 = 5, P3 = 15, P4 = 16인 경우에는 3개 들어있는 카드팩과 1개 들어있는 카드팩을 구매해 18원을 지불하는 것이 최댓값이다.

     카드 팩의 가격이 주어졌을 때, N개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최댓값을 구하는 프로그램을 작성하시오.
     N개보다 많은 개수의 카드를 산 다음, 나머지 카드를 버려서 N개를 만드는 것은 불가능하다.
     즉, 구매한 카드팩에 포함되어 있는 카드 개수의 합은 N과 같아야 한다.

     입력
     첫째 줄에 민규가 구매하려고 하는 카드의 개수 N이 주어진다. (1 ≤ N ≤ 1,000)

     둘째 줄에는 Pi가 P1부터 PN까지 순서대로 주어진다. (1 ≤ Pi ≤ 10,000)

     출력
     첫째 줄에 민규가 카드 N개를 갖기 위해 지불해야 하는 금액의 최댓값을 출력한다.

     예제 입력 1
     4
     1 5 6 7
     예제 출력 1
     10

     예제 입력 2
     5
     10 9 8 7 6
     예제 출력 2
     50

     예제 입력 3
     10
     1 1 2 3 5 8 13 21 34 55
     예제 출력 3
     55

     예제 입력 4
     10
     5 10 11 12 13 30 35 40 45 47
     예제 출력 4
     50

     예제 입력 5
     4
     5 2 8 10
     예제 출력 5
     20

     예제 입력 6
     4
     3 5 15 16
     예제 출력 6
     18
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        System.out.println(solution(n, arr));
    }

    private int solution(int n, int[] arr) {
        int[] dp = new int[n + 1];

        /**
         * 카드 4개 구매
         * 최대 금액
         *
         * 카드 3개 구매 최댓값 + 1개짜리 카드팩
         * 카드 2개 구매 최댓값 + 2개짜리 카드팩
         * 카드 1개 구매 최댓값 + 3개짜리 카드팩
         * 카드 0개 구매 최대값 + 4개짜리 카드팩 구매
         *
         * dp[4-i] + arr[i]
         */
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i ; j++) {
                dp[i] = Math.max(dp[i],dp[i-j]+arr[j-1]);
            }
        }

        return dp[n];
    }
}

class DP2011 {
    /**
     암호코드

     문제
     상근이와 선영이가 다른 사람들이 남매간의 대화를 듣는 것을 방지하기 위해서 대화를 서로 암호화 하기로 했다. 그래서 다음과 같은 대화를 했다.

     상근: 그냥 간단히 암호화 하자. A를 1이라고 하고, B는 2로, 그리고 Z는 26으로 하는거야.
     선영: 그럼 안돼. 만약, "BEAN"을 암호화하면 25114가 나오는데, 이걸 다시 글자로 바꾸는 방법은 여러 가지가 있어.
     상근: 그렇네. 25114를 다시 영어로 바꾸면, "BEAAD", "YAAD", "YAN", "YKD", "BEKD", "BEAN" 총 6가지가 나오는데,
     BEAN이 맞는 단어라는건 쉽게 알수 있잖아?
     선영: 예가 적절하지 않았네 ㅠㅠ 만약 내가 500자리 글자를 암호화 했다고 해봐. 그 때는 나올 수 있는 해석이 정말 많은데, 그걸 언제 다해봐?
     상근: 얼마나 많은데?
     선영: 구해보자!
     어떤 암호가 주어졌을 때, 그 암호의 해석이 몇 가지가 나올 수 있는지 구하는 프로그램을 작성하시오.

     입력
     첫째 줄에 5000자리 이하의 암호가 주어진다. 암호는 숫자로 이루어져 있다.

     출력
     나올 수 있는 해석의 가짓수를 구하시오. 정답이 매우 클 수 있으므로, 1000000으로 나눈 나머지를 출력한다.

     암호가 잘못되어 암호를 해석할 수 없는 경우에는 0을 출력한다.

     예제 입력 1
     25114
     예제 출력 1
     6
     예제 입력 2
     1111111111
     예제 출력 2
     89
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        System.out.println(solution(s));
    }

    private long solution(String s) {
        long mod = 1000000;

        if (s.startsWith("0")){
            return 0;
        }

        int n = s.length();
        s = "0" + s;
        char[] arr = s.toCharArray();
        long[] dp = new long[n + 1];

        dp[0] = 1;
        dp[1] = 1; // 1 ~ 9까지
        for (int i = 2; i <= n; i++) {
            int preNum = arr[i - 1] - 48;
            int curNum = arr[i] - 48;

            if (curNum == 0) { // 현재 숫자가 0일 경우 : 10, 20
                if (preNum == 1 || preNum == 2) {
                    dp[i] = dp[i - 2];
                } else {
                    dp[i] = 0;
                }
            } else {
                int a = preNum * 10 + curNum;

                if (a <= 26 && preNum != 0) {
                    dp[i] = dp[i - 1] + dp[i - 2];
                } else {
                    dp[i] = dp[i - 1];
                }
            }

            dp[i] = dp[i] % mod;
        }


//        System.out.println("Arrays.toString(dp) = " + Arrays.toString(dp));

        return dp[n];
    }
}

class DP2225 {
    /**
     합분해

     문제
     0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.

     덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.

     입력
     첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.

     출력
     첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.

     예제 입력 1
     20 2
     예제 출력 1
     21
     예제 입력 2
     6 4
     예제 출력 2
     84
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        System.out.println(solution(arr));

    }

    private long solution(int[] arr) {
        long mod = 1000000000;

        int n = arr[0];
        int k = arr[1];

        long[][] dp = new long[n + 1][k + 1];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                if (j == 1) {
                    dp[i][j] = 1;
                } else if(i == 1) {
                    dp[i][j] = j;
                } else {
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod;
                }
            }
        }

        return dp[n][k];
    }
}

class DP2133 {
    /**
     타일 채우기
     시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
     2 초	128 MB	44413	15948	12631	35.765%
     문제
     3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

     입력
     첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.

     출력
     첫째 줄에 경우의 수를 출력한다.
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        System.out.println(solution(n));
    }

    private int solution(int n) {
        int[] dp = new int[31];

        dp[0] = 1;
        dp[2] = 3;

        if (n % 2 == 1) {
            return 0;
        }

        for (int i = 4; i <= n; i++) {
            dp[i] = dp[i-2] * 3;
            for (int j = 4; j <= i; j+=2) {
                dp[i] += dp[i - j] * 2;
            }
        }

        return dp[n];
    }
}


class DP1699 {
    /**
     제곱수의 합

     문제
     어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다.
     예를 들어 11=3^2+1^2+1^2(3개 항)이다. 이런 표현방법은 여러 가지가 될 수 있는데,
     11의 경우 11=2^2+2^2+1^2+1^2+1^2(5개 항)도 가능하다. 이 경우,
     수학자 숌크라테스는 “11은 3개 항의 제곱수 합으로 표현할 수 있다.”라고 말한다.
     또한 11은 그보다 적은 항의 제곱수 합으로 표현할 수 없으므로, 11을 그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3이다.

     주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의 최소개수를 구하는 프로그램을 작성하시오.

     입력
     첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000)

     출력
     주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력한다.

     예제 입력 1
     7
     예제 출력 1
     4
     예제 입력 2
     1
     예제 출력 2
     1
     예제 입력 3
     4
     예제 출력 3
     1
     예제 입력 4
     11
     예제 출력 4
     3
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        System.out.println(solution(n));
    }

    private int solution(int n) {

        // 1부터 시작, dp : n을 제곱수들의 합으로 표현햇을 때 나올 수 있는 최소 항의 갯수 배열
        int[] dp = new int[n+1];

        //
        for (int i = 1; i <= n; i++) {
            dp[i] = i; // 초기화 : 1의 제곱수로 표현했을 경우

            for (int j = 1; j * j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
            }
        }

        return dp[n];

    }
}

class DP2579 {
    /**
     * 계단 오르기
     * 문제
     * 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다.
     * <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.
     *
     *
     *
     * <그림 1>
     *
     * 예를 들어 <그림 2>와 같이 시작점에서부터 첫 번째, 두 번째, 네 번째, 여섯 번째 계단을 밟아 도착점에 도달하면
     * 총 점수는 10 + 20 + 25 + 20 = 75점이 된다.
     *
     *
     *
     * <그림 2>
     *
     * 계단 오르는 데는 다음과 같은 규칙이 있다.
     *
     * 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
     * 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
     *
     * 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
     * 마지막 도착 계단은 반드시 밟아야 한다.
     *
     * 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나,
     * 세 번째 계단으로 오를 수 있다.
     * 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.
     *
     * 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.
     *
     * 입력
     * 입력의 첫째 줄에 계단의 개수가 주어진다.
     *
     * 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다.
     * 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.
     *
     * 출력
     * 첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.
     *
     6
     10
     20
     15
     25
     10
     20

     75
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        System.out.println(solution(n, arr));
    }

    private int solution(int n, int[] arr) {
        int[] dp = new int[n];

        dp[0] = arr[0];
        if (n == 1){
            return dp[0];
        }
        dp[1] = arr[0] + arr[1];
        if (n == 2){
            return dp[1];
        }
        dp[2] = Math.max(arr[2] + dp[0], arr[1] + arr[2]);
        if (n == 3) {
            return dp[2];
        }

        for (int i = 3; i < n; i++) {
            dp[i] = Math.max(dp[i - 2] + arr[i], dp[i - 3] + arr[i-1] + arr[i]);
        }

        return dp[n-1];
    }
}

class DP1912 {
    /**
     연속합

     문제
     n개의 정수로 이루어진 임의의 수열이 주어진다.
     우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.

     예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

     입력
     첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고
     둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

     출력
     첫째 줄에 답을 출력한다.

     예제 입력 1
     10
     10 -4 3 1 5 6 -35 12 21 -1
     예제 출력 1
     33

     예제 입력 2
     10
     2 1 -4 3 4 -4 6 5 -5 1
     예제 출력 2
     14

     예제 입력 3
     5
     -1 -2 -3 -4 -5
     예제 출력 3
     -1
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        System.out.println(solution(n, arr));
    }

    private int solution(int n, int[] arr) {
        int[] dp = new int[n];

        dp[0] = arr[0];
        int answer = arr[0];
        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(dp[i - 1] + arr[i], arr[i]);
            answer = Math.max(dp[i], answer);
        }

//        System.out.println("Arrays.toString(dp) = " + Arrays.toString(dp));
        return answer;
    }
}

class DP11054 {
    /**
     가장 긴 바이토닉 부분 수열
     시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
     1 초	256 MB	42934	21925	17145	50.716%

     문제
     수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

     예를 들어, {30}과 {40}, {50} 은 바이토닉 수열이지만,
     {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

     수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

     입력
     첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

     출력
     첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

     예제 입력 1
     10
     1 5 2 1 4 3 4 5 2 1
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        System.out.println(solution(n, arr));
    }

    private int solution(int n, int[] arr) {
        int[] uDp = new int[n];
        int[] dDp = new int[n];

        for (int i = 0; i < n ; i++) {
            // 증가하는 부분수열의 길이
            uDp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j] && uDp[i] < uDp[j] + 1) {
                    uDp[i] = uDp[j] + 1;
                }
            }
        }
        // 방향을 바꿔서 증가하는 수열을 구해야 한다.
        for (int i = n - 1; i >= 0 ; i--) {
            // 감소하는 부분수열의 길이
            dDp[i] = 1;
            for (int j = n - 1; j >= i; j--) {
                if (arr[i] > arr[j] && dDp[i] < dDp[j] + 1) {
                    dDp[i] = dDp[j] + 1;
                }
            }
        }

//        System.out.println(Arrays.toString(uDp));
//        System.out.println(Arrays.toString(dDp));
        int max = 1;
        for (int i = 0; i < n; i++) {
            int sum = uDp[i] + dDp[i] - 1;
            if (sum > max) {
                max = sum;
            }
        }

        return max;
    }
}

class DP11722 {
    /**
     가장 긴 감소하는 부분 수열

     문제
     수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.

     예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {30, 20, 10}  이고, 길이는 3이다.

     입력
     첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

     둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

     출력
     첫째 줄에 수열 A의 가장 긴 감소하는 부분 수열의 길이를 출력한다.

     예제 입력 1
     6
     10 30 10 20 20 10
     예제 출력 1
     3
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        System.out.println(solution(n, arr));
    }

    private int solution(int n, int[] arr) {
        int[] dp = new int[n];

        for (int i = 0; i < n ; i++) {
            dp[i] = 1;

            for (int j = 0; j < i; j++) {
                if (arr[i] < arr[j] // 감소하면서
                        && dp[i] < dp[j] + 1 // 이전 dp들 중 길이가 젤 길면 갱신
                ) {
                    dp[i] = dp[j] + 1;
                }
            }
        }


//        System.out.println(Arrays.toString(dp));

        int max = 1;
        for (int i = 0; i < n; i++) {
            if (dp[i] > max){
                max = dp[i];
            }
        }
        return max;
    }
}

class DP11055 {
    /**
     가장 큰 증가하는 부분 수열

     문제
     수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

     예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에
     합이 가장 큰 증가하는 부분 수열은 A = {1, 2, 50, 60} 이고, 합은 113이다.

     입력
     첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

     둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

     출력
     첫째 줄에 수열 A의 합이 가장 큰 증가하는 부분 수열의 합을 출력한다.

     예제 입력 1
     10
     1 100 2 50 60 3 5 6 7 8
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        System.out.println(solution(n, arr));
    }

    private int solution(int n, int[] arr) {
        int[] dp = new int[n];

        for (int i = 0; i < n ; i++) {
            dp[i] = arr[i];
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j] // 증가하면서
                        && dp[i] < dp[j] + arr[i] // 이전 dp 값 더하기 지금 값이 크면
                ) {
                    dp[i] = dp[j] + arr[i]; // 갱신
                }
            }
        }

//        System.out.println(Arrays.toString(dp));

        int max = 1;
        for (int i = 0; i < n; i++) {
            if (dp[i] > max){
                max = dp[i];
            }

        }
        return max;
    }
}

class DP11053 {
    /**
     가장 긴 증가하는 부분 수열

     문제
     수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

     예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 30, 50} 이고, 길이는 4이다.

     입력
     첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.


     둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

     출력
     첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        System.out.println(solution(n, arr));
    }

    private int solution(int n, int[] arr) {
        int[] dp = new int[n];

        for (int i = 0; i < n ; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
        int max = -1;
        for (int i = 0; i < n; i++) {
            max = Math.max(dp[i], max);

        }
        return max;
    }
}


class DP2156 {
    /**
     문제
     효주는 포도주 시식회에 갔다. 그 곳에 갔더니,
     테이블 위에 다양한 포도주가 들어있는 포도주 잔이 일렬로 놓여 있었다.
     효주는 포도주 시식을 하려고 하는데, 여기에는 다음과 같은 두 가지 규칙이 있다.

     포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
     연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
     효주는 될 수 있는 대로 많은 양의 포도주를 맛보기 위해서 어떤 포도주 잔을 선택해야 할지 고민하고 있다.
     1부터 n까지의 번호가 붙어 있는 n개의 포도주 잔이 순서대로 테이블 위에 놓여 있고, 각 포도주 잔에 들어있는 포도주의 양이 주어졌을 때,
     효주를 도와 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성하시오.

     예를 들어 6개의 포도주 잔이 있고, 각각의 잔에 순서대로 6, 10, 13, 9, 8, 1 만큼의 포도주가 들어 있을 때,
     첫 번째, 두 번째, 네 번째, 다섯 번째 포도주 잔을 선택하면 총 포도주 양이 33으로 최대로 마실 수 있다.

     입력
     첫째 줄에 포도주 잔의 개수 n이 주어진다. (1 ≤ n ≤ 10,000)
     둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 포도주의 양은 1,000 이하의 음이 아닌 정수이다.

     출력
     첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        System.out.println(solution(n,arr));
    }

    private int solution(int n, int[] arr) {

        int[] dp = new int[arr.length + 1];

        if (n == 1) {
            return arr[0];
        }
        else if (n==2) {
            return arr[0] + arr[1];
        } else{
            dp[0] = 0;
            dp[1] = arr[0];
            dp[2] = arr[0] + arr[1];

            for (int i = 3; i <= arr.length; i++) {
                dp[i] = Math.max(Math.max(dp[i-1], dp[i-2] + arr[i-1]), dp[i-3] + arr[i-2] + arr[i-1]);
            }
//            System.out.println("Arrays.toString(dp) = " + Arrays.toString(dp));
            return dp[n];
        }
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
