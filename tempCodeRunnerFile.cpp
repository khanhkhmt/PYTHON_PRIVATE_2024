#include <bits/stdc++.h>

using namespace std ;

vector<int> tt ; int t ;
vector<vector<int>> ans ;

void backtracking( vector<int> a , int cur = 0 , int _i = 0 ){

    if(cur == t) ans.push_back(a) ;
    if(cur < t){
    for( int i = _i ; i < tt.size() ; i++ ){
        a.push_back(tt[i]) ;
        backtracking(a , cur + tt[i] , i ) ;
        a.pop_back() ;
     }
    }
}

signed main(){
    int n ; cin >> n ; tt.resize(n) ;
    for( auto &x : tt) cin >> x ;
    cin >> t ;
    sort(tt.begin() , tt.end()) ;
    vector<int> a ;
    //
    backtracking(a ) ;
    for(auto x : ans){
        for(auto y : x) cout << y << " " ; cout << endl ;
    }
}