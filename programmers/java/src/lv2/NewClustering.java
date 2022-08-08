package lv2;

import java.util.ArrayList;

public class NewClustering {
    /**
     * 문제 설명
     * 뉴스 클러스터링
     *
     * 입력 형식
     * 입력으로는 str1과 str2의 두 문자열이 들어온다. 각 문자열의 길이는 2 이상, 1,000 이하이다.
     * 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다.
     * 예를 들어 "ab+"가 입력으로 들어오면, "ab"만 다중집합의 원소로 삼고, "b+"는 버린다.
     * 다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. "AB"와 "Ab", "ab"는 같은 원소로 취급한다.
     * 출력 형식
     * 입력으로 들어온 두 문자열의 자카드 유사도를 출력한다. 유사도 값은 0에서 1 사이의 실수이므로, 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.
     *
     * 예제 입출력
     * str1	str2	answer
     * FRANCE	french	16384
     * handshake	shake hands	65536
     * aa1+aa2	AAAA12	43690
     * E=M*C^2	e=m*c^2	65536
     */

    public int solution(String str1, String str2) {
        int answer = 0;

        str1 = str1.toUpperCase();
        str2 = str2.toUpperCase();

        ArrayList<String> list1 = new ArrayList<>();
        ArrayList<String> list2 = new ArrayList<>();

        parsingAndAddSet(str1, list1);
        parsingAndAddSet(str2, list2);

        ArrayList<String> intersection = new ArrayList<>();
        ArrayList<String> union = new ArrayList<>();

        for (String s : list1) {
            if (list2.contains(s)) {
                intersection.add(s);
                list2.remove(s);
            }
            union.add(s);
        }

        for (String s : list2) {
            union.add(s);
        }
        if (intersection.size() == 0 && union.size() == 0) {
            return 65536;
        }

        double temp = intersection.size() / (double) union.size();

        answer = (int) (65536 * temp);

        return answer;
    }

    private void parsingAndAddSet(String str, ArrayList<String> list) {
        for (int i = 0; i < str.length() - 1; i++) {
            if (String.valueOf(str.charAt(i)).matches("^[A-Z]") && String.valueOf(str.charAt(i+1)).matches("^[A-Z]")) {
                StringBuilder temp = new StringBuilder();
                temp.append(str.charAt(i));
                temp.append(str.charAt(i+1));
                list.add(temp.toString());
            }
        }
    }

    public static void main(String[] args) {
        NewClustering newClustering = new NewClustering();
        int sol = newClustering.solution("aa1+aa2", "AAAA12");
        System.out.println("sol = " + sol);
    }
}
