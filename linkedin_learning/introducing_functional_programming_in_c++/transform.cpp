#include<iostream>
#include<algorithm>
#include<vector>
#include<numeric>

using namespace std;

int main()
{
    auto render = [](auto collection)
    {
        for(const auto& val : collection)
        {
            cout << val << endl;
        }
    };

    vector<int> inCollection{1,2,3,4,5,6,7,8,9};
    vector<int> outCollection;
    transform(inCollection.begin(), inCollection.end(), back_inserter(outCollection), [](const int& val){return val * 3;});

    cout << "Transform" << endl;
    render(outCollection);

    //adding usgae of copy_if
    vector<int> filteredCollection;
    copy_if(inCollection.begin(), inCollection.end(), back_inserter(filteredCollection), [](int& value){return value % 2  != 0;});
    cout << "copy_if" << endl;
    render(filteredCollection);
    return 0;

}