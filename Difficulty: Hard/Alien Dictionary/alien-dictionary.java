import java.util.*;

class Solution {
    public String findOrder(String[] words) {
        
        HashMap<Character, HashSet<Character>> graph = new HashMap<>();
        HashMap<Character, Integer> indegree = new HashMap<>();
        
        for (String word : words) {
            for (char ch : word.toCharArray()) {
                graph.putIfAbsent(ch, new HashSet<>());
                indegree.putIfAbsent(ch, 0);
            }
        }
        
        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i];
            String w2 = words[i + 1];
            
            if (w1.length() > w2.length() && w1.startsWith(w2))
                return "";
                
            int len = Math.min(w1.length(), w2.length());
            
            for (int j = 0; j < len; j++) {
                char c1 = w1.charAt(j);
                char c2 = w2.charAt(j);
                
                if (c1 != c2) {
                    if (!graph.get(c1).contains(c2)) {
                        graph.get(c1).add(c2);
                        indegree.put(c2, indegree.get(c2) + 1);
                    }
                    break;
                }
            }   
        }
        
        Queue<Character> queue = new LinkedList<>();
        
        for (char ch : indegree.keySet()) {
            if (indegree.get(ch) == 0)
                queue.offer(ch);
        }
        
        StringBuilder ans = new StringBuilder();
        
        while (!queue.isEmpty()) {
            char curr = queue.poll();
            ans.append(curr);
        
            for (char next : graph.get(curr)) {
                indegree.put(next, indegree.get(next) - 1);
                if (indegree.get(next) == 0)
                    queue.offer(next);
            }
        }
        
        if (ans.length() != indegree.size())
            return "";
            
        return ans.toString();
        
    }   
}