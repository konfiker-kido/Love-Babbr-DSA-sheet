#include <iostream>
using namespace std;

int maxsubArraySum(int arr[], int size)
{

    int maxSum = arr[0], sum = 0;
    for (int i = 0; i < size; i++)
    {

        sum += arr[i];
        maxSum = max(maxSum, sum);
        if (sum < 0)
        {
            sum = 0;
        }
    }
    return maxSum;
}

int main()
{
    int arr[] = {-2, -3, 4, -1, -2, 1, 5, -3};
    int size = sizeof(arr) / sizeof(arr[0]);

    cout << maxsubArraySum(arr, size);

    return 0;
}
