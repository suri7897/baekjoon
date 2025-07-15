#include <iostream>

using namespace std;

void hanoi(int num_top, int start, int mid, int to){
    if(num_top == 1){
        cout << start << " " << to << '\n';
        return;
    }
    hanoi(num_top - 1, start, to, mid);
    cout << start << " " << to << '\n';
    hanoi(num_top - 1, mid, start, to);
    return;
}

int pow(int a, int b){
    int result=1;
    if(b<0)
        return 1;
    for(int i = 0; i<b; i++){
        result *= a;
    }
    return result;
}   

int main(){
    int num_hanoi;
    cin >> num_hanoi;
    cout << pow(2,num_hanoi) - 1 << endl;  
    hanoi(num_hanoi,1,2,3);
}