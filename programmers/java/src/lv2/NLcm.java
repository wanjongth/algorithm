package lv2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.LinkedList;

public class NLcm {

    /**
     * N개의 최소공배수
     * 문제 설명
     * 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
     * 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
     * n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
     * <p>
     * 제한 사항
     * arr은 길이 1이상, 15이하인 배열입니다.
     * arr의 원소는 100 이하인 자연수입니다.
     * 입출력 예
     * arr	result
     * [2,6,8,14]	168
     * [1,2,3]	6
     */

    public int solution(int[] arr) {
        int answer = 1;

        if (arr.length == 1) {
            return arr[0];
        }

        Deque<Long> deque = new LinkedList<>();

        for (Integer integer : arr) {
            deque.add(integer.longValue());
        }

        while (deque.size() >= 2) {
            Long a = deque.pollFirst();
            Long b = deque.pollFirst();

            if (a == b) {
                deque.add(a);
            } else {
                long getLcm = getLcm(a, b);
                deque.add(getLcm);
            }
        }

        answer = deque.getFirst().intValue();

        return answer;
    }

    public long getLcm(long n, long m) {
        long cha = Math.abs(n - m);

        if (cha == 0) {
            return n;
        }

        ArrayList<Long> yaksu_list = new ArrayList<>();

        for (int i = 1; i < cha / 2 + 1; i++) {
            if (cha % i == 0) {
                yaksu_list.add((cha / i));
            }
        }
        yaksu_list.add(1L);

        Collections.sort(yaksu_list);

        long gcd = 0;

        for (Long l : yaksu_list) {
            if (n % l == 0L && m % l == 0L) {
                gcd = l;
            }
        }

        return n * m / gcd;
    }

    public static void main(String[] args) {
        NLcm nLcm = new NLcm();
        int solution = nLcm.solution(new int[]{2, 6, 8, 14});
        System.out.println("solution = " + solution);
    }
}
