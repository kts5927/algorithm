#include <iostream>
#include <string>
#include <map>


using namespace std;




int main() {
	int q;
	cin >> q;
	string a, b;

	while (q--) {
		int w;
		cin >> w;
		map<string, int> cloth;
		while (w--) {
			
			
			cin >> b >> a ;

			if (cloth.find(a) == cloth.end()) {

				cloth.insert({ a,1 });
			}
			else cloth[a]++;
		}
			int ans = 1;
			for (auto i : cloth)
			{
				ans *= (i.second + 1);

			}ans -= 1;
			cout << ans << '\n';

		
	}
}