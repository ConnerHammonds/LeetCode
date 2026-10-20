class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> map;
        if (s.size() != t.size()) return false;

        for (char i : s) {
            map[i]++;
        }
        
        for (char i : t) {
            if (!map.contains(i)) return false;
            map[i] -= 1;
        }

        for (const auto pair : map) {
            if (pair.second != 0) return false;
        }
        return true;
    }
};
