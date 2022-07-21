package lv1;

import java.util.TreeSet;

public class SelectNumPlus {
    /**
     * 두 개 뽑아서 더하기
     * 문제 설명
     * 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
     *
     * 제한사항
     * numbers의 길이는 2 이상 100 이하입니다.
     * numbers의 모든 수는 0 이상 100 이하입니다.
     */

    public int[] solution(int[] numbers) {
//        ArrayList<Integer> list = new ArrayList<>();

        TreeSet<Integer> set = new TreeSet<>();
        for (int i = 0; i < numbers.length; i++) {

            for (int j = i+1; j < numbers.length; j++) {
                set.add(numbers[i] + numbers[j]);
            }
        }

        int[] answer = new int[set.size()];

        int i = 0;
        for (Integer integer : set) {
            answer[i++] = integer;
        }

        return answer;
    }

    public static void main(String[] args) {
        SelectNumPlus selectNumPlus = new SelectNumPlus();

        int[] num = {2, 1, 3, 4, 1};
        int[] solution = selectNumPlus.solution(num);

        for (int i : solution) {
            System.out.println("i = " + i);
        }
    }
}

