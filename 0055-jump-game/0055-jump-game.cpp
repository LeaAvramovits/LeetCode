class Solution {
public:
    bool canJump(vector<int>& nums) {
    int n = nums.size();
    vector<bool> canArrive(n, false);
    canArrive[0] = true;

    for (int i = 0; i < n; i++) {
        if (!canArrive[i]) continue; 
        int farthest = min(n - 1, i + nums[i]);
        for (int j = i + 1; j <= farthest; j++) {
            canArrive[j] = true;
        }
    }

    return canArrive[n - 1];
}

};