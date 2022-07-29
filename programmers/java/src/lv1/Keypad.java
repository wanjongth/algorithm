package lv1;

public class Keypad {
    /**
     * 키패드 누르기
     *
     * 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
     * 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.
     *
     * 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
     * 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
     * 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
     * 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
     * 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
     * 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때,
     * 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
     */

    public String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();

        int left_cursor = 10;
        int right_cursor = 12;

        for (int number : numbers) {
            if (number % 3 == 1) {
                answer.append("L");
                left_cursor = number;
            } else if (number % 3 == 0 && number != 0) {
                answer.append("R");
                right_cursor = number;
            } else {
                if (number == 0) {
                    number = 11;
                }

                int left_len = Math.abs(number-left_cursor) / 3 + Math.abs(number-left_cursor) % 3;
                int right_len = Math.abs(number-right_cursor) / 3 + Math.abs(number-right_cursor) % 3;

                if (left_len == right_len) {
                    if (hand.equals("left")) {
                        answer.append("L");
                        left_cursor = number;
                    } else {
                        answer.append("R");
                        right_cursor = number;
                    }
                } else if (left_len < right_len) {
                    answer.append("L");
                    left_cursor = number;
                } else {
                    answer.append("R");
                    right_cursor = number;
                }
            }
        }

        return answer.toString();
    }

    public static void main(String[] args) {
        Keypad keypad = new Keypad();
        String solution = keypad.solution(new int[]{1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5}, "right");
        System.out.println("solution = " + solution);
    }
}
