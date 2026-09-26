class Solution {
private:
    vector<vector<vector<int>>> dp;
    int h(vector<int> &nums, int i, int prev, int k){
        if(i>=nums.size()) return 0;
        if(dp[i][prev+1][k]!=-1) return dp[i][prev+1][k];
        int take=0,ntake=h(nums, i+1, prev, k);
        if(prev==-1) take=1+h(nums, i+1, i, k);
        else if(k>0) {
            if(nums[prev]!=nums[i]) take=1+h(nums, i+1, i, k-1);
            else take=1+h(nums, i+1, i, k);
        }
        else if(k==0 && nums[prev]==nums[i]) take=1+h(nums, i+1, i, k);
        return dp[i][prev+1][k]=max(take, ntake);  
    }
public:
    int maximumLength(vector<int>& nums, int k) {
        dp.assign(nums.size()+2, vector<vector<int>>(nums.size()+2, vector<int>(k+2, -1)));
        return h(nums, 0, -1, k);
    }
};