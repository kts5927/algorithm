#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int power;
int dp[101][100001];

struct things
{
	int value;
	int weight;
};

things vacation[101];

void insert(int n) 
{
	for (int i = 1; i <= n; i++) 
	{
		cin >> vacation[i].weight >> vacation[i].value;
	}
}

void calculate(int n) {

	for (int i = 1; i <= n; i++) {

		for (int j = 1; j <= power; j++) {

			if (j - vacation[i].weight >= 0)dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - vacation[i].weight] + vacation[i].value);
			else dp[i][j] = dp[i - 1][j];

		}
	}
	cout << dp[n][power];



}



int main() {
	
	int n;
	cin >> n>>power;

	insert(n);

	
	calculate(n);

	

}
