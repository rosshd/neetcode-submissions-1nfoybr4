public class Solution {
    public bool IsAnagram(string s, string t) 
    {
        if(s.Length != t.Length)
        {
            return false;
        }
        Dictionary<char, int> word_map = new Dictionary<char, int>();

        foreach(char charactor in s)
        {
            if(word_map.ContainsKey(charactor))
            {
                word_map[charactor]++;
            }
            else
            {
                word_map.Add(charactor, 1);
            }
        }
        for(int index = 0; index < t.Length; index++)
        {
            if(word_map.ContainsKey(t[index]))
            {
                char tempChar = t[index];
                Console.WriteLine(index + " is the index : " + t[index] + " : " + word_map[t[index]]);

                if(word_map[t[index]] <= 1)
                {
                    word_map.Remove(tempChar);
                    
                }
                else
                {
                    word_map[tempChar]--;
                }
            }
            else
            {
                return false;
            }
        }

        return true;
    }
}
