package lv1;

public class TernaryReverse {
    /**
     * 3진법 뒤집기
     * 문제 설명
     * 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
     *
     * 제한사항
     * n은 1 이상 100,000,000 이하인 자연수입니다.
     */

    public String convertTenToThreeReverse(int n) {
        StringBuilder result = new StringBuilder();

        int mok = n;
        int na;
        while (mok >= 3) {
            mok = n / 3;
//            System.out.println("mok = " + mok);
            na = n % 3;
//            System.out.println("na = " + na);
            n /= 3;
//            System.out.println("n = " + n);

            result.append(na);
        }
        result.append(n);

        return result.toString();
    }

    public int convertThreeToTen(String s) {

        int result = 0;

        char[] array = s.toCharArray();

        int length = array.length;

        for (char c : array) {
            int i = Integer.parseInt(String.valueOf(c));
//            System.out.println("i = " + i);

            for (int j = 0; j < length -1; j++) {
                i *= 3;
//                System.out.println("j = " + j);
            }
            length --;
            result += i;
        }

        return result;
    }

    public int solution(int n) {
        int answer = 0;
        String s = convertTenToThreeReverse(n);
//        System.out.println("s = " + s);
        answer = convertThreeToTen(s);

        //  Integer.parseInt(a,3); -> a를 3진법 수로 반환
        return answer;
    }

    public static void main(String[] args) {
        TernaryReverse ternaryReverse = new TernaryReverse();
        int solution1 = ternaryReverse.solution(45);
        int solution2 = ternaryReverse.solution(125);

        System.out.println("solution1 = " + solution1);
        System.out.println("solution2 = " + solution2);


    }
}
