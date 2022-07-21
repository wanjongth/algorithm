package lv1;

import java.util.Arrays;

public class Budget {
    /**
     * 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때,
     * 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.
     *
     * 제한사항
     * d는 부서별로 신청한 금액이 들어있는 배열이며, 길이(전체 부서의 개수)는 1 이상 100 이하입니다.
     * d의 각 원소는 부서별로 신청한 금액을 나타내며, 부서별 신청 금액은 1 이상 100,000 이하의 자연수입니다.
     * budget은 예산을 나타내며, 1 이상 10,000,000 이하의 자연수입니다.
     */
    public int solution(int[] d, int budget) {
        int answer = 0;

        /*
        // 굳이 자료구조 하나 더 쓰지 않기
        ArrayList<Integer> list = new ArrayList<>();
        for (int i : d) {
            list.add(i);
        }
        Collections.sort(list);*/

        Arrays.sort(d);

        for (Integer dd : d) {
            budget -= dd;

            if (budget < 0) {
                break;
            }
            answer ++;
        }

        return answer;
    }

    public static void main(String[] args) {
        Budget budget = new Budget();

        int[] d = {1, 3, 2, 5, 4};

        int solution = budget.solution(d, 9);

        System.out.println("solution = " + solution);
    }
}
