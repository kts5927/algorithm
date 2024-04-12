#include <iostream>
#include <algorithm>
using namespace std;
int count1;

int tri[501][501];
int angle[501][501];
int ans;
void insert(int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++) {
			cin >> tri[i][j];
		}

	}

}

void calculate(int n) {

	angle[0][0] = tri[0][0];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++) {

			if (j == i&&i>0) {
				angle[i][j] = angle[i - 1][j - 1]+tri[i][j];
			}
			else if (j == 0&&i>0) {
				angle[i][j] = angle[i - 1][j]+tri[i][j];
			}
			else if(i > 0) {
				angle[i][j] = max(angle[i - 1][j], angle[i - 1][j - 1])+tri[i][j];
			}
		}
	}

}

void max(int n) {
	ans = angle[n-1][0];
	for (int j = 0; j < n; j++) {
		
		ans = max(ans, angle[n-1][j]);
		
	}

}

int main() {
	int n;
	cin >> n;

	insert(n);
	calculate(n);
	max(n);

	cout << ans;

}
