#include "stdafx.h"
#include<iostream>
#include<string>

using namespace std;

int main() {

	string lat;
	int count = 0;
	cin >> lat;

	for (int i = 0; i < lat.length(); i++) {

		switch (lat[i]) {

		case 'M':
			count += 1000;
			break;
		case 'D':
			count += 500;
			break;
		case 'C':

			if (i + 1 < lat.length() && (lat[i + 1] == 'D' || lat[i + 1] == 'M'))
				count -= 100;
			else
				count += 100;
			break;
		case 'L':
			count += 50;
			break;
		case 'X':
			if (i + 1 < lat.length() && (lat[i + 1] == 'L' || lat[i + 1] == 'C' || lat[i + 1] == 'M'))
				count -= 10;
			else
				count += 10;

			break;
		case 'V':
			count += 5;
			break;
		case 'I':
			if (i + 1 < lat.length() && (lat[i + 1] == 'V' || lat[i + 1] == 'X' || lat[i + 1] == 'C'))
				count -= 1;
			else count += 1;

			break;
		}
	}
	cout << count << endl;
	system("pause");
	return 0;
}