package com.prac;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class PMain {
    public static void main(String[] args) throws IOException {
        new P1850().input();
    }
}

class P1850 {
    /**
     * 최대공약수
     * 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
     * 2 초	256 MB	22035	7008	5692	34.041%
     * 문제
     * 모든 자리가 1로만 이루어져있는 두 자연수 A와 B가 주어진다. 이때, A와 B의 최대 공약수를 구하는 프로그램을 작성하시오.
     *
     * 예를 들어, A가 111이고, B가 1111인 경우에 A와 B의 최대공약수는 1이고, A가 111이고, B가 111111인 경우에는 최대공약수가 111이다.
     *
     * 입력
     * 첫째 줄에 두 자연수 A와 B를 이루는 1의 개수가 주어진다. 입력되는 수는 263보다 작은 자연수이다.
     *
     * 출력
     * 첫째 줄에 A와 B의 최대공약수를 출력한다. 정답은 천만 자리를 넘지 않는다.
     *
     * 예제 입력 1
     * 3 4
     * 예제 출력 1
     * 1
     * 예제 입력 2
     * 3 6
     * 예제 출력 2
     * 111
     * 예제 입력 3
     * 500000000000000000 500000000000000002
     * 예제 출력 3
     * 11
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long[] input = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();
        solution(input);

    }

    private void solution(long[] input) {

        StringBuilder sb = new StringBuilder();
        long gcd = gcd(input[0], input[1]);

        for (int i = 0; i < gcd; i++) {
            sb.append("1");
        }

        System.out.println(sb);
    }

    private long gcd(long a, long b) {
        long temp;
        if (a < b) {
            temp = a;
            a = b;
            b = temp;
        }
        while(b!=0) {
            long n = a % b;
            a = b;
            b = n;
        }
        return a;
    }
}

class P1934 {
    /**
     * 최소공배수
     * 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
     * 1 초	128 MB	56606	31704	27109	57.494%
     * 문제
     * 두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
     * 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.
     *
     * 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
     *
     * 입력
     * 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)
     *
     * 출력
     * 첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.
     *
     * 예제 입력 1
     * 3
     * 1 45000
     * 6 10
     * 13 17
     * 예제 출력 1
     * 45000
     * 30
     * 221
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int sol = solution(input);
            sb.append(sol).append("\n");
        }

        System.out.println(sb);
    }

    private int solution(int[] input) {
        int a = input[0];
        int b = input[1];

        int gcd = gcd(a, b);
        int lcm  = a * b / gcd;

        return lcm;
    }


    private int gcd(int a, int b) {
        int temp;
        if (a < b) {
            temp = a;
            a = b;
            b = temp;
        }
        while(b!=0) {
            int n = a % b;
            a = b;
            b = n;
        }
        return a;
    }
}

class P2609 {
    /**
     * 최대공약수와 최소공배수
     * 문제
     * 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
     *
     * 입력
     * 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
     *
     * 출력
     * 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
     *
     * 예제 입력 1
     * 24 18
     * 예제 출력 1
     * 6
     * 72
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        solution(input);
    }

    private void solution(int[] input) {
        StringBuilder sb = new StringBuilder();
        int a = input[0];
        int b = input[1];

        int gcd = gcd(a, b);
        int lcm  = a * b / gcd;

        System.out.println(gcd);
        System.out.println(lcm);
    }

    private int gcd(int a, int b) {
        int temp;
        if (a < b) {
            temp = a;
            a = b;
            b = temp;
        }
        while(b!=0) {
            int n = a % b;
            a = b;
            b = n;
        }
        return a;
    }

    public int gcd2(int p, int q) {
        if (q == 0) {
            return p;
        }
        return gcd2(q, p%q);
    }
}

class P10430 {
    /**
     * 나머지
     * 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
     * 1 초	256 MB	308537	162172	140899	52.997%
     * 문제
     * (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
     *
     * (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
     *
     * 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
     *
     * 입력
     * 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
     *
     * 출력
     * 첫째 줄에 (A+B)%C,
     * 둘째 줄에 ((A%C) + (B%C))%C,
     * 셋째 줄에 (A×B)%C,
     * 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
     *
     * 예제 입력 1
     * 5 8 4
     * 예제 출력 1
     * 1
     * 1
     * 0
     * 0
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        solution(input);
    }

    private void solution(int[] input) {
        StringBuilder sb = new StringBuilder();
        int a = input[0];
        int b = input[1];
        int c = input[2];

        sb.append((a + b) % c).append("\n");
        sb.append(((a%c) + (b%c)) % c).append("\n");
        sb.append((a * b) % c).append("\n");
        sb.append(((a%c) * (b%c)) % c);

        System.out.println(sb);
    }
}

class P1158 {
    /**
     * 요세푸스 문제
     * 문제
     * 요세푸스 문제는 다음과 같다.
     *
     * 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고,
     * 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
     * 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
     * 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
     * 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
     * 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
     *
     * N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
     *
     * 입력
     * 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)
     *
     * 출력
     * 예제와 같이 요세푸스 순열을 출력한다.
     *
     * 예제 입력 1
     * 7 3
     * 예제 출력 1
     * <3, 6, 2, 7, 5, 1, 4>
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        solution(input);

    }

    private void solution(int[] input) {
        StringBuilder sb = new StringBuilder();
        sb.append('<');

        int n = input[0];
        int k = input[1];

        Deque<Integer> deque = new LinkedList<>();

        for (int i = 1; i <= n; i++) {
            deque.add(i);
        }

        while (deque.size() != 1) {
            for (int i = 0; i < k - 1; i++) {
                deque.offer(deque.poll());
            }
            sb.append(deque.poll() + ", ");
        }
        sb.append(deque.poll() + ">");

        System.out.println(sb);
    }
}

class P1406 {
    /**
     * 에디터 다국어
     * <p>
     * 문제
     * 한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로,
     * 최대 600,000글자까지 입력할 수 있다.
     * <p>
     * 이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽),
     * 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다.
     * 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.
     * <p>
     * 이 편집기가 지원하는 명령어는 다음과 같다.
     * <p>
     * L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
     * D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
     * B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
     * <p>
     * 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
     * <p>
     * P $ : $라는 문자를 커서 왼쪽에 추가함
     * 초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때,
     * 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오.
     * 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.
     * <p>
     * 입력
     * 첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다. 이 문자열은 길이가 N이고,
     * 영어 소문자로만 이루어져 있으며, 길이는 100,000을 넘지 않는다.
     * 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다.
     * 셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다. 명령어는 위의 네 가지 중 하나의 형태로만 주어진다.
     * <p>
     * 출력
     * 첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다.
     * <p>
     * 예제 입력 1
     * abcd
     * 3
     * P x
     * L
     * P y
     * 예제 출력 1
     * abcdyx
     * <p>
     * <p>
     * abc
     * 9
     * L
     * L
     * L
     * L
     * L
     * P x
     * L
     * B
     * P y
     */

    public String content = "";
    public int cursor = 0;

    public Stack<String> leftStack;
    public Stack<String> rightStack;

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        leftStack = new Stack<>();
        rightStack = new Stack<>();

        // left Stack 할당
        for (int i = 0; i < s.length(); i++) {
            leftStack.push(String.valueOf(s.charAt(i)));
        }
//        content = br.readLine();
//        cursor = content.length();

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            command2(br.readLine());
        }

        while (!leftStack.isEmpty()) {
            rightStack.push(leftStack.pop());
        }

        StringBuilder sb = new StringBuilder();
        while (!rightStack.isEmpty()) {
            sb.append(rightStack.pop());
        }

        System.out.println(sb);
//        System.out.println(content);
    }

    private void command2(String s) {
        switch (s) {
            case "L":
                if(!leftStack.isEmpty()){
                    rightStack.push(leftStack.pop());
                }
                break;
            case "D":
                if(!rightStack.isEmpty()){
                    leftStack.push(rightStack.pop());
                }
                break;
            case "B":
                if(!leftStack.isEmpty()){
                    leftStack.pop();
                }
                break;
            default:
                char t = s.charAt(2);
                leftStack.push(String.valueOf(t));
                break;
        }
    }

    private void command(String s) {
        switch (s) {
            case "L":
                if (cursor != 0) {
                    cursor--;
                }
                break;
            case "D":
                if (cursor != content.length() + 1) {
                    cursor++;
                }
                break;
            case "B":
                if (cursor != 0) {
                    content = content.substring(0, cursor - 1) + content.substring(cursor);
                    cursor--;
                }
                break;
            default:
                // 커서 오른쪽으로 옮겼을 경우 때문에 길이 조정
                if (cursor > content.length()) {
                    cursor = content.length();
                }
                content = content.substring(0, cursor) + s.split(" ")[1] + content.substring(cursor);
                cursor++;
                break;
        }
    }
}

class P11656 {
    /**
     접미사 배열

     문제
     접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.

     baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고,
     이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.

     문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.

     입력
     첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000보다 작거나 같다.

     출력
     첫째 줄부터 S의 접미사를 사전순으로 한 줄에 하나씩 출력한다.

     예제 입력 1
     baekjoon
     예제 출력 1
     aekjoon
     baekjoon
     ekjoon
     joon
     kjoon
     n
     on
     oon
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();

        ArrayList<String> list = new ArrayList<>();

        for (int i = 0; i < s.length(); i++) {
            String parsed = s.substring(i);
            list.add(parsed);
        }

        list.sort((a, b) -> {
            int n = a.length();

            if (b.length() < a.length()) {
                n = b.length();
            }
            for (int i = 0; i < n; i++) {
                if (a.charAt(i) == b.charAt(i)) {
                    continue;
                }
                return a.charAt(i) - b.charAt(i);
            }

            // 문자열의 사전순 정렬 시 주의할 것. a -> aa -> aaa-> aaaa
            return a.length() - b.length();
        });

        for (String val : list) {
            System.out.println(val);
        }
    }
}


class P10824 {
    /**
     네 수

     문제
     네 자연수 A, B, C, D가 주어진다. 이때, A와 B를 붙인 수와 C와 D를 붙인 수의 합을 구하는 프로그램을 작성하시오.

     두 수 A와 B를 합치는 것은 A의 뒤에 B를 붙이는 것을 의미한다. 즉, 20과 30을 붙이면 2030이 된다.

     입력
     첫째 줄에 네 자연수 A, B, C, D가 주어진다. (1 ≤ A, B, C, D ≤ 1,000,000)

     출력
     A와 B를 붙인 수와 C와 D를 붙인 수의 합을 출력한다.

     예제 입력 1
     10 20 30 40
     예제 출력 1
     4060
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long[] arr = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();

        String a = String.valueOf(arr[0]);
        String b = String.valueOf(arr[1]);
        String c = String.valueOf(arr[2]);
        String d = String.valueOf(arr[3]);

        long answer = Long.parseLong(a + b) + Long.parseLong(c + d);
        System.out.println(answer);
    }

}

class P11655 {
    /**
     ROT13

     문제
     ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.

     예를 들어, "Baekjoon Online Judge"를 ROT13으로 암호화하면 "Onrxwbba Bayvar Whqtr"가 된다.
     ROT13으로 암호화한 내용을 원래 내용으로 바꾸려면 암호화한 문자열을 다시 ROT13하면 된다.
     앞에서 암호화한 문자열 "Onrxwbba Bayvar Whqtr"에 다시 ROT13을 적용하면 "Baekjoon Online Judge"가 된다.

     ROT13은 알파벳 대문자와 소문자에만 적용할 수 있다. 알파벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다.
     예를 들어, "One is 1"을 ROT13으로 암호화하면 "Bar vf 1"이 된다.

     문자열이 주어졌을 때, "ROT13"으로 암호화한 다음 출력하는 프로그램을 작성하시오.

     입력
     첫째 줄에 알파벳 대문자, 소문자, 공백, 숫자로만 이루어진 문자열 S가 주어진다. S의 길이는 100을 넘지 않는다.

     출력
     첫째 줄에 S를 ROT13으로 암호화한 내용을 출력한다.

     예제 입력 1
     Baekjoon Online Judge
     예제 출력 1
     Onrxwbba Bayvar Whqtr
     예제 입력 2
     One is 1
     예제 출력 2
     Bar vf 1
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        rot(br.readLine());

    }

    private void rot(String s) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            char c1 = (char) (c + 13);
            char c2 = (char) (c - 13);

            if (Character.isUpperCase(c)) {
                if(Character.isUpperCase(c1)) {
                    sb.append(c1);
                } else {
                    sb.append(c2);
                }
            } else if(Character.isLowerCase(c)) {
                if(Character.isLowerCase(c1)) {
                    sb.append(c1);
                } else {
                    sb.append(c2);
                }
            } else {
                sb.append(c);
            }
        }

        System.out.println(sb);
    }
}

class P10820 {
    /**
     문자열 분석
     시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
     1 초	256 MB	27426	11161	9207	41.217%
     문제
     문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.

     각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.

     입력
     첫째 줄부터 N번째 줄까지 문자열이 주어진다. (1 ≤ N ≤ 100) 문자열의 길이는 100을 넘지 않는다.

     출력
     첫째 줄부터 N번째 줄까지 각각의 문자열에 대해서 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.

     예제 입력 1
     This is String
     SPACE    1    SPACE
     S a M p L e I n P u T
     0L1A2S3T4L5I6N7E8

     예제 출력 1
     10 2 0 2
     0 10 1 8
     5 6 0 16
     0 8 9 0
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 100; i++) {
            String s = br.readLine();
            if (s == null) {
                break;
            }
            analyz(s);
            System.out.println();
        }
    }

    private void analyz(String s) {
        int[] cnts = new int[4];

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLowerCase(c)) {
                cnts[0]++;
            } else if (Character.isUpperCase(c)) {
                cnts[1]++;
            } else if (Character.isDigit(c)) {
                cnts[2]++;
            } else {
                cnts[3]++;
            }
        }

        for (int cnt : cnts) {
            System.out.print(cnt + " ");
        }
    }
}

class P10809 {
    /**
     알파벳 찾기

     문제
     알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서,
     단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

     입력
     첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

     출력
     각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

     만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

     예제 입력 1
     baekjoon
     예제 출력 1
     1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();

        HashMap<Character, Integer> lowercase = new HashMap<>();
        int[] locs = new int[26];
        Arrays.fill(locs, -1);

        for (int i = 0; i < 26; i++) {
            lowercase.put((char) ('a' + i), i);
        }

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            locs[lowercase.get(c)] = s.indexOf(c);
        }

        StringBuilder sb = new StringBuilder();
        for (int loc : locs) {
            sb.append(loc).append(" ");
        }
        System.out.println(sb);
    }
}

class P10808 {
    /**
     알파벳 개수

     문제
     알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.

     입력
     첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

     출력
     단어에 포함되어 있는 a의 개수, b의 개수, …, z의 개수를 공백으로 구분해서 출력한다.

     예제 입력 1
     baekjoon
     예제 출력 1
     1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0
     */

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();

        HashMap<Character, Integer> lowercase = new HashMap<>();
        int[] cnts = new int[26];
        Arrays.fill(cnts, 0);

        for (int i = 0; i < 26; i++) {
            lowercase.put((char) ('a' + i), i);
        }

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            cnts[lowercase.get(c)]++;
        }

        StringBuilder sb = new StringBuilder();
        for (int cnt : cnts) {
            sb.append(cnt).append(" ");
        }
        System.out.println(sb);

    }
}

class P10866 {
    /**
     * 덱
     * 문제
     * 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
     *
     * 명령은 총 여덟 가지이다.
     *
     * push_front X: 정수 X를 덱의 앞에 넣는다.
     * push_back X: 정수 X를 덱의 뒤에 넣는다.
     * pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
     * pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
     * size: 덱에 들어있는 정수의 개수를 출력한다.
     * empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
     * front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
     * back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
     *
     *
     15
     push_back 1
     push_front 2
     front
     back
     size
     empty
     pop_front
     pop_back
     pop_front
     size
     empty
     pop_back
     push_front 3
     empty
     front
     */

    private final LinkedList<Integer> deq = new LinkedList<>();
    private final StringBuilder sb = new StringBuilder();

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            deqCommand(br.readLine());
        }

        System.out.println(sb);
    }

    private void deqCommand(String command) {
        if (command.contains("push")) {
            String[] s = command.split(" ");
            String command2 = s[0].split("_")[1];
            Integer val = Integer.parseInt(s[1]);

            if ("front".equals(command2)) {
                deq.addFirst(val);
            } else {
                deq.addLast(val);
            }
        } else if (command.contains("pop")) {
            if (deq.isEmpty()) {
                sb.append("-1").append("\n");
                return;
            }
            String command2 = command.split("_")[1];
            if ("front".equals(command2)) {
                sb.append(deq.removeFirst()).append("\n");
            } else {
                sb.append(deq.removeLast()).append("\n");
            }
        } else {
            switch (command) {
                case "size" :
                    sb.append(deq.size()).append("\n");
                    break;
                case "empty" :
                    if (deq.isEmpty()) {
                        sb.append(1).append("\n");
                    } else {
                        sb.append(0).append("\n");
                    }
                    break;
                case "front" :
                    if (deq.isEmpty()) {
                        sb.append("-1").append("\n");
                    }else {
                        sb.append(deq.getFirst()).append("\n");
                    }
                    break;
                case "back" :
                    if (deq.isEmpty()) {
                        sb.append("-1").append("\n");
                    } else {
                        sb.append(deq.getLast()).append("\n");
                    }
                    break;
            }
        }
    }
}

class P10845 {
    /**
     * 큐
     * 문제
     * 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
     * <p>
     * 명령은 총 여섯 가지이다.
     * <p>
     * push X: 정수 X를 큐에 넣는 연산이다.
     * pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
     * size: 큐에 들어있는 정수의 개수를 출력한다.
     * empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
     * front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
     * back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
     * 입력
     * 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
     * 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
     * <p>
     * 출력
     * 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
     * <p>
     * 예제 입력 1
     * 15
     * push 1
     * push 2
     * front
     * back
     * size
     * empty
     * pop
     * pop
     * pop
     * size
     * empty
     * pop
     * push 3
     * empty
     * front
     */

    private LinkedList<Integer> que = new LinkedList<>();
    private StringBuilder sb = new StringBuilder();

    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            queCommand(br.readLine());
        }

        System.out.println(sb);
    }

    private void queCommand(String command) {
        LinkedList<Integer> que = this.que;

        if (command.contains("push")){
            String val = command.split(" ")[1];
            que.add(Integer.parseInt(val));
        } else if ("pop".equals(command)) {
            if (que.isEmpty()) {
                sb.append("-1").append("\n");
            } else {
                sb.append(que.remove()).append("\n");
            }
        } else if ("size".equals(command)) {
            sb.append(que.size()).append("\n");
        } else if ("empty".equals(command)) {
            if (que.isEmpty()) {
                sb.append("1").append("\n");
            } else {
                sb.append(0).append("\n");
            }
        } else {
            if (que.isEmpty()) {
                sb.append("-1").append("\n");
            } else {
                if ("front".equals(command)) {
                    sb.append(que.getFirst()).append("\n");
                } else {
                    sb.append(que.getLast()).append("\n");
                }
            }
        }
    }
}

class P10799 {
    /**
     * 쇠막대기

     * 문제
     * 여러 개의 쇠막대기를 레이저로 절단하려고 한다. 효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고,
     * 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다. 쇠막대기와 레이저의 배치는 다음 조건을 만족한다.
     *
     * 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다. - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되,
     * 끝점은 겹치지 않도록 놓는다.
     * 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
     * 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.
     * 아래 그림은 위 조건을 만족하는 예를 보여준다. 수평으로 그려진 굵은 실선은 쇠막대기이고,
     * 점은 레이저의 위치, 수직으로 그려진 점선 화살표는 레이저의 발사 방향이다.
     *
     *
     *
     * 이러한 레이저와 쇠막대기의 배치는 다음과 같이 괄호를 이용하여 왼쪽부터 순서대로 표현할 수 있다.
     *
     * 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현된다. 또한, 모든 ‘( ) ’는 반드시 레이저를 표현한다.
     * 쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다.
     * 위 예의 괄호 표현은 그림 위에 주어져 있다.
     *
     * 쇠막대기는 레이저에 의해 몇 개의 조각으로 잘려지는데, 위 예에서 가장 위에 있는 두 개의 쇠막대기는 각각 3개와 2개의 조각으로 잘려지고,
     * 이와 같은 방식으로 주어진 쇠막대기들은 총 17개의 조각으로 잘려진다.
     *
     * 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램을 작성하시오.
     *
     * 입력
     * 한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.
     *
     *
     * 3 + 3 + 3 + 2 + 1  + 1
     ()(((()())(())()))(())
     * 출력
     * 잘려진 조각의 총 개수를 나타내는 정수를 한 줄에 출력한다.
     */
    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ironPipe(br.readLine());
    }

    private void ironPipe(String s) {
        ArrayList<Character> stack = new ArrayList<>();

        int result = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.add(c);
            } else {
                stack.remove(stack.size() - 1);
                if (i != 0 && s.charAt(i -1) == '(') {
                    result += stack.size();
                }else {
                    result ++;
                }
            }
        }
        System.out.println(result);
    }
}


class P9012 {
    /**
     * 괄호
     * 문제
     * 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
     * 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
     * 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은
     * 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
     *
     * 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.
     *
     * 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.
     *
     * 입력
     * 입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다.
     * 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
     * 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다.
     *
     * 출력
     * 출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다.
     */
    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        String[] result = new String[t];

        for (int i = 0; i < t; i++) {
            result[i] = isOk(br.readLine());
        }

        for (String s : result) {
            System.out.println(s);
        }
    }

    private String isOk(String s) {
        ArrayList<Character> stack = new ArrayList<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.add(c);
            } else {
                if (stack.isEmpty()) {
                    return "NO";
                }else {
                    stack.remove(stack.size() - 1);
                }
            }
        }

        if (stack.isEmpty()) {
            return "YES";
        }else {
            return "NO";
        }
    }
}

class P10828 {
    /**
     * 스택
     * <p>
     * 문제
     * 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
     * <p>
     * 명령은 총 다섯 가지이다.
     * <p>
     * push X: 정수 X를 스택에 넣는 연산이다.
     * pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
     * size: 스택에 들어있는 정수의 개수를 출력한다.
     * empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
     * top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
     * 입력
     * 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
     * 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
     *
     * 출력
     * 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
     */

    private ArrayList<Integer> stack = new ArrayList<>();
    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            command(br.readLine());
        }

    }

    private void command(String s) {
        if (s.contains("push")) {
            stack.add(Integer.parseInt(s.split(" ")[1]));
        } else if ("top".equals(s)){
            if (!stack.isEmpty()) {
                System.out.println(stack.get(stack.size()-1));
            } else {
                System.out.println(-1);
            }
        } else if ("size".equals(s)){
            System.out.println(stack.size());
        } else if ("empty".equals(s)){
            if (stack.isEmpty()) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        } else if ("pop".equals(s)) {
            if (!stack.isEmpty()) {
                System.out.println(stack.get(stack.size()-1));
                stack.remove(stack.size() - 1);
            } else {
                System.out.println(-1);
            }
        }
    }
}

class P11004 {
    /**
     * K번째 수
     * 문제
     * 수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.
     *
     * 입력
     * 첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.
     *
     * 둘째에는 A1, A2, ..., AN이 주어진다. (-10^9 ≤ Ai ≤ 10^9)
     *
     * 출력
     * A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.
     *
     * 예제 입력 1
     5 2
     4 1 2 3 5
     *
     * 예제 출력 1
     * 2
     */
    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        long n = Long.parseLong(s[0]);
        long k = Long.parseLong(s[1]);

        long[] arr = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();

        Arrays.sort(arr);

        System.out.println(arr[(int) (k - 1)]);

    }
}


class P11652 {
    /**
     카드
     문제
     준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -2^62보다 크거나 같고, 2^62보다 작거나 같다.

     준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오.
     만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.

     입력
     첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
     둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.

     출력
     첫째 줄에 준규가 가장 많이 가지고 있는 정수를 출력한다.

     */
    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        HashMap<Long, Integer> countMap = new HashMap<>();


        int max = 0;
        long x = 0;
        for (int i = 0; i < n; i++) {
            long key = Long.parseLong(br.readLine());
            countMap.put(key, countMap.getOrDefault(key, 0) + 1);

            if (countMap.get(key) > max) {
                max = countMap.get(key);
                x = key;
            }
            else if(countMap.get(key) == max) {
                x = Math.min(x, key);
            }
        }

        System.out.println(x);

        /*
        List<Map.Entry<Long, Integer>> collect =
                countMap.entrySet().stream().sorted((a, b) -> {
                    if (a.getValue() - b.getValue() == 0) {
                        return (int) (a.getKey() - b.getKey());
                    }
                    return b.getValue() - a.getValue();
                }).collect(Collectors.toList());

        System.out.println(collect);

        System.out.println(collect.get(0).getKey());*/
    }
}

class P10825 {
    /**
     국영수
     문제
     도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.

     국어 점수가 감소하는 순서로
     국어 점수가 같으면 영어 점수가 증가하는 순서로
     국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
     모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
     입력
     첫째 줄에 도현이네 반의 학생의 수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 한 줄에 하나씩 각 학생의 이름,국어, 영어, 수학 점수가
     공백으로 구분해 주어진다. 점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.
     이름은 알파벳 대소문자로 이루어진 문자열이고, 길이는 10자리를 넘지 않는다.

     출력
     문제에 나와있는 정렬 기준으로 정렬한 후 첫째 줄부터 N개의 줄에 걸쳐 각 학생의 이름을 출력한다.

     예제 입력 1
     12
     Junkyu 50 60 100
     Sangkeun 80 60 50
     Sunyoung 80 70 100
     Soong 50 60 90
     Haebin 50 60 100
     Kangsoo 60 80 100
     Donghyuk 80 60 100
     Sei 70 70 70
     Wonseob 70 70 90
     Sanghyun 70 70 80
     nsj 80 80 80
     Taewhan 50 60 90
     예제 출력 1
     Donghyuk
     Sangkeun
     Sunyoung
     nsj
     Wonseob
     Sanghyun
     Sei
     Kangsoo
     Haebin
     Junkyu
     Soong
     Taewhan
     */
    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        ArrayList<Pair<String, int[]>> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String line = br.readLine();

            String[] arr = line.split(" ");
            int[] score = new int[3];
            score[0] = Integer.parseInt(arr[1]);
            score[1] = Integer.parseInt(arr[2]);
            score[2] = Integer.parseInt(arr[3]);
            Pair<String, int[]> pair = new Pair<>(arr[0], score);
            list.add(pair);
        }

        list.sort((a, b) -> {
                    /**
                     * idx 0 : 국
                     * idx 1 : 영
                     * idx 2 : 수
                     */
                    int[] scoreA = a.getElement1();
                    int[] scoreB = b.getElement1();

                    if (scoreA[0] == scoreB[0]) {
                        if (scoreA[1] == scoreB[1]) {
                            if(scoreA[2] == scoreB[2]) {
                                return a.getElement0().compareTo(b.getElement0());
                            }
                            return scoreB[2] -scoreA[2];
                        }
                        return scoreA[1] - scoreB[1];
                    }

                    return scoreB[0] - scoreA[0];
                }
        );

        StringBuilder sb = new StringBuilder();

        for (Pair<String, int[]> pair : list) {
            sb.append(pair.getElement0()).append("\n");

        }

        System.out.println(sb);


    }
}

class P10814 {
    /**
     나이순 정렬

     문제
     온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때,
     회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

     입력
     첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

     둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며,
     200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

     출력
     첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순,
     나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

     예제 입력 1
     3
     21 Junkyu
     21 Dohyun
     20 Sunyoung
     예제 출력 1
     20 Sunyoung
     21 Junkyu
     21 Dohyun
     */
    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        ArrayList<Pair<Integer, String>> coords = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            Pair<Integer, String> coord = new Pair<>(Integer.parseInt(s[0]), s[1]);
            coords.add(coord);
        }

        coords.sort(Comparator.comparingInt(Pair::getElement0));

        StringBuilder sb = new StringBuilder();
        for (Pair<Integer, String> coord : coords) {
            sb.append((coord.getElement0())).append(" ").append(coord.getElement1()).append("\n");
        }

        System.out.println(sb);
    }
}

class Pair<K, V> {

    private final K element0;
    private final V element1;

    public static <K, V> Pair<K, V> createPair(K element0, V element1) {
        return new Pair<K, V>(element0, element1);
    }

    public Pair(K element0, V element1) {
        this.element0 = element0;
        this.element1 = element1;
    }

    public K getElement0() {
        return element0;
    }

    public V getElement1() {
        return element1;
    }

}

class P11651 {
    /**
     * 좌표 정렬하기 2
     * <p>
     * 문제
     * 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로,
     * y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
     * <p>
     * 입력
     * 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
     * <p>
     * 출력
     * 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
     * <p>
     * 예제 입력 1
     * 5
     * 0 4
     * 1 2
     * 1 -1
     * 2 2
     * 3 3
     * 예제 출력 1
     * 1 -1
     * 1 2
     * 2 2
     * 3 3
     * 0 4
     */
    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        ArrayList<int[]> coords = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            coords.add(arr);
        }

        coords.sort((a, b) -> {
            if (a[1] == b[1]) {
                return a[0] - b[0];
            } else {
                return a[1] - b[1];
            }
        });

        StringBuilder sb = new StringBuilder();
        for (int[] coord : coords) {
            sb.append(coord[0]).append(" ").append(coord[1]).append("\n");
        }

        System.out.println(sb);
    }
}

class P11650 {
    /**
     * 좌표 정렬하기
     * 문제
     * 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
     * <p>
     * 입력
     * 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다.
     * (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
     * <p>
     * 출력
     * 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
     * <p>
     * 예제 입력 1
     * 5
     * 3 4
     * 111 -1
     * 111 -11
     * 1 2
     * 3 3
     * 예제 출력 1
     * 1 -1
     * 1 1
     * 2 2
     * 3 3
     * 3 4
     */
    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        ArrayList<int[]> coords = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            coords.add(arr);
        }

        coords.sort((a, b) -> {
            if (a[0] == b[0]) {
                return a[1] - b[1];
            } else {
                return a[0] - b[0];
            }
        });

        StringBuilder sb = new StringBuilder();
        for (int[] coord : coords) {
            sb.append(coord[0]).append(" ").append(coord[1]).append("\n");
        }

        System.out.println(sb);
    }
}

class P2751 {
    /**
     * 수 정렬하기 2

     * 문제
     * N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
     *
     * 입력
     * 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다.
     * 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
     *
     * 출력
     * 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
     *
     * 예제 입력 1
     * 5
     * 5
     * 4
     * 3
     * 2
     * 1
     * 예제 출력 1
     * 1
     * 2
     * 3
     * 4
     * 5
     * 출처
     */
    public void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        TreeMap<Integer, Integer> map = new TreeMap<>();

        for (int i = 0; i < n; i++) {
            int val = Integer.parseInt(br.readLine());
            map.put(val, 0);
        }

        StringBuilder sb = new StringBuilder();
        for (Integer integer : map.keySet()) {
            sb.append(integer).append("\n");
        }

        System.out.println(sb);
    }
}
