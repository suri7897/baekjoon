#include <iostream>

using namespace std;

void starboxMaker(int row, int col, int N);

int main() {
	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			starboxMaker(i, j, N);
		}
		cout << "\n";
	}

	return 0;
}

void starboxMaker(int row, int col, int N) {
	if ((row / N) % 3 == 1 && (col / N) % 3 == 1) {
		cout << " ";
	}
	else {
		if (N / 3 == 0) {
			cout << "*";
		}
		else {
			starboxMaker(row, col, N / 3);
		}
	}
}