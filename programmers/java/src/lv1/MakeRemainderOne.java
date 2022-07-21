package lv1;

public class MakeRemainderOne {
    /**
     * 나머지가 1이 되는 수 찾기
     * 문제 설명
     * 자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요.
     * 답이 항상 존재함은 증명될 수 있습니다.
     *
     * 제한사항
     * 3 ≤ n ≤ 1,000,000
     */

    public int solution(int n) {
        int answer = 0;

        for (int j = 2; j < n; j++) {
            if (n % j == 1) {
                answer = j;
                return answer;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        MakeRemainderOne makeRemainderOne = new MakeRemainderOne();
        int solution1 = makeRemainderOne.solution(10);
        int solution2 = makeRemainderOne.solution(12);

        System.out.println("solution1 = " + solution1);
        System.out.println("solution2 = " + solution2);
    }

}
