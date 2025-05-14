#include <iostream>

using namespace std;

int N;
pair<int, int> stud[3];
int ab, ac, ba, bc, ca, cb;

int main() {
	cin >> N;
	for (int i = 0; i < 3; i++) {
		cin >> stud[i].first >> stud[i].second;
	}
	if (stud[0].first > stud[1].second + stud[2].second || stud[1].first > stud[0].second + stud[2].second || stud[2].first > stud[0].second + stud[1].second) cout << 0;
	for (int i = 0; i < stud[0].first; i++) {
		ab = i;
		ac = stud[0].first - i;
		for (int j = 0; j < stud[0].second; j++) {
			ba = j;
			bc = stud[1].first - ba;
			ca = stud[0].second - ba;
			cb = stud[1].second - ab;
			if (ba+ca == stud[0].second && ab+cb == stud[1].second && ac+bc == stud[2].second) {
				cout << 1 << '\n';
				cout << ab << ' ' << ac << '\n';
				cout << ba << ' ' << bc << '\n';
				cout << ca << ' ' << cb << '\n';
				return 0;
			}
		}
	}
	cout << 0;
}
