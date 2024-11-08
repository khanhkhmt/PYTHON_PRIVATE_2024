# include <bits/stdc++.h> 

using namespace std ;

double trace (vector<vector<double>> a) {
    double sum = 0 ;
    for (int i = 0 ; i < a.size() ; i++) {
            sum += a[i][i] ;
    }
    return sum ;
}
vector <vector<double>> operator - (vector <vector<double>> a , double n) {
   // vector <vector<double>> h (a.size() , vector<double> (a.size())) ;
    for (int i = 0 ; i < a.size() ; i++) {
        a[i][i] -= n ;
    }
    return a ; 
}
vector <vector<double>> operator * (vector<vector<double>> a , vector<vector<double>> b ) {
    vector <vector<double>> t (a.size() , vector<double> (a.size())) ;
    for (int i = 0 ; i < a.size() ; i++) {
        for (int j = 0 ; j < b[i].size() ; j++) {
            for (int k = 0 ; k < a.size() ; k++) {
                t[i][j] += a[i][k] * b[k][j] ;
            }
        }
    }
    return t ;
}
// vector <vector<double>> operator * (int x  , vector<vector<double>> a) {
//     for (int i = 0 ; i < a.size() ; i++) {
//         for (int j = 0 ; j < a[i].size() ; j++) {
//             a[i][j] *= x ;
//         }
//     }
//     return a ;
// }
int main() {
    int n ; 
    cout << "ma tran cap: " ; cin >> n ;
    vector <vector<double>> a (n , vector <double> (n )) ;
    for (int i = 0 ; i < n ; i++) {
        for (int j = 0 ; j < n ; j++) {
            cin >> a[i][j] ;
        }
    }
    vector <double> k ;
    double p = trace(a) ; k.push_back(p) ;
    vector<vector<double>> y = a  ;
    for (int i = 2 ; i <= n ; i++) {
         y = a*( y - p ) ;
         p = trace(y) * (1/(double)i) ; k.push_back(p) ;
    }
   for(auto x : k) cout << x << " "  ;
   
    // for(auto x : y){
    //     for(auto y : x) cout << y << " " ; cout << endl ;
    //     }
}