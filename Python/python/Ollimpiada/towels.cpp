#include <iostream>
#include <cmath>

using namespace std;

bool isTower(int num) {
    bool state = false;
    if (num == 1) {
        return true;
    }

    for (int i = 2; i <= sqrt(num); i++) {

        int j = i;
        while (j < num) {
            if (pow(i, j) == num) {
                state = true;
                break;
            }
            j+=i;
        }
    }
    return state;
}

int main() {
    int n = 0;
    cin >> n;
    int count = 0;
    for (int i = 1; i <= n; i++) {
        if (isTower(i)) {
            count++;
        }
    }
    cout << count<< endl;
    return 0;
}