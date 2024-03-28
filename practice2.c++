#include<bits/stdc++.h>

using namespace std;


int n, m, startX, startY;
string s;
int dp[1001][1001] = { 0, };
char _map[1001][1001];
int ans = 0;
bool check = false;

void move()
{
	for (int j = startY; j < m; ++j)
	{
		for (int i = 0; i < n; ++i)
		{
			if ('#' == _map[i][j])
				continue;
			if (i - 1 >= 0 && j - 1 >= 0 && dp[i - 1][j - 1] != -1)
				dp[i][j] = max(dp[i][j], dp[i - 1][j - 1]);
			if (j - 1 >= 0 && dp[i][j - 1] != -1)
				dp[i][j] = max(dp[i][j], dp[i][j - 1]);
			if (i + 1 < n && j - 1 >= 0 && dp[i + 1][j - 1] != -1)
				dp[i][j] = max(dp[i][j], dp[i + 1][j - 1]);
			
			if ('C' == _map[i][j] && dp[i][j] != -1)
				++dp[i][j];
			if ('O' == _map[i][j] && dp[i][j] != -1)
			{
				check = true;
				ans = max(ans, dp[i][j]);
			}

		}
	}
}

int main()
{
	memset(dp, -1, sizeof(dp));
	cin >> n >> m;
	for (int i = 0; i < n; ++i)
	{
		cin >> s;
		for (int j = 0; j < s.size(); ++j)
		{
			_map[i][j] = s[j];
			if ('R' == _map[i][j])
			{
				startX = i;
				startY = j;
				dp[i][j] = 0;
			}
		}
	}
	move();
	if (check)
		cout << ans << "\n";
	else
		cout << "-1" << "\n";

	return 0;
}