package lv2;

import java.util.Arrays;

public class Bit {

    /**
     * 2개 이하로 다른 비트
     * 문제 설명
     * 양의 정수 x에 대한 함수 f(x)를 다음과 같이 정의합니다.
     *
     * x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
     * 예를 들어,
     *
     * f(2) = 3 입니다. 다음 표와 같이 2보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 제일 작은 수가 3이기 때문입니다.
     * 수	비트	다른 비트의 개수
     * 2	000...0010
     * 3	000...0011	1
     * f(7) = 11 입니다. 다음 표와 같이 7보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 제일 작은 수가 11이기 때문입니다.
     * 수	비트	다른 비트의 개수
     * 7	000...0111
     * 8	000...1000	4
     * 9	000...1001	3
     * 10	000...1010	3
     * 11	000...1011	2
     * 정수들이 담긴 배열 numbers가 매개변수로 주어집니다.
     * numbers의 모든 수들에 대하여 각 수의 f 값을 배열에 차례대로 담아 return 하도록 solution 함수를 완성해주세요.
     *
     * 제한사항
     * 1 ≤ numbers의 길이 ≤ 100,000
     * 0 ≤ numbers의 모든 수 ≤ 1015
     * 입출력 예
     * numbers	result
     * [2,7]	[3,11]
     */

    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] % 2 == 0) {
                answer[i] = numbers[i] + 1;
            }
            else {
                String s = Long.toBinaryString(numbers[i]);

                StringBuilder temp = new StringBuilder();

                if (!s.contains("0")) {
                    temp.append("10");
                    for (int j = 0; j < s.length() - 1; j++) {
                        temp.append("1");
                    }
                } else {
                    int lastZeroIdx = s.lastIndexOf('0');

                    /**
                     * 마지막 0 전까지 일단 담음
                     * StringBuilder 쓸 때는 substring (시작, 끝) 필요 없음
                     */
//                    temp.append(s.substring(0, lastZeroIdx));
                    temp.append(s, 0, lastZeroIdx); // 마지막 0 전까지 일단 담음
                    temp.append("10"); // 0-> 1로 뒤에 0 붙임
                    temp.append(s.substring(lastZeroIdx + 2)); // 나머지 문자열 이어붙임
                }

                answer[i] = Long.parseLong(temp.toString(), 2);
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Bit bit = new Bit();

        long[] solution = bit.solution(new long[]{2, 7});

        System.out.println("Arrays.toString(solution) = " + Arrays.toString(solution));
    }
}
