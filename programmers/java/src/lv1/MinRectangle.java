package lv1;

public class MinRectangle {

    /**
     * 최소직사각형
     * 문제 설명
     * 명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다.
     * 다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서,
     * 작아서 들고 다니기 편한 지갑을 만들어야 합니다.
     * 이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.
     *
     * 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다.
     * 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.
     *
     * sizes의 길이는 1 이상 10,000 이하입니다.
     * sizes의 원소는 [w, h] 형식입니다.
     * w는 명함의 가로 길이를 나타냅니다.
     * h는 명함의 세로 길이를 나타냅니다.
     * w와 h는 1 이상 1,000 이하인 자연수입니다.
     */

    public int solution(int[][] sizes) {
        int answer = 0;

        int max_garo = 0;
        int max_sero = 0;

        for (int i = 0; i < sizes.length; i++) {
            int garo = Math.max(sizes[i][0], sizes[i][1]);
            int sero = Math.min(sizes[i][0], sizes[i][1]);

            max_garo = Math.max(max_garo, garo);
            max_sero = Math.max(max_sero, sero);
        }

        answer = max_garo * max_sero;

        return answer;
    }

    public static void main(String[] args) {
        MinRectangle minRectangle = new MinRectangle();

        int solution = minRectangle.solution(new int[][]{{60, 50}, {30, 70}, {60, 30}, {80, 40}});
        System.out.println("solution = " + solution);
    }
}
