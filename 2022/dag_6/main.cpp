#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

void deel_1();
void deel_2();

int main()
{
    deel_2();

    return 0;
}

void deel_1()
{
    string file1 = "input.txt";
    ifstream myfile1; myfile1.open(file1);
    string str;

    vector <string> waardes;

    int size, j = 0;
    string tijdelijk;

    getline(myfile1, str);

    size  =str.length();

    for(int i=0; i<size; i++)
    {
        tijdelijk = str[i];
        waardes.push_back(tijdelijk);
    }

    for(int i=0; i<size-4; i++)
    {
        if(waardes.at(i) != waardes.at(i+1) and waardes.at(i) != waardes.at(i+2) and waardes.at(i) != waardes.at(i+3))
        {
            if(waardes.at(i+1) != waardes.at(i+2) and waardes.at(i+1) != waardes.at(i+3))
            {
                if(waardes.at(i+2) != waardes.at(i+3))
                {
                    j = i+4;
                    break;
                }
            }

        }
    }

    cout << "**** " << j << " ****" << endl;
}

void deel_2()
{
    string file1 = "input.txt";
    ifstream myfile1; myfile1.open(file1);
    string str;

    vector <string> waardes;

    int size, j = 0;
    string tijdelijk;

    getline(myfile1, str);

    size  =str.length();

    for(int i=0; i<size; i++)
    {
        tijdelijk = str[i];
        waardes.push_back(tijdelijk);
    }

    for(int i=0; i<size-14; i++)
    {
        if(waardes.at(i) != waardes.at(i+1) and waardes.at(i) != waardes.at(i+2) and waardes.at(i) != waardes.at(i+3) and waardes.at(i) != waardes.at(i+4) and waardes.at(i) != waardes.at(i+5) and waardes.at(i) != waardes.at(i+6) and waardes.at(i) != waardes.at(i+7) and waardes.at(i) != waardes.at(i+8) and waardes.at(i) != waardes.at(i+9) and waardes.at(i) != waardes.at(i+10) and waardes.at(i) != waardes.at(i+11) and waardes.at(i) != waardes.at(i+12) and waardes.at(i) != waardes.at(i+13))
        {
            if(waardes.at(i+1) != waardes.at(i+2) and waardes.at(i+1) != waardes.at(i+3) and waardes.at(i+1) != waardes.at(i+4) and waardes.at(i+1) != waardes.at(i+5) and waardes.at(i+1) != waardes.at(i+6) and waardes.at(i+1) != waardes.at(i+7) and waardes.at(i+1) != waardes.at(i+8) and waardes.at(i+1) != waardes.at(i+9) and waardes.at(i+1) != waardes.at(i+10) and waardes.at(i+1) != waardes.at(i+11) and waardes.at(i+1) != waardes.at(i+12) and waardes.at(i+1) != waardes.at(i+13))
            {
                if(waardes.at(i+2) != waardes.at(i+3) and waardes.at(i+2) != waardes.at(i+4) and waardes.at(i+2) != waardes.at(i+5) and waardes.at(i+2) != waardes.at(i+6) and waardes.at(i+2) != waardes.at(i+7) and waardes.at(i+2) != waardes.at(i+8) and waardes.at(i+2) != waardes.at(i+9) and waardes.at(i+2) != waardes.at(i+10) and waardes.at(i+2) != waardes.at(i+11) and waardes.at(i+2) != waardes.at(i+12) and waardes.at(i+2) != waardes.at(i+13))
                {
                    if(waardes.at(i+3) != waardes.at(i+4) and waardes.at(i+3) != waardes.at(i+5) and waardes.at(i+3) != waardes.at(i+6) and waardes.at(i+3) != waardes.at(i+7) and waardes.at(i+3) != waardes.at(i+8) and waardes.at(i+3) != waardes.at(i+9) and waardes.at(i+3) != waardes.at(i+10) and waardes.at(i+3) != waardes.at(i+11) and waardes.at(i+3) != waardes.at(i+12) and waardes.at(i+3) != waardes.at(i+13))
                    {
                        if(waardes.at(i+4) != waardes.at(i+5) and waardes.at(i+4) != waardes.at(i+6)and waardes.at(i+4) != waardes.at(i+7) and waardes.at(i+4) != waardes.at(i+8) and waardes.at(i+4) != waardes.at(i+9) and waardes.at(i+4) != waardes.at(i+10) and waardes.at(i+4) != waardes.at(i+11) and waardes.at(i+4) != waardes.at(i+12) and waardes.at(i+4) != waardes.at(i+13))
                        {
                            if(waardes.at(i+5) != waardes.at(i+6) and waardes.at(i+5) != waardes.at(i+7) and waardes.at(i+5) != waardes.at(i+8) and waardes.at(i+5) != waardes.at(i+9) and waardes.at(i+5) != waardes.at(i+10) and waardes.at(i+5) != waardes.at(i+11) and waardes.at(i+5) != waardes.at(i+12) and waardes.at(i+5) != waardes.at(i+13))
                            {
                                if(waardes.at(i+6) != waardes.at(i+7) and waardes.at(i+6) != waardes.at(i+8) and waardes.at(i+6) != waardes.at(i+9) and waardes.at(i+6) != waardes.at(i+10) and waardes.at(i+6) != waardes.at(i+11) and waardes.at(i+6) != waardes.at(i+12) and waardes.at(i+6) != waardes.at(i+13))
                                {
                                    if(waardes.at(i+7) != waardes.at(i+8) and waardes.at(i+7) != waardes.at(i+9) and waardes.at(i+7) != waardes.at(i+10) and waardes.at(i+7) != waardes.at(i+11) and waardes.at(i+7) != waardes.at(i+12) and waardes.at(i+7) != waardes.at(i+13))
                                    {
                                        if(waardes.at(i+8) != waardes.at(i+9) and waardes.at(i+8) != waardes.at(i+10) and waardes.at(i+8) != waardes.at(i+11) and waardes.at(i+8) != waardes.at(i+12) and waardes.at(i+8) != waardes.at(i+13))
                                        {
                                            if(waardes.at(i+9) != waardes.at(i+10) and waardes.at(i+9) != waardes.at(i+11) and waardes.at(i+9) != waardes.at(i+12) and waardes.at(i+9) != waardes.at(i+13))
                                            {
                                                if(waardes.at(i+10) != waardes.at(i+11) and waardes.at(i+10) != waardes.at(i+12) and waardes.at(i+10) != waardes.at(i+13))
                                                {
                                                    if(waardes.at(i+11) != waardes.at(i+12) and waardes.at(i+11) != waardes.at(i+13))
                                                    {
                                                        if(waardes.at(i+12) != waardes.at(i+13))
                                                        {
                                                            j = i+14;
                                                            break;
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

        }
    }

    cout << "**** " << j << " ****" << endl;
}
