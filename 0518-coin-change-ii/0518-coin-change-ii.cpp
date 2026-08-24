class Solution {
int a;

private:

    int h(int i, int t, vector<int>& c, vector<vector<int>> &dp){
        if(i==c.size() || t>a) return 0;
        if(t==a) return 1;
        if(dp[i][t]!=-1) return dp[i][t];
        int take=h(i, t+c[i], c,dp);
        int ntake=h(i+1, t, c,dp);
        return dp[i][t]=take+ntake;
    }
public:
    int change(int amount, vector<int>& coins) {
     vector<vector<int>> dp(coins.size(), vector<int>(amount+1, -1));
    a=amount;
        
        return h(0, 0, coins,dp);
    }
};