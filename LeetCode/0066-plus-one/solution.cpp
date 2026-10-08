class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        size_t s = size(digits)-1; // 0

        for (int i = s; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            } else {
                digits[i] = 0;
            }
        }

        //if the program gets to this point, that means that the input array was only 9's
        //in that case, all numbers will be 0 by the end of the above for loop
        //simply change the first digit to 1 and add a 0 on the end.
        //Ex. {9, 9, 9} -> {1, 0, 0, 0}
        digits.push_back(0);
        digits[0] = 1;
        return digits;
    }
};
