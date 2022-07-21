package lv1;

public class NumStringAndWord {
    /*
    숫자 문자열과 영단어
    1478 → "one4seveneight"
    234567 → "23four5six7"
    10203 → "1zerotwozero3"
    이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나,
    혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다.
    s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.
     */

    public int solution(String s) {
        String[] num = {
                "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
        };

        for (int i = 0 ; i < 10 ; i ++) {
            s = s.replace(num[i], String.valueOf(i));
        }

        return Integer.parseInt(s);
    }

    public static void main(String[] args) {
        NumStringAndWord numStringAndWord = new NumStringAndWord();
        int sol1 = numStringAndWord.solution("one4seveneight");
        int sol2 = numStringAndWord.solution("23four5six7");

        System.out.println("sol1 = " + sol1);
        System.out.println("sol2 = " + sol2);
    }

}
