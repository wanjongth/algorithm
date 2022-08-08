package lv2;

public class BracketConversion {
    /**
     * 괄호 변환
     *
     * 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
     * 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
     * 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
     * 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
     *   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
     * 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
     *   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
     *   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
     *   4-3. ')'를 다시 붙입니다.
     *   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
     *   4-5. 생성된 문자열을 반환합니다.
     * "균형잡힌 괄호 문자열" p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 "올바른 괄호 문자열"로 변환한 결과를 return 하도록 solution 함수를 완성해 주세요.
     *
     * 매개변수 설명
     * p는 '(' 와 ')' 로만 이루어진 문자열이며 길이는 2 이상 1,000 이하인 짝수입니다.
     * 문자열 p를 이루는 '(' 와 ')' 의 개수는 항상 같습니다.
     * 만약 p가 이미 "올바른 괄호 문자열"이라면 그대로 return 하면 됩니다.
     */

    static final char open = '(';
    static final char close = ')';

    public String solution(String p) {
        String answer;
        if (isBalancedBracket(p)) {
            return p;
        }
        answer = toCorrectBracket(p);
        return answer;
    }

    public static String reverse(String str){
        StringBuilder s = new StringBuilder();

        for(int i = 1; i<str.length()-1;i++){
            if(str.charAt(i) == open) s.append(close);
            else s.append(open);
        }
        return s.toString();
    }

    public static boolean isBalancedBracket(String str){
        int openCnt = 0;
        if (str.charAt(0) == close) {
            return false;
        }

        for(int i =0;i<str.length();i++){
            if(str.charAt(i) == open) openCnt++;
            else {
                openCnt--;
                if (openCnt < 0) {
                    return false;
                }
            }
        }
        return true;
    }

    public static String toCorrectBracket(String s){

        StringBuilder u = new StringBuilder();
        StringBuilder v = new StringBuilder();

        if (s.length() == 0) {
            return "";
        }

        int openCnt = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == open) {
                openCnt++;
            } else {
                openCnt--;
            }

            if (openCnt == 0) {
                u.append(s.substring(0, i + 1));
                v.append(s.substring(i + 1, s.length()));

                if (isBalancedBracket(u.toString())) {
                    u.append(toCorrectBracket(v.toString()));
                } else {
                    StringBuilder str = new StringBuilder();
                    str.append(open);
                    str.append(toCorrectBracket(v.toString()));
                    str.append(close);
                    str.append(reverse(u.toString()));
                    return str.toString();
                }
                break;
            }
        }
        return u.toString();
    }

    public static void main(String[] args) {
        BracketConversion bracketConversion = new BracketConversion();
        String solution = bracketConversion.solution("(()())()");
        System.out.println("solution = " + solution);
    }
}
