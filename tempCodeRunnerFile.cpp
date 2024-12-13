# include <bits/stdc++.h>

using namespace std ;
bool kt (int m , int n , int a[10000] , int k) {
    bool g = true ;
    for (int i = 0 ; i < n ; i++) {
        if (i != m) {
        if (abs(a[i] - a[m]) % k == 0) {
            g = false ;
        }
        }
    }
    if (g == true ) return true ;
    else return false ;
}
int main() {
    int t ; cin >> t ;
    vector <string> kq ;
    for (int j = 0 ; j < t ; j++) {
        int n , k ; cin >> n >> k ;
        int a[n] ;
        for (int i = 0 ; i < n ;i++) cin >> a[i] ;
        bool kt1 = false ;
        int dem = 0 ;
        for (int i = 0 ; i < n ; i++) {
             if (kt(i,n,a,k)) {
                kt1 = true ;
                dem = i ;
                break ;
        }
        // cout << kt(i,n,a,k) << " " ;
        }
        if (kt1) {
            kq.push_back ("yes") ;
            kq.push_back (to_string(dem+1)) ;
        }
        else kq.push_back("no") ;
    }
    for (int i = 0 ; i < kq.size() ; i++) cout << kq[i] << endl ;
}