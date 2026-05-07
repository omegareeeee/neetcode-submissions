class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<String, List<String>>();
        for(String word: strs){
            char[] charWord = word.toCharArray();
            Arrays.sort(charWord);
            String sortedWord = new String(charWord);
            res.putIfAbsent(sortedWord, new ArrayList());
            res.get(sortedWord).add(word);
        }
        return new ArrayList(res.values());
    }
}
