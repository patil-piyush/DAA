#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class karastuba
{
public:
    string x;
    string y;

    karastuba()
    {
        x = ' ';
        y = ' ';
    }

    karastuba(string a, string b)
    {
        x = a;
        y = b;
    }

    int addition(int a, int b)
    {
        return a + b;
    }

    int multiplication(int a, int b)
    {
        return a * b;
    }

    

    int karastubamulti(string x, string y)
    {
        // checking the basic conditions 
        if (x.length() == 1 && y.length() == 1)
        {
            return multiplication(stoi(x), stoi(y));
        }
        else if (x.length() > 1 && y.length() > 1 && x.length() > y.length())
        {
            // add leading zeros to y
            while (y.length() < x.length())
                y = '0' + y;
        }
        else if (x.length() > 1 && y.length() > 1 && x.length() < y.length())
        {
            // add leading zeros to x
            while (x.length() < y.length())
                x = '0' + x;
        }
        else if (x.length() > 1 && y.length() > 1 && x.length() % 2 != 0)
        {
            x = '0' + x;
            // add leading zeros to both
            if (x.length() > 1 && y.length() > 1 && x.length() > y.length())
            {
                // add leading zeros to y
                while (y.length() < x.length())
                    y = '0' + y;
            }
            else if (x.length() > 1 && y.length() > 1 && x.length() < y.length())
            {
                // add leading zeros to x
                while (x.length() < y.length())
                    x = '0' + x;
            }
        }
        else if (x.length() > 1 && y.length() > 1 && y.length() % 2 != 0)
        {
            y = '0' + y;
            // add leading zeros to both
            if (x.length() > 1 && y.length() > 1 && x.length() > y.length())
            {
                // add leading zeros to y
                while (y.length() < x.length())
                    y = '0' + y;
            }
            else if (x.length() > 1 && y.length() > 1 && x.length() < y.length())
            {
                // add leading zeros to x
                while (x.length() < y.length())
                    x = '0' + x;
            }
        }
        else if (x.length() > 1 && y.length() > 1 && y.length() % 2 != 0 && x.length() % 2 != 0)
        {
            y = '0' + y;
            x = '0' + x;
            // add leading zeros to both
            if (x.length() > 1 && y.length() > 1 && x.length() > y.length())
            {
                // add leading zeros to y
                while (y.length() < x.length())
                    y = '0' + y;
            }
            else if (x.length() > 1 && y.length() > 1 && x.length() < y.length())
            {
                // add leading zeros to x
                while (x.length() < y.length())
                    x = '0' + x;
            }
        }

        int n = x.length();
        int halfn = n / 2;

        string xleft = x.substr(0, halfn);
        string xright = x.substr(halfn, n - halfn);
        string yleft = y.substr(0, halfn);
        string yright = y.substr(halfn, n - halfn);

        

    }
};

int main()
{

    return 0;
}