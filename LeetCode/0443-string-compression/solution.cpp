class Solution {
public:
    int compress(vector<char>& chars) {
      int write = 0;
      int start = 0;

      if (chars.size() == 1){return 1;}

      while (start < chars.size()) {
        int end = start;
        while (end < chars.size() && chars[start] == chars[end]) {
          end++;
        }
        int len = end - start;
        chars[write] = chars[start];
        write++;

        if (len > 1) {
          string s = to_string(len);
          for (char c: s) {
          chars[write] = c;
          write++;
          }
        }
        start = end;
      }
      return write;
    }
};
