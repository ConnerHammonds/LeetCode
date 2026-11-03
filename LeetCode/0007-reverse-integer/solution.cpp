class Solution {
public:
    int reverse(int x) {
      int ans = 0;

      while ((ans > INT_MIN / 10 + (x%10)) && (ans < INT_MAX / 10 + (x%10))) {
        int digit = x % 10; //last digit
        ans *= 10; //make room for digit (add a zero)
        ans += digit; //add the digit which is remainder 10)
        x /= 10; //remove last digit (don't have to worry about decimal since it's int)
        
        if (x == 0) return ans;
      }

      return 0;
    }
};
