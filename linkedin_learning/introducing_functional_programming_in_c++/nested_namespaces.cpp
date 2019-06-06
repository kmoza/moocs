#include<iostream>

namespace A::B::C
{
    int i;
}

int main()
{
    A::B::C::i = 20;
    std::cout << A::B::C::i;
    return 0;
}