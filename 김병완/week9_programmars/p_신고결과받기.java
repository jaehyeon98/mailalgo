import java.util.HashMap;
import java.util.Map.Entry;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Set;

class Solution {

    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = {};
        HashMap<String, Integer> reported = new HashMap<>();
        HashMap<String, ArrayList> relations = new HashMap<>();
        for (String id : id_list) {
            reported.put(id, 0);
            relations.put(id, new ArrayList());
        }
        Set<String> set = new HashSet<String>();
        for (String rep : report) {
            set.add(rep);
        }

        for (String info : set) {
            String[] tmp = info.split(" ");
            reported.replace(tmp[1], reported.get(tmp[1]) + 1);
            relations.replace(tmp[0], relations.get(tmp[0]).asList().add(tmp[1]));
        }
        return answer;
    }
}