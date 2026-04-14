public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {

        var result = new Dictionary<string, List<string>>();

        for(int index = 0; index < strs.Length; index++)
        {
            int[] count = new int[26];

            foreach(char c in strs[index])
            {
                count[c - 'a']++;
            }
            string key = string.Join(",", count);
            if(!result.ContainsKey(key))
            {
                result[key] = new List<string>();
            }
            result[key].Add(strs[index]);
        }
        return result.Values.ToList<List<string>>();
    }
}
