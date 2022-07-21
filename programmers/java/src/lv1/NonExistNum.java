package lv1;

import java.util.Arrays;

public class NonExistNum {
    /*
    없는 숫자 더하기

    0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
    numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

    제한사항
    1 ≤ numbers의 길이 ≤ 9
    0 ≤ numbers의 모든 원소 ≤ 9
    numbers의 모든 원소는 서로 다릅니다.
     */

    public int solution(int[] numbers) {
        int sum = Arrays.stream(numbers).sum();
        return 45 - sum;
    }

    public static void main(String[] args) {
        NonExistNum nonExistNum = new NonExistNum();

        int[] ex = {1, 2, 3, 4, 6, 7, 8, 0};

        int solution = nonExistNum.solution(ex);
        System.out.println("solution = " + solution);
    }
}
