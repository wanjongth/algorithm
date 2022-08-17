package lv2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PowNArrayCut {
    /**
     * n^2 배열 자르기
     * 문제 설명
     * 정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.
     *
     * n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
     * i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
     * 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
     * 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
     * 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.
     * 정수 n, left, right가 매개변수로 주어집니다. 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.
     *
     * 제한사항
     * 1 ≤ n ≤ 107
     * 0 ≤ left ≤ right < n2
     * right - left < 105
     * 입출력 예
     * n	left	right	result
     * 3	2	5	[3,2,2,3]
     * 4	7	14	[4,3,3,3,4,4,4,4]
     */

    // 명시된 순서대로 구현 시 메모리 초과
//    public int[] solution(int n, long left, long right) {
//        int[][] temp = new int[n][n];
//
//        for (int i = 1; i < n + 1; i++) {
//            for (int j = 1; j < i + 1; j++) {
//                temp[i-1][j-1] = i;
//                if(j < i) {
//                    temp[j-1][i-1] = i;
//                }
//            }
//        }
//
//        int[] arr = new int[(int) (right - left + 1)];
//
//        int cnt = 0;
//        int idx = 0;
//        for (int i = 0; i < temp.length; i++) {
//            for (int j = 0; j < temp[i].length; j++) {
//                cnt ++;
//                if (cnt > left && cnt < right + 2) {
//                    arr[idx] = temp[i][j];
//                    idx++;
//                }
//            }
//        }
//
//        return arr;
//    }
    public int[] solution(int n, long left, long right) {

        List<Long> list = new ArrayList<>();

        // 해당 범위 index max 값 추출
        for (long i = left; i < right + 1; i++) {
            list.add(Math.max(i / n, i % n) + 1);
        }

        int[] answer = list.stream().mapToInt(Long::intValue).toArray();


        return answer;
    }

    public static void main(String[] args) {
        PowNArrayCut powNArrayCut = new PowNArrayCut();
        int[] solution = powNArrayCut.solution(3, 2, 5);
        System.out.println("Arrays.toString(solution) = " + Arrays.toString(solution));
    }
}
