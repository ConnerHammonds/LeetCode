class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        string longest = strs[0];

        for (string word : strs) {
            int letter = 0;
            
            while (letter < word.length() && letter < longest.length() && longest[letter] == word[letter]) {
                letter++;
            }
            longest = word.substr(0,letter);
        }
        return longest;
    }
};
