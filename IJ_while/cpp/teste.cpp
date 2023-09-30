#include <iostream>
#include <vector>

using namespace std;

int main() 
{
	vector<int> array {1, 2, 3};
	int *ptr1 = array.data();
	int *ptr2 = ptr1+1;
	cout << *ptr2;

	// to be continued
}
