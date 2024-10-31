# include <bits/stdc++.h> 

using namespace std ;
int g (int n) {
    int t = 1 ;
    for (int i = 1 ; i <= n ; i++) t *= i ;
    return t ;
} 
int c (int a) {
    if (a < 2) return 0 ;
    if (a == 2) return 1 ;
    return g (a) / (g (a-2) * 2) ;
    
}
int main () {
    int n ; cin >> n ;
    vector <int> a(n) ;
    vector <int> visit (n+1) ; 
    for (int i = 0 ; i < n ; i++) cin >> a[i] ;
    int dem = 1 ;
    int dem1 = 0 ;
    for (int i = 0 ; i < n ; i++) {

        if (!visit[i]) {
            
        
        for (int j = i+1 ; j < n ; j++) {
            if (a[i] == a[j]) dem++ , visit [j] = true ;
        }
        //cout << dem << endl ;
        dem1 += c (dem) ;
        dem = 1 ;
    }
    }
    // n! / (n-k) ! * k !
    cout << dem1 ;
}