#include<iostream>

using namespace std;
int main()
{
    int val = 100;
    int i = 10;

    //= means pass by value
    [=](){
        cout << val << endl;
        cout << i << endl;
    }();

    //& means pass by refrence
    [&](){
        cout << val << endl;
        cout << i << endl;
    }();
}