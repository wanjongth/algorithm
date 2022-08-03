package lv2;

import java.util.Arrays;

public class Hindex {

    /**
     * H-Index
     * 문제 설명
     * H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.
     *
     * 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
     *
     * 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때,
     * 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
     *
     * 제한사항
     * 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
     * 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
     * 입출력 예
     * citations	return
     * [3, 0, 6, 1, 5]	3
     */

    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);

        for (int i = 0; i < citations.length; i++) {
            int h = citations.length - i;

            if (citations[i] >= h) {
                answer = h;
                break;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Hindex hindex = new Hindex();
        int solution = hindex.solution(new int[]{3, 0, 6, 1, 5});
        System.out.println("solution = " + solution);
    }
}
