package lv2;

import java.util.Stack;

public class Bracket {
    /**
     * 올바른 괄호
     * 문제 설명
     * 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어
     *
     * "()()" 또는 "(())()" 는 올바른 괄호입니다.
     * ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
     * '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고,
     * 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
     *
     * 제한사항
     * 문자열 s의 길이 : 100,000 이하의 자연수
     * 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
     */
    boolean solution(String s) {
        boolean answer = false;
        int count = 0;
        for(int i = 0; i<s.length();i++){
            if(s.charAt(i) == '('){
                count++;
            }
            if(s.charAt(i) == ')'){
                count--;
            }
            if(count < 0){
                break;
            }
        }
        if(count == 0){
            answer = true;
        }

        return answer;
    }

    // stack
    boolean solution2(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();

        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) == '(')
                stack.push('(');
            else{
                if(stack.isEmpty())
                    return false;
                else
                    stack.pop();
            }
        }

        answer = stack.isEmpty();
        return answer;
    }

    public static void main(String[] args) {
        Bracket bracket = new Bracket();
        boolean solution = bracket.solution("(())()");
        boolean solution2 = bracket.solution2("(())()");
        System.out.println("solution = " + solution);
        System.out.println("solution2 = " + solution2);
    }


}
