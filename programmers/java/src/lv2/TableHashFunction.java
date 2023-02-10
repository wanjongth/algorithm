package lv2;

import java.util.ArrayList;
import java.util.Arrays;

public class TableHashFunction {
    /**
     * 테이블 해시 함수
     * 문제 설명
     * 완호가 관리하는 어떤 데이터베이스의 한 테이블은 모두 정수 타입인 컬럼들로 이루어져 있습니다.
     * 테이블은 2차원 행렬로 표현할 수 있으며 열은 컬럼을 나타내고, 행은 튜플을 나타냅니다.
     * 첫 번째 컬럼은 기본키로서 모든 튜플에 대해 그 값이 중복되지 않도록 보장됩니다
     * 완호는 이 테이블에 대한 해시 함수를 다음과 같이 정의하였습니다.
     *
     * 해시 함수는 col, row_begin, row_end을 입력으로 받습니다.
     * 테이블의 튜플을 col번째 컬럼의 값을 기준으로 오름차순 정렬을 하되, 만약 그 값이 동일하면 기본키인 첫 번째 컬럼의 값을 기준으로 내림차순 정렬합니다.
     * 정렬된 데이터에서 S_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 나머지들의 합으로 정의합니다.
     * row_begin ≤ i ≤ row_end 인 모든 S_i를 누적하여 bitwise XOR 한 값을 해시 값으로서 반환합니다.
     * 테이블의 데이터 data와 해시 함수에 대한 입력 col, row_begin, row_end이 주어졌을 때
     * 테이블의 해시 값을 return 하도록 solution 함수를 완성해주세요.
     *
     * 제한 사항
     * 1 ≤ data의 길이 ≤ 2,500
     * 1 ≤ data의 원소의 길이 ≤ 500
     * 1 ≤ data[i][j] ≤ 1,000,000
     * data[i][j]는 i + 1 번째 튜플의 j + 1 번째 컬럼의 값을 의미합니다.
     * 1 ≤ col ≤ data의 원소의 길이
     * 1 ≤ row_begin ≤ row_end ≤ data의 길이
     *
     * 입출력 예
     * data	col	row_begin	row_end	result
     * [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]	2	2	3	4
     */
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;

        // stream 연습
            /*List<int[]> sortedData = Arrays.stream(data).sorted((o1, o2) -> {
                if (o1[col-1] > o2[col-1]) {
                    return 1;
                } else if (o1[col-1] == o2[col-1]) {
                    return o2[0] - o1[0];
                } else {
                    return -1;
                }
            }).collect(Collectors.toList());*/

        ArrayList<Integer> siList = new ArrayList<>();

        // Arrays.sort
        Arrays.sort(data, (a, b)-> {
            if (a[col-1] == b[col-1]) {
                return Integer.compare(b[0], a[0]);
            } else {
                return Integer.compare(a[col-1], b[col-1]);
            }
        });

        for (int i = row_begin - 1; i < row_end ; i++) {
            int si = 0;
            int[] tup = data[i];
//                System.out.println("Arrays.toString(tup) = " + Arrays.toString(tup));

            for (int val : tup) {
//                    System.out.println("i = " + i + 1);
//                    System.out.println("val = " + val);
                si += val % (i + 1);
            }
            siList.add(si);
        }

//            System.out.println("siList = " + siList);

//            List<String> bitwiseSiList = siList.stream().map(v -> Integer.toBinaryString(v)).collect(Collectors.toList());
//            List<String> bitwiseSiList = siList.stream().map(Integer::toBinaryString).collect(Collectors.toList());
//            siList.stream().map(Integer::toBinaryString).reduce((a, b) -> a ^ b);
        answer = siList.stream().reduce((a, b) -> a ^ b).get();

        return answer;
    }
}
