package lv3;

import java.util.*;
import java.util.stream.Stream;

public class BestAlbum {

    /**
     * 베스트앨범
     * 문제 설명
     * 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
     * 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
     *
     * 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
     * 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
     * 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
     * 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
     * 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
     *
     * 제한사항
     * genres[i]는 고유번호가 i인 노래의 장르입니다.
     * plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
     * genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
     * 장르 종류는 100개 미만입니다.
     * 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
     * 모든 장르는 재생된 횟수가 다릅니다.
     * 입출력 예
     * genres	plays	return
     * ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
     * 입출력 예 설명
     *
     */

    public int[] solution(String[] genres, int[] plays) {
        ArrayList<Integer> list = new ArrayList<>();

        HashMap<String, Integer> map = new HashMap<>();
        HashMap<Integer, String> genresMap = new HashMap<>();
        HashMap<Integer, Integer> playsMap = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            // 많이 재생된 장르 찾기
            if (map.containsKey(genres[i])) {
                map.put(genres[i], map.get(genres[i]) + plays[i]);
            }else {
                map.put(genres[i], plays[i]);
            }
            genresMap.put(i, genres[i]);
            playsMap.put(i, plays[i]);
        }

//        System.out.println("map = " + map);

        // 장르 순서는 map의 key 순서임
        Stream<Map.Entry<String, Integer>> sortedMap = map.entrySet().stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        String[] genreOrder = new String[map.size()];

        int i = 0;
        for (Object o : sortedMap.toArray()) {
            String[] split = o.toString().split("=");
            genreOrder[i] = split[0];
            i++;
        }

        Stream<Map.Entry<Integer, Integer>> sortedPlayMap = playsMap.entrySet().stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        String[] playOrder = new String[playsMap.size()];

        int j = 0;

        for (Object o : sortedPlayMap.toArray()) {
            String[] split = o.toString().split("=");
            playOrder[j] = split[0];
            j++;
        }
        System.out.println("playOrder = " + Arrays.toString(playOrder));
//        System.out.println("playsMap = " + playsMap);
//        System.out.println("genreOrder = " + Arrays.toString(genreOrder));
//        System.out.println("genresMap = " + genresMap);

        for (int k = 0; k < genreOrder.length; k++) {
            String gen = genreOrder[k];
            int cnt = 0;

            for (String num : playOrder) {
                String s = genresMap.get(Integer.parseInt(num));
                if (s.equals(gen) && cnt < 2) {
                    list.add(Integer.parseInt(num));
                    cnt++;
                }
            }
        }

        return list.stream().mapToInt(z -> z).toArray();
    }

    public static void main(String[] args) {
        BestAlbum bestAlbum = new BestAlbum();
        int[] solution = bestAlbum.solution(new String[]{"classic", "pop", "classic", "classic", "pop"}, new int[]{500, 600, 150, 800, 2500});

        System.out.println("solution = " + Arrays.toString(solution));
    }
}
