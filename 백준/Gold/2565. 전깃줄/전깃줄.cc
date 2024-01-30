#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<pair<int,int>> wire;
int dp[501];


void insert(int n) 
{
	int a, b;
	for (int i = 0; i < n; i++)
	{
		cin >> a >> b;
		wire.push_back(make_pair(a, b));
	}

	sort(wire.begin(), wire.end());

}

void calculate(int n) {
	int ans = 0;
	for (int i = 0; i < n; i++) {

		dp[i] = 1;
		for (int j = 0; j < i; j++) {
			if (wire[i].second > wire[j].second) {
				dp[i] = max(dp[j] + 1, dp[i]);
				
			}
		}

		ans = max(ans, dp[i]);
	}
	cout << n - ans;

}



int main() {
	
	int n;
	cin >> n;

	insert(n);

	
	calculate(n);

	

}