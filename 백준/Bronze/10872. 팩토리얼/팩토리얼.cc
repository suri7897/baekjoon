#include <iostream>

using namespace std;

long long fact(int x){
    if(x==0)
        return 1;
    return x * fact(x-1);
}

int main(){
    int input;
    cin >> input;
    cout << flush;
    cout << fact(input) << endl;
}