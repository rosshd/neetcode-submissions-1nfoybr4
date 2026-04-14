public class Solution {
    public bool IsPalindrome(string s) {
        s = s.ToLower();
        string forwards = "";
        string backwards = "";
        foreach(char c in s){
            if((c - 'a' >= 0 && c - 'a' < 26) || (c - '0' >= 0 && c - '0' < 9)){
                forwards+=c;
            }
        }
        for(int i = s.Length - 1; i >= 0; i--){
            if((s[i] - 'a' >= 0 && s[i] - 'a' < 26) || (s[i] - '0' >= 0 && s[i] - '0' < 9)){
                backwards+=s[i];
            }
        }
        Console.WriteLine(backwards + " : " + forwards);
        if(forwards == backwards){
            return true;
        }
        else return false;
    }
}
