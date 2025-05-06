#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
    int N, X;
    cin >> N >> X;

    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    int min_cost = INT_MAX;
    for (int i = 0; i < N - 1; ++i) {
        int cost = (A[i] + A[i + 1]) * X;
        if (cost < min_cost) {
            min_cost = cost;
        }
    }

    cout << min_cost << '\n';
    return 0;
}
