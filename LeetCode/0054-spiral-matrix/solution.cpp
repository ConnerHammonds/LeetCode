
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;

        int rows = matrix.size();
        int cols = matrix[0].size();
        int tot = rows * cols;

        int right = cols - 1;
        int bottom = rows - 1;
        int left = 0;
        int top = 0;

        while (res.size() < tot) {

            // Traverse top: left -> right
            for (int p = left; p <= right && res.size() < tot; p++) {
                res.push_back(matrix[top][p]);
            }
            top++;

            // Traverse right: top -> bottom
            for (int p = top; p <= bottom && res.size() < tot; p++) {
                res.push_back(matrix[p][right]);
            }
            right--;

            // Traverse bottom: right -> left
            for (int p = right; p >= left && res.size() < tot; p--) {
                res.push_back(matrix[bottom][p]);
            }
            bottom--;

            // Traverse left: bottom -> top
            for (int p = bottom; p >= top && res.size() < tot; p--) {
                res.push_back(matrix[p][left]);
            }
            left++;
        }

        return res;
    }
};

