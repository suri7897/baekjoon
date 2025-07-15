#include <iostream>

using namespace std;

int is_prime(int a){
    if(a == 1)
        return 0;
    if(a == 2)
        return 1;
    for(int i = 2; i<a; i++){
        if(a % i == 0)
            return 0;
    }
    return 1;
}

void prime_print(int a, int b){
    int sum = 0;
    int smallest = b+100;
    for(int i = a; i <= b; i++){
        if(is_prime(i) == 1){
            sum += i;
            if(i < smallest)
                smallest = i;
        }
    }
    if(sum == 0)
            cout << -1 << endl;
        else{
            cout << sum << "\n";
            cout << smallest << endl;
        }
}

int main(){
    int first;
    int last;
    cin >> first;
    cin >> last;
    prime_print(first, last);
    return 0;
}