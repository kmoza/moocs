#include <iostream>
#include <thread>
#include <future>

using namespace std;

void asyncFunc()
{
    cout << "Async thread =" << this_thread::get_id() << endl;
    cout << "I am inside a async..." << endl;
}

int main()
{
    cout << "Main Threads" <<this_thread::get_id()<<endl;
    future<void> fn = async(launch::async, asyncFunc);
    fn.get();
    return 0;
}