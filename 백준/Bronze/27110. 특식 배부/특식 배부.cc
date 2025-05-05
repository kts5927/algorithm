#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N;         // 각 치킨 종류당 주문 마릿수
    int A, B, C;   // 후라이드, 간장, 양념 선호 인원수

    cin >> N;
    cin >> A >> B >> C;

    int answer = min(N, A) + min(N, B) + min(N, C);

    cout << answer << '\n';
    return 0;
}
