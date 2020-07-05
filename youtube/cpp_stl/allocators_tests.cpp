#include<iostream>
#include<vector>

using namespace std;

template<typename type>
struct MyAlloc:allocator<type>
{
    type* allocate(size_t size)
    {
        cout << "allocation request size = " << size << endl;
        return new type[size];
    }

    template <typename U>
    struct rebind
    {
        typedef MyAlloc<U> other;
    };

    void deallocate(type* ptr, size_t size)
    {
        cout << "deallocating size = " << size << endl;
        delete[] ptr;
    }
};

int main()
{
    vector<int, MyAlloc<int>> v1;
    v1.push_back(20);

    for(auto& var:v1)
    {
        cout << var << endl;
    }
}