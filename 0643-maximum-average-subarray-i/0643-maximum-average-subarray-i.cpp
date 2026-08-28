class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double sum = 0;
        for (int i = 0; i < k; ++i) sum += nums[i];
        double max_sum = sum;
        for (int i = 0; i < nums.size() - k; ++i) {
            sum += nums[k + i] - nums[i];
            max_sum = max(max_sum, sum);
        }
        return max_sum / k;
    }
};