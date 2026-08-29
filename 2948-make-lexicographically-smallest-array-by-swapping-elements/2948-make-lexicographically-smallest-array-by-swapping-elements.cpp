class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        vector<int> sted=nums;
        sort(sted.begin(), sted.end());
        int gn=0;
        unordered_map<int, int> sgnum;
        unordered_map<int, queue<int>> ele;
        int prev=sted[0];int i=0;
        for(int i:sted){
            if(i-prev<=limit) {sgnum[i]=gn;ele[gn].push(i);}
            else {gn++;sgnum[i]=gn;ele[gn].push(i);}
            prev=i;
        }
        for(int i=0;i<nums.size();i++){
            int group=sgnum[nums[i]];
            nums[i]=ele[group].front();
            ele[group].pop();
        }
        return nums;
    }
};