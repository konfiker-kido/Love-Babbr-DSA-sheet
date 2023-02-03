#include <iostream>
#include <map>
using namespace std;

string changeCase(string str)
{
    string newStr;
    int i = 0;
    while (str[i] != '\0')
    {
        if (str[i] >= 65 && str[i] <= 90)
        {
            str[i] = str[i] + 32;
        }
        i++;
    }
    return str;
}

void uniqueChar(string strng)
{
    string str = changeCase(strng);
    map<char, int> countUni;
    int i = 0;
    while (str[i] != '\0')
    {
        countUni[str[i]]++;
        i++;
    }

    map<char, int>::iterator itr = countUni.begin();

    while (itr != countUni.end())
    {
        if (itr->second == 1)
        {
            cout << itr->first << endl;
        }
        itr++;
    }
}

int main()
{

    string str = "AkashjZ mauryaz";

    uniqueChar(str);

    return 0;
}
