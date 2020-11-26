#include<omp.h>
#include<stdio.h>

int main()
{
    //compiler directive
    #pragma omp parallel
    {   
        printf("Hello World\n");
    }
    return 0;
}