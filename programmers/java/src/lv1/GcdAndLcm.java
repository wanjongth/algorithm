package lv1;

import java.util.ArrayList;
import java.util.Collections;

public class GcdAndLcm {

    /**
     * 최대공약수와 최소공배수
     * 문제 설명
     * 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
     * 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
     * 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
     *
     * 제한 사항
     * 두 수는 1이상 1000000이하의 자연수입니다.
     */

    public int[] solution(int n, int m) {
        int cha = Math.abs(n - m);

        if (cha == 0) {
            return new int[]{n, n};
        }

        ArrayList<Integer> yaksu_list = new ArrayList<>();

        for (int i = 1; i < cha / 2 + 1; i++) {
            if (cha % i == 0) {
                yaksu_list.add(cha / i);
            }
        }
        yaksu_list.add(1);

        Collections.sort(yaksu_list);
//        System.out.println("yaksu_list = " + yaksu_list);

        int gcd = 0;
        int lcm = 0;

        for (Integer integer : yaksu_list) {
            if (n % integer == 0 && m % integer == 0) {
                gcd = integer;
            }
        }

        lcm = n * m / gcd;

        int[] answer = {gcd, lcm};

        return answer;
    }

    public static void main(String[] args) {
        GcdAndLcm gcdAndLcm = new GcdAndLcm();

        int[] solution = gcdAndLcm.solution(3, 12);
    }
}
