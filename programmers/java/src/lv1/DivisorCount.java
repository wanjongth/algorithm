package lv1;

public class DivisorCount {

    /**
     * 약수의 개수와 덧셈
     * 문제 설명
     * 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
     */

    public int countDivisor(int num) {
        int cnt = 0;
        for (int i = 1; i < num + 1; i++) {
            if (num % i == 0) {
                cnt ++;
            }
        }
        return cnt;
    }


    public int solution(int left, int right) {
        int answer = 0;
        for (int i = left; i < right + 1; i++) {
            if(countDivisor(i) % 2 == 0) {
                answer += i;
            } else {
                answer -= i;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        DivisorCount divisorCount = new DivisorCount();
        int solution1 = divisorCount.solution(13, 17); // 43
        int solution2 = divisorCount.solution(24, 27); // 52

        System.out.println("solution1 = " + solution1);
        System.out.println("solution2 = " + solution2);
    }
}
