#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
using namespace std;

int factorial(int n){
    int storage = 1;
    for (int i = 1; i <= n; i++){
        storage *=i;
    }
    return storage;
}
int main() {
    int m, k;
    cin >> m >> k;
    int n = 2;
    if ( m >1 && k < 10e9){
        long long int d = pow(m,k);
        while(factorial(n) % d != 0){  
            n+=1;
        }   
        cout << n<<endl;
    }
    else{
        return 0;
    }
}
