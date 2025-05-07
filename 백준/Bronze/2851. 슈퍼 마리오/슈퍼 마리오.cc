#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int score[10];
    for (int i = 0; i < 10; ++i) {
        cin >> score[i];
    }

    int sum = 0;
    int result = 0;

    for (int i = 0; i < 10; ++i) {
        sum += score[i];

        if (abs(100 - sum) < abs(100 - result)) {
            result = sum;
        } else if (abs(100 - sum) == abs(100 - result)) {
            if (sum > result) result = sum;
        }
    }

    cout << result << '\n';
    return 0;
}
