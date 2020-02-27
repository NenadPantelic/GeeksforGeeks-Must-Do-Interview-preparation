#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int knapsack01(int* weights, int* values, int n, int W){
    int dp[n+1][W+1];
    memset(dp, 0, sizeof(dp));
    for(int i=1; i <= n; i++){
        for(int j=0; j <= W; j++){
            if (i==0)
                continue;
            if (weights[i-1] > j){
                dp[i][j] = dp[i-1][j];
            } else {
                dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j-weights[i-1]]);
            }
        }
    }
    return dp[n][W];

}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int t, n, W;
  cin >> t;
  //int values[1000], weights[1000];
  for(int i=0; i < t; i++){
    cin >> n;
    cin >> W;
    int values[n], weights[n];
    for(int j=0; j < n; j++) cin >> values[j];
    for(int k=0; k < n; k++) cin >> weights[k];
    cout << knapsack01(weights, values, n, W) << endl;
  }
	return 0;
}
