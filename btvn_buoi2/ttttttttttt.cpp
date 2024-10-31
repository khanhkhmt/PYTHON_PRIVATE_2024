#ifndef LOCAL
#include <bits/stdc++.h>
#else 
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>                                  
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <stack>
#endif

using namespace std;

//#define my_love cout << "Thanh" << endl

#define int int64_t
#define vt vector
#define ii pair<int,int>
#define pb push_back
#define no cout<<"No"<<endl 
#define yes cout<<"Yes"<<endl
#define Zz endl

//const int MOD = 1e9 + 7;
const int N = 1e5 + 5;
//const int _N = 320;


void solve() {
    int n; cin >> n;
    vt<int> w(100 + 1, 0), h(100 + 1, 0);
    for (int i = 0; i < n; i++) {
        int u, v; cin >> u >> v;
        for (int j = u; j > 0; j--) {
            h[j] = max(h[j], v);
        }
        for (int j = v; j > 0; j--) {
            w[j] = max(w[j], u);
        }
    }



    int dem = 0;
    for (int i = h[1]; i > 1; i--) {
        dem += h[i - 1] - h[i];
        // dem += w[i] - w[i - 1];
        // cout << dem << endl;
    }
    for (int i = w[1]; i > 1; i--) {
        //dem += h[i] - h[i - 1];
        dem += w[i - 1] - w[i];
        //cout << dem << endl;
    }
    cout << dem + h[1] + w[1] + h[w[1]] + w[h[1]] << endl;

}

signed main() {
#ifndef LOCAL
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
#endif

    int t;
    std::cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}
/*

5
5
1 5
2 4
3 3
4 2
5 1
3
2 2
1 1
1 2
1
3 2
3
100 100
100 100
100 100
4
1 4
2 3
1 5
3 2

*/