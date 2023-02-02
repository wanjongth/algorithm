package lv1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class CollectionPeriod {
    /**
     * 2023 kakao
     * 개인정보 수집 유효기간
     * 문제 설명
     * 고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다. 약관 종류는 여러 가지 있으며 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다.
     * 당신은 각 개인정보가 어떤 약관으로 수집됐는지 알고 있습니다. 수집된 개인정보는 유효기간 전까지만 보관 가능하며, 유효기간이 지났다면 반드시 파기해야 합니다.
     *
     * 예를 들어, A라는 약관의 유효기간이 12 달이고, 2021년 1월 5일에 수집된 개인정보가 A약관으로 수집되었다면 해당 개인정보는 2022년 1월 4일까지 보관 가능하며
     * 2022년 1월 5일부터 파기해야 할 개인정보입니다.
     * 당신은 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 합니다.
     *
     * 모든 달은 28일까지 있다고 가정합니다.
     */
    public int[] solution(String today, String[] terms, String[] privacies){
        ArrayList<Integer> answer = new ArrayList<>();

        HashMap<String, Integer> termMap = new HashMap<>();

        Integer todayAmount = parsingAmount("2000.01.01", 28, today);

        for (String term : terms) {
            String key = term.substring(0,1);
            Integer value = Integer.parseInt(term.substring(2));
            termMap.put(key, value);
        }

        int cnt = 0;

        for (String privacy : privacies) {
            cnt++;

            String termKey = privacy.substring(privacy.length() - 1);
            String date = privacy.substring(0, privacy.length() - 2);

            int year = toInteger(date, 0, 4);
            int month = toInteger(date, 5, 7);
            int day = toInteger(date, 8, 10);

            month = month + termMap.get(termKey);
            if (month > 12) {
                month = month - 12;
                year++;
            }

            String newDate = "";

            newDate += year + ".";
            if (month / 10 == 0) {
                newDate += "0";
            }
            newDate += month + ".";
            if (day / 10 == 0) {
                newDate += "0";
            }
            newDate += day;

//            System.out.println("newDate = " + newDate);

            Integer targetDateAmount = parsingAmount("2000.01.01", 28, newDate);

//            System.out.println("todayAmount = " + todayAmount);
//            System.out.println("targetDateAmount = " + targetDateAmount);

            if (todayAmount >= targetDateAmount) {
                answer.add(cnt);
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }

    private Integer parsingAmount(String benchmark, Integer dayOfMonth, String target) {
        // 기준
        int year =  toInteger(benchmark, 0, 4);
        int month = toInteger(benchmark, 5, 7);
        int day =   toInteger(benchmark, 8, 10);

        // 비교군
        int targetYear  = toInteger(target, 0, 4);
        int targetMonth = toInteger(target, 5, 7);
        int targetDay   = toInteger(target, 8, 10);

        // 차
        int retYear = targetYear - year;
        int retMonth = targetMonth - month;
        int retDay = targetDay - day;

        if (retDay < 0) {
            retDay += dayOfMonth;
            retMonth--;
        }
        if (retMonth < 0){
            retMonth += 12;
            retYear--;
        }

        // day 로 변환
        retDay += retMonth * 28;
        retDay += retYear * 28 * 12;

        return retDay;
    }

    private Integer toInteger(String format, int start, int end) {
        return Integer.parseInt(format.substring(start, end));
    }

    public static void main(String[] args) {
        CollectionPeriod collectionPeriod = new CollectionPeriod();

        int[] solution = collectionPeriod.solution("2022.05.19", new String[]{"A 6", "B 12", "C 3"}, new String[]{"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"});

        System.out.println("solution = " + Arrays.toString(solution));
    }
}
