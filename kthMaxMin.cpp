// 1st method -> priority queue (minHeap)
// quickSort
// This question is solved by priority queue with time complexity of 
#include <iostream>
#include <queue>
using namespace std;

int kthSmallest(int arr[], int r, int k)
{

    priority_queue<int, vector<int>, greater<int>> minHeap;

    for (int i = 0; i <= r; i++)
    {
        minHeap.push(arr[i]);
    }

    int count = 1;
    while (k != count)
    {
        minHeap.top();
        minHeap.pop();
        count++;
    }
    return minHeap.top();
}
int main()
{

    int arr[] = {7, 10, 4, 3, 20, 15};
    int k;
    cout << "Enter kth max element " << endl;
    cin >> k;

    cout << k << " minimum element is " << kthSmallest(arr, 6, k);
    return 0;
}
