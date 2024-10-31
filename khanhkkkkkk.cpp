#include <bits/stdc++.h>
using namespace std;
int n, m;
const string m1 = "YOKOHAMA" ;
vector<int> dx = {-1, 1, 0, 0};
vector<int> dy = {0, 0, 1, -1};
int dem ;

void dfs(vector<string> a, int x, int y, int vt ) {
    if (vt == 7) {  
        dem++;
        return;
    }
    
    for (int i = 0; i < 4; i++) {
        int s = x + dx[i];
        int t = y + dy[i];
        if (s >= 0 && t >= 0 && s < n && t < m && a[s][t] == m1[vt + 1]) {
            dfs(a, s, t, vt + 1);  
        }
    }
}

void ham(vector<string> a) {
    dem = 0 ;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] == 'Y') {
                dfs(a, i, j, 0);  
            }
        }
    }
}

int main() {
    cin >> n >> m;
    vector <string> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    ham(a);
    cout <<  dem ;
}