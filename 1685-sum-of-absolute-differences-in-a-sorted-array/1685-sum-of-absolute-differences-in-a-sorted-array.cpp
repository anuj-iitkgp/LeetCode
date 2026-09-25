auto init = []() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}();
#include <vector>
#include <numeric>

class Solution {
public:
    std::vector<int> getSumAbsoluteDifferences(std::vector<int>& nums) {
        int n = nums.size();
        
        // Using long long to prevent integer overflow during sum operations
        long long total_sum = 0;
        for (int num : nums) {
            total_sum += num;
        }

        long long left_sum = 0;
        std::vector<int> ans(n, 0);

        for (int i = 0; i < n; ++i) {
            long long right_sum = total_sum - left_sum - nums[i];

            long long left_diff = (long long)nums[i] * i - left_sum;
            long long right_diff = right_sum - (long long)nums[i] * (n - i - 1);

            ans[i] = left_diff + right_diff;
            left_sum += nums[i];
        }

        return ans;
    }
};