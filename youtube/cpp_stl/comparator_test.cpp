#include<iostream>
#include<set>
#include<map>

using namespace std;

template <typename type>
struct mycomp
{
    bool operator()(const type& first, const type& second) const
    {
        return first > second;
    }
};

int main()
{
    map<int, string, mycomp<int>> mymap;
    mymap[10] = "abc", mymap[30] = "def", mymap[20] = "xyz";

    for (auto &elem:mymap)
    {
        cout << elem.first << " - " << elem.second << endl;
    }

    set<int, mycomp<int>> myset;
    myset.insert(40), myset.insert(20), myset.insert(30);
    for(auto &elem: myset)
    {
        cout << elem << endl;
    }

    return 0;
}