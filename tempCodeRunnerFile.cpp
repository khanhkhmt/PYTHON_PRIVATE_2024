# include <bits/stdc++.h>

using namespace std ;

void binary (int n) {
    if (n < 2) cout << n % 2;
    else {
        binary (n / 2) ;
        cout << n % 2;
    }
}
int main() {
    int n ; cin >> n ;
    binary (n) ;
}