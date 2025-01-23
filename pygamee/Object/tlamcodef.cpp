# include <bits/stdc++.h> 

using namespace std ;

int main() {
    int t ;
    cin >> t ;
    for (int k = 0 ; k < t ; k++) {
        int n ; 
        cin >> n ;
        vector <int> a(n) ;
        vector <int> b(n) ;
        for (int i = 0 ; i < n ; i++) cin >> a[i] ;
        for (int i = 0 ; i < n ; i++) cin >> b[i] ;
        b.push_back (0) ;
        int m = 0 ;
        int s = 0 ;
        for (int i = 0 ; i < n ; i++) {
            if (a[i] > b[i+1]) {
                m += a[i] ;
                s += b[i+1] ;
            }
        }
        cout << m - s << endl ;
    }
}