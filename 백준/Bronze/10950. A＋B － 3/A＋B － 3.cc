#include <iostream>

int main(){
    int *a,*b;
    int num;
    std::cin >> num;
    a = (int*)malloc(sizeof(int)*num);
    b = (int*)malloc(sizeof(int)*num);
    for(int i = 0; i<num; i++){
        std::cin >> a[i] >> b[i];
    }
    for(int i = 0; i<num; i++){
        std::cout << a[i]+b[i] << std::endl;
    }
    free(a);
    free(b);
    return 0;
}