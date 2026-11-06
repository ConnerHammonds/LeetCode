class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
      if (str1 + str2 != str2 + str1) return ""; //strings aren't made up of same characters. No GCD
      
      //create copy of smaller string
      string x;
      if (str1.size() == min(str1.size(), str2.size())) x = str1;
      else x = str2;
      int p = x.size()-1; // pointer to end of smaller string
      
      //x must divide str.size() for both strings
      //if str1.size() % x == 0 && str2.size() % x == 0, return x
      //start with smaller string as x, move a pointer from the end of the string leftward until if is satisfied
      while (p >= 0) {
        string sub = x.substr(0, p+1); //Note: substr isn't inclusive of second arg
        if (str1.size() % sub.size() == 0 && str2.size() % sub.size() == 0) return sub;
        p--; 
      }

      return "";
    }
};
