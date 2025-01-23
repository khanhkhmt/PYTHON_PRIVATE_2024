# include <bits/stdc++.h> 
using namespace std;
void permuteRec(vector<int>& nums, int begin, vector<vector<int>>& result) { 
        if (begin == nums.size()) { 
            result.push_back(nums); 
            return; 
        } 
        for (int i = begin; i < nums.size(); i++) { 
            swap(nums[begin], nums[i]); 
            permuteRec(nums, begin + 1, result); 
            swap(nums[begin], nums[i]); 
        } 
    } 
                                                                                                   
vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> result; 
    permuteRec(nums, 0, result); 
    return result;                       
}
int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = permute(nums);
    for (int i = 0; i < result.size(); i++) {
        for (int j = 0; j < result[i].size(); j++) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}