#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0

int czy_pierwsza(int x){
    int i;
    if(x==1){
        return FALSE;
    }
    for(i=2; i*i<=x; i++){
        if(x%i == 0){
            return FALSE;
        }
    }
    return TRUE;
}

int main()
{
    int n, i, x;
    scanf("%d", &n);
    for(i=0; i<n; i++){
        scanf("%d", &x);
        if(czy_pierwsza(x) == TRUE){
            printf("TAK\n");
        }
        else{
            printf("NIE\n");
        }
    }
    return 0;
}
