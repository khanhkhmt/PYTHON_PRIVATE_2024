# include <bits/stdc++.h> 

using namespace std ;

int main() {
    int t ; cin >> t ;
    vector<int> kq1 ;
    vector<int> kq2 ;
    for (int i = 0 ; i < t ; i++) {
        int n ; cin >> n ;
        vector <int> ct (2*n) ;
        for (int i = 0 ; i < 2*n ; i++) cin >> ct[i] ;
        int dem0 = 0 ;
        int dem1 = 0 ;
        for (int i = 0 ; i < 2*n ; i++) {
            if (ct[i] == 0) dem0 ++ ;
            if (ct[i] == 1) dem1 ++ ;
        }
        if (dem1 >= dem0) kq1.push_back (dem0) ;
        else  kq1.push_back (dem1) ;
        if (dem1 % 2 != 0) kq2.push_back (1) ;
        else kq2.push_back (0) ;
    }
    for (int i = 0 ; i < kq1.size() ; i++) {
        cout << kq2[i] << " " << kq1[i] << endl; 
    }
}