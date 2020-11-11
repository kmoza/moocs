#include <iostream>
#include <functional>

using namespace std;
int main()
{
    std::function<void(int)> lnfunc = [](int val) {
        cout << "The value passed in the function is = " << val << endl;
    }; lnfunc(100);
    return 0;
}