#include <iostream>

using namespace std;

size_t check_perfect(int a, int* array){
    int factor_num = 1;
    if(a == 1)
        return 1;
    if(a == 0)
        return SIZE_MAX;
    int factor_sum = 1;
    array[0] = 1;
    for (int i = 2; i < a;)
        if (a % i == 0){
            factor_sum += i;
            array[factor_num] = i;
            i++;
            factor_num++;
        } else
            i++;
    if(factor_sum == a)
        return factor_num;
    else
        return SIZE_MAX;
}

int main(){
    int array[1000];
    int input[1000];
    int n;
    int ind = 0;
    size_t num=0;
    while(ind != 1){
        cin >> n;
        if(n == -1)
            ind = 1;
        else{
        input[num] = n;
        num++;
        }
    }
    for(size_t i = 0; i < num; i++){
        size_t perfect = check_perfect(input[i], array);
        if(perfect == SIZE_MAX)
            cout << input[i] << " is NOT perfect." << endl;
        else{
            cout << input[i] << " = ";
            for(size_t j = 0; j<perfect; j++){
                cout << array[j] << flush;
                if(j != perfect - 1)
                    cout << " + ";
            }
            cout << endl;
        }
    }
    return 0;
}