#include <iostream>
#include <map>
using namespace std;

void duplicateChar(string str)
{
    map<char, int> charCount;

    int i = 0;
    while (str[i] != '\0')
    {
        charCount[str[i]]++;
        i++;
    }
    map<char, int>::iterator itr = charCount.begin();
    while (itr != charCount.end())
    {
        if ((itr->second) > 1)
        {
            cout << itr->first << " " << itr->second << " times" << endl;
        }
        itr++;
    }
}

int main()
{

    string str = "test string";
    duplicateChar(str);

    return 0;
}
