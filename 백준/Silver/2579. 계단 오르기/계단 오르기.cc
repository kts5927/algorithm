#include <iostream>
#include <algorithm>
using namespace std;

int stair[301];
int sum[301];
void insert(int n) {
	for (int i = 0; i < n; i++) {

		cin >> stair[i];
	}

}

void calculate(int n) {

	sum[0] = stair[0];
	sum[1] = stair[1]+stair[0];
	sum[2] = max(stair[0] + stair[2], stair[1] + stair[2]);
	
	for (int i = 3; i < n; i++) {

		sum[i] = max(sum[i - 2] + stair[i], sum[i - 3] + stair[i - 1] + stair[i]);
		
	}




}



int main() {
	int n;
	cin >> n;
	insert(n);
	calculate(n);

	cout << sum[n-1];




}